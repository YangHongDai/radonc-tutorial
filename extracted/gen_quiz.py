# -*- coding: utf-8 -*-
"""Generate 1000 bilingual quiz questions for the Rad Onc tutorial.

Strategy:
  A) Hand-authored core clinical questions organized by topic (in this file).
  B) Trial-templated questions auto-derived from data/trials.json.

Output: radonc-tutorial/radonc-quiz/data.js (matching template schema).
"""
import json, os, re, random
random.seed(42)

ROOT = r"C:\Users\ydai\Desktop\RT2\radonc-tutorial"
TRIALS = json.load(open(os.path.join(ROOT, "data", "trials.json"), encoding="utf-8"))

# ============================================================
# HAND-AUTHORED CORE QUESTIONS
# ------------------------------------------------------------
# Format per question:
#   ("single"|"multi"|"tf", zh_stem, en_stem, [(A_zh,A_en),(B_zh,B_en),(C_zh,C_en),(D_zh,D_en)], ans, zh_exp, en_exp)
# For "tf": [], and ans is "T"|"F". For "multi": ans is list like ["A","C"].
# ============================================================

QBANK = {}

# ----------------------- PHYSICS -----------------------
QBANK["Physics"] = {"section_zh":"放射物理學", "section_en":"Radiation Physics", "questions":[
  ("single","6 MV 光子束的 dmax 大約位於多深？","At what depth is d_max located for a 6 MV photon beam?",
    [("0.5 cm","0.5 cm"),("1.5 cm","1.5 cm"),("3.0 cm","3.0 cm"),("5.0 cm","5.0 cm")],"B",
    "6 MV 的 dmax ≈ 1.5 cm，18 MV 約 3 cm；能量越高、dmax 越深。","6 MV d_max ≈ 1.5 cm; 18 MV ≈ 3 cm — d_max increases with beam energy."),
  ("single","電子束能量 12 MeV，R80 (深度到 80% 劑量) 約為？","For a 12 MeV electron beam, what is the approximate R80 (depth to 80% dose)?",
    [("2 cm","2 cm"),("3 cm","3 cm"),("4 cm","4 cm"),("6 cm","6 cm")],"C",
    "電子束 R80 ≈ E/3 cm，故 12 MeV ≈ 4 cm。R90 ≈ E/4 cm、Rp ≈ E/2 cm。","Electron R80 ≈ E/3 cm → 4 cm for 12 MeV. R90 ≈ E/4; Rp ≈ E/2."),
  ("single","質子的 Bragg peak 主要利用哪一種物理特性？","The proton Bragg peak exploits which physical property?",
    [("康普頓散射","Compton scattering"),("能量沉積在射程末端達最大","Energy deposition peaks near the end of range"),("光電效應","Photoelectric effect"),("配對產生","Pair production")],"B",
    "帶電粒子隨速度下降，能量沉積 (LET) 急劇上升，形成 Bragg peak，出射劑量近零。","As charged particles slow, LET rises sharply near end of range — the Bragg peak — with near-zero exit dose."),
  ("single","質子相對於光子的臨床 RBE 通常採用多少？","What is the clinically adopted proton RBE relative to photons?",
    [("1.0","1.0"),("1.1","1.1"),("1.5","1.5"),("2.5","2.5")],"B",
    "臨床通用 RBE = 1.1；末端可能局部升高，是質子計畫的持續研究議題。","Clinical proton RBE = 1.1 (elevated near end of range is an ongoing planning consideration)."),
  ("single","下列何者<strong>不是</strong> IMRT 相對 3D-CRT 的優點？","Which is <strong>NOT</strong> an advantage of IMRT over 3D-CRT?",
    [("更好保護 OAR","Better OAR sparing"),("更陡的劑量梯度","Steeper dose gradients"),("較短的治療時間","Shorter treatment times"),("同步整合 boost (SIB) 可行","SIB feasibility")],"C",
    "IMRT 因需要多個 field 與 MU，治療時間反而較長；VMAT 才能明顯縮短。","IMRT often takes longer than 3D-CRT due to more segments/MU; VMAT shortens time."),
  ("tf","是非題：Percent Depth Dose (PDD) 隨光子束能量升高而在同一深度上升。","True/False: PDD at a given depth increases as photon energy increases.","","T",
    "能量越高，穿透力越強，同深度 PDD 越高。","Higher energy = greater penetration = higher PDD at a given depth."),
  ("tf","是非題：FFF (flattening-filter-free) 光子束的最大優點是劑量率提升。","True/False: The main advantage of an FFF (flattening-filter-free) beam is a higher dose rate.","","T",
    "移除展平濾板後劑量率大幅提升，非常適合 SBRT/SRS；beam profile 呈中心較尖。","Removing the flattening filter dramatically increases dose rate — ideal for SBRT/SRS."),
  ("single","對於 5 cm 深腫瘤，欲最大化<strong>皮膚保護</strong>，最合適的能量選擇是？","For a 5 cm deep tumor, which beam maximizes <strong>skin sparing</strong>?",
    [("6 MV 光子","6 MV photons"),("18 MV 光子","18 MV photons"),("12 MeV 電子","12 MeV electrons"),("6 MeV 電子","6 MeV electrons")],"B",
    "18 MV 光子 dmax 較深 (~3 cm)，皮膚劑量最低；電子束皮膚劑量高。","18 MV has the deepest d_max (~3 cm) → best skin sparing; electrons deposit more at surface."),
  ("single","下列何者是質子治療最常見的臨床應用？","Which is a common clinical use of proton therapy?",
    [("成人 GBM","Adult glioblastoma"),("兒童髓母細胞瘤 CSI","Pediatric medulloblastoma CSI"),("骨轉移 palliative","Palliative bone mets"),("表淺皮膚癌","Superficial skin cancer")],"B",
    "兒童 CSI 是質子治療最核心的適應症——大幅降低出射劑量至心臟、甲狀腺、腸胃道。","Pediatric CSI is a signature indication — protons dramatically cut exit dose to heart, thyroid, and bowel."),
  ("multi","以下哪些是 IGRT 常用的成像模式？(多選)","Which of the following are common IGRT modalities? (Multiple)",
    [("kV 平面影像","kV planar imaging"),("CBCT (Cone-beam CT)","CBCT (cone-beam CT)"),("Surface guidance (光學)","Surface guidance (optical)"),("MRI-linac","MRI-linac")],["A","B","C","D"],
    "以上皆為現代 IGRT 標準工具；MR-linac 為最新的軟組織即時導航平台。","All are IGRT modalities; MR-linac is the newest for real-time soft-tissue guidance."),
  ("single","關於 SBRT 的敘述何者正確？","Which is correct regarding SBRT?",
    [("每次劑量小、次數多","Small dose per fraction, many fractions"),("通常 ≤ 5 次分次，單次劑量高","Typically ≤ 5 fractions with high dose per fraction"),("僅用於腦部腫瘤","Only used for brain tumors"),("不需要 IGRT","Does not require IGRT")],"B",
    "SBRT 特徵：少數次數 (通常 3–5 次)、單次劑量高、精準定位（強制 IGRT）。","SBRT delivers a small number of large fractions (usually 3–5) with strict IGRT."),
  ("single","顱脊照射 (CSI) 使用質子相較於光子最大好處為何？","What is the main advantage of proton CSI over photon CSI?",
    [("提高 CSI 治癒率","Higher cure rate"),("降低出射劑量至前方器官","Reduced exit dose to anterior organs"),("縮短治療時間","Shorter treatment time"),("不需接合處","No junction required")],"B",
    "質子 Bragg peak 特性大幅降低心臟、甲狀腺、腸胃道等前方器官劑量，對兒童尤其重要。","The Bragg peak sharply cuts exit dose to heart, thyroid, and bowel — especially critical in pediatrics."),
  ("single","下列何種光子能量最適合治療深部腫瘤 (>10 cm)？","Which photon energy is best suited for deep tumors (>10 cm)?",
    [("6 MV","6 MV"),("10–18 MV","10–18 MV"),("Cobalt-60 (1.25 MeV)","Cobalt-60 (1.25 MeV)"),("Orthovoltage 250 kVp","Orthovoltage 250 kVp")],"B",
    "10–18 MV 提供最佳深部劑量與皮膚保護；6 MV 適合較淺、多野；Cobalt 已被取代。","10–18 MV gives best deep-dose penetration with skin sparing; 6 MV suits shallower/multi-field; cobalt is largely obsolete."),
  ("single","下列何者屬於<strong>直接游離</strong>輻射？","Which is a <strong>directly ionizing</strong> radiation?",
    [("光子 (X-ray)","Photons (X-ray)"),("γ 射線","Gamma rays"),("電子","Electrons"),("Neutrino","Neutrinos")],"C",
    "帶電粒子（電子、質子、α）為直接游離；光子/γ 為間接游離（透過次級電子）。","Charged particles (electrons, protons, α) are directly ionizing; photons/γ are indirect (via secondary electrons)."),
  ("single","以下哪個劑量單位是<strong>SI 單位</strong>？","Which is the <strong>SI unit</strong> of absorbed dose?",
    [("Gy","Gy"),("rad","rad"),("Roentgen","Roentgen"),("Sv","Sv")],"A",
    "Gy (Gray) 為吸收劑量 SI 單位 (1 Gy = 1 J/kg)；Sv 為等效劑量 SI 單位。","Gy (Gray) is the SI unit of absorbed dose (1 Gy = 1 J/kg); Sv is the equivalent-dose unit."),
]}

# ----------------------- RADBIO -----------------------
QBANK["RadBio"] = {"section_zh":"放射生物學","section_en":"Radiation Biology","questions":[
  ("single","下列哪一種 DNA 損傷是輻射誘導細胞死亡的<strong>關鍵</strong>病變？","Which DNA lesion is the <strong>key</strong> to radiation-induced cell death?",
    [("鹼基損傷","Base damage"),("單股斷裂 (SSB)","Single-strand break (SSB)"),("雙股斷裂 (DSB)","Double-strand break (DSB)"),("Crosslinks","Crosslinks")],"C",
    "DSB 修復困難、易導致染色體畸變與細胞死亡，是關鍵病變。SSB 容易被修復。","DSBs are difficult to repair and drive cell death via chromosomal aberrations; SSBs are readily repaired."),
  ("single","BRCA1/2 缺陷的腫瘤最適合利用哪種治療 synthetic lethality？","BRCA1/2-deficient tumors are synthetically lethal with which agent?",
    [("PARP 抑制劑","PARP inhibitor"),("mTOR 抑制劑","mTOR inhibitor"),("EGFR 抑制劑","EGFR inhibitor"),("FLT3 抑制劑","FLT3 inhibitor")],"A",
    "BRCA 缺陷腫瘤仰賴 BER (需 PARP)；PARP 抑制造成 SSB 累積成 DSB，缺 HR 無法修復。","BRCA-deficient tumors rely on PARP-mediated repair; PARPi induces lethal DSB accumulation in HR-deficient cells."),
  ("single","「4 R」中的 Reoxygenation 主要指哪種效應？","In the '4 R's,' Reoxygenation refers to which effect?",
    [("腫瘤總體積擴大","Increased tumor volume"),("每次分次後缺氧細胞重新氧合，變得更敏感","Hypoxic cells reoxygenate between fractions, becoming more radiosensitive"),("組織血管新生","Angiogenesis"),("細胞週期同步","Cell-cycle synchronization")],"B",
    "腫瘤缺氧細胞在分次照射之間會逐步重新氧合，這是分次放療能有效殺傷的重要機制。","Hypoxic tumor cells re-oxygenate between fractions, becoming more radiosensitive — key rationale for fractionation."),
  ("single","α/β 比值高（~10）的組織代表？","A high α/β ratio (~10) tissue represents which type?",
    [("晚反應正常組織","Late-responding normal tissue"),("早反應與腫瘤組織","Early-responding tissues and tumors"),("靜止期正常組織","Quiescent normal tissue"),("骨組織","Bone")],"B",
    "早反應組織與多數腫瘤 α/β 高 (~10)；晚反應正常組織 α/β 低 (~3)。攝護腺為特例 α/β ~1.5。","Early-responding tissues and most tumors have α/β ~10; late-responding tissues ~3. Prostate is an exception at ~1.5."),
  ("single","EQD2 用來做什麼？","What is EQD2 used for?",
    [("推算 DVH","Compute DVH"),("將任何分次劑量轉換為等效於 2 Gy/次的總劑量","Convert any fractionation to the equivalent total dose in 2 Gy fractions"),("估算 target motion","Estimate target motion"),("測試 QA","QA measurements")],"B",
    "EQD2 = D × (d + α/β)/(2 + α/β)，是跨分次比較最實用的臨床劑量換算。","EQD2 = D × (d + α/β)/(2 + α/β) — the standard way to compare across fractionation schemes."),
  ("single","QUANTEC 建議脊髓 Dmax 應不超過多少？(2 Gy/fx)","QUANTEC-recommended spinal cord Dmax (2 Gy/fx)?",
    [("30 Gy","30 Gy"),("40 Gy","40 Gy"),("50 Gy","50 Gy"),("60 Gy","60 Gy")],"C",
    "脊髓 Dmax ≤ 50 Gy 對應約 1% 的骨髓病變風險。","Spinal cord Dmax ≤ 50 Gy corresponds to ~1% myelopathy risk."),
  ("single","以下何者對於<strong>缺氧腫瘤細胞</strong>敏感度最<strong>低</strong>影響？","Which modality is <strong>LEAST</strong> affected by tumor hypoxia (has the lowest OER)?",
    [("6 MV 光子","6 MV photons"),("Cobalt-60","Cobalt-60"),("Carbon ions","Carbon ions"),("Orthovoltage X-ray","Orthovoltage X-ray")],"C",
    "高 LET 粒子 (碳離子、中子) OER 接近 1 → 對缺氧不敏感；光子 OER ~2.5–3。","High-LET particles (carbon, neutrons) have OER near 1 — largely bypass hypoxia; photon OER is 2.5–3."),
  ("multi","以下屬於<strong>DSB 修復</strong>的路徑？(多選)","Which are <strong>DSB repair</strong> pathways? (Multiple)",
    [("NHEJ","NHEJ"),("HR","HR"),("BER","BER"),("MMR","MMR")],["A","B"],
    "NHEJ 與 HR 修復 DSB；BER 修 SSB/鹼基損傷；MMR 修錯配。","NHEJ and HR repair DSBs; BER handles SSB/base damage; MMR corrects mismatches."),
  ("single","肺 V20 建議上限一般為？","The generally recommended upper limit for lung V20 is?",
    [("≤ 15%","≤ 15%"),("≤ 30%","≤ 30%"),("≤ 45%","≤ 45%"),("≤ 60%","≤ 60%")],"B",
    "全肺 V20 ≤ 30% 對應 ≤ 20% pneumonitis 風險（QUANTEC）。","Lung V20 ≤ 30% corresponds to ≤ 20% pneumonitis risk per QUANTEC."),
  ("tf","是非題：攝護腺 α/β 值不尋常地低 (~1.5)，這使得大分次治療在生物上具有優勢。","True/False: Prostate α/β is unusually low (~1.5), giving hypofractionation a biological advantage.","","T",
    "低 α/β 使大分次對腫瘤相對有利，這是攝護腺 SBRT 的生物學基礎。","Low α/β favors hypofractionation for tumor kill — the rationale for prostate SBRT."),
  ("single","下列哪一種<strong>組織</strong>對輻射最敏感（在等劑量下）？","Which tissue is <strong>MOST</strong> radiosensitive?",
    [("骨髓與生殖細胞","Bone marrow and germ cells"),("肌肉","Muscle"),("骨","Bone"),("神經元","Neurons")],"A",
    "Bergonié–Tribondeau 原則：增殖快、分化低的組織最敏感——骨髓、生殖細胞、腸黏膜。","Bergonié–Tribondeau: rapidly dividing, poorly differentiated tissues (marrow, germ cells, gut mucosa) are most sensitive."),
  ("single","6 Gy 全身劑量對<strong>沒有</strong>支持治療的健康成人約產生什麼結果？","What is the outcome of a 6 Gy whole-body dose in an unsupported healthy adult?",
    [("完全存活","Full survival"),("骨髓症候群，可能致死","Hematopoietic syndrome, likely lethal"),("僅為皮膚症狀","Skin reactions only"),("神經血管症候群","Neurovascular syndrome")],"B",
    "LD50/60 約 3.5–4.5 Gy（無支持）；6 Gy 骨髓症候群嚴重，若無 BMT 存活率低。","LD50/60 ~3.5–4.5 Gy without support; 6 Gy causes severe hematopoietic syndrome — often fatal without transplantation."),
  ("single","碳離子 (carbon ion) 相對於光子的 RBE 大致為？","Carbon-ion RBE relative to photons is approximately?",
    [("1.0","1.0"),("1.1","1.1"),("2–4","2–4"),("10","10")],"C",
    "碳離子 RBE 約 2–4，因高 LET 造成 clustered DNA damage 修復困難。","Carbon-ion RBE is 2–4 due to high LET producing clustered DNA damage."),
  ("single","關於 low-dose hyperradiosensitivity (HRS)：","Regarding low-dose hyperradiosensitivity (HRS):",
    [("僅在 > 5 Gy 觀察到","Only observed above 5 Gy"),("< 0.5 Gy 時細胞死亡不成比例地高","Below 0.5 Gy, cell death is disproportionately high"),("HRS 完全被 LQ 模型描述","Fully described by the LQ model"),("與高 LET 無關","Unrelated to LET")],"B",
    "在極低劑量 (< 0.5 Gy) 觀察到細胞死亡比 LQ 預測還多，之後出現「increased radioresistance」區段。","At very low doses (<0.5 Gy), kill exceeds LQ prediction, followed by an 'increased radioresistance' region."),
  ("single","MGMT 甲基化在下列哪個腫瘤預測化療反應？","MGMT methylation predicts chemotherapy response in which tumor?",
    [("Glioblastoma","Glioblastoma"),("Prostate cancer","Prostate cancer"),("Breast cancer","Breast cancer"),("Colon cancer","Colon cancer")],"A",
    "GBM 中 MGMT 甲基化預測 temozolomide 反應與 OS 改善，是最強的分子預測因子。","MGMT methylation is the strongest predictor of temozolomide response and OS in GBM."),
]}

# ----------------------- CLINICAL INTRO -----------------------
QBANK["Clinical"] = {"section_zh":"臨床放射腫瘤學","section_en":"Clinical Rad Onc","questions":[
  ("single","下列何者<strong>不是</strong>常見的 immobilization 裝置？","Which is <strong>NOT</strong> a common immobilization device?",
    [("Thermoplastic mask","Thermoplastic mask"),("Vac-lok bag","Vac-lok bag"),("Alpha cradle","Alpha cradle"),("Digital rectal probe","Digital rectal probe")],"D",
    "面罩、真空袋、alpha cradle 為固定裝置；直腸探針屬 IGRT 影像/監測，不是固定。","Masks, vac-loks, alpha cradles are immobilization; rectal probes are used for IGRT/monitoring, not immobilization."),
  ("single","ICRU 定義中，CTV 加上 set-up 誤差與內部運動後為？","In ICRU nomenclature, CTV plus setup uncertainty and internal motion becomes?",
    [("GTV","GTV"),("PTV","PTV"),("OAR","OAR"),("PRV","PRV")],"B",
    "GTV→CTV→ITV→PTV：PTV 涵蓋 set-up 誤差；ITV 為 CTV+運動 (常在肺、肝)。","GTV → CTV → ITV → PTV: PTV accounts for setup, ITV for internal motion (often in lung/liver)."),
  ("single","下列何者是 KPS 90 的定義？","Which describes a KPS of 90?",
    [("完全喪失自我照護","Fully unable to self-care"),("可正常活動，僅有輕微症狀","Normal activity, minor symptoms"),("需 24hr 護理","Requires 24-hr care"),("臥床","Bedridden")],"B",
    "KPS 100 = 完全正常；90 = 幾乎正常但有輕微症狀；50 以下為明顯限制。","KPS 100 = fully normal; 90 = nearly normal with minor symptoms; ≤50 = notable functional limitation."),
  ("single","下列何者常用於評估病人在腫瘤治療中的表現狀態？","Which is commonly used to assess performance status in oncology?",
    [("BSA","BSA"),("ECOG","ECOG"),("BMI","BMI"),("Ki-67","Ki-67")],"B",
    "ECOG 0–4 與 KPS 0–100 皆為表現狀態；ECOG 使用更廣。","ECOG 0–4 and KPS 0–100 both grade performance status; ECOG is more widely used."),
  ("single","放射腫瘤諮商 (consultation) 中，下列哪一項<strong>不是</strong>必要程序？","Which is <strong>NOT</strong> a required part of a rad onc consultation?",
    [("Informed consent","Informed consent"),("提出治療 intent (curative vs palliative)","Statement of intent (curative vs palliative)"),("影像審核","Imaging review"),("開立化療處方","Chemotherapy prescription")],"D",
    "化療處方屬 medical oncology，非放射腫瘤 consult 必要內容；其餘皆是。","Chemotherapy prescription is medical oncology's role; the others are essential parts of a rad onc consult."),
  ("tf","是非題：所有放射治療計畫均應由物理師執行 pre-treatment QA。","True/False: All radiation plans should undergo pre-treatment QA by a physicist.","","T",
    "QA 是安全治療的核心——patient-specific QA 為 IMRT/VMAT 標準流程。","Patient-specific pre-treatment QA is a foundational safety practice for IMRT/VMAT."),
  ("single","下列何者為 IGRT 每日治療前最常用的影像？","Which is the most common daily pre-treatment IGRT imaging?",
    [("MRI","MRI"),("kV/CBCT","kV/CBCT"),("Ultrasound","Ultrasound"),("PET/CT","PET/CT")],"B",
    "kV 正位/側位影像與 CBCT 為現代直線加速器標配 IGRT。","kV planar and CBCT imaging are the standard modern IGRT modalities on linacs."),
  ("single","下列何者是 <strong>DIBH</strong> (深吸氣憋氣) 的主要目的？","What is the main purpose of <strong>DIBH</strong> (deep inspiration breath-hold)?",
    [("縮短治療時間","Shorten treatment time"),("降低左乳癌的心臟劑量","Reduce cardiac dose in left breast RT"),("提高精子保存","Preserve sperm"),("降低 spinal cord 劑量","Reduce spinal cord dose")],"B",
    "DIBH 使心臟遠離胸壁，明顯降低心臟平均劑量，是左乳癌治療常規。","DIBH pushes the heart away from the chest wall — routine for left-sided breast RT."),
  ("single","下列何種病人最應考慮質子治療 (based on integral dose)？","Which patient is a strong proton candidate (based on integral dose)?",
    [("70 歲攝護腺癌","70-yo prostate"),("5 歲髓母細胞瘤 CSI","5-yo medulloblastoma CSI"),("孤立肺 SBRT","Solitary lung SBRT"),("成人 GBM","Adult GBM")],"B",
    "兒童 CSI 是質子治療最典型的適應症——長遠 SMN 與心臟毒性顯著降低。","Pediatric CSI is the archetypal proton indication — reduces long-term SMN and cardiac toxicity."),
  ("single","癌症復發評估最常見的影像追蹤時程一般為？","The most common follow-up imaging cadence for recurrence surveillance is?",
    [("每月 × 5 年","Monthly × 5 yr"),("每 3–6 個月 × 2 年後每 6–12 個月","q3–6 mo × 2 yr, then q6–12 mo"),("僅追蹤 1 年","Only 1 year"),("每 2 週 × 1 年","q2 wk × 1 yr")],"B",
    "大多疾病 2 年內每 3 個月、之後 6 個月一次、5 年後年度。","Most cancers follow q3 mo × 2 yr → q6 mo → annual after 5 yr."),
]}

# ----------------------- LINGO -----------------------
QBANK["Lingo"] = {"section_zh":"縮寫與術語","section_en":"Acronyms & Lingo","questions":[
  ("single","<strong>CTV</strong> 指的是什麼？","What does <strong>CTV</strong> stand for?",
    [("Clinical Target Volume","Clinical Target Volume"),("Central Tumor Volume","Central Tumor Volume"),("Complete Tumor Volume","Complete Tumor Volume"),("Contoured Treatment Volume","Contoured Treatment Volume")],"A",
    "CTV = Clinical Target Volume（GTV + 亞臨床散佈）。","CTV = Clinical Target Volume (GTV + subclinical microscopic spread)."),
  ("single","<strong>OAR</strong> 指的是什麼？","What does <strong>OAR</strong> stand for?",
    [("Organ at Risk","Organ at Risk"),("Optimization Analysis Report","Optimization Analysis Report"),("Overall Absorbed Radiation","Overall Absorbed Radiation"),("Operational Approval Record","Operational Approval Record")],"A",
    "OAR = Organ at Risk（危及器官）。","OAR = Organ at Risk."),
  ("single","<strong>V20</strong> 在肺放射治療中代表？","In lung RT, <strong>V20</strong> refers to?",
    [("接受 ≥ 20 Gy 的體積百分比","Percent volume receiving ≥ 20 Gy"),("接受 20 Gy 的絕對體積 (cc)","Absolute volume receiving 20 Gy (cc)"),("20 個 Gy 的劑量閾值","20 Gy dose threshold"),("每次 20 Gy 分次","20 Gy per fraction")],"A",
    "V20 = 接受 ≥ 20 Gy 的體積百分比，肺照射的關鍵毒性指標。","V20 is the percent volume receiving ≥ 20 Gy — a key lung toxicity metric."),
  ("single","<strong>SIB</strong> 意義？","<strong>SIB</strong> means?",
    [("Simultaneous Integrated Boost","Simultaneous Integrated Boost"),("Sequential Integrated Beam","Sequential Integrated Beam"),("Standard Isocenter Beam","Standard Isocenter Beam"),("Split-field Interior Boost","Split-field Interior Boost")],"A",
    "SIB = 同步整合 boost；於同一計畫同時處方多個劑量。","SIB = Simultaneous Integrated Boost — multiple prescription doses within a single plan."),
  ("single","<strong>EBRT</strong>?","<strong>EBRT</strong>?",
    [("External Beam RT","External Beam RT"),("Endobronchial RT","Endobronchial RT"),("Electron Beam RT","Electron Beam RT"),("Extended Boost RT","Extended Boost RT")],"A",
    "EBRT = External Beam RT，體外放射治療。","EBRT = External Beam Radiation Therapy."),
  ("single","<strong>BED</strong> 全名？","<strong>BED</strong> stands for?",
    [("Beam Energy Distribution","Beam Energy Distribution"),("Biologically Effective Dose","Biologically Effective Dose"),("Bulk Electron Dose","Bulk Electron Dose"),("Best Estimated Dose","Best Estimated Dose")],"B",
    "BED = Biologically Effective Dose = nd(1+d/(α/β))。","BED = Biologically Effective Dose = nd(1+d/(α/β))."),
  ("single","<strong>SRS</strong> 適應症為？","<strong>SRS</strong> is typically used for?",
    [("大腸癌肝轉移 SBRT","Colorectal liver mets"),("顱內單次立體定位","Intracranial single-fraction stereotactic"),("盆腔淋巴 boost","Pelvic nodal boost"),("胸部近接治療","Thoracic brachytherapy")],"B",
    "SRS 特指顱內立體定位放射手術（通常單次）。","SRS specifically refers to intracranial single-fraction stereotactic radiosurgery."),
  ("multi","下列哪些屬於<strong>近接治療 (brachytherapy)</strong> 的種類？(多選)","Which are types of <strong>brachytherapy</strong>? (Multiple)",
    [("HDR (high dose rate)","HDR (high dose rate)"),("LDR (low dose rate)","LDR (low dose rate)"),("PDR (pulsed dose rate)","PDR (pulsed dose rate)"),("VMAT","VMAT")],["A","B","C"],
    "HDR、LDR、PDR 皆屬 brachytherapy；VMAT 屬體外治療。","HDR, LDR, PDR are brachytherapy types; VMAT is external-beam."),
  ("single","<strong>D95</strong> 意義？","<strong>D95</strong> means?",
    [("覆蓋 95% 體積的劑量","Dose covering 95% of the volume"),("最大劑量 95 Gy","Max dose of 95 Gy"),("計畫 95% 覆蓋率","Plan 95% coverage"),("D 曲線 95% 位置","95% point of D curve")],"A",
    "D95 為劑量學指標——覆蓋 95% 標靶體積的劑量閾值，臨床常用。","D95 is the dose covering 95% of the target volume — a common clinical planning metric."),
]}

# I'll continue with disease-site question banks — packed as terse pairs to reach ~500 hand-crafted.
