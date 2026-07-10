#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const targetArg = process.argv[2] || "data_refined.js";
const targetPath = path.resolve(process.cwd(), targetArg);

function readQuizData(filePath) {
  const source = fs.readFileSync(filePath, "utf8");
  const sandbox = { window: {} };
  vm.runInNewContext(source, sandbox, { filename: filePath, timeout: 2000 });
  if (!sandbox.window || !sandbox.window.QUIZ_DATA) {
    throw new Error("window.QUIZ_DATA is missing");
  }
  return { source, data: sandbox.window.QUIZ_DATA };
}

function normalizeText(text) {
  return String(text || "")
    .toLowerCase()
    .replace(/<[^>]+>/g, " ")
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function tokenize(text) {
  return new Set(normalizeText(text).split(" ").filter(Boolean));
}

function jaccard(a, b) {
  const A = tokenize(a);
  const B = tokenize(b);
  if (!A.size || !B.size) return 0;
  let inter = 0;
  for (const token of A) {
    if (B.has(token)) inter += 1;
  }
  return inter / (A.size + B.size - inter);
}

function digits(text) {
  return (String(text || "").match(/\d+(?:\.\d+)?/g) || []).join("|");
}

function hasUnit(text) {
  return /\b(gy|fx|fraction|fractions|cm|mm|%|mv|mev|cc|ml|month|months|year|years|day|days)\b/i.test(String(text || ""));
}

function likelyClinicalStem(text) {
  return /\b(stage|cancer|tumou?r|lymphoma|glioma|metast|radiotherapy|chemoradiotherapy|surgery|postoperative|adjuvant|salvage|definitive|palliative)\b/i.test(text);
}

function hasClinicalContext(text) {
  return /\b(stage|t\d|n\d|m\d|risk|ecog|performance status|resect|metast|postoperative|adjuvant|salvage|definitive|palliative|peripheral|central|bulky|deauville|mgmt|idh|p16|psa|gleason|figo|ajcc)\b/i.test(text);
}

function negativeStemNotEmphasized(textZh, textEn) {
  const enHasNegative = /\b(incorrect|except|least appropriate|not appropriate)\b/i.test(textEn);
  const enEmphasized = /\b(INCORRECT|EXCEPT|LEAST APPROPRIATE|NOT APPROPRIATE)\b/.test(textEn);
  const zhHasNegative = /(不正確|錯誤|除外|最不適當)/.test(textZh);
  const zhEmphasized = /[「『](不正確|錯誤|除外|最不適當)[」』]/.test(textZh) || /(不正確|錯誤|除外|最不適當)/.test(textZh);
  return (enHasNegative && !enEmphasized) || (zhHasNegative && !zhEmphasized);
}

function summarizeDistribution(counter) {
  return Object.keys(counter)
    .sort()
    .map((key) => `${key}:${counter[key]}`)
    .join(" ");
}

function main() {
  const critical = [];
  const warnings = [];
  let parsed;

  try {
    parsed = readQuizData(targetPath);
  } catch (err) {
    console.error(`CRITICAL: failed to parse ${targetPath}`);
    console.error(String(err && err.stack ? err.stack : err));
    process.exit(1);
  }

  const { data } = parsed;
  if (!data.radonc || !data.radonc.subjects) {
    critical.push("QUIZ_DATA.radonc.subjects is missing");
  }

  const subjects = (data.radonc && data.radonc.subjects) || {};
  const countsBySection = {};
  const answerDistribution = { A: 0, B: 0, C: 0, D: 0, multi: 0, tf: 0 };
  const exactStems = new Map();
  const correctFacts = new Set();
  const allQuestions = [];
  let totalQuestions = 0;

  for (const [top, subs] of Object.entries(subjects)) {
    for (const [sub, questions] of Object.entries(subs)) {
      countsBySection[`${top} / ${sub}`] = questions.length;
      for (let i = 0; i < questions.length; i += 1) {
        const q = questions[i];
        const qid = `${top} / ${sub} / Q${i + 1}`;
        totalQuestions += 1;
        allQuestions.push({ qid, question: q, top, sub });
        exactStems.set(q.stem_en, (exactStems.get(q.stem_en) || 0) + 1);
        if (q.type === "single") {
          if (!/^[ABCD]$/.test(q.ans || "")) {
            critical.push(`${qid}: single question has invalid answer key`);
          } else {
            answerDistribution[q.ans] += 1;
            correctFacts.add(q[`${q.ans}_en`]);
          }
        } else if (q.type === "multi") {
          if (!Array.isArray(q.ans) || q.ans.length < 2) {
            critical.push(`${qid}: multi question must have at least two answers`);
          } else {
            answerDistribution.multi += 1;
          }
        } else if (q.type === "tf") {
          if (!["T", "F"].includes(q.ans)) {
            critical.push(`${qid}: tf question must have T or F answer`);
          } else {
            answerDistribution.tf += 1;
          }
        } else {
          critical.push(`${qid}: unrecognized question type "${q.type}"`);
        }
      }
    }
  }

  for (const entry of allQuestions) {
    const { qid, question: q } = entry;

    if (!q.stem || !q.stem_en) {
      critical.push(`${qid}: missing Chinese or English stem`);
    }
    if (!q.exp || !q.exp_en) {
      critical.push(`${qid}: missing Chinese or English explanation`);
    }

    const optionLetters = q.type === "tf" ? [] : ["A", "B", "C", "D"];
    const optionTextsZh = [];
    const optionTextsEn = [];

    for (const letter of optionLetters) {
      if (!q[letter] || !q[`${letter}_en`]) {
        critical.push(`${qid}: missing ${letter}/${letter}_en`);
        continue;
      }
      if (!String(q[letter]).trim() || !String(q[`${letter}_en`]).trim()) {
        critical.push(`${qid}: blank ${letter}/${letter}_en`);
      }
      optionTextsZh.push(String(q[letter]).trim());
      optionTextsEn.push(String(q[`${letter}_en`]).trim());

      const digitMismatch = digits(q[letter]) !== digits(q[`${letter}_en`]);
      if (digits(q[letter]) && digits(q[`${letter}_en`]) && digitMismatch) {
        warnings.push(`${qid}: possible zh/en numeric mismatch in option ${letter}`);
      }
      if (hasUnit(q[letter]) !== hasUnit(q[`${letter}_en`]) && (hasUnit(q[letter]) || hasUnit(q[`${letter}_en`]))) {
        warnings.push(`${qid}: possible zh/en unit mismatch in option ${letter}`);
      }
    }

    if (new Set(optionTextsZh).size !== optionTextsZh.length || new Set(optionTextsEn).size !== optionTextsEn.length) {
      critical.push(`${qid}: duplicate options within the same question`);
    }

    if (q.type === "single" && !q[q.ans] && !q[`${q.ans}_en`]) {
      critical.push(`${qid}: keyed answer does not map to an existing option`);
    }
    if (q.type === "multi") {
      for (const ans of q.ans) {
        if (!q[ans] || !q[`${ans}_en`]) {
          critical.push(`${qid}: multi answer key ${ans} does not map to an existing option`);
        }
      }
    }

    const lengths = optionTextsEn.map((text) => text.length);
    const median = lengths.slice().sort((a, b) => a - b)[Math.floor(lengths.length / 2)] || 1;
    if (lengths.some((len) => len > median * 1.9)) {
      warnings.push(`${qid}: one option is much longer than the others`);
    }

    if (negativeStemNotEmphasized(q.stem, q.stem_en)) {
      warnings.push(`${qid}: negative stem is not clearly emphasized`);
    }
    if (String(q.exp_en).length < 120 || String(q.exp).length < 60) {
      warnings.push(`${qid}: explanation may be too short to teach reasoning`);
    }
    if (/\d/.test(q.stem_en) && !hasUnit(q.stem_en) && !optionTextsEn.some(hasUnit)) {
      warnings.push(`${qid}: numeric question may lack explicit units`);
    }
    if (likelyClinicalStem(q.stem_en) && !hasClinicalContext(q.stem_en)) {
      warnings.push(`${qid}: clinical-style stem may lack stage/setting context`);
    }

    const overlaps = optionTextsEn.map((opt) => jaccard(opt, q.stem_en));
    if (optionTextsEn.length && overlaps.every((score) => score < 0.05)) {
      warnings.push(`${qid}: all options have very low lexical overlap with the stem; review topical relevance`);
    }

    for (const field of ["source_url", "url"]) {
      if (q[field]) {
        try {
          new URL(q[field]);
        } catch (err) {
          critical.push(`${qid}: invalid URL in ${field}`);
        }
      }
    }
  }

  let recognizedTrueDistractors = 0;
  for (const entry of allQuestions) {
    const q = entry.question;
    if (q.type !== "single") continue;
    for (const letter of ["A", "B", "C", "D"]) {
      if (letter === q.ans) continue;
      if (correctFacts.has(q[`${letter}_en`])) {
        recognizedTrueDistractors += 1;
        warnings.push(`${entry.qid}: distractor ${letter} matches a keyed correct answer elsewhere`);
      }
    }
  }

  const exactDuplicateStemCount = [...exactStems.values()].reduce((sum, count) => sum + Math.max(0, count - 1), 0);
  if (exactDuplicateStemCount > 0) {
    warnings.push(`Exact duplicate English stems detected: ${exactDuplicateStemCount}`);
  }

  const semanticDuplicates = [];
  for (let i = 0; i < allQuestions.length; i += 1) {
    const a = allQuestions[i];
    const aNorm = normalizeText(a.question.stem_en);
    for (let j = i + 1; j < allQuestions.length; j += 1) {
      const b = allQuestions[j];
      const bNorm = normalizeText(b.question.stem_en);
      if (!aNorm || !bNorm) continue;
      if (Math.abs(aNorm.length - bNorm.length) > 20) continue;
      const score = jaccard(aNorm, bNorm);
      if (score >= 0.92) {
        semanticDuplicates.push(`${a.qid} <-> ${b.qid}`);
        if (semanticDuplicates.length >= 25) break;
      }
    }
    if (semanticDuplicates.length >= 25) break;
  }
  if (semanticDuplicates.length) {
    warnings.push(`Potential semantic duplicate stems flagged: ${semanticDuplicates.length}`);
  }

  console.log(`Validated file: ${path.basename(targetPath)}`);
  console.log(`Total questions: ${totalQuestions}`);
  console.log(`Answer distribution: ${summarizeDistribution(answerDistribution)}`);
  console.log("Question counts by section:");
  Object.keys(countsBySection)
    .sort()
    .forEach((key) => console.log(`  ${key}: ${countsBySection[key]}`));
  console.log(`Exact duplicate English stems: ${exactDuplicateStemCount}`);
  console.log(`Distractors that are keyed correct elsewhere: ${recognizedTrueDistractors}`);
  console.log(`Critical issues: ${critical.length}`);
  console.log(`Warnings: ${warnings.length}`);

  if (semanticDuplicates.length) {
    console.log("Sample semantic-duplicate flags:");
    semanticDuplicates.slice(0, 10).forEach((line) => console.log(`  ${line}`));
  }
  if (warnings.length) {
    console.log("Sample warnings:");
    warnings.slice(0, 20).forEach((line) => console.log(`  ${line}`));
  }
  if (critical.length) {
    console.log("Critical details:");
    critical.slice(0, 20).forEach((line) => console.log(`  ${line}`));
    process.exit(1);
  }
}

main();
