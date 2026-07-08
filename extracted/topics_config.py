# -*- coding: utf-8 -*-
"""Bilingual teaching content for all 18 Rad Onc topic pages."""

PAGES = []

# ============================================================
# INTRO TO RAD ONC (4 pages)
# ============================================================

PAGES.append({
    "slug": "intro-clinical",
    "emoji": "🩺",
    "title_zh": "臨床放射腫瘤學導論",
    "title_en": "Introduction to Clinical Radiation Oncology",
    "sub_zh": "從初診到治療完成——放射腫瘤科的工作流程與角色。",
    "sub_en": "From consult to end-of-treatment — the workflow and role of a radiation oncologist.",
    "sections": [
      {
        "label_zh": "概觀", "label_en": "OVERVIEW",
        "h2_zh": "放射腫瘤科在癌症照護中的角色",
        "h2_en": "The role of Rad Onc in cancer care",
        "body_zh": "<p>放射腫瘤科 (Radiation Oncology) 是使用<strong>游離輻射</strong>治療癌症與少數良性疾病的臨床專科。約 50% 的癌症病人在治療歷程中會接受放射治療，貢獻約 40% 的癌症治癒率。</p><p>放射腫瘤醫師與外科、腫瘤內科組成癌症多專科團隊，負責諮商、模擬、勾畫、計畫審核、發放與追蹤。</p>",
        "body_en": "<p>Radiation Oncology is the medical specialty using <strong>ionizing radiation</strong> to treat cancer and select benign conditions. About 50% of cancer patients receive radiation at some point, and RT contributes ~40% of cancer cures.</p><p>The rad onc physician works alongside surgical and medical oncology in multidisciplinary care, owning the workflow of consultation, simulation, contouring, plan review, on-treatment care, and survivorship follow-up.</p>"
      },
      {
        "label_zh": "工作流程", "label_en": "WORKFLOW",
        "h2_zh": "放射治療的完整流程",
        "h2_en": "The end-to-end RT workflow",
        "body_zh": "<div class='workflow'><div class='workflow-step' data-step='1'><h4>諮商 (Consultation)</h4><p>檢視病史、影像、病理與分期，決定是否放療、治療目的（根治 vs 姑息）與 informed consent。</p></div><div class='workflow-step' data-step='2'><h4>模擬 (Simulation)</h4><p>以 CT-Sim 取得治療姿勢的定位影像；必要時融合 MRI/PET。使用固定裝置（面罩、真空袋、乳房板等）。</p></div><div class='workflow-step' data-step='3'><h4>勾畫 (Contouring)</h4><p>依 ICRU 定義 GTV → CTV → ITV → PTV；同時勾畫 OARs。近年 AI auto-contouring 已可加速流程但需醫師審核。</p></div><div class='workflow-step' data-step='4'><h4>計畫 (Planning)</h4><p>物理師以 IMRT/VMAT/3DCRT/質子等技術製作劑量分佈；醫師審核並要求 QA。</p></div><div class='workflow-step' data-step='5'><h4>發放 (Delivery)</h4><p>直線加速器或質子機每日發放；每次治療前以 kV/CBCT 進行 image guidance (IGRT)。</p></div><div class='workflow-step' data-step='6'><h4>追蹤 (Follow-up)</h4><p>治療完成後定期評估腫瘤反應與晚期副作用，通常 2 年內每 3 個月，5 年內每 6 個月。</p></div></div>",
        "body_en": "<div class='workflow'><div class='workflow-step' data-step='1'><h4>Consultation</h4><p>Review history, imaging, pathology, and stage. Decide if RT is indicated, intent (curative vs palliative), and obtain informed consent.</p></div><div class='workflow-step' data-step='2'><h4>Simulation</h4><p>CT-simulation in treatment position; MRI/PET fusion as indicated. Immobilization devices (thermoplastic masks, vac-lok bags, breast boards).</p></div><div class='workflow-step' data-step='3'><h4>Contouring</h4><p>Per ICRU: GTV → CTV → ITV → PTV; contour OARs. AI auto-contouring can accelerate but requires MD review.</p></div><div class='workflow-step' data-step='4'><h4>Planning</h4><p>Medical physicist builds dose distribution with IMRT/VMAT/3DCRT/protons; MD reviews and orders QA.</p></div><div class='workflow-step' data-step='5'><h4>Delivery</h4><p>Daily fractions on a linac or proton unit with image guidance (kV/CBCT) before each treatment.</p></div><div class='workflow-step' data-step='6'><h4>Follow-up</h4><p>Assess tumor response and late toxicity — typically q3 months for 2 years, then q6 months to year 5, then annually.</p></div></div>"
      },
      {
        "label_zh": "劑量單位", "label_en": "DOSE UNITS",
        "h2_zh": "劑量、分次與生物有效劑量",
        "h2_en": "Dose, fractionation & biologically effective dose",
        "body_zh": "<p><strong>Gy (灰):</strong> 吸收劑量的 SI 單位，1 Gy = 1 J/kg。臨床通常以每日 <strong>分次 (fraction)</strong> 給予，如 2 Gy × 30 次 = 60 Gy。</p><p><strong>BED (生物有效劑量):</strong> BED = nd(1 + d/(α/β))，用於跨分次比較。腫瘤 α/β 通常較高 (~10)，晚期正常組織較低 (~3)，故大分次 (SBRT) 對腫瘤相對有利。</p><p><strong>EQD2:</strong> 等效於每次 2 Gy 的總劑量，臨床最常用來換算。</p>",
        "body_en": "<p><strong>Gray (Gy):</strong> SI unit of absorbed dose; 1 Gy = 1 J/kg. Clinical RT is delivered in daily <strong>fractions</strong>, e.g., 2 Gy × 30 = 60 Gy total.</p><p><strong>BED:</strong> BED = nd(1 + d/(α/β)) — enables comparison across fractionation schemes. Tumor α/β is typically high (~10) and late-responding normal tissue is low (~3), so hypofractionation (SBRT) can be biologically favorable.</p><p><strong>EQD2:</strong> Total dose expressed as-if delivered in 2 Gy fractions — the most common clinical conversion.</p>"
      },
      {
        "label_zh": "治療技術", "label_en": "MODALITIES",
        "h2_zh": "常見治療技術",
        "h2_en": "Common treatment modalities",
        "body_zh": "<ul><li><strong>3D-CRT:</strong> 三維適形放射治療，多野合成。</li><li><strong>IMRT:</strong> 強度調控，適合複雜靶區（頭頸、攝護腺）。</li><li><strong>VMAT:</strong> 旋轉式 IMRT，治療時間更短。</li><li><strong>SBRT / SABR:</strong> 立體定位大分次，用於早期肺癌、寡轉移、肝癌等。</li><li><strong>SRS:</strong> 顱內立體定位單次治療，用於腦轉移、AVM、聽神經瘤。</li><li><strong>近接治療 (Brachytherapy):</strong> 放射源直接置入腫瘤（婦科、攝護腺）。</li><li><strong>質子治療 (Proton):</strong> 利用 Bragg peak 減少出射劑量，特別用於兒童與顱底腫瘤。</li></ul>",
        "body_en": "<ul><li><strong>3D-CRT:</strong> 3D conformal RT, multiple shaped beams.</li><li><strong>IMRT:</strong> Intensity-modulated for complex targets (H&amp;N, prostate).</li><li><strong>VMAT:</strong> Rotational IMRT — faster delivery.</li><li><strong>SBRT / SABR:</strong> Stereotactic body RT, hypofractionated — early lung, oligomets, HCC.</li><li><strong>SRS:</strong> Intracranial single-fraction — brain mets, AVMs, vestibular schwannomas.</li><li><strong>Brachytherapy:</strong> Radioactive sources placed in/near tumor (Gyn, prostate).</li><li><strong>Protons:</strong> Bragg peak reduces exit dose — pediatric, skull-base tumors.</li></ul>"
      },
    ],
    "excel_sheet": None,
    "prev": None,
    "next": ["physics.html", "放射物理學", "Physics"],
})

PAGES.append({
    "slug": "physics",
    "emoji": "⚛️",
    "title_zh": "放射物理學",
    "title_en": "Radiation Physics",
    "sub_zh": "光子、電子、質子束的物理性質與臨床應用。",
    "sub_en": "Photon, electron, and proton beam properties and clinical applications.",
    "sections": [
      {
        "label_zh": "光子束", "label_en": "PHOTON BEAMS",
        "h2_zh": "光子束特性",
        "h2_en": "Photon beam properties",
        "body_zh": "<p><strong>光子束 (X-ray):</strong> 由高速電子撞擊靶產生，屬<strong>間接游離輻射</strong>。臨床常用 6–18 MV。</p><ul><li><strong>Percent Depth Dose (PDD):</strong> 隨能量升高、深度增加而增大 (skin sparing)。6 MV 的 dmax ≈ 1.5 cm，18 MV ≈ 3 cm。</li><li><strong>Buildup region:</strong> 電子平衡未達之前的區域，皮膚劑量較低。</li><li><strong>Beam profile:</strong> 由平坦度 (flatness) 與對稱性 (symmetry) 描述，用 FFF (flattening-filter-free) 可提升劑量率。</li></ul>",
        "body_en": "<p><strong>Photons (X-rays):</strong> Produced by high-speed electrons striking a target — <strong>indirectly ionizing</strong>. Clinical range 6–18 MV.</p><ul><li><strong>Percent Depth Dose (PDD):</strong> Increases with energy and depth (skin sparing). 6 MV d_max ≈ 1.5 cm; 18 MV ≈ 3 cm.</li><li><strong>Buildup region:</strong> Region prior to electronic equilibrium — lower skin dose.</li><li><strong>Beam profile:</strong> Characterized by flatness and symmetry; FFF (flattening-filter-free) increases dose rate.</li></ul>"
      },
      {
        "label_zh": "電子束", "label_en": "ELECTRON BEAMS",
        "h2_zh": "電子束特性",
        "h2_en": "Electron beam properties",
        "body_zh": "<p><strong>電子束:</strong> 直接游離輻射，能量 6–20 MeV，用於皮膚、乳房疤痕、chest wall boost。</p><ul><li><strong>射程 (Range) rule:</strong> R80 (深度到 80% dose) ≈ E/3 cm；R90 ≈ E/4 cm。例如 12 MeV → R80 ≈ 4 cm。</li><li><strong>Practical range Rp:</strong> ≈ E/2 cm。</li><li><strong>Skin dose:</strong> 電子束皮膚劑量較光子高 (80–95%)。</li><li><strong>Bolus:</strong> 用於將 dmax 移至皮膚表面。</li></ul>",
        "body_en": "<p><strong>Electrons:</strong> Directly ionizing, 6–20 MeV — used for skin, breast scar, chest wall boost.</p><ul><li><strong>Range rule:</strong> R80 ≈ E/3 cm; R90 ≈ E/4 cm. Example: 12 MeV → R80 ≈ 4 cm.</li><li><strong>Practical range Rp:</strong> ≈ E/2 cm.</li><li><strong>Skin dose:</strong> Higher than photons (80–95%).</li><li><strong>Bolus:</strong> Used to shift d_max to the skin surface.</li></ul>"
      },
      {
        "label_zh": "質子束", "label_en": "PROTON BEAMS",
        "h2_zh": "質子束與 Bragg peak",
        "h2_en": "Proton beams and the Bragg peak",
        "body_zh": "<p><strong>質子:</strong> 帶正電粒子，能量 70–250 MeV，具有<strong>Bragg peak</strong>——大部分劑量集中在射程末端，之後急劇下降。</p><ul><li><strong>Spread-Out Bragg Peak (SOBP):</strong> 多個能量疊加以覆蓋靶區。</li><li><strong>RBE:</strong> 質子相對光子 RBE ≈ 1.1 (臨床通用值)。</li><li><strong>臨床適用:</strong> 兒童（減少發育中組織的整體劑量）、顱底、脊索瘤、眼部黑色素瘤。</li><li><strong>不確定性:</strong> 射程對 CT HU 換算敏感，需嚴格 QA。</li></ul>",
        "body_en": "<p><strong>Protons:</strong> Positively charged particles, 70–250 MeV, with a <strong>Bragg peak</strong> — dose is concentrated near the end of range, then falls sharply.</p><ul><li><strong>Spread-Out Bragg Peak (SOBP):</strong> Multiple energies summed to cover a target.</li><li><strong>RBE:</strong> Clinical RBE ≈ 1.1 vs. photons.</li><li><strong>Clinical use:</strong> Pediatrics (reduce integral dose to developing tissues), skull base, chordoma, ocular melanoma.</li><li><strong>Uncertainty:</strong> Range is sensitive to CT HU conversion — rigorous QA required.</li></ul>"
      },
      {
        "label_zh": "顱脊照射", "label_en": "CSI",
        "h2_zh": "顱脊照射 (Craniospinal Irradiation)",
        "h2_en": "Craniospinal Irradiation (CSI)",
        "body_zh": "<p>CSI 用於髓母細胞瘤、生殖細胞瘤等需覆蓋整個中樞神經軸的疾病。</p><ul><li><strong>靶區:</strong> 全腦 + 全脊髓 (至 S2/3)。</li><li><strong>技術:</strong> 光子 CSI 需 2–3 個等中心，接合處逐日移位以避免熱點；<strong>質子 CSI</strong> 可用單一 field，並顯著降低出射劑量至心臟、甲狀腺、腸胃道。</li><li><strong>劑量:</strong> 標準風險髓母 23.4 Gy CSI + 後顱窩 boost 至 54 Gy；高風險 36 Gy CSI。</li></ul>",
        "body_en": "<p>CSI is used for medulloblastoma, germinomas, and other neoplasms requiring coverage of the entire craniospinal axis.</p><ul><li><strong>Target:</strong> Whole brain + entire spinal cord (to S2/3).</li><li><strong>Technique:</strong> Photon CSI requires 2–3 isocenters with daily junction shifts. <strong>Proton CSI</strong> uses a single field and substantially reduces exit dose to heart, thyroid, and bowel.</li><li><strong>Dose:</strong> Average-risk medulloblastoma 23.4 Gy CSI + posterior fossa boost to 54 Gy; high-risk 36 Gy CSI.</li></ul>"
      },
    ],
    "excel_sheet": None,
    "prev": ["intro-clinical.html", "臨床導論", "Clinical Intro"],
    "next": ["radbio.html", "放射生物", "RadBio"],
})

PAGES.append({
    "slug": "radbio",
    "emoji": "🧬",
    "title_zh": "放射生物學",
    "title_en": "Radiation Biology",
    "sub_zh": "DNA 損傷與修復、OER/LET/RBE、分次與晚期毒性。",
    "sub_en": "DNA damage & repair, OER/LET/RBE, fractionation & late toxicity.",
    "sections": [
      {
        "label_zh": "DNA 損傷", "label_en": "DNA DAMAGE",
        "h2_zh": "游離輻射的 DNA 損傷機制",
        "h2_en": "Mechanisms of radiation-induced DNA damage",
        "body_zh": "<p>游離輻射透過<strong>直接作用</strong>（電子直接撞擊 DNA）與<strong>間接作用</strong>（水解離產生 ·OH 自由基）造成傷害。光子/電子中 ~2/3 為間接作用；高 LET 粒子（α、中子）以直接作用為主。</p><ul><li><strong>單股斷裂 (SSB):</strong> 常見，容易修復。</li><li><strong>雙股斷裂 (DSB):</strong> 較少見但是<strong>細胞死亡的關鍵</strong>。1 Gy 光子造成約 40 個 DSB。</li><li><strong>Base damage / crosslinks / clustered lesions:</strong> 高 LET 造成的複雜傷害修復困難。</li></ul>",
        "body_en": "<p>Ionizing radiation causes DNA damage via <strong>direct action</strong> (electrons striking DNA) and <strong>indirect action</strong> (water radiolysis producing ·OH radicals). For photons/electrons ~2/3 is indirect; high-LET particles (α, neutrons) are predominantly direct.</p><ul><li><strong>Single-strand breaks (SSB):</strong> Common, easily repaired.</li><li><strong>Double-strand breaks (DSB):</strong> Less common but <strong>the key lesion for cell death</strong>. 1 Gy of photons produces ~40 DSBs.</li><li><strong>Base damage / crosslinks / clustered lesions:</strong> Complex damage from high LET is difficult to repair.</li></ul>"
      },
      {
        "label_zh": "修復路徑", "label_en": "REPAIR PATHWAYS",
        "h2_zh": "DSB 修復：NHEJ 與 HR",
        "h2_en": "DSB repair: NHEJ vs. HR",
        "body_zh": "<p><strong>NHEJ (Non-Homologous End Joining):</strong> 貫穿整個細胞週期，快速但易產生錯誤；由 Ku70/80、DNA-PKcs、Ligase IV 主導。</p><p><strong>HR (Homologous Recombination):</strong> 需要姊妹染色分體作為模板，僅在 S/G2 期進行；由 BRCA1/2、RAD51 主導。BRCA 缺陷腫瘤對<strong>PARP 抑制劑</strong>有 synthetic lethality。</p>",
        "body_en": "<p><strong>NHEJ (Non-Homologous End Joining):</strong> Active throughout the cell cycle — fast but error-prone. Ku70/80, DNA-PKcs, Ligase IV.</p><p><strong>HR (Homologous Recombination):</strong> Requires a sister chromatid template — only in S/G2. BRCA1/2, RAD51. BRCA-deficient tumors show synthetic lethality with <strong>PARP inhibitors</strong>.</p>"
      },
      {
        "label_zh": "OER · LET · RBE", "label_en": "OER · LET · RBE",
        "h2_zh": "氧效應、線性能量轉移與相對生物效應",
        "h2_en": "Oxygen effect, LET, and RBE",
        "body_zh": "<p><strong>OER (Oxygen Enhancement Ratio):</strong> 有氧比缺氧達到同樣殺傷所需劑量的比值，光子 ~2.5–3.0；粒子 (高 LET) OER 較低 (~1)。</p><p><strong>LET (Linear Energy Transfer):</strong> 單位路徑的能量沉積 (keV/μm)。光子/電子低 LET；α 粒子、中子高 LET。</p><p><strong>RBE (Relative Biological Effectiveness):</strong> 相對於 250 kVp X-ray 產生相同生物效應所需劑量的比值。質子臨床 RBE = 1.1，中子 ≈ 3，碳離子 2–4。</p><p><strong>4 R:</strong> Repair、Reassortment (cell cycle redistribution)、Repopulation、Reoxygenation——分次照射利用這些機制。</p>",
        "body_en": "<p><strong>OER (Oxygen Enhancement Ratio):</strong> Ratio of dose needed under hypoxia vs. normoxia for the same kill; ~2.5–3.0 for photons; near 1 for high-LET particles.</p><p><strong>LET (Linear Energy Transfer):</strong> Energy deposited per unit path (keV/μm). Photons/electrons are low-LET; α particles and neutrons are high-LET.</p><p><strong>RBE (Relative Biological Effectiveness):</strong> Ratio of doses producing the same biological effect vs. 250 kVp X-ray. Clinical proton RBE = 1.1; neutrons ≈ 3; carbon ions 2–4.</p><p><strong>The 4 R's:</strong> Repair, Reassortment (cell-cycle redistribution), Repopulation, Reoxygenation — fractionation exploits these.</p>"
      },
      {
        "label_zh": "分次照射", "label_en": "FRACTIONATION",
        "h2_zh": "分次照射與 α/β 比值",
        "h2_en": "Fractionation and α/β ratio",
        "body_zh": "<p><strong>Linear-Quadratic model:</strong> S = e^(−αD−βD²)。α/β 描述細胞對分次的敏感度。</p><ul><li><strong>早反應組織 (early)</strong> α/β ~ 10：多數上皮腫瘤、皮膚黏膜。</li><li><strong>晚反應組織 (late)</strong> α/β ~ 3：脊髓、腎、肺、心。</li><li><strong>攝護腺</strong> α/β 罕見地低 ~ 1.5，適合大分次。</li></ul><p><strong>BED = nd(1 + d/(α/β))；EQD2 = D × (d + α/β)/(2 + α/β)</strong></p><h4>常見劑量限制 (QUANTEC 摘要)</h4><ul><li>脊髓：Dmax &lt; 50 Gy（分次 2 Gy）— 1% 骨髓病變。</li><li>肺 (V20)：≤ 30% — pneumonitis ≤ 20%。</li><li>心臟 mean dose：越低越好；乳癌左側目標 &lt; 4–5 Gy。</li><li>Parotid mean：≤ 26 Gy 減少長期口乾。</li><li>直腸 V70：&lt; 20–25%（攝護腺 78–80 Gy 標準分次）。</li></ul>",
        "body_en": "<p><strong>Linear-Quadratic model:</strong> S = e^(−αD−βD²). α/β describes fractionation sensitivity.</p><ul><li><strong>Early-responding tissues</strong> α/β ~ 10: most epithelial tumors, skin, mucosa.</li><li><strong>Late-responding tissues</strong> α/β ~ 3: spinal cord, kidney, lung, heart.</li><li><strong>Prostate</strong> α/β is unusually low ~ 1.5 — favorable for hypofractionation.</li></ul><p><strong>BED = nd(1 + d/(α/β)); EQD2 = D × (d + α/β)/(2 + α/β)</strong></p><h4>Common constraints (QUANTEC digest)</h4><ul><li>Spinal cord Dmax &lt; 50 Gy (2 Gy/fx) → 1% myelopathy.</li><li>Lung V20 ≤ 30% → pneumonitis ≤ 20%.</li><li>Heart mean: as low as possible; left breast target &lt; 4–5 Gy.</li><li>Parotid mean ≤ 26 Gy to preserve long-term function.</li><li>Rectum V70 &lt; 20–25% (standard-fx prostate 78–80 Gy).</li></ul>"
      },
    ],
    "excel_sheet": None,
    "prev": ["physics.html", "物理", "Physics"],
    "next": ["cns.html", "CNS", "CNS"],
})

PAGES.append({
    "slug": "lingo",
    "emoji": "📚",
    "title_zh": "縮寫與術語速查",
    "title_en": "Acronyms & Lingo",
    "sub_zh": "放射腫瘤科常見縮寫與臨床術語速查表。",
    "sub_en": "Quick-reference glossary of common Rad Onc acronyms and terminology.",
    "sections": [
      {
        "label_zh": "體積與靶區", "label_en": "VOLUMES",
        "h2_zh": "靶區與體積術語 (ICRU 50/62/83)",
        "h2_en": "Target and volume terminology (ICRU 50/62/83)",
        "body_zh": "<ul><li><strong>GTV</strong> Gross Tumor Volume — 影像/臨床可見腫瘤</li><li><strong>CTV</strong> Clinical Target Volume — GTV + 亞臨床散佈</li><li><strong>ITV</strong> Internal Target Volume — CTV + 內部器官運動</li><li><strong>PTV</strong> Planning Target Volume — ITV + set-up 誤差</li><li><strong>OAR</strong> Organ At Risk</li><li><strong>PRV</strong> Planning Risk Volume — OAR + margin</li></ul>",
        "body_en": "<ul><li><strong>GTV</strong> Gross Tumor Volume — clinically/radiographically visible tumor</li><li><strong>CTV</strong> Clinical Target Volume — GTV + subclinical microscopic spread</li><li><strong>ITV</strong> Internal Target Volume — CTV + internal motion</li><li><strong>PTV</strong> Planning Target Volume — ITV + set-up uncertainty</li><li><strong>OAR</strong> Organ At Risk</li><li><strong>PRV</strong> Planning Risk Volume — OAR + margin</li></ul>"
      },
      {
        "label_zh": "劑量學", "label_en": "DOSIMETRY",
        "h2_zh": "劑量與計畫縮寫",
        "h2_en": "Dose & planning acronyms",
        "body_zh": "<ul><li><strong>Gy</strong> Gray；<strong>cGy</strong> centigray（1 Gy = 100 cGy）</li><li><strong>Dmax / Dmin / Dmean</strong> 最大 / 最小 / 平均劑量</li><li><strong>V20 / V70</strong> 接受 ≥ 20 Gy / ≥ 70 Gy 的體積百分比</li><li><strong>D95</strong> 覆蓋 95% 體積的劑量</li><li><strong>CI / HI</strong> Conformity Index / Homogeneity Index</li><li><strong>BED / EQD2</strong> 生物有效劑量 / 等效 2 Gy 分次總劑量</li><li><strong>DVH</strong> Dose Volume Histogram</li></ul>",
        "body_en": "<ul><li><strong>Gy</strong> Gray; <strong>cGy</strong> centigray (1 Gy = 100 cGy)</li><li><strong>Dmax / Dmin / Dmean</strong> Max / min / mean dose</li><li><strong>V20 / V70</strong> Volume % receiving ≥ 20 Gy / ≥ 70 Gy</li><li><strong>D95</strong> Dose covering 95% of volume</li><li><strong>CI / HI</strong> Conformity Index / Homogeneity Index</li><li><strong>BED / EQD2</strong> Biologically effective dose / equivalent 2 Gy total dose</li><li><strong>DVH</strong> Dose Volume Histogram</li></ul>"
      },
      {
        "label_zh": "治療技術", "label_en": "TECHNIQUES",
        "h2_zh": "治療技術縮寫",
        "h2_en": "Modality acronyms",
        "body_zh": "<ul><li><strong>3D-CRT</strong> 3D conformal RT</li><li><strong>IMRT / VMAT</strong> 強度調控 / 弧形</li><li><strong>SBRT / SABR</strong> 立體定位大分次</li><li><strong>SRS</strong> 立體定位放射手術（顱內單次）</li><li><strong>IGRT</strong> Image-Guided RT</li><li><strong>DIBH</strong> Deep Inspiration Breath Hold（左乳）</li><li><strong>Brachytherapy: LDR / HDR / PDR</strong></li><li><strong>SIB</strong> Simultaneous Integrated Boost</li></ul>",
        "body_en": "<ul><li><strong>3D-CRT</strong> 3D conformal RT</li><li><strong>IMRT / VMAT</strong> Intensity-modulated / rotational</li><li><strong>SBRT / SABR</strong> Stereotactic body / ablative RT</li><li><strong>SRS</strong> Stereotactic radiosurgery (intracranial, single fx)</li><li><strong>IGRT</strong> Image-Guided RT</li><li><strong>DIBH</strong> Deep Inspiration Breath Hold (left breast)</li><li><strong>Brachytherapy: LDR / HDR / PDR</strong></li><li><strong>SIB</strong> Simultaneous Integrated Boost</li></ul>"
      },
      {
        "label_zh": "臨床評估", "label_en": "CLINICAL",
        "h2_zh": "臨床評估與副作用分級",
        "h2_en": "Clinical scales & toxicity grading",
        "body_zh": "<ul><li><strong>KPS</strong> Karnofsky Performance Status (0–100)</li><li><strong>ECOG</strong> 0–4 (0 = fully active, 4 = bedridden)</li><li><strong>CTCAE</strong> NCI 副作用分級 1–5 版</li><li><strong>RTOG toxicity</strong> 急性與晚期分級</li><li><strong>RECIST 1.1</strong> 實體瘤反應標準 (CR/PR/SD/PD)</li></ul>",
        "body_en": "<ul><li><strong>KPS</strong> Karnofsky Performance Status (0–100)</li><li><strong>ECOG</strong> 0–4 (0 = fully active, 4 = bedridden)</li><li><strong>CTCAE</strong> NCI toxicity grading v1–5</li><li><strong>RTOG toxicity</strong> acute and late</li><li><strong>RECIST 1.1</strong> Solid tumor response criteria (CR/PR/SD/PD)</li></ul>"
      },
    ],
    "excel_sheet": None,
    "prev": ["radbio.html", "放射生物", "RadBio"],
    "next": ["cns.html", "CNS", "CNS"],
})

# ============================================================
# DISEASE SITES
# ============================================================

PAGES.append({
    "slug": "cns",
    "emoji": "🧠",
    "title_zh": "原發性中樞神經系統腫瘤",
    "title_en": "Adult Primary CNS Tumors",
    "sub_zh": "膠質瘤概論、WHO 2021 分子分類、低惡度膠質瘤、Grade 3 膠質瘤、GBM、復發與放療靶區。",
    "sub_en": "Glioma overview, WHO 2021 molecular classification, low-grade glioma, grade 3 glioma, GBM, recurrence, and RT contouring.",
    "sections": [

      {
        "label_zh": "概觀",
        "label_en": "OVERVIEW",
        "h2_zh": "膠質瘤概論與 WHO 2021 分類",
        "h2_en": "Glioma overview and WHO 2021 classification",
        "body_zh": """
        <p>膠質瘤是<strong>原發性中樞神經系統腫瘤</strong>，源自神經系統支持細胞，包括 astrocytes、oligodendrocytes 與 microglial-lineage cells。與多數癌症不同，膠質瘤通常不以 stage 分期，而以 <strong>WHO grade</strong> 分級；grade 越高，侵襲性通常越強。</p>
        <ul>
          <li><strong>GBM</strong>：成人最常見的原發性 CNS 惡性腫瘤，WHO 2021 下應為 <strong>IDH-wildtype grade 4</strong>。</li>
          <li><strong>Astrocytoma, IDH-mutant</strong>：grade 2–4；若有 CDKN2A/B homozygous deletion，可升為 grade 4。</li>
          <li><strong>Oligodendroglioma, IDH-mutant and 1p/19q-codeleted</strong>：grade 2–3。</li>
        </ul>
        <p>重要分子標記包括 <strong>IDH mutation、1p/19q codeletion、ATRX loss、TP53 mutation、MGMT promoter methylation、EGFR amplification、TERT promoter mutation、chromosome +7/−10、CDKN2A/B deletion</strong>。</p>
        """,
        "body_en": """
        <p>Gliomas are <strong>primary CNS tumors</strong> arising from glial-supporting cells, including astrocytic, oligodendroglial, and microglial-lineage cells. Unlike many extracranial cancers, gliomas are generally <strong>graded rather than staged</strong>; higher grade usually means more aggressive biology.</p>
        <ul>
          <li><strong>Glioblastoma</strong>: the most common adult primary CNS malignancy; under WHO 2021 it is <strong>IDH-wildtype grade 4</strong>.</li>
          <li><strong>Astrocytoma, IDH-mutant</strong>: grade 2–4; CDKN2A/B homozygous deletion can upgrade to grade 4.</li>
          <li><strong>Oligodendroglioma, IDH-mutant and 1p/19q-codeleted</strong>: grade 2–3.</li>
        </ul>
        <p>Key molecular markers: <strong>IDH mutation, 1p/19q codeletion, ATRX loss, TP53 mutation, MGMT promoter methylation, EGFR amplification, TERT promoter mutation, chromosome +7/−10, and CDKN2A/B deletion</strong>.</p>
        """
      },

      {
        "label_zh": "診斷",
        "label_en": "WORKUP",
        "h2_zh": "檢查、影像與初始處置",
        "h2_en": "Workup, imaging, and initial management",
        "body_zh": """
        <p>常見表現包括頭痛、局部神經缺損、癲癇、意識或認知改變。初始評估包括完整病史與神經學檢查；若懷疑顱壓上升，需眼底檢查。</p>
        <ul>
          <li><strong>實驗室</strong>：CBC、CMP。</li>
          <li><strong>影像</strong>：CT head without contrast 可先排除出血；標準診斷影像為 <strong>MRI brain with and without gadolinium</strong>，包含 T1 post-contrast、T1c FSPGR 與 T2/FLAIR。</li>
          <li><strong>其他</strong>：若有癲癇考慮 EEG；可做基準 neurocognitive testing。</li>
        </ul>
        <p>MRI 上，GBM 常見 ring enhancement、necrosis、edema；低級別膠質瘤不一定顯影。若有 peripheral nodular enhancement 或 necrosis，較支持高級別病灶。</p>
        """,
        "body_en": """
        <p>Typical presentations include headache, focal neurologic deficit, seizure, confusion, or cognitive change. Initial assessment includes full history and neurologic examination; fundoscopy is considered when increased intracranial pressure is suspected.</p>
        <ul>
          <li><strong>Labs</strong>: CBC and CMP.</li>
          <li><strong>Imaging</strong>: CT head without contrast may rule out bleeding; standard evaluation is <strong>MRI brain with and without gadolinium</strong>, including T1 post-contrast, T1c FSPGR, and T2/FLAIR sequences.</li>
          <li><strong>Other</strong>: EEG if seizures; baseline neurocognitive testing can be useful.</li>
        </ul>
        <p>GBM commonly shows contrast enhancement, necrosis, and edema. Lower-grade gliomas may be non-enhancing; nodular enhancement or necrosis suggests higher-grade disease.</p>
        """
      },

      {
        "label_zh": "治療原則",
        "label_en": "PRINCIPLES",
        "h2_zh": "手術、放療與化療總覽",
        "h2_en": "Surgery, radiotherapy, and chemotherapy overview",
        "body_zh": """
        <p><strong>最大安全切除</strong>是治療核心，目標是在保留神經功能下達成 gross total resection。若腫瘤位於深部、eloquent cortex 或 multifocal，可考慮 subtotal resection、debulking 或 stereotactic biopsy。術後應於 <strong>24–48 小時內，最晚 72 小時內</strong>做 MRI 評估切除範圍。</p>
        <ul>
          <li><strong>GBM</strong>：60 Gy/30 fx；poor PS 可用 40 Gy/15 fx、34 Gy/10 fx、25 Gy/5 fx 或 TMZ alone。</li>
          <li><strong>Grade 3 glioma</strong>：59.4 Gy/33 fx。</li>
          <li><strong>Low-grade glioma</strong>：54 Gy/30 fx。</li>
        </ul>
        <p><strong>TMZ</strong> 是口服 alkylating agent，會在 DNA guanine 加 methyl group，MGMT promoter methylation 會降低 MGMT 修復能力，因此預測 TMZ benefit 較佳。GBM concurrent TMZ 劑量為 75 mg/m²/day；adjuvant TMZ 為 150–200 mg/m²/day, days 1–5, q28 days，通常 6 cycles。</p>
        <p><strong>PCV</strong> 包含 procarbazine、lomustine/CCNU、vincristine，常用於 IDH-mutant, 1p/19q-codeleted oligodendroglioma。</p>
        """,
        "body_en": """
        <p><strong>Maximal safe resection</strong> is central, aiming for gross total resection while preserving neurologic function. Deep-seated, eloquent, or multifocal tumors may require subtotal resection, debulking, or stereotactic biopsy. Postoperative MRI should be obtained within <strong>24–48 hours, and no later than 72 hours</strong>, to assess extent of resection.</p>
        <ul>
          <li><strong>GBM</strong>: 60 Gy/30 fx; poor performance status may receive 40 Gy/15 fx, 34 Gy/10 fx, 25 Gy/5 fx, or TMZ alone.</li>
          <li><strong>Grade 3 glioma</strong>: 59.4 Gy/33 fx.</li>
          <li><strong>Low-grade glioma</strong>: 54 Gy/30 fx.</li>
        </ul>
        <p><strong>Temozolomide</strong> is an oral alkylating agent that methylates DNA guanine bases. MGMT promoter methylation reduces MGMT-mediated repair and predicts greater TMZ benefit. GBM dosing: concurrent TMZ 75 mg/m²/day during RT; adjuvant TMZ 150–200 mg/m²/day on days 1–5 every 28 days, typically 6 cycles.</p>
        <p><strong>PCV</strong> consists of procarbazine, lomustine/CCNU, and vincristine, and is especially important for IDH-mutant, 1p/19q-codeleted oligodendroglioma.</p>
        """
      },

      {
        "label_zh": "低惡度膠質瘤",
        "label_en": "LGG",
        "h2_zh": "低惡度膠質瘤 — Grade 2",
        "h2_en": "Low-grade gliomas — Grade 2",
        "body_zh": """
        <p><strong>風險評估</strong>：Pignatti/SATAN 高風險因子包括 <strong>Size ≥6 cm、Age &gt;40、Tumor crossing midline、Astrocytoma histology、Neurologic symptoms</strong>。RTOG 9802 也指出 residual disease、astrocytoma/oligoastrocytoma histology、tumor size 會影響復發。</p>
        <ul>
          <li><strong>EORTC 22844</strong>：45 Gy/25 fx vs 59.4 Gy/33 fx，dose escalation 未改善 OS 或 PFS；5-year OS 59% vs 58%，5-year PFS 50% vs 47%。</li>
          <li><strong>RTOG 9110</strong>：50.4 Gy/28 fx vs 64.8 Gy/36 fx，長期結果未見 OS/PFS benefit；高劑量增加 radiation necrosis 風險。</li>
          <li><strong>EORTC 22845</strong>：immediate RT 54 Gy/30 fx vs observation with RT at progression；immediate RT 改善 5-year PFS 55% vs 35% 與 1-year seizure rate 25% vs 41%，但未改善 OS。</li>
          <li><strong>RTOG 9802 observation cohort</strong>：&lt;40 歲且 GTR 者仍有 5-year recurrence 58%；5-year OS 93%，5-year PFS 42%。</li>
          <li><strong>RTOG 9802 phase III</strong>：高風險 LGG 接受 RT 54 Gy/30 fx ± PCV；加入 PCV 改善 10-year OS 60% vs 40%，10-year PFS 51% vs 21%。</li>
          <li><strong>RTOG 0424</strong>：高風險 LGG 使用 RT 54 Gy/30 fx + concurrent/adjuvant TMZ，3-year OS 74% vs historical 54%；但屬 single-arm phase II，未直接比較 TMZ 與 PCV。</li>
        </ul>
        <p><strong>實務重點</strong>：GTR 且低風險者可討論嚴密追蹤；高風險或殘餘腫瘤者通常給 adjuvant RT。最有 phase III OS 證據的標準是 <strong>54 Gy/30 fx followed by PCV ×6 cycles</strong>。</p>
        """,
        "body_en": """
        <p><strong>Risk assessment</strong>: Pignatti/SATAN high-risk factors are <strong>Size ≥6 cm, Age &gt;40, Tumor crossing midline, Astrocytoma histology, and Neurologic symptoms</strong>. RTOG 9802 also identified residual disease, astrocytoma/oligoastrocytoma histology, and tumor size as recurrence predictors.</p>
        <ul>
          <li><strong>EORTC 22844</strong>: 45 Gy/25 fx vs 59.4 Gy/33 fx; dose escalation did not improve OS or PFS; 5-year OS 59% vs 58%, 5-year PFS 50% vs 47%.</li>
          <li><strong>RTOG 9110</strong>: 50.4 Gy/28 fx vs 64.8 Gy/36 fx; no long-term OS/PFS benefit from higher dose, with more radiation necrosis concern.</li>
          <li><strong>EORTC 22845</strong>: immediate RT 54 Gy/30 fx vs observation with RT at progression; immediate RT improved 5-year PFS 55% vs 35% and 1-year seizure rate 25% vs 41%, but not OS.</li>
          <li><strong>RTOG 9802 observation cohort</strong>: even patients &lt;40 years old with GTR had 5-year recurrence of 58%; 5-year OS 93%, 5-year PFS 42%.</li>
          <li><strong>RTOG 9802 phase III</strong>: high-risk LGG treated with RT 54 Gy/30 fx ± PCV; PCV improved 10-year OS 60% vs 40% and 10-year PFS 51% vs 21%.</li>
          <li><strong>RTOG 0424</strong>: high-risk LGG treated with RT 54 Gy/30 fx plus concurrent/adjuvant TMZ; 3-year OS 74% vs 54% historical control, but this was single-arm phase II and did not directly compare TMZ with PCV.</li>
        </ul>
        <p><strong>Practice point</strong>: low-risk GTR patients may be observed with close MRI follow-up; high-risk or residual disease usually warrants adjuvant RT. The strongest phase III OS evidence supports <strong>54 Gy/30 fx followed by PCV ×6 cycles</strong>.</p>
        """
      },

      {
        "label_zh": "Grade 3 Oligo",
        "label_en": "G3 OLIGO",
        "h2_zh": "Grade 3 Oligodendroglioma — IDH-mutant, 1p/19q-codeleted",
        "h2_en": "Grade 3 oligodendroglioma — IDH-mutant, 1p/19q-codeleted",
        "body_zh": """
        <p>分子特徵：<strong>IDH-mutant、1p/19q-codeleted</strong>，通常沒有 ATRX loss/mutation 或 TP53 mutation。標準放療劑量為 <strong>59.4 Gy/33 fx</strong>。</p>
        <ul>
          <li><strong>RTOG 9402</strong>：RT 59.4 Gy ± neoadjuvant PCV ×4；整體 cohort OS 差異不明顯，但 1p/19q-codeleted subgroup 加 PCV 顯著改善 OS，約 14.7 vs 7.3 years。</li>
          <li><strong>EORTC 26951</strong>：RT 59.4 Gy ± adjuvant PCV ×6；PCV 改善 OS 42.3 vs 31.6 months 與 PFS 25.3 vs 13.2 months，1p/19q-codeleted benefit 更明顯。</li>
          <li><strong>Long-term combined analysis</strong>：RT + PCV 可達約 20-year OS 35%；benefit 尤其集中於 1p/19q-codeleted tumors。</li>
          <li><strong>Original CODEL</strong>：RT alone、RT + TMZ、TMZ alone；TMZ alone PFS 較差，支持治療需包含 RT + chemotherapy。</li>
          <li><strong>POLA cohort</strong>：非隨機資料顯示 PCV/RT 可能優於 TMZ/RT；5-year OS 89% vs 75%，10-year OS 72% vs 60%。</li>
        </ul>
        <p><strong>實務重點</strong>：目前最強證據支持 <strong>RT + PCV</strong>。TMZ 較方便但證據層級較弱；需等待 redesigned CODEL 的 RT/PCV vs RT/TMZ 結果。</p>
        """,
        "body_en": """
        <p>Molecular profile: <strong>IDH-mutant and 1p/19q-codeleted</strong>, usually without ATRX loss/mutation or TP53 mutation. Standard RT dose is <strong>59.4 Gy/33 fx</strong>.</p>
        <ul>
          <li><strong>RTOG 9402</strong>: RT 59.4 Gy ± neoadjuvant PCV ×4; no OS difference in the entire cohort, but PCV significantly improved OS in 1p/19q-codeleted tumors, approximately 14.7 vs 7.3 years.</li>
          <li><strong>EORTC 26951</strong>: RT 59.4 Gy ± adjuvant PCV ×6; PCV improved OS 42.3 vs 31.6 months and PFS 25.3 vs 13.2 months, with greater benefit in 1p/19q-codeleted disease.</li>
          <li><strong>Long-term combined analysis</strong>: RT + PCV achieved approximately 35% 20-year OS, with benefit concentrated in 1p/19q-codeleted tumors.</li>
          <li><strong>Original CODEL</strong>: RT alone, RT + TMZ, or TMZ alone; TMZ alone had inferior PFS, supporting treatment with both RT and chemotherapy.</li>
          <li><strong>POLA cohort</strong>: non-randomized data suggested PCV/RT may outperform TMZ/RT; 5-year OS 89% vs 75%, 10-year OS 72% vs 60%.</li>
        </ul>
        <p><strong>Practice point</strong>: the strongest evidence supports <strong>RT + PCV</strong>. TMZ is more convenient but less established; the redesigned CODEL trial is intended to compare RT/PCV vs RT/TMZ.</p>
        """
      },

      {
        "label_zh": "Grade 3 Astro",
        "label_en": "G3 ASTRO",
        "h2_zh": "Grade 3 Astrocytoma — IDH-mutant, 1p/19q-intact",
        "h2_en": "Grade 3 astrocytoma — IDH-mutant, 1p/19q-intact",
        "body_zh": """
        <p>分子特徵：<strong>IDH-mutant、1p/19q-intact</strong>，常見 ATRX loss/mutation 或 TP53 mutation；若為 grade 3，通常應為 <strong>CDKN2A/B wildtype</strong>。標準放療劑量為 <strong>59.4 Gy/33 fx</strong>。</p>
        <ul>
          <li><strong>NOA-04</strong>：RT → chemotherapy at progression vs upfront chemotherapy → RT at progression，TTF、OS、PFS 類似；分子特徵，尤其 IDH1 mutation，比傳統 histology 更能預測預後。</li>
          <li><strong>CATNON</strong>：751 位 1p/19q non-codeleted anaplastic glioma；RT alone、RT + concurrent TMZ、RT + adjuvant TMZ、RT + concurrent/adjuvant TMZ 四組比較。</li>
          <li>CATNON 第二次 interim analysis 顯示 <strong>concurrent TMZ futility</strong>；adjuvant TMZ 明顯改善 OS，82.3 vs 46.9 months。</li>
          <li>CATNON 的 OS benefit 主要限於 <strong>IDH-mutant</strong> tumors；TMZ 主要毒性為 hematologic toxicity。</li>
        </ul>
        <p><strong>實務重點</strong>：Grade 3 IDH-mutant astrocytoma 的核心策略是 <strong>RT 59.4 Gy/33 fx followed by adjuvant TMZ</strong>；concurrent TMZ 不是主要 benefit driver。</p>
        """,
        "body_en": """
        <p>Molecular profile: <strong>IDH-mutant and 1p/19q-intact</strong>, often with ATRX loss/mutation or TP53 mutation; grade 3 disease should generally be <strong>CDKN2A/B wildtype</strong>. Standard RT dose is <strong>59.4 Gy/33 fx</strong>.</p>
        <ul>
          <li><strong>NOA-04</strong>: RT followed by chemotherapy at progression vs upfront chemotherapy followed by RT at progression showed similar TTF, OS, and PFS; molecular features, especially IDH1 mutation, were more prognostic than histology.</li>
          <li><strong>CATNON</strong>: 751 patients with 1p/19q non-codeleted anaplastic glioma randomized to RT alone, RT + concurrent TMZ, RT + adjuvant TMZ, or RT + concurrent/adjuvant TMZ.</li>
          <li>CATNON second interim analysis declared <strong>futility for concurrent TMZ</strong>; adjuvant TMZ significantly improved OS, 82.3 vs 46.9 months.</li>
          <li>CATNON OS benefit was mainly seen in <strong>IDH-mutant</strong> tumors; TMZ toxicity was primarily hematologic.</li>
        </ul>
        <p><strong>Practice point</strong>: for grade 3 IDH-mutant astrocytoma, the key regimen is <strong>RT 59.4 Gy/33 fx followed by adjuvant TMZ</strong>; concurrent TMZ is not the major driver of benefit.</p>
        """
      },

      {
        "label_zh": "GBM",
        "label_en": "GBM",
        "h2_zh": "Glioblastoma — IDH-wildtype Grade 4",
        "h2_en": "Glioblastoma — IDH-wildtype Grade 4",
        "body_zh": """
        <p>GBM 是成人最常見的原發性腦部惡性腫瘤，治療後 median OS 約 14 個月，中位年齡約 65 歲，男性略多。病理特徵可用 <strong>AMEN</strong> 記憶：Atypia、Mitosis、Endothelial proliferation、Necrosis。WHO 2021 下 GBM 必須是 <strong>IDH-wildtype</strong>，並可伴隨 TERT promoter mutation、EGFR amplification、chromosome +7/−10。<strong>MGMT promoter methylation</strong> 預測 TMZ benefit 較佳。</p>
        <ul>
          <li><strong>BTSG dose escalation</strong>：建立 60 Gy/30 fx 為 GBM 標準 RT 劑量。</li>
          <li><strong>Stupp regimen</strong>：60 Gy/30 fx + concurrent TMZ 75 mg/m²/day → adjuvant TMZ 150–200 mg/m² days 1–5 q28 days ×6 cycles；OS 14.6 vs 12.1 months，PFS 6.9 vs 5.0 months。</li>
          <li><strong>TTFields / EF-14</strong>：maintenance TMZ + TTFields ≥18 h/day 改善 PFS 6.7 vs 4.0 months、OS 20.9 vs 16.0 months；主要副作用為頭皮紅、癢、刺激。</li>
          <li><strong>CeTeG/NOA-09</strong>：MGMT-methylated GBM 中加入 CCNU 使 OS 48 vs 31 months，但 PFS 未改善且毒性較高，因此未廣泛成為標準。</li>
        </ul>
        <p><strong>標準流程</strong>：clinical trial whenever possible → maximal safe resection → postoperative MRI &lt;72 h → concurrent chemoRT within 3–6 weeks → adjuvant TMZ ± TTFields。</p>
        """,
        "body_en": """
        <p>GBM is the most common adult primary brain malignancy, with median OS around 14 months with treatment, median age around 65, and slight male predominance. Histologic features can be remembered as <strong>AMEN</strong>: Atypia, Mitosis, Endothelial proliferation, and Necrosis. Under WHO 2021, GBM must be <strong>IDH-wildtype</strong> and may be defined by TERT promoter mutation, EGFR amplification, or chromosome +7/−10. <strong>MGMT promoter methylation</strong> predicts greater TMZ benefit.</p>
        <ul>
          <li><strong>BTSG dose escalation</strong>: established 60 Gy/30 fx as the standard GBM RT dose.</li>
          <li><strong>Stupp regimen</strong>: 60 Gy/30 fx + concurrent TMZ 75 mg/m²/day → adjuvant TMZ 150–200 mg/m² days 1–5 every 28 days ×6 cycles; OS 14.6 vs 12.1 months and PFS 6.9 vs 5.0 months.</li>
          <li><strong>TTFields / EF-14</strong>: maintenance TMZ + TTFields ≥18 h/day improved PFS 6.7 vs 4.0 months and OS 20.9 vs 16.0 months; main toxicity is scalp redness, itchiness, and irritation.</li>
          <li><strong>CeTeG/NOA-09</strong>: in MGMT-methylated GBM, adding CCNU improved OS 48 vs 31 months but not PFS and increased toxicity, so it has not been widely adopted as routine standard.</li>
        </ul>
        <p><strong>Standard flow</strong>: clinical trial whenever possible → maximal safe resection → postoperative MRI &lt;72 h → concurrent chemoradiation within 3–6 weeks → adjuvant TMZ ± TTFields.</p>
        """
      },

      {
        "label_zh": "老年 GBM",
        "label_en": "ELDERLY GBM",
        "h2_zh": "老年或體能較差 GBM",
        "h2_en": "Elderly or frail GBM",
        "body_zh": """
        <p>老年或 frail GBM 需高度個別化。若 60–70 歲以上但體能佳，仍可考慮標準 60 Gy/30 fx + TMZ；若 poor PS，可選 hypofractionated RT 或 TMZ alone，尤其 MGMT promoter methylated 者。</p>
        <ul>
          <li><strong>Canadian trial</strong>：≥60 歲，60 Gy/30 fx vs 40 Gy/15 fx；OS 5.1 vs 5.6 months，40 Gy/15 fx non-inferior 且 steroid increase 較少。</li>
          <li><strong>Nordic trial</strong>：≥60 歲，60 Gy/30 fx vs 34 Gy/10 fx vs TMZ alone；≥70 歲中 TMZ alone 或 34 Gy/10 fx 優於 60 Gy。</li>
          <li><strong>IAEA trial</strong>：40 Gy/15 fx vs 25 Gy/5 fx；OS 6.4 vs 7.9 months，PFS 與 QoL 無明顯差異。</li>
          <li><strong>Perry NEJM 2017</strong>：≥65 歲，40 Gy/15 fx ± TMZ；加入 TMZ 改善 OS 9.3 vs 7.6 months、PFS 5.3 vs 3.9 months，MGMT-methylated benefit 更大。</li>
        </ul>
        """,
        "body_en": """
        <p>Elderly or frail GBM requires individualized treatment. Fit patients aged ≥60–70 may still receive standard 60 Gy/30 fx + TMZ. Poor-performance patients may receive hypofractionated RT or TMZ alone, especially if MGMT promoter methylated.</p>
        <ul>
          <li><strong>Canadian trial</strong>: age ≥60, 60 Gy/30 fx vs 40 Gy/15 fx; OS 5.1 vs 5.6 months, supporting 40 Gy/15 fx as non-inferior with less steroid increase.</li>
          <li><strong>Nordic trial</strong>: age ≥60, 60 Gy/30 fx vs 34 Gy/10 fx vs TMZ alone; in patients ≥70, TMZ alone or 34 Gy/10 fx performed better than 60 Gy.</li>
          <li><strong>IAEA trial</strong>: 40 Gy/15 fx vs 25 Gy/5 fx; OS 6.4 vs 7.9 months, with similar PFS and QoL.</li>
          <li><strong>Perry NEJM 2017</strong>: age ≥65, 40 Gy/15 fx ± TMZ; TMZ improved OS 9.3 vs 7.6 months and PFS 5.3 vs 3.9 months, with greater benefit in MGMT-methylated tumors.</li>
        </ul>
        """
      },

      {
        "label_zh": "升劑量",
        "label_en": "ESCALATION",
        "h2_zh": "GBM dose escalation、SRS boost 與 brachytherapy boost",
        "h2_en": "GBM dose escalation, SRS boost, and brachytherapy boost",
        "body_zh": """
        <p>目前沒有足夠證據支持在臨床試驗外常規使用 GBM dose escalation、SRS boost 或 brachytherapy boost。</p>
        <ul>
          <li><strong>18F-DOPA PET-guided dose escalation phase II</strong>：51/60/76 Gy SIB 顯示某些 subgroup PFS 或 OS 改善訊號，但屬 phase II/historical control。</li>
          <li><strong>NRG-BN001</strong>：60 Gy/30 fx vs 75 Gy/30 fx IMRT dose-intensification，初步結果未顯示 PFS 或 OS benefit。</li>
          <li><strong>RTOG 9305</strong>：SRS boost + RT + BCNU vs RT + BCNU，OS 13.5 vs 13.6 months，無 benefit。</li>
          <li><strong>Brachytherapy boost trials</strong>：BTSG NIH 87-01 與 Laperriere RCT 均未顯示 GBM benefit。</li>
        </ul>
        """,
        "body_en": """
        <p>Current evidence does not support routine GBM dose escalation, SRS boost, or brachytherapy boost outside clinical trials.</p>
        <ul>
          <li><strong>18F-DOPA PET-guided dose-escalation phase II</strong>: 51/60/76 Gy SIB showed signals of PFS or OS improvement in selected subgroups, but used phase II/historical-control data.</li>
          <li><strong>NRG-BN001</strong>: 60 Gy/30 fx vs 75 Gy/30 fx IMRT dose-intensification; initial results did not show PFS or OS benefit.</li>
          <li><strong>RTOG 9305</strong>: SRS boost + RT + BCNU vs RT + BCNU; OS 13.5 vs 13.6 months, no benefit.</li>
          <li><strong>Brachytherapy boost trials</strong>: BTSG NIH 87-01 and the Laperriere RCT did not show GBM benefit.</li>
        </ul>
        """
      },

      {
        "label_zh": "復發 GBM",
        "label_en": "RECURRENT GBM",
        "h2_zh": "復發 GBM、pseudoprogression 與 salvage treatment",
        "h2_en": "Recurrent GBM, pseudoprogression, and salvage treatment",
        "body_zh": """
        <p>約 <strong>80%</strong> GBM 復發發生於原發腫瘤 2 cm 內。RT 後追蹤建議 brain MRI 於完成 RT 後 2–8 週，之後 q2–4 months ×3 years，再 q3–6 months indefinitely。</p>
        <p><strong>Pseudoprogression</strong> 常在 chemoRT 後約 6 個月內發生，通常會逐漸消退；<strong>radiation necrosis</strong> 常在 RT 後約 1 年發生，較不會自行消退。MGMT methylation 與 pseudoprogression 風險較高相關。</p>
        <ul>
          <li><strong>RANO progression/recurrence criteria</strong>：enhancing lesion perpendicular diameters sum 增加 ≥25%、T2/FLAIR nonenhancing lesion 顯著增加、新病灶、nonmeasurable lesion 明確進展、或非其他原因造成的 clinical deterioration。</li>
          <li><strong>Re-resection</strong>：若有 mass effect 或可安全切除可考慮。</li>
          <li><strong>Reirradiation</strong>：常用 35 Gy/10 fx 或其他 hypofractionated regimens；Fogh retrospective data median OS 約 11 months。</li>
          <li><strong>Bevacizumab</strong>：抗 VEGF-A；recurrent GBM 可用。RTOG 1205 顯示 bevacizumab + re-RT 改善 PFS 7.1 vs 3.8 months，但 OS 無差異。</li>
          <li><strong>GammaTile/STaRT</strong>：Cs-131 brachytherapy tile，可作特定復發情境考量。</li>
        </ul>
        """,
        "body_en": """
        <p>Approximately <strong>80%</strong> of GBM recurrences occur within 2 cm of the primary tumor. Follow-up after RT: brain MRI at 2–8 weeks, then every 2–4 months for 3 years, then every 3–6 months indefinitely.</p>
        <p><strong>Pseudoprogression</strong> usually occurs within about 6 months after chemoradiation and often subsides; <strong>radiation necrosis</strong> usually occurs around 1 year after RT and is less likely to subside spontaneously. MGMT methylation is associated with higher pseudoprogression risk.</p>
        <ul>
          <li><strong>RANO progression/recurrence criteria</strong>: ≥25% increase in sum of perpendicular diameters of enhancing lesions, significant increase in T2/FLAIR non-enhancing disease, new lesion, clear progression of nonmeasurable disease, or definite clinical deterioration not otherwise explained.</li>
          <li><strong>Re-resection</strong>: consider for mass effect or safely resectable recurrence.</li>
          <li><strong>Reirradiation</strong>: often 35 Gy/10 fx or other hypofractionated regimens; Fogh retrospective data reported median OS around 11 months.</li>
          <li><strong>Bevacizumab</strong>: anti-VEGF-A therapy used in recurrent GBM. RTOG 1205 showed bevacizumab + re-RT improved PFS 7.1 vs 3.8 months but not OS.</li>
          <li><strong>GammaTile/STaRT</strong>: Cs-131 brachytherapy tile may be considered in selected recurrent settings.</li>
        </ul>
        """
      },

      {
        "label_zh": "靶區",
        "label_en": "CONTOURING",
        "h2_zh": "GBM 放療靶區與正常組織限制",
        "h2_en": "GBM RT contouring and organ-at-risk constraints",
        "body_zh": """
        <p><strong>EORTC/Stupp method</strong>：GTV = postoperative T1 contrast-enhancing cavity/residual disease；CTV = GTV + 2 cm；PTV = CTV + 0.5 cm。部分教學資料亦提到 T1c cavity + 1.5 cm margin，並依 T2 mass-like tumor 調整。</p>
        <p><strong>RTOG method</strong>：T2/FLAIR edema volume 給 46 Gy/23 fx，再 sequential boost 至 T1 contrast-enhancing cavity/residual tumor 到 60 Gy。常用 GTV1 = T2/FLAIR，CTV1 = GTV1 + 2 cm，PTV1 = CTV1 + 0.3–0.5 cm；GTV2 = postop T1 cavity/residual，CTV2 = GTV2 + 2 cm，PTV2 = CTV2 + 0.3–0.5 cm。</p>
        <ul>
          <li>Coverage：100% GTV covered by 60 Gy；95% PTV covered by prescription dose。</li>
          <li>Optic nerves/chiasm：常見 max 約 52–54 Gy；RTOG 0825 約 optic nerves 55 Gy、chiasm 56 Gy。</li>
          <li>Brainstem：max 約 54 Gy，PRV 可至 60 Gy；RTOG 0825 約 60 Gy。</li>
          <li>Eyes：約 15 Gy；retina 約 50 Gy。</li>
          <li>Cochlea：mean &lt;40–45 Gy，ALARA。</li>
          <li>Lens：約 6 Gy。</li>
        </ul>
        """,
        "body_en": """
        <p><strong>EORTC/Stupp method</strong>: GTV = postoperative T1 contrast-enhancing cavity/residual disease; CTV = GTV + 2 cm; PTV = CTV + 0.5 cm. The teaching slides also mention a T1c cavity + 1.5 cm margin approach, modified by mass-like T2 disease.</p>
        <p><strong>RTOG method</strong>: T2/FLAIR edema volume to 46 Gy/23 fx, then sequential boost to the T1 contrast-enhancing cavity/residual tumor to 60 Gy. Typical definitions: GTV1 = T2/FLAIR, CTV1 = GTV1 + 2 cm, PTV1 = CTV1 + 0.3–0.5 cm; GTV2 = postop T1 cavity/residual, CTV2 = GTV2 + 2 cm, PTV2 = CTV2 + 0.3–0.5 cm.</p>
        <ul>
          <li>Coverage: 100% of GTV covered by 60 Gy; 95% of PTV covered by prescription dose.</li>
          <li>Optic nerves/chiasm: common max around 52–54 Gy; RTOG 0825 approximately optic nerves 55 Gy and chiasm 56 Gy.</li>
          <li>Brainstem: max around 54 Gy, PRV up to 60 Gy; RTOG 0825 approximately 60 Gy.</li>
          <li>Eyes: approximately 15 Gy; retina approximately 50 Gy.</li>
          <li>Cochlea: mean &lt;40–45 Gy, ALARA.</li>
          <li>Lens: approximately 6 Gy.</li>
        </ul>
        """
      },

      {
        "label_zh": "速記",
        "label_en": "QUICK DOSES",
        "h2_zh": "考試速記：劑量與關鍵 regimen",
        "h2_en": "Exam quick facts: doses and key regimens",
        "body_zh": """
        <ul>
          <li><strong>LGG</strong>：54 Gy/30 fx；高風險 → RT + PCV ×6。</li>
          <li><strong>Grade 3 oligodendroglioma</strong>：59.4 Gy/33 fx + PCV。</li>
          <li><strong>Grade 3 astrocytoma, IDH-mutant</strong>：59.4 Gy/33 fx + adjuvant TMZ。</li>
          <li><strong>GBM standard</strong>：60 Gy/30 fx + concurrent TMZ 75 mg/m²/day → adjuvant TMZ 150–200 mg/m² days 1–5 q28 days ×6 ± TTFields。</li>
          <li><strong>Elderly/frail GBM</strong>：40 Gy/15 fx ± TMZ、34 Gy/10 fx、25 Gy/5 fx 或 TMZ alone。</li>
          <li><strong>Recurrent GBM re-RT</strong>：常見 35 Gy/10 fx；bevacizumab ± re-RT 可改善 PFS 但未改善 OS。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>LGG</strong>: 54 Gy/30 fx; high-risk → RT + PCV ×6.</li>
          <li><strong>Grade 3 oligodendroglioma</strong>: 59.4 Gy/33 fx + PCV.</li>
          <li><strong>Grade 3 astrocytoma, IDH-mutant</strong>: 59.4 Gy/33 fx + adjuvant TMZ.</li>
          <li><strong>GBM standard</strong>: 60 Gy/30 fx + concurrent TMZ 75 mg/m²/day → adjuvant TMZ 150–200 mg/m² days 1–5 q28 days ×6 ± TTFields.</li>
          <li><strong>Elderly/frail GBM</strong>: 40 Gy/15 fx ± TMZ, 34 Gy/10 fx, 25 Gy/5 fx, or TMZ alone.</li>
          <li><strong>Recurrent GBM re-RT</strong>: commonly 35 Gy/10 fx; bevacizumab ± re-RT may improve PFS but not OS.</li>
        </ul>
        """
      },

    ],
    "excel_sheet": "CNS",
    "trial_filter": [
        "glioma", "glioblastoma", "gbm", "astrocytoma", "oligodendroglioma",
        "low-grade glioma", "anaplastic glioma", "IDH", "1p19q", "1p/19q",
        "MGMT", "temozolomide", "PCV", "TTFields", "meningioma", "pituitary",
        "ependymoma", "chordoma"
    ],
    "prev": ["radbio.html", "放射生物", "RadBio"],
    "next": ["brain-mets.html", "腦轉移", "Brain Mets"],
})

PAGES.append({
    "slug": "cns",
    "emoji": "🧠",
    "title_zh": "中樞神經系統腫瘤",
    "title_en": "Central Nervous System Tumors",
    "sub_zh": "膠質瘤、低級別膠質瘤、第三級膠質瘤、膠質母細胞瘤、復發性膠質母細胞瘤：分子分類、放療劑量、化療、電場治療、影像判讀、復發鑑別與臨床試驗。",
    "sub_en": "Glioma, low-grade glioma, grade III glioma, glioblastoma, and recurrent glioblastoma: molecular classification, radiotherapy dose, chemotherapy, tumor treating fields, imaging interpretation, recurrence assessment, and clinical trials.",
    "sections": [

      {
        "label_zh": "總覽",
        "label_en": "OVERVIEW",
        "h2_zh": "膠質瘤總論與中樞神經系統腫瘤治療邏輯",
        "h2_en": "Glioma overview and CNS tumor treatment logic",
        "body_zh": """
        <p>膠質瘤是中樞神經系統最重要的原發性腫瘤，也是成人原發性中樞神經系統惡性腫瘤最常見的來源。膠質瘤來自神經膠質細胞，也就是神經系統的支持細胞，包括星形膠質細胞、少突膠質細胞與小膠質細胞。</p>
        <ul>
          <li><strong>與一般實體癌不同</strong>：膠質瘤通常不使用傳統「第一期到第四期」分期，因為它們一般不常規轉移到中樞神經系統以外。臨床上更重要的是世界衛生組織（WHO）分級、分子分型、手術切除程度與病人功能狀態。</li>
          <li><strong>分級概念</strong>：WHO 第 1–2 級通常屬於低級別膠質瘤；WHO 第 3 級為間變性膠質瘤；WHO 第 4 級包含膠質母細胞瘤與分子上被升級為第 4 級的星形膠質細胞瘤。</li>
          <li><strong>膠質母細胞瘤（GBM）</strong>：是成人最常見的原發性中樞神經系統惡性腫瘤，約占成人原發性中樞神經系統惡性腫瘤的 80%。臨床行為快速且侵襲性強，中位總生存期約 14 個月。</li>
          <li><strong>第三級膠質瘤</strong>：傳統稱為間變性膠質瘤，約占高級別膠質瘤的 25%。現代分類需先區分少突膠質細胞瘤與星形膠質細胞瘤，因為兩者治療證據不同。</li>
          <li><strong>低級別膠質瘤</strong>：較少見、異質性高，較常見於年輕成人與兒童。治療重點不是單純「是否治療」，而是依年齡、症狀、腫瘤大小、跨中線、病理型態與切除程度決定觀察、放療或放療加化療。</li>
          <li><strong>治療總原則</strong>：盡可能安全切除，依病理與分子分型決定術後放療劑量與全身治療；若是膠質母細胞瘤，臨床試驗應盡量優先考慮。</li>
        </ul>
        """,
        "body_en": """
        <p>Gliomas are the most important primary tumors of the central nervous system and represent the most common source of adult primary CNS malignancy. They arise from glial cells, the supportive cells of the nervous system, including astrocytes, oligodendrocytes, and microglial cells.</p>
        <ul>
          <li><strong>Different from most solid tumors</strong>: gliomas are usually not staged from stage I to IV because they do not routinely metastasize outside the CNS. WHO grade, molecular subtype, extent of resection, and functional status are more important.</li>
          <li><strong>Grading concept</strong>: WHO grade 1–2 tumors are usually low-grade gliomas; WHO grade 3 tumors are anaplastic gliomas; WHO grade 4 includes glioblastoma and molecularly upgraded grade 4 astrocytoma.</li>
          <li><strong>Glioblastoma (GBM)</strong>: the most common adult primary CNS malignancy, accounting for about 80% of adult primary CNS malignant tumors. It behaves aggressively, with median overall survival around 14 months.</li>
          <li><strong>Grade III glioma</strong>: historically called anaplastic glioma and accounting for about 25% of high-grade gliomas. Modern classification separates oligodendroglioma from astrocytoma because the treatment evidence differs.</li>
          <li><strong>Low-grade glioma</strong>: less common and heterogeneous, occurring more often in young adults and children. Management is risk-adapted rather than simply treatment versus no treatment.</li>
          <li><strong>Overall treatment principle</strong>: maximal safe resection when feasible, followed by postoperative radiotherapy and systemic therapy according to histology and molecular classification; clinical trial enrollment should be strongly considered for GBM.</li>
        </ul>
        """
      },

      {
        "label_zh": "WHO 分類",
        "label_en": "WHO CLASSIFICATION",
        "h2_zh": "WHO 2021 膠質瘤分類：從顯微鏡診斷走向整合分子診斷",
        "h2_en": "WHO 2021 glioma classification: from microscopy to integrated molecular diagnosis",
        "body_zh": """
        <p>膠質瘤分類過去主要依賴組織學，但 2016 年 WHO 第 4 版開始整合分子特徵，2021 年 WHO 第 5 版進一步將成人型與兒童型膠質瘤分開，並依 IDH 突變狀態重整成人型瀰漫性膠質瘤。</p>
        <ul>
          <li><strong>核心概念</strong>：現在的「膠質母細胞瘤」基本上指 <strong>IDH 野生型膠質母細胞瘤，WHO 第 4 級</strong>。</li>
          <li><strong>IDH 突變型瀰漫性膠質瘤</strong>：不再稱為膠質母細胞瘤，而是分為 IDH 突變型星形膠質細胞瘤或 IDH 突變且 1p/19q 共同缺失型少突膠質細胞瘤。</li>
          <li><strong>成人型瀰漫性膠質瘤三大類</strong>：第一，IDH 野生型膠質母細胞瘤，WHO 第 4 級；第二，IDH 突變型星形膠質細胞瘤，WHO 第 2–4 級；第三，IDH 突變且 1p/19q 共同缺失型少突膠質細胞瘤，WHO 第 2–3 級。</li>
          <li><strong>分流邏輯</strong>：若 IDH 突變且有 1p/19q 共同缺失，走向少突膠質細胞瘤；若 IDH 突變但沒有 1p/19q 共同缺失，且有 ATRX 缺失或 TP53 突變，走向星形膠質細胞瘤。</li>
          <li><strong>IDH 野生型升級規則</strong>：若組織學看似第 2 或第 3 級，但有 EGFR 擴增、整條第 7 號染色體增加合併整條第 10 號染色體缺失，或 TERT 啟動子突變任一項，即可指定為 IDH 野生型膠質母細胞瘤，WHO 第 4 級。</li>
          <li><strong>IDH 突變型升級規則</strong>：若 IDH 突變型第 2–3 級星形膠質細胞瘤具有 CDKN2A/B 同型合子缺失，則分類為 IDH 突變型星形膠質細胞瘤，WHO 第 4 級。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table marker-table">
            <caption>膠質瘤重要分子標記與臨床意義</caption>
            <thead>
              <tr><th scope="col">分子標記</th><th scope="col">主要意義</th><th scope="col">分類與治療用途</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>IDH 突變</strong></td><td>獨立良好預後因子，通常與較佳總生存期相關。</td><td>膠質母細胞瘤多為 IDH 野生型；星形膠質細胞瘤與少突膠質細胞瘤多為 IDH 突變型。</td></tr>
              <tr><td><strong>1p/19q 共同缺失</strong></td><td>第 1p 與第 19q 染色體臂整臂缺失。</td><td>少突膠質細胞瘤的定義性特徵。</td></tr>
              <tr><td><strong>ATRX 缺失</strong></td><td>通常與 1p/19q 共同缺失互斥。</td><td>支持瀰漫性星形膠質細胞瘤譜系。</td></tr>
              <tr><td><strong>TP53 突變</strong></td><td>常見於 IDH 突變型星形膠質細胞瘤。</td><td>支持星形膠質細胞瘤譜系。</td></tr>
              <tr><td><strong>MGMT 啟動子甲基化</strong></td><td>使 MGMT 表現沉默，降低 DNA 修復能力，通常增加替莫唑胺敏感性。</td><td>在膠質母細胞瘤與替莫唑胺治療情境中，是重要預後與預測性標記。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>Glioma classification was historically based on histology. The 2016 WHO classification incorporated molecular features, and the 2021 WHO 5th edition further separated adult-type from pediatric-type gliomas and reorganized adult-type diffuse gliomas around IDH mutation status.</p>
        <ul>
          <li><strong>Core concept</strong>: glioblastoma now essentially means <strong>glioblastoma, IDH-wildtype, WHO grade 4</strong>.</li>
          <li><strong>IDH-mutant diffuse glioma</strong>: these tumors are no longer called glioblastoma. They are classified as IDH-mutant astrocytoma or IDH-mutant, 1p/19q-codeleted oligodendroglioma.</li>
          <li><strong>Three adult-type diffuse glioma categories</strong>: glioblastoma, IDH-wildtype, WHO grade 4; astrocytoma, IDH-mutant, WHO grade 2–4; and oligodendroglioma, IDH-mutant and 1p/19q-codeleted, WHO grade 2–3.</li>
          <li><strong>Branching logic</strong>: IDH-mutant tumors with 1p/19q codeletion are oligodendroglioma; IDH-mutant tumors without 1p/19q codeletion but with ATRX loss or TP53 mutation are astrocytoma.</li>
          <li><strong>IDH-wildtype molecular upgrade</strong>: a histologic grade 2 or 3 IDH-wildtype diffuse glioma can be designated glioblastoma, IDH-wildtype, WHO grade 4 if it has EGFR amplification, combined whole chromosome 7 gain and whole chromosome 10 loss, or TERT promoter mutation.</li>
          <li><strong>IDH-mutant molecular upgrade</strong>: an IDH-mutant grade 2–3 astrocytoma with CDKN2A/B homozygous deletion is classified as astrocytoma, IDH-mutant, WHO grade 4.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table marker-table">
            <caption>Key molecular markers in glioma</caption>
            <thead>
              <tr><th scope="col">Molecular marker</th><th scope="col">Main significance</th><th scope="col">Classification and treatment use</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>IDH mutation</strong></td><td>Independent favorable prognostic factor associated with better overall survival.</td><td>GBM is usually IDH-wildtype; astrocytoma and oligodendroglioma are commonly IDH-mutant.</td></tr>
              <tr><td><strong>1p/19q codeletion</strong></td><td>Whole-arm deletion of chromosome arms 1p and 19q.</td><td>Defining feature of oligodendroglioma.</td></tr>
              <tr><td><strong>ATRX loss</strong></td><td>Usually mutually exclusive with 1p/19q codeletion.</td><td>Supports diffuse astrocytoma lineage.</td></tr>
              <tr><td><strong>TP53 mutation</strong></td><td>Common in IDH-mutant astrocytoma.</td><td>Supports astrocytoma lineage.</td></tr>
              <tr><td><strong>MGMT promoter methylation</strong></td><td>Silences MGMT expression, reduces DNA repair capacity, and usually increases temozolomide sensitivity.</td><td>Important prognostic and predictive marker in GBM and temozolomide-treated disease.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "病理/檢查",
        "label_en": "PATH/WORKUP",
        "h2_zh": "病理分級、臨床表現、檢查流程與磁振影像判讀",
        "h2_en": "Histologic grading, presentation, workup, and MRI interpretation",
        "body_zh": """
        <p>雖然分子分類已經成為現代膠質瘤診斷核心，組織學仍然重要。膠質瘤分級可用「AMEN」或「MEAN」記憶：核異型性、有絲分裂活性、內皮或微血管增生、壞死。特徵越多，分級通常越高。</p>
        <ul>
          <li><strong>膠質母細胞瘤典型病理</strong>：高細胞密度、間變性細胞核、有絲分裂像、微血管增生，以及具代表性的假柵欄狀壞死。</li>
          <li><strong>間變性星形膠質細胞瘤</strong>：可見高細胞性、明顯核多形性與有絲分裂像，但缺乏內皮血管增生或壞死。</li>
          <li><strong>少突膠質細胞瘤</strong>：典型可見圓形細胞、清楚細胞膜與空泡樣細胞質，也就是常說的「煎蛋樣外觀」。</li>
          <li><strong>常見臨床表現</strong>：頭痛、局部神經學缺損、癲癇、意識混亂或認知改變。</li>
          <li><strong>基本檢查</strong>：完整病史與理學檢查，重點是神經學檢查；若懷疑顱內壓升高，需做眼底檢查。實驗室檢查包括全血球計數與完整代謝套組。</li>
          <li><strong>影像檢查</strong>：非增強頭部電腦斷層可先排除出血；核心檢查是含釓增強與非增強腦部磁振造影，需包含增強 T1 影像與 T2-FLAIR 序列。</li>
          <li><strong>其他檢查</strong>：若有癲癇需考慮腦波；若後續治療可能影響認知，可做神經認知測試建立基準值。</li>
          <li><strong>鑑別診斷</strong>：轉移性腫瘤、其他原發性中樞神經系統腫瘤、腦膜瘤、神經鞘瘤、原發性中樞神經系統淋巴瘤、感染、發炎、毒性或代謝性疾病與遺傳性病因。</li>
          <li><strong>GBM 磁振影像</strong>：常呈現 T1 低訊號、增強 T1 環狀或不規則增強、中央壞死，以及 T2-FLAIR 高訊號水腫或浸潤。</li>
          <li><strong>低級別膠質瘤影像陷阱</strong>：低級別膠質瘤不一定增強；若看似低級別的病灶出現增強，尤其周邊結節樣增強或壞死，應懷疑高級別轉化或本來就是高級別病灶。</li>
        </ul>
        """,
        "body_en": """
        <p>Although molecular classification is central to modern glioma diagnosis, histology remains important. Glioma grading can be remembered using “AMEN” or “MEAN”: nuclear atypia, mitotic activity, endothelial or microvascular proliferation, and necrosis. More features generally indicate higher grade.</p>
        <ul>
          <li><strong>Typical GBM pathology</strong>: dense cellularity, anaplastic nuclei, mitotic figures, microvascular proliferation, and characteristic pseudopalisading necrosis.</li>
          <li><strong>Anaplastic astrocytoma</strong>: hypercellularity, marked nuclear pleomorphism, and mitotic figures, but no endothelial vascular proliferation or necrosis.</li>
          <li><strong>Oligodendroglioma</strong>: rounded cells, well-defined cytoplasmic membranes, and empty-looking cytoplasm, classically called a fried-egg appearance.</li>
          <li><strong>Common presentation</strong>: headache, focal neurologic deficits, seizures, confusion, or cognitive change.</li>
          <li><strong>Basic evaluation</strong>: complete history and physical examination with emphasis on neurologic examination; fundoscopic examination if increased intracranial pressure is suspected. Laboratory evaluation includes CBC and CMP.</li>
          <li><strong>Imaging</strong>: noncontrast head CT can exclude hemorrhage, but the key test is brain MRI with and without gadolinium, including postcontrast T1 and T2-FLAIR sequences.</li>
          <li><strong>Additional tests</strong>: EEG when seizures are present; baseline neurocognitive testing when treatment may affect cognition.</li>
          <li><strong>Differential diagnosis</strong>: metastatic tumor, other primary CNS neoplasm, meningioma, schwannoma, primary CNS lymphoma, infection, inflammation, toxic-metabolic disease, and genetic etiologies.</li>
          <li><strong>GBM MRI</strong>: typically low T1 signal, ring or irregular enhancement on postcontrast T1, central necrosis, and T2-FLAIR hyperintense edema or infiltrative signal.</li>
          <li><strong>Low-grade glioma imaging pitfall</strong>: low-grade gliomas may be non-enhancing; enhancement, especially peripheral nodular enhancement or necrosis, increases suspicion for high-grade transformation or an intrinsically higher-grade lesion.</li>
        </ul>
        """
      },

      {
        "label_zh": "治療架構",
        "label_en": "TREATMENT FRAMEWORK",
        "h2_zh": "膠質瘤治療總架構：最大安全切除、放療、替莫唑胺與 MGMT",
        "h2_en": "Glioma treatment framework: maximal safe resection, radiotherapy, temozolomide, and MGMT",
        "body_zh": """
        <p>膠質瘤治療第一步通常是最大安全切除，目標是在保留神經功能的前提下盡可能切除腫瘤。若腫瘤位於深部或功能區，或為多發病灶而不適合全切除，可考慮次全切除、減積手術或立體定位活檢。</p>
        <ul>
          <li><strong>全切除定義</strong>：通常由神經外科醫師與術後影像共同評估，接近或超過約 95% 切除可視為全切除或接近全切除。</li>
          <li><strong>術後磁振造影時機</strong>：評估切除程度時，應在術後 24–48 小時內做含釓腦部磁振造影，最晚不超過 72 小時，避免術後血液產物與腔壁增強干擾殘存腫瘤判斷。</li>
          <li><strong>放療固定方式</strong>：模擬定位通常使用三點式熱塑面罩，並將術前與術後磁振影像融合到計畫用電腦斷層。</li>
          <li><strong>常用放療劑量</strong>：膠質母細胞瘤標準 60 Gy / 30 次；功能狀態差者可用 40 Gy / 15 次或 25 Gy / 5 次；第三級膠質瘤常用 59.4 Gy / 33 次；低級別膠質瘤常用 54 Gy / 30 次。</li>
          <li><strong>放療急性毒性</strong>：疲倦、落髮、放射性皮膚炎、頭痛、噁心嘔吐、原有神經症狀惡化；合併替莫唑胺時可能有血球低下，尤其血小板低下。</li>
          <li><strong>放療晚期或亞急性毒性</strong>：嗜睡症候群、神經認知下降、短期記憶下降、放射性壞死、白質腦病變與脊髓病變。</li>
          <li><strong>替莫唑胺（TMZ）</strong>：口服烷化劑，可穿過血腦障壁；其作用是將甲基加到 DNA 鳥嘌呤上，造成 DNA 損傷並使細胞停滯在 G2/M 期。</li>
          <li><strong>MGMT</strong>：DNA 修復酵素，可移除 TMZ 造成的 O6-烷基鳥嘌呤損傷。MGMT 表現高會造成 TMZ 抗藥性；MGMT 啟動子甲基化會使 MGMT 表現沉默，通常增加 TMZ 敏感性，也是重要良好預後因子。</li>
          <li><strong>PCV 化療</strong>：較早期的烷化劑為主組合，包含丙卡巴肼、洛莫司汀（CCNU）與長春新鹼。高風險低級別膠質瘤最強第 III 期證據支持放療後輔助 PCV 六個療程。</li>
          <li><strong>PCV 與 TMZ 的實務差異</strong>：TMZ 口服且較容易耐受，臨床常被使用；但低級別膠質瘤中，TMZ 尚無直接隨機試驗證明優於 PCV。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>膠質瘤常用放療劑量</caption>
            <thead><tr><th scope="col">臨床情境</th><th scope="col">常用劑量</th><th scope="col">重點</th></tr></thead>
            <tbody>
              <tr><td><strong>膠質母細胞瘤</strong></td><td>60 Gy / 30 次</td><td>標準根治性術後放療劑量。</td></tr>
              <tr><td><strong>功能狀態較差或高齡 GBM</strong></td><td>40 Gy / 15 次，或 25 Gy / 5 次</td><td>縮短療程以降低治療負擔。</td></tr>
              <tr><td><strong>第三級膠質瘤</strong></td><td>59.4 Gy / 33 次</td><td>適用於第三級少突膠質細胞瘤與第三級星形膠質細胞瘤。</td></tr>
              <tr><td><strong>低級別膠質瘤</strong></td><td>54 Gy / 30 次</td><td>不建議常規升劑量到高級別膠質瘤範圍。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>The first step in glioma management is usually maximal safe resection, with the goal of removing as much tumor as possible while preserving neurologic function. For deep-seated, eloquent, or multifocal tumors, subtotal resection, debulking, or stereotactic biopsy may be appropriate.</p>
        <ul>
          <li><strong>Gross total resection definition</strong>: typically assessed by the neurosurgeon and postoperative imaging; resection approaching or exceeding about 95% is considered gross or near-total resection.</li>
          <li><strong>Postoperative MRI timing</strong>: brain MRI with and without gadolinium should be obtained within 24–48 hours, and no later than 72 hours, to avoid confusing postoperative blood products and cavity enhancement with residual tumor.</li>
          <li><strong>Radiotherapy immobilization</strong>: simulation usually uses a three-point thermoplastic mask, with preoperative and postoperative MRI fused to the planning CT.</li>
          <li><strong>Common radiotherapy doses</strong>: GBM standard dose is 60 Gy / 30 fractions; poor-performance patients may receive 40 Gy / 15 fractions or 25 Gy / 5 fractions; grade III gliomas commonly receive 59.4 Gy / 33 fractions; low-grade gliomas commonly receive 54 Gy / 30 fractions.</li>
          <li><strong>Acute toxicity</strong>: fatigue, alopecia, radiation dermatitis, headache, nausea/vomiting, worsening baseline neurologic symptoms, and cytopenias, especially thrombocytopenia, when combined with temozolomide.</li>
          <li><strong>Subacute and late toxicity</strong>: somnolence syndrome, neurocognitive decline, short-term memory loss, radiation necrosis, leukoencephalopathy, and myelopathy.</li>
          <li><strong>Temozolomide (TMZ)</strong>: an oral alkylating agent that crosses the blood-brain barrier; it methylates DNA guanine bases, causes DNA damage, and arrests cells in G2/M.</li>
          <li><strong>MGMT</strong>: a DNA repair enzyme that removes O6-alkylguanine lesions caused by TMZ. High MGMT expression leads to TMZ resistance; MGMT promoter methylation silences MGMT expression, usually increases TMZ sensitivity, and is a favorable prognostic marker.</li>
          <li><strong>PCV chemotherapy</strong>: an older alkylator-based regimen consisting of procarbazine, lomustine (CCNU), and vincristine. The strongest phase III evidence in high-risk low-grade glioma supports radiotherapy followed by six cycles of adjuvant PCV.</li>
          <li><strong>PCV versus TMZ in practice</strong>: TMZ is oral and often more tolerable, but in low-grade glioma there is no direct randomized trial proving that TMZ is superior to PCV.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>Common glioma radiotherapy doses</caption>
            <thead><tr><th scope="col">Clinical setting</th><th scope="col">Common dose</th><th scope="col">Key point</th></tr></thead>
            <tbody>
              <tr><td><strong>Glioblastoma</strong></td><td>60 Gy / 30 fractions</td><td>Standard postoperative definitive radiotherapy dose.</td></tr>
              <tr><td><strong>Poor-performance or elderly GBM</strong></td><td>40 Gy / 15 fractions, or 25 Gy / 5 fractions</td><td>Shorter treatment to reduce treatment burden.</td></tr>
              <tr><td><strong>Grade III glioma</strong></td><td>59.4 Gy / 33 fractions</td><td>Used for grade III oligodendroglioma and grade III astrocytoma.</td></tr>
              <tr><td><strong>Low-grade glioma</strong></td><td>54 Gy / 30 fractions</td><td>Routine escalation to high-grade glioma dose is not recommended.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "低級別膠質瘤",
        "label_en": "LOW-GRADE GLIOMA",
        "h2_zh": "低級別膠質瘤：風險分層、放療時機、劑量與 PCV/TMZ",
        "h2_en": "Low-grade glioma: risk stratification, timing of radiotherapy, dose, and PCV/TMZ",
        "body_zh": """
        <p>低級別膠質瘤的核心問題是哪些病人可先密切追蹤，哪些病人應早期接受輔助放療與化療。即使年輕且全切除的病人，5 年進展風險仍可超過 50%，因此若選擇觀察，必須規律磁振造影追蹤。</p>

        <div class="table-wrap">
          <table class="oncology-table mnemonic-table">
            <caption>Pignatti 高風險因子：SATAN 記憶法</caption>
            <thead><tr><th scope="col">字母</th><th scope="col">風險因子</th><th scope="col">中文說明</th></tr></thead>
            <tbody>
              <tr><td><strong>S</strong></td><td>Size ≥6 cm</td><td>腫瘤最大徑大於或等於 6 公分。</td></tr>
              <tr><td><strong>A</strong></td><td>Age &gt;40</td><td>年齡大於 40 歲。</td></tr>
              <tr><td><strong>T</strong></td><td>Tumor crossing midline</td><td>腫瘤跨越中線。</td></tr>
              <tr><td><strong>A</strong></td><td>Astrocytoma histology</td><td>星形膠質細胞瘤病理型態。</td></tr>
              <tr><td><strong>N</strong></td><td>Neurologic symptoms</td><td>有神經學症狀。</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>EORTC 22844「Believers’ Trial」</strong>：343 位低級別膠質瘤術後接受 45 Gy / 25 次或 59.4 Gy / 33 次。升劑量未改善總生存期或無進展生存期；5 年總生存期 59% 對 58%，5 年無進展生存期 50% 對 47%。因此低級別膠質瘤不應常規升劑量到接近高級別膠質瘤劑量。</li>
          <li><strong>RTOG 9110 / NCCTG 86-72-51</strong>：比較 50.4 Gy / 28 次與 64.8 Gy / 36 次。高劑量沒有改善總生存期；5 年總生存期 64% 對 72%，15 年總生存期 22% 對 25%。放射性壞死第 3 級以上約 5% 對 3%。</li>
          <li><strong>EORTC 22845「Non-Believers’ Trial」</strong>：311 位第 1–2 級低級別膠質瘤術後隨機立即放療 54 Gy / 30 次或觀察，進展後再放療。立即放療改善無進展生存期但不改善總生存期；5 年無進展生存期 55% 對 35%，4 年總生存期 69% 對 66%。立即放療也改善 1 年癲癇控制。</li>
          <li><strong>RTOG 9802 觀察組</strong>：小於 40 歲、低級別膠質瘤、術後全切除者觀察。即使看似低風險，5 年仍有 58% 復發；殘存腫瘤越多，復發率越高。</li>
          <li><strong>RTOG 9802 第 III 期</strong>：高風險低級別膠質瘤接受 54 Gy / 30 次放療，隨機加或不加 6 個療程 PCV。加 PCV 顯著改善總生存期與無進展生存期：10 年總生存期 60% 對 40%，10 年無進展生存期 51% 對 21%。</li>
          <li><strong>RTOG 0424</strong>：高風險低級別膠質瘤單臂第 II 期，54 Gy / 30 次合併同步 TMZ，後續輔助 TMZ 最多 12 個療程。3 年總生存期 74%，高於歷史對照 54%；但沒有直接與 PCV 隨機比較。</li>
          <li><strong>PCV 與 TMZ 的臨床解讀</strong>：高風險低級別膠質瘤最強證據仍是 54 Gy / 30 次後接 PCV 六個療程。若病人不適合 PCV，可考慮 TMZ，但證據層級較低。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>低級別膠質瘤實用臨床決策表</caption>
            <thead><tr><th scope="col">臨床情境</th><th scope="col">合理策略</th><th scope="col">依據</th></tr></thead>
            <tbody>
              <tr><td><strong>年輕、全切除、低風險且症狀控制良好</strong></td><td>可密切追蹤，起始可每 6 個月做腦部磁振造影。</td><td>立即放療不改善總生存期；但需理解 5 年復發風險仍不低。</td></tr>
              <tr><td><strong>全切除但有高風險特徵</strong></td><td>討論輔助放療，可視情況合併化療。</td><td>Pignatti 因子與 RTOG 9802 風險分層。</td></tr>
              <tr><td><strong>次全切除、僅活檢或明顯殘存腫瘤</strong></td><td>輔助放療，通常 54 Gy / 30 次。</td><td>殘存腫瘤是復發風險因子。</td></tr>
              <tr><td><strong>年齡大於 40 歲</strong></td><td>採高風險低級別膠質瘤治療策略。</td><td>RTOG 9802 納入大於 40 歲且任何切除程度的病人。</td></tr>
              <tr><td><strong>高風險且體能狀態佳</strong></td><td>54 Gy / 30 次後接 PCV 六個療程。</td><td>RTOG 9802 顯著改善總生存期與無進展生存期。</td></tr>
              <tr><td><strong>高風險但不適合 PCV</strong></td><td>可考慮放療合併同步與輔助 TMZ。</td><td>RTOG 0424 第 II 期單臂證據。</td></tr>
              <tr><td><strong>癲癇負擔明顯</strong></td><td>早期放療可改善癲癇控制。</td><td>EORTC 22845 顯示立即放療改善 1 年癲癇控制。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>The key question in low-grade glioma is which patients can be closely observed and which patients should receive early adjuvant radiotherapy and chemotherapy. Even young patients after gross total resection can have a 5-year progression risk exceeding 50%, so observation requires regular MRI surveillance.</p>

        <div class="table-wrap">
          <table class="oncology-table mnemonic-table">
            <caption>Pignatti high-risk factors: SATAN mnemonic</caption>
            <thead><tr><th scope="col">Letter</th><th scope="col">Risk factor</th><th scope="col">Explanation</th></tr></thead>
            <tbody>
              <tr><td><strong>S</strong></td><td>Size ≥6 cm</td><td>Maximum tumor diameter 6 cm or greater.</td></tr>
              <tr><td><strong>A</strong></td><td>Age &gt;40</td><td>Age greater than 40 years.</td></tr>
              <tr><td><strong>T</strong></td><td>Tumor crossing midline</td><td>Tumor crosses the midline.</td></tr>
              <tr><td><strong>A</strong></td><td>Astrocytoma histology</td><td>Astrocytoma histology.</td></tr>
              <tr><td><strong>N</strong></td><td>Neurologic symptoms</td><td>Presence of neurologic symptoms.</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>EORTC 22844 “Believers’ Trial”</strong>: 343 postoperative low-grade glioma patients received 45 Gy / 25 fractions or 59.4 Gy / 33 fractions. Dose escalation did not improve overall survival or progression-free survival; 5-year OS was 59% versus 58%, and 5-year PFS was 50% versus 47%.</li>
          <li><strong>RTOG 9110 / NCCTG 86-72-51</strong>: compared 50.4 Gy / 28 fractions with 64.8 Gy / 36 fractions. High-dose radiotherapy did not improve survival; 5-year OS was 64% versus 72%, and 15-year OS was 22% versus 25%. Grade 3 or higher radiation necrosis was about 5% versus 3%.</li>
          <li><strong>EORTC 22845 “Non-Believers’ Trial”</strong>: 311 grade 1–2 low-grade glioma patients were randomized after surgery to immediate radiotherapy 54 Gy / 30 fractions or observation with radiotherapy at progression. Immediate radiotherapy improved PFS but not OS; 5-year PFS was 55% versus 35%, and 4-year OS was 69% versus 66%. Immediate radiotherapy also improved 1-year seizure control.</li>
          <li><strong>RTOG 9802 observation component</strong>: patients younger than 40 years with low-grade glioma after gross total resection were observed. Even in this apparently low-risk group, 5-year recurrence was 58%; recurrence increased with residual tumor volume.</li>
          <li><strong>RTOG 9802 phase III</strong>: high-risk low-grade glioma patients received 54 Gy / 30 fractions and were randomized to six cycles of PCV or no PCV. PCV significantly improved OS and PFS: 10-year OS 60% versus 40%, and 10-year PFS 51% versus 21%.</li>
          <li><strong>RTOG 0424</strong>: single-arm phase II trial of high-risk low-grade glioma using 54 Gy / 30 fractions with concurrent TMZ followed by up to 12 cycles of adjuvant TMZ. Three-year OS was 74%, better than the historical control of 54%, but there was no randomized comparison with PCV.</li>
          <li><strong>PCV versus TMZ interpretation</strong>: the strongest evidence for high-risk low-grade glioma remains 54 Gy / 30 fractions followed by six cycles of PCV. TMZ is a reasonable alternative when PCV is not appropriate, but the evidence level is lower.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Practical clinical decision table for low-grade glioma</caption>
            <thead><tr><th scope="col">Clinical scenario</th><th scope="col">Reasonable strategy</th><th scope="col">Basis</th></tr></thead>
            <tbody>
              <tr><td><strong>Young, gross total resection, low risk, and good symptom control</strong></td><td>Close surveillance; initial brain MRI can be performed every 6 months.</td><td>Immediate radiotherapy does not improve overall survival, but 5-year recurrence risk remains substantial.</td></tr>
              <tr><td><strong>Gross total resection with high-risk features</strong></td><td>Discuss adjuvant radiotherapy, with chemotherapy depending on risk and patient factors.</td><td>Pignatti criteria and RTOG 9802 risk stratification.</td></tr>
              <tr><td><strong>Subtotal resection, biopsy only, or obvious residual tumor</strong></td><td>Adjuvant radiotherapy, usually 54 Gy / 30 fractions.</td><td>Residual disease is a recurrence risk factor.</td></tr>
              <tr><td><strong>Age greater than 40 years</strong></td><td>Treat using a high-risk low-grade glioma approach.</td><td>RTOG 9802 included patients older than 40 years regardless of extent of resection.</td></tr>
              <tr><td><strong>High-risk and fit</strong></td><td>54 Gy / 30 fractions followed by six cycles of PCV.</td><td>RTOG 9802 improved OS and PFS.</td></tr>
              <tr><td><strong>High-risk but not suitable for PCV</strong></td><td>Consider radiotherapy with concurrent and adjuvant TMZ.</td><td>RTOG 0424 phase II single-arm evidence.</td></tr>
              <tr><td><strong>Significant seizure burden</strong></td><td>Early radiotherapy can improve seizure control.</td><td>EORTC 22845 showed improved seizure control at 1 year.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "第三級少突",
        "label_en": "GRADE III OLIGO",
        "h2_zh": "第三級少突膠質細胞瘤：IDH 突變、1p/19q 共同缺失與 PCV 證據",
        "h2_en": "Grade III oligodendroglioma: IDH mutation, 1p/19q codeletion, and PCV evidence",
        "body_zh": """
        <p>第三級少突膠質細胞瘤的典型分子特徵是 IDH 突變、1p/19q 共同缺失，且沒有 ATRX 缺失或 TP53 突變。標準放療劑量為 59.4 Gy / 33 次。最強治療證據支持放療合併 PCV，而不是單用 TMZ 取代放療為基礎的治療。</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>第三級少突膠質細胞瘤關鍵隨機試驗：RTOG 9402 與 EORTC 26951</caption>
            <thead><tr><th scope="col">試驗</th><th scope="col">病人</th><th scope="col">治療設計</th><th scope="col">主要結果</th><th scope="col">臨床解讀</th></tr></thead>
            <tbody>
              <tr><td><strong>RTOG 9402</strong></td><td>間變性少突膠質細胞瘤或混合型少突星形膠質細胞瘤。</td><td>59.4 Gy 放療，加或不加術前 PCV 四個療程，每 6 週一次。</td><td>全體族群中位總生存期約 4.6–4.7 年，無顯著差異；但 1p/19q 共同缺失腫瘤中，PCV 組總生存期顯著較佳，約 14.7 年對 7.3 年。</td><td>PCV 加放療對 1p/19q 共同缺失腫瘤有明顯長期效益。</td></tr>
              <tr><td><strong>EORTC 26951</strong></td><td>間變性少突膠質細胞瘤。</td><td>59.4 Gy 放療，加或不加輔助 PCV 六個療程。</td><td>加入 PCV 改善總生存期，約 42.3 個月對 31.6 個月；也改善無進展生存期，約 25.3 個月對 13.2 個月。</td><td>放療加 PCV 改善間變性少突膠質細胞瘤的總生存期與無進展生存期。</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>長期追蹤</strong>：RTOG 9402 中 1p/19q 共同缺失族群總生存期約 13.2 年對 7.3 年；EORTC 26951 中 1p/19q 共同缺失族群約 14.2 年對 9.3 年。投影片總結為放療加 PCV 可達約 35% 的 20 年總生存率。</li>
          <li><strong>CODEL 原始設計</strong>：納入 WHO 第 3 級、1p/19q 共同缺失少突膠質細胞瘤，分為單純放療、放療加同步與輔助 TMZ、以及單用 TMZ。單用 TMZ 組無進展生存期顯著較差；3 年無進展生存期約 50%，而放療為基礎的治療約 83%。</li>
          <li><strong>CODEL 臨床訊息</strong>：第三級 1p/19q 共同缺失少突膠質細胞瘤不應以 TMZ 單藥取代放療為基礎的治療。後續 CODEL 重新設計為比較放療加 PCV 對放療加 TMZ。</li>
          <li><strong>POLA cohort</strong>：法國大型前瞻性網絡世代的回溯分析，305 位第三級 IDH 突變且 1p/19q 共同缺失少突膠質細胞瘤；68% 接受 PCV/RT，32% 接受 TMZ/RT。PCV/RT 組總生存期較佳，5 年 89% 對 75%，10 年 72% 對 60%。但這不是隨機試驗，仍可能有選擇偏差。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>第三級少突膠質細胞瘤教學結論</caption>
            <thead><tr><th scope="col">臨床問題</th><th scope="col">教學答案</th></tr></thead>
            <tbody>
              <tr><td><strong>分子特徵</strong></td><td>IDH 突變、1p/19q 共同缺失，且無 ATRX 缺失與 TP53 突變。</td></tr>
              <tr><td><strong>放療劑量</strong></td><td>59.4 Gy / 33 次。</td></tr>
              <tr><td><strong>化療標準證據</strong></td><td>PCV 對總生存期與無進展生存期的證據最強，來自 RTOG 9402 與 EORTC 26951。</td></tr>
              <tr><td><strong>TMZ 單藥是否可作為標準</strong></td><td>不建議。CODEL 原始設計顯示 TMZ 單藥無進展生存期較差。</td></tr>
              <tr><td><strong>PCV 對 TMZ</strong></td><td>POLA cohort 支持 PCV/RT 可能優於 TMZ/RT，但仍需隨機試驗確認。</td></tr>
              <tr><td><strong>考試式答案</strong></td><td>59.4 Gy / 33 次放療加 PCV 是最有證據支持的答案。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>Grade III oligodendroglioma is characterized by IDH mutation, 1p/19q codeletion, and absence of ATRX loss or TP53 mutation. The standard radiotherapy dose is 59.4 Gy / 33 fractions. The strongest evidence supports radiotherapy plus PCV rather than TMZ alone replacing radiotherapy-based therapy.</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Key randomized trials in grade III oligodendroglioma: RTOG 9402 and EORTC 26951</caption>
            <thead><tr><th scope="col">Trial</th><th scope="col">Patients</th><th scope="col">Treatment design</th><th scope="col">Main result</th><th scope="col">Clinical interpretation</th></tr></thead>
            <tbody>
              <tr><td><strong>RTOG 9402</strong></td><td>Anaplastic oligodendroglioma or mixed anaplastic oligoastrocytoma.</td><td>59.4 Gy radiotherapy with or without neoadjuvant PCV for four cycles every 6 weeks.</td><td>Overall cohort median OS was about 4.6–4.7 years without significant difference; in 1p/19q-codeleted tumors, PCV significantly improved OS, about 14.7 versus 7.3 years.</td><td>PCV plus radiotherapy provides a clear long-term benefit in 1p/19q-codeleted tumors.</td></tr>
              <tr><td><strong>EORTC 26951</strong></td><td>Anaplastic oligodendroglioma.</td><td>59.4 Gy radiotherapy with or without six cycles of adjuvant PCV.</td><td>PCV improved OS, about 42.3 versus 31.6 months, and improved PFS, about 25.3 versus 13.2 months.</td><td>Radiotherapy plus PCV improves OS and PFS in anaplastic oligodendroglioma.</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>Long-term follow-up</strong>: in RTOG 9402, OS in the 1p/19q-codeleted subgroup was about 13.2 versus 7.3 years; in EORTC 26951, it was about 14.2 versus 9.3 years. The teaching summary is that radiotherapy plus PCV can achieve about 35% 20-year OS.</li>
          <li><strong>Original CODEL design</strong>: enrolled WHO grade III 1p/19q-codeleted oligodendroglioma and randomized patients to radiotherapy alone, radiotherapy with concurrent/adjuvant TMZ, or TMZ alone. The TMZ-alone arm had significantly worse PFS; 3-year PFS was about 50% with TMZ alone versus about 83% with radiotherapy-based therapy.</li>
          <li><strong>CODEL clinical message</strong>: TMZ alone should not replace radiotherapy-based therapy for grade III 1p/19q-codeleted oligodendroglioma. The redesigned CODEL trial compares radiotherapy plus PCV versus radiotherapy plus TMZ.</li>
          <li><strong>POLA cohort</strong>: retrospective analysis of a large French prospective network cohort including 305 patients with grade III IDH-mutant, 1p/19q-codeleted oligodendroglioma; 68% received PCV/RT and 32% received TMZ/RT. OS favored PCV/RT: 5-year OS 89% versus 75%, and 10-year OS 72% versus 60%. This is not randomized evidence and may be affected by selection bias.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Teaching conclusions for grade III oligodendroglioma</caption>
            <thead><tr><th scope="col">Clinical question</th><th scope="col">Teaching answer</th></tr></thead>
            <tbody>
              <tr><td><strong>Molecular features</strong></td><td>IDH mutation, 1p/19q codeletion, no ATRX loss, and no TP53 mutation.</td></tr>
              <tr><td><strong>Radiotherapy dose</strong></td><td>59.4 Gy / 33 fractions.</td></tr>
              <tr><td><strong>Best chemotherapy evidence</strong></td><td>PCV has the strongest OS and PFS evidence, from RTOG 9402 and EORTC 26951.</td></tr>
              <tr><td><strong>Can TMZ alone be standard?</strong></td><td>No. The original CODEL design showed worse PFS with TMZ alone.</td></tr>
              <tr><td><strong>PCV versus TMZ</strong></td><td>The POLA cohort supports possible superiority of PCV/RT over TMZ/RT, but randomized confirmation is needed.</td></tr>
              <tr><td><strong>Exam-style answer</strong></td><td>59.4 Gy / 33 fractions plus PCV is the most evidence-based answer.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "第三級星形",
        "label_en": "GRADE III ASTRO",
        "h2_zh": "第三級星形膠質細胞瘤：NOA-04、CATNON 與輔助 TMZ",
        "h2_en": "Grade III astrocytoma: NOA-04, CATNON, and adjuvant TMZ",
        "body_zh": """
        <p>第三級星形膠質細胞瘤的典型分子特徵是 IDH 突變、1p/19q 未共同缺失、ATRX 缺失或 TP53 突變，且 CDKN2A/B 未同型合子缺失。標準放療劑量同樣是 59.4 Gy / 33 次。與第三級少突膠質細胞瘤不同，這裡最重要的證據是 CATNON，支持的是輔助 TMZ，而不是同步 TMZ 的獨立總生存期效益。</p>
        <ul>
          <li><strong>NOA-04</strong>：318 位間變性膠質瘤，約 25% 為間變性少突膠質細胞瘤，約 75% 為間變性星形膠質細胞瘤。病人隨機接受先放療後化療，或先化療後放療；化療可為 TMZ 或 PCV。</li>
          <li><strong>NOA-04 結果</strong>：兩種順序在治療失敗時間、總生存期與無進展生存期上相似。IDH1 突變是重要預後因子，甚至比 1p/19q 共同缺失或 MGMT 啟動子甲基化更重要。</li>
          <li><strong>NOA-04 教學點</strong>：放療與化療誰先誰後對整體結果影響不大；真正決定預後的是分子特徵，而非單純組織學名稱。</li>
          <li><strong>CATNON</strong>：751 位 1p/19q 未共同缺失間變性膠質瘤，2×2 因子設計，比較單純放療、放療加同步 TMZ、放療加輔助 TMZ，以及放療加同步與輔助 TMZ。放療劑量為 59.4 Gy / 33 次；同步 TMZ 為每日 75 mg/m²；輔助 TMZ 為每 4 週第 1–5 天 150–200 mg/m²，共 12 個療程。</li>
          <li><strong>CATNON 同步 TMZ</strong>：第二次期中分析宣告同步 TMZ 無效益；同步 TMZ 中位總生存期約 66.9 個月，無同步 TMZ 約 60.4 個月，未達顯著差異。</li>
          <li><strong>CATNON 輔助 TMZ</strong>：輔助 TMZ 顯著改善總生存期；中位總生存期約 82.3 個月對 46.9 個月，且效益主要出現在 IDH 突變腫瘤，而不是 IDH 野生型腫瘤。</li>
          <li><strong>毒性</strong>：TMZ 主要造成血液學毒性；投影片列出單純放療血液學毒性約 9%，輔助 TMZ 約 15%。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>第三級星形膠質細胞瘤教學結論</caption>
            <thead><tr><th scope="col">臨床問題</th><th scope="col">教學答案</th></tr></thead>
            <tbody>
              <tr><td><strong>分子特徵</strong></td><td>IDH 突變、ATRX 缺失或 TP53 突變、1p/19q 未共同缺失、CDKN2A/B 未同型合子缺失。</td></tr>
              <tr><td><strong>放療劑量</strong></td><td>59.4 Gy / 33 次。</td></tr>
              <tr><td><strong>最重要試驗</strong></td><td>CATNON。</td></tr>
              <tr><td><strong>同步 TMZ</strong></td><td>沒有明確總生存期效益。</td></tr>
              <tr><td><strong>輔助 TMZ</strong></td><td>有明顯總生存期效益，尤其在 IDH 突變腫瘤。</td></tr>
              <tr><td><strong>考試式答案</strong></td><td>59.4 Gy / 33 次放療後接輔助 TMZ 12 個療程。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>第三級膠質瘤實用決策表</caption>
            <thead><tr><th scope="col">腫瘤類型</th><th scope="col">分子特徵</th><th scope="col">標準放療劑量</th><th scope="col">最支持的全身治療</th><th scope="col">主要證據</th></tr></thead>
            <tbody>
              <tr><td><strong>第三級少突膠質細胞瘤</strong></td><td>IDH 突變、1p/19q 共同缺失。</td><td>59.4 Gy / 33 次</td><td>PCV。</td><td>RTOG 9402、EORTC 26951。</td></tr>
              <tr><td><strong>第三級星形膠質細胞瘤</strong></td><td>IDH 突變、1p/19q 未共同缺失、ATRX 或 TP53 改變。</td><td>59.4 Gy / 33 次</td><td>輔助 TMZ。</td><td>CATNON。</td></tr>
              <tr><td><strong>1p/19q 共同缺失腫瘤考慮 TMZ 單藥</strong></td><td>IDH 突變、1p/19q 共同缺失。</td><td>不建議以 TMZ 單藥取代放療為基礎的治療。</td><td>需要放療加化療。</td><td>CODEL 原始設計。</td></tr>
              <tr><td><strong>少突膠質細胞瘤中 PCV 對 TMZ</strong></td><td>IDH 突變、1p/19q 共同缺失。</td><td>59.4 Gy。</td><td>目前偏向 PCV，但仍需隨機試驗確認。</td><td>POLA cohort、重新設計的 CODEL。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>Grade III astrocytoma is typically IDH-mutant, 1p/19q-intact, with ATRX loss or TP53 mutation, and without CDKN2A/B homozygous deletion. The standard radiotherapy dose is 59.4 Gy / 33 fractions. Unlike grade III oligodendroglioma, the key evidence is CATNON, which supports adjuvant TMZ rather than an independent survival benefit from concurrent TMZ.</p>
        <ul>
          <li><strong>NOA-04</strong>: 318 patients with anaplastic glioma, about 25% anaplastic oligodendroglioma and 75% anaplastic astrocytoma. Patients were randomized to radiotherapy followed by chemotherapy at progression or chemotherapy followed by radiotherapy at progression; chemotherapy was TMZ or PCV.</li>
          <li><strong>NOA-04 results</strong>: treatment failure time, OS, and PFS were similar between sequences. IDH1 mutation was an important prognostic factor, even stronger than 1p/19q codeletion or MGMT promoter methylation.</li>
          <li><strong>NOA-04 teaching point</strong>: whether radiotherapy or chemotherapy comes first does not substantially change overall outcome; molecular features are more prognostic than histologic label alone.</li>
          <li><strong>CATNON</strong>: 751 patients with 1p/19q non-codeleted anaplastic glioma in a 2×2 factorial design: radiotherapy alone, radiotherapy plus concurrent TMZ, radiotherapy plus adjuvant TMZ, and radiotherapy plus concurrent and adjuvant TMZ. Radiotherapy was 59.4 Gy / 33 fractions; concurrent TMZ was 75 mg/m² daily; adjuvant TMZ was 150–200 mg/m² on days 1–5 every 4 weeks for 12 cycles.</li>
          <li><strong>CATNON concurrent TMZ</strong>: the second interim analysis declared futility for concurrent TMZ; median OS was about 66.9 months with concurrent TMZ versus 60.4 months without, not significant.</li>
          <li><strong>CATNON adjuvant TMZ</strong>: adjuvant TMZ significantly improved OS; median OS was about 82.3 months versus 46.9 months, with benefit mainly in IDH-mutant tumors rather than IDH-wildtype tumors.</li>
          <li><strong>Toxicity</strong>: TMZ mainly causes hematologic toxicity; the slide summary lists hematologic toxicity around 9% with radiotherapy alone and about 15% with adjuvant TMZ.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Teaching conclusions for grade III astrocytoma</caption>
            <thead><tr><th scope="col">Clinical question</th><th scope="col">Teaching answer</th></tr></thead>
            <tbody>
              <tr><td><strong>Molecular features</strong></td><td>IDH mutation, ATRX loss or TP53 mutation, 1p/19q intact, and CDKN2A/B wildtype.</td></tr>
              <tr><td><strong>Radiotherapy dose</strong></td><td>59.4 Gy / 33 fractions.</td></tr>
              <tr><td><strong>Most important trial</strong></td><td>CATNON.</td></tr>
              <tr><td><strong>Concurrent TMZ</strong></td><td>No clear overall survival benefit.</td></tr>
              <tr><td><strong>Adjuvant TMZ</strong></td><td>Clear overall survival benefit, especially in IDH-mutant tumors.</td></tr>
              <tr><td><strong>Exam-style answer</strong></td><td>59.4 Gy / 33 fractions followed by 12 cycles of adjuvant TMZ.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Practical decision table for grade III glioma</caption>
            <thead><tr><th scope="col">Tumor type</th><th scope="col">Molecular profile</th><th scope="col">Standard radiotherapy dose</th><th scope="col">Best-supported systemic therapy</th><th scope="col">Key evidence</th></tr></thead>
            <tbody>
              <tr><td><strong>Grade III oligodendroglioma</strong></td><td>IDH-mutant, 1p/19q-codeleted.</td><td>59.4 Gy / 33 fractions</td><td>PCV.</td><td>RTOG 9402 and EORTC 26951.</td></tr>
              <tr><td><strong>Grade III astrocytoma</strong></td><td>IDH-mutant, 1p/19q-intact, ATRX or TP53 altered.</td><td>59.4 Gy / 33 fractions</td><td>Adjuvant TMZ.</td><td>CATNON.</td></tr>
              <tr><td><strong>1p/19q-codeleted tumor considering TMZ alone</strong></td><td>IDH-mutant, 1p/19q-codeleted.</td><td>TMZ alone should not replace radiotherapy-based treatment.</td><td>Radiotherapy plus chemotherapy is required.</td><td>Original CODEL design.</td></tr>
              <tr><td><strong>PCV versus TMZ in oligodendroglioma</strong></td><td>IDH-mutant, 1p/19q-codeleted.</td><td>59.4 Gy.</td><td>PCV favored, but randomized confirmation is still needed.</td><td>POLA cohort and redesigned CODEL.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "GBM 標準",
        "label_en": "GBM STANDARD",
        "h2_zh": "膠質母細胞瘤標準治療：手術、60 Gy、替莫唑胺與電場治療",
        "h2_en": "Glioblastoma standard therapy: surgery, 60 Gy, temozolomide, and tumor treating fields",
        "body_zh": """
        <p>膠質母細胞瘤是成人最常見的原發性腦部惡性腫瘤，預後差，即使標準治療後中位總生存期也約 14 個月。中位年齡約 65 歲，男性稍多於女性。病理核心特徵包括核異型性、高有絲分裂活性、內皮增生與壞死。</p>
        <ul>
          <li><strong>分子特徵</strong>：現代 GBM 強調 IDH 野生型；支持診斷或分子定義的特徵包括 TERT 啟動子突變、EGFR 擴增、第 7 號染色體增加合併第 10 號染色體缺失。</li>
          <li><strong>MGMT 啟動子甲基化</strong>：代表 TMZ 反應較好，也預後較佳。</li>
          <li><strong>總原則</strong>：若可行，盡量進入臨床試驗；標準治療包括最大安全切除、術後 60 Gy / 30 次放療、同步 TMZ、輔助 TMZ，以及適合者討論腫瘤治療電場。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>新診斷膠質母細胞瘤標準治療架構</caption>
            <thead><tr><th scope="col">治療階段</th><th scope="col">標準內容</th></tr></thead>
            <tbody>
              <tr><td><strong>手術</strong></td><td>最大安全切除；可為全切除、接近全切除或次全切除；若不適合切除則做活檢。</td></tr>
              <tr><td><strong>術後影像</strong></td><td>術後腦部磁振造影應在 72 小時內完成；投影片另列出術後 2–3 週脊椎磁振造影。</td></tr>
              <tr><td><strong>輔助治療開始時間</strong></td><td>通常在術後 3–6 週開始。</td></tr>
              <tr><td><strong>放療</strong></td><td>標準劑量 60 Gy / 30 次。</td></tr>
              <tr><td><strong>同步 TMZ</strong></td><td>放療期間每日 75 mg/m²，每週 7 天。</td></tr>
              <tr><td><strong>輔助 TMZ</strong></td><td>每 28 天第 1–5 天 150–200 mg/m²，通常 6 個療程。</td></tr>
              <tr><td><strong>支持療法</strong></td><td>肺囊蟲肺炎預防，例如 TMP-SMX；止吐藥，例如 ondansetron；監測血小板低下。</td></tr>
              <tr><td><strong>腫瘤治療電場</strong></td><td>適用於幕上病灶；與維持 TMZ 一起開始，持續到疾病進展或約 2 年。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table prognostic-table">
            <caption>RTOG 膠質母細胞瘤 RPA 預後分層</caption>
            <thead><tr><th scope="col">RPA 類別</th><th scope="col">病人族群</th><th scope="col">中位生存期</th><th scope="col">1 年總生存率</th><th scope="col">3 年總生存率</th><th scope="col">5 年總生存率</th></tr></thead>
            <tbody>
              <tr><td><strong>III</strong></td><td>小於 50 歲且 KPS ≥90。</td><td>17.1 個月</td><td>70%</td><td>20%</td><td>14%</td></tr>
              <tr><td><strong>IV</strong></td><td>小於 50 歲且 KPS &lt;90；或大於等於 50 歲、KPS ≥70、有切除且仍能工作。</td><td>11.2 個月</td><td>46%</td><td>7%</td><td>3%</td></tr>
              <tr><td><strong>V + VI</strong></td><td>大於等於 50 歲、KPS ≥70、有切除但不能工作；或僅活檢；或 KPS &lt;70。</td><td>7.5 個月</td><td>28%</td><td>1%</td><td>0%</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>Glioblastoma is the most common adult primary brain malignancy and has poor prognosis, with median overall survival around 14 months even after standard therapy. Median age is around 65 years, and men are slightly more affected than women. Key pathologic features include nuclear atypia, high mitotic activity, endothelial proliferation, and necrosis.</p>
        <ul>
          <li><strong>Molecular features</strong>: modern GBM emphasizes IDH-wildtype disease; diagnostic or molecular-defining features include TERT promoter mutation, EGFR amplification, and chromosome 7 gain with chromosome 10 loss.</li>
          <li><strong>MGMT promoter methylation</strong>: associated with better TMZ response and better prognosis.</li>
          <li><strong>Overall principle</strong>: clinical trial whenever possible; standard therapy includes maximal safe resection, postoperative 60 Gy / 30 fractions, concurrent TMZ, adjuvant TMZ, and discussion of tumor treating fields when appropriate.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Standard treatment framework for newly diagnosed glioblastoma</caption>
            <thead><tr><th scope="col">Treatment phase</th><th scope="col">Standard content</th></tr></thead>
            <tbody>
              <tr><td><strong>Surgery</strong></td><td>Maximal safe resection; gross, near-total, or subtotal resection; biopsy if resection is not feasible.</td></tr>
              <tr><td><strong>Postoperative imaging</strong></td><td>Postoperative brain MRI should be obtained within 72 hours; the slide also lists spine MRI at 2–3 weeks postoperatively.</td></tr>
              <tr><td><strong>Adjuvant treatment timing</strong></td><td>Usually begins 3–6 weeks after surgery.</td></tr>
              <tr><td><strong>Radiotherapy</strong></td><td>Standard dose 60 Gy / 30 fractions.</td></tr>
              <tr><td><strong>Concurrent TMZ</strong></td><td>75 mg/m² daily, 7 days per week during radiotherapy.</td></tr>
              <tr><td><strong>Adjuvant TMZ</strong></td><td>150–200 mg/m² on days 1–5 every 28 days, usually for 6 cycles.</td></tr>
              <tr><td><strong>Supportive care</strong></td><td>Pneumocystis prophylaxis, such as TMP-SMX; antiemetic therapy, such as ondansetron; monitoring for thrombocytopenia.</td></tr>
              <tr><td><strong>Tumor treating fields</strong></td><td>Appropriate for supratentorial disease; started with maintenance TMZ and continued until progression or about 2 years.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table prognostic-table">
            <caption>RTOG GBM RPA prognostic classification</caption>
            <thead><tr><th scope="col">RPA class</th><th scope="col">Patient group</th><th scope="col">Median survival</th><th scope="col">1-year OS</th><th scope="col">3-year OS</th><th scope="col">5-year OS</th></tr></thead>
            <tbody>
              <tr><td><strong>III</strong></td><td>Age &lt;50 years and KPS ≥90.</td><td>17.1 months</td><td>70%</td><td>20%</td><td>14%</td></tr>
              <tr><td><strong>IV</strong></td><td>Age &lt;50 years with KPS &lt;90; or age ≥50 years, KPS ≥70, resection, and working.</td><td>11.2 months</td><td>46%</td><td>7%</td><td>3%</td></tr>
              <tr><td><strong>V + VI</strong></td><td>Age ≥50 years, KPS ≥70, resection but not working; or biopsy only; or KPS &lt;70.</td><td>7.5 months</td><td>28%</td><td>1%</td><td>0%</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "GBM 證據",
        "label_en": "GBM EVIDENCE",
        "h2_zh": "膠質母細胞瘤關鍵證據：60 Gy、Stupp、電場治療與 CeTeG/NOA-09",
        "h2_en": "Glioblastoma key evidence: 60 Gy, Stupp, tumor treating fields, and CeTeG/NOA-09",
        "body_zh": """
        <ul>
          <li><strong>BTSG 劑量升階研究</strong>：來自三個連續研究，依放療劑量分組分析，結果顯示 60 Gy 放療產生最佳總生存期，因此建立 60 Gy / 30 次為 GBM 標準放療劑量。GBM 標準不是 54 Gy，也不是常規升劑量到 70–75 Gy。</li>
          <li><strong>Stupp trial</strong>：573 位新診斷組織學 GBM 病人，術後 6 週內隨機接受 60 Gy / 30 次單純放療，或 60 Gy / 30 次加同步與輔助 TMZ。同步 TMZ 為每日 75 mg/m²；輔助 TMZ 為每 28 天第 1–5 天 150–200 mg/m²，共 6 個療程。</li>
          <li><strong>MGMT 重點</strong>：MGMT 啟動子甲基化病人的 TMZ 效益更明顯；MGMT 未甲基化病人在未預先計畫的次群分析中效益不顯著。不過標準教學是 Stupp trial 仍建立放療加同步與輔助 TMZ 為標準，體能狀態佳者通常不因 MGMT 未甲基化就完全省略 TMZ。</li>
          <li><strong>腫瘤治療電場機轉</strong>：低強度、中頻率交變電場，約 200 kHz，透過干擾有絲分裂紡錘體形成破壞細胞分裂。使用四組電極貼片，每組九個絕緣電極，貼於剃髮頭皮並連接可攜式裝置。需高配戴順從性，目標每日平均至少 18 小時。僅適用於幕上腫瘤。</li>
          <li><strong>CeTeG/NOA-09</strong>：納入 MGMT 啟動子甲基化 GBM，標準 RT-TMZ 對比 RT-TMZ 加 CCNU。加 CCNU 改善總生存期但未改善無進展生存期，且雙化療毒性較高，因此尚未廣泛成為所有病人的標準。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Stupp trial：放療加 TMZ 對比單純放療</caption>
            <thead><tr><th scope="col">終點</th><th scope="col">單純放療</th><th scope="col">放療加 TMZ</th><th scope="col">結論</th></tr></thead>
            <tbody>
              <tr><td><strong>中位總生存期</strong></td><td>12.1 個月</td><td>14.6 個月</td><td>總生存期改善約 2.5 個月。</td></tr>
              <tr><td><strong>2 年總生存率</strong></td><td>10%</td><td>26%</td><td>長期存活尾端增加。</td></tr>
              <tr><td><strong>5 年總生存率</strong></td><td>2%</td><td>10%</td><td>少數長期存活者增加。</td></tr>
              <tr><td><strong>中位無進展生存期</strong></td><td>5.0 個月</td><td>6.9 個月</td><td>無進展生存期改善。</td></tr>
              <tr><td><strong>第 3–4 級血液學毒性</strong></td><td>未特別列出</td><td>7%</td><td>主要為嗜中性球低下與血小板低下。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>腫瘤治療電場加維持 TMZ：JAMA 2017</caption>
            <thead><tr><th scope="col">終點</th><th scope="col">單用維持 TMZ</th><th scope="col">維持 TMZ 加電場治療</th><th scope="col">P 值</th></tr></thead>
            <tbody>
              <tr><td><strong>中位無進展生存期</strong></td><td>4.0 個月</td><td>6.7 個月</td><td>&lt;0.001</td></tr>
              <tr><td><strong>中位總生存期</strong></td><td>16.0 個月</td><td>20.9 個月</td><td>&lt;0.001</td></tr>
            </tbody>
          </table>
        </div>
        <p>約 75% 病人可達每日 18 小時以上使用量，中位使用時間為 8 個月。主要毒性為皮膚紅、癢與刺激；第 3–4 級毒性未顯著增加。考試式結論：維持 TMZ 加電場治療改善無進展生存期與總生存期，約增加 2–3 個月無進展生存期與約 5 個月總生存期。</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>CeTeG/NOA-09：MGMT 甲基化 GBM 中加入 CCNU</caption>
            <thead><tr><th scope="col">終點</th><th scope="col">RT-TMZ</th><th scope="col">RT-TMZ 加 CCNU</th></tr></thead>
            <tbody>
              <tr><td><strong>中位總生存期</strong></td><td>31 個月</td><td>48 個月</td></tr>
              <tr><td><strong>中位無進展生存期</strong></td><td>16.7 個月</td><td>16.7 個月</td></tr>
              <tr><td><strong>第 3 級以上事件</strong></td><td>51%</td><td>59%</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <ul>
          <li><strong>BTSG dose escalation study</strong>: based on three successive protocols and analyzed by radiotherapy dose group. The best OS was seen with 60 Gy, establishing 60 Gy / 30 fractions as the standard GBM radiotherapy dose. GBM standard dose is not 54 Gy, and routine escalation to 70–75 Gy is not standard.</li>
          <li><strong>Stupp trial</strong>: 573 newly diagnosed histologic GBM patients were randomized within 6 weeks after surgery to 60 Gy / 30 fractions alone or 60 Gy / 30 fractions with concurrent and adjuvant TMZ. Concurrent TMZ was 75 mg/m² daily; adjuvant TMZ was 150–200 mg/m² on days 1–5 every 28 days for 6 cycles.</li>
          <li><strong>MGMT point</strong>: MGMT promoter methylated patients benefited more from TMZ; MGMT-unmethylated patients did not show significant benefit in an unplanned subgroup analysis. However, Stupp remains the standard, and fit patients are not routinely denied TMZ solely because MGMT is unmethylated.</li>
          <li><strong>Tumor treating fields mechanism</strong>: low-intensity, intermediate-frequency alternating electric fields around 200 kHz disrupt mitotic spindle formation and cell division. The device uses four transducer arrays, each with nine insulated electrodes, applied to the shaved scalp and connected to a portable device. High compliance is needed, with a target of at least 18 hours per day. It applies only to supratentorial tumors.</li>
          <li><strong>CeTeG/NOA-09</strong>: enrolled MGMT promoter methylated GBM and compared standard RT-TMZ with RT-TMZ plus CCNU. Adding CCNU improved OS but not PFS and increased dual-chemotherapy toxicity; therefore it has not become a universal standard.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Stupp trial: radiotherapy plus TMZ versus radiotherapy alone</caption>
            <thead><tr><th scope="col">Endpoint</th><th scope="col">Radiotherapy alone</th><th scope="col">Radiotherapy plus TMZ</th><th scope="col">Conclusion</th></tr></thead>
            <tbody>
              <tr><td><strong>Median OS</strong></td><td>12.1 months</td><td>14.6 months</td><td>Overall survival improved by about 2.5 months.</td></tr>
              <tr><td><strong>2-year OS</strong></td><td>10%</td><td>26%</td><td>Long-term survival tail increased.</td></tr>
              <tr><td><strong>5-year OS</strong></td><td>2%</td><td>10%</td><td>More long-term survivors.</td></tr>
              <tr><td><strong>Median PFS</strong></td><td>5.0 months</td><td>6.9 months</td><td>Progression-free survival improved.</td></tr>
              <tr><td><strong>Grade 3–4 hematologic toxicity</strong></td><td>Not specifically listed</td><td>7%</td><td>Mainly neutropenia and thrombocytopenia.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Tumor treating fields plus maintenance TMZ: JAMA 2017</caption>
            <thead><tr><th scope="col">Endpoint</th><th scope="col">Maintenance TMZ alone</th><th scope="col">Maintenance TMZ plus TTFields</th><th scope="col">P value</th></tr></thead>
            <tbody>
              <tr><td><strong>Median PFS</strong></td><td>4.0 months</td><td>6.7 months</td><td>&lt;0.001</td></tr>
              <tr><td><strong>Median OS</strong></td><td>16.0 months</td><td>20.9 months</td><td>&lt;0.001</td></tr>
            </tbody>
          </table>
        </div>
        <p>About 75% of patients achieved at least 18 hours per day of use, with a median TTFields duration of 8 months. Main toxicity was skin-related, such as redness, itchiness, and irritation; grade 3–4 toxicity was not significantly increased. Exam-style conclusion: TTFields plus maintenance TMZ improves PFS and OS by about 2–3 months and 5 months, respectively.</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>CeTeG/NOA-09: adding CCNU in MGMT-methylated GBM</caption>
            <thead><tr><th scope="col">Endpoint</th><th scope="col">RT-TMZ</th><th scope="col">RT-TMZ plus CCNU</th></tr></thead>
            <tbody>
              <tr><td><strong>Median OS</strong></td><td>31 months</td><td>48 months</td></tr>
              <tr><td><strong>Median PFS</strong></td><td>16.7 months</td><td>16.7 months</td></tr>
              <tr><td><strong>Grade 3+ events</strong></td><td>51%</td><td>59%</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "高齡/虛弱 GBM",
        "label_en": "ELDERLY/FRAIL GBM",
        "h2_zh": "高齡或虛弱膠質母細胞瘤：短療程放療與 TMZ 單藥",
        "h2_en": "Elderly or frail GBM: hypofractionated radiotherapy and TMZ alone",
        "body_zh": """
        <p>高齡或虛弱病人不一定適合標準 60 Gy / 30 次，治療需高度個人化。可選擇 40 Gy / 15 次、34 Gy / 10 次、25 Gy / 5 次，或在 MGMT 啟動子甲基化且功能狀態不佳時考慮 TMZ 單藥。</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>高齡或虛弱 GBM 主要短療程放療試驗</caption>
            <thead><tr><th scope="col">試驗</th><th scope="col">納入條件</th><th scope="col">治療組</th><th scope="col">結果</th><th scope="col">臨床重點</th></tr></thead>
            <tbody>
              <tr><td><strong>Canadian trial，Roa 2004</strong></td><td>年齡 ≥60 歲。</td><td>60 Gy / 30 次對 40 Gy / 15 次，無化療。</td><td>中位總生存期約 5.1–5.6 個月，無顯著差異。</td><td>40 Gy / 15 次可作為高齡 GBM 的較短療程。</td></tr>
              <tr><td><strong>Nordic trial，Malmstrom 2012</strong></td><td>年齡 ≥60 歲。</td><td>60 Gy / 30 次、34 Gy / 10 次、或 TMZ 單藥。</td><td>TMZ 單藥中位總生存期 8.4 個月，34 Gy 放療 7.4 個月。</td><td>年齡 ≥70 歲時，TMZ 單藥或 34 Gy / 10 次優於 60 Gy。</td></tr>
              <tr><td><strong>IAEA trial，Roa 2015</strong></td><td>年齡 ≥50 且 KPS 50–70，或年齡 ≥65 且 KPS ≥50。</td><td>40 Gy / 15 次對 25 Gy / 5 次，無化療。</td><td>25 Gy 中位總生存期 7.9 個月，40 Gy 為 6.4 個月；無進展生存期不劣。</td><td>25 Gy / 5 次是非常虛弱或高齡病人的合理短療程選項。</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>Perry trial</strong>：562 位年齡 ≥65 歲、ECOG 0–2 的 GBM 病人，接受 40 Gy / 15 次單純放療或 40 Gy / 15 次加同步與輔助 TMZ。TMZ 改善總生存期與無進展生存期，MGMT 啟動子甲基化腫瘤效益更明顯，約改善總生存期 6 個月，但 TMZ 增加第 3–4 級血液學毒性。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Perry trial：40 Gy / 15 次加 TMZ</caption>
            <thead><tr><th scope="col">終點</th><th scope="col">40 Gy / 15 次單獨治療</th><th scope="col">40 Gy / 15 次加 TMZ</th></tr></thead>
            <tbody>
              <tr><td><strong>中位總生存期</strong></td><td>7.6 個月</td><td>9.3 個月</td></tr>
              <tr><td><strong>中位無進展生存期</strong></td><td>3.9 個月</td><td>5.3 個月</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>高齡或虛弱 GBM 實用決策表</caption>
            <thead><tr><th scope="col">病人狀態</th><th scope="col">合理策略</th></tr></thead>
            <tbody>
              <tr><td><strong>60–70 歲以上但功能狀態良好</strong></td><td>仍可考慮標準 Stupp 方案：60 Gy / 30 次加 TMZ。</td></tr>
              <tr><td><strong>65 歲以上、ECOG 0–2，但不適合 6 週放療</strong></td><td>40 Gy / 15 次加 TMZ。</td></tr>
              <tr><td><strong>70 歲以上或虛弱</strong></td><td>34 Gy / 10 次、25 Gy / 5 次、40 Gy / 15 次，可依 MGMT 與功能狀態決定是否加 TMZ。</td></tr>
              <tr><td><strong>MGMT 啟動子甲基化且功能狀態差</strong></td><td>可考慮 TMZ 單藥。</td></tr>
              <tr><td><strong>MGMT 未甲基化且功能狀態差</strong></td><td>以放療為基礎的緩和治療通常比 TMZ 單藥更合理。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>Elderly or frail patients may not tolerate standard 60 Gy / 30 fractions, so treatment should be individualized. Options include 40 Gy / 15 fractions, 34 Gy / 10 fractions, 25 Gy / 5 fractions, or TMZ alone in selected MGMT promoter methylated patients with poor performance status.</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Major hypofractionation trials in elderly or frail GBM</caption>
            <thead><tr><th scope="col">Trial</th><th scope="col">Inclusion</th><th scope="col">Arms</th><th scope="col">Outcomes</th><th scope="col">Clinical point</th></tr></thead>
            <tbody>
              <tr><td><strong>Canadian trial, Roa 2004</strong></td><td>Age ≥60 years.</td><td>60 Gy / 30 fractions versus 40 Gy / 15 fractions, no chemotherapy.</td><td>Median OS about 5.1–5.6 months, without significant difference.</td><td>40 Gy / 15 fractions is a reasonable shorter regimen for elderly GBM.</td></tr>
              <tr><td><strong>Nordic trial, Malmstrom 2012</strong></td><td>Age ≥60 years.</td><td>60 Gy / 30 fractions, 34 Gy / 10 fractions, or TMZ alone.</td><td>Median OS 8.4 months with TMZ alone versus 7.4 months with 34 Gy radiotherapy.</td><td>In patients age ≥70 years, TMZ alone or 34 Gy / 10 fractions was better than 60 Gy.</td></tr>
              <tr><td><strong>IAEA trial, Roa 2015</strong></td><td>Age ≥50 with KPS 50–70, or age ≥65 with KPS ≥50.</td><td>40 Gy / 15 fractions versus 25 Gy / 5 fractions, no chemotherapy.</td><td>Median OS 7.9 months with 25 Gy versus 6.4 months with 40 Gy; PFS non-inferior.</td><td>25 Gy / 5 fractions is a reasonable short regimen for very frail or elderly patients.</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>Perry trial</strong>: 562 patients age ≥65 years with GBM and ECOG 0–2 received 40 Gy / 15 fractions alone or 40 Gy / 15 fractions plus concurrent and adjuvant TMZ. TMZ improved OS and PFS, with greater benefit in MGMT promoter methylated tumors, but increased grade 3–4 hematologic toxicity.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Perry trial: 40 Gy / 15 fractions plus TMZ</caption>
            <thead><tr><th scope="col">Endpoint</th><th scope="col">40 Gy / 15 fractions alone</th><th scope="col">40 Gy / 15 fractions plus TMZ</th></tr></thead>
            <tbody>
              <tr><td><strong>Median OS</strong></td><td>7.6 months</td><td>9.3 months</td></tr>
              <tr><td><strong>Median PFS</strong></td><td>3.9 months</td><td>5.3 months</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Practical decision table for elderly or frail GBM</caption>
            <thead><tr><th scope="col">Patient status</th><th scope="col">Reasonable strategy</th></tr></thead>
            <tbody>
              <tr><td><strong>Age 60–70 or older, but good functional status</strong></td><td>Consider standard Stupp regimen: 60 Gy / 30 fractions plus TMZ.</td></tr>
              <tr><td><strong>Age ≥65, ECOG 0–2, but unsuitable for 6 weeks of radiotherapy</strong></td><td>40 Gy / 15 fractions plus TMZ.</td></tr>
              <tr><td><strong>Age ≥70 or frail</strong></td><td>34 Gy / 10 fractions, 25 Gy / 5 fractions, or 40 Gy / 15 fractions, with TMZ based on MGMT status and performance status.</td></tr>
              <tr><td><strong>MGMT promoter methylated and poor performance status</strong></td><td>TMZ alone can be considered.</td></tr>
              <tr><td><strong>MGMT unmethylated and poor performance status</strong></td><td>Radiotherapy-based palliation is usually more reasonable than TMZ alone.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "復發 GBM",
        "label_en": "RECURRENT GBM",
        "h2_zh": "復發性 GBM：復發、假性進展、放射性壞死與治療選項",
        "h2_en": "Recurrent GBM: recurrence, pseudoprogression, radiation necrosis, and treatment options",
        "body_zh": """
        <p>約 80% GBM 復發發生在原發腫瘤 2 公分內。完成放療後，建議 2–8 週做第一次治療後腦部磁振造影，之後每 2–4 個月追蹤 3 年，再每 3–6 個月長期追蹤。復發性 GBM 與假性進展在磁振影像上常很難區分；同步放化療後假性進展可高達 30–40%。</p>

        <div class="table-wrap">
          <table class="oncology-table criteria-table">
            <caption>2020 RANO 進展或復發判定標準</caption>
            <thead><tr><th scope="col">判定項目</th><th scope="col">內容</th></tr></thead>
            <tbody>
              <tr><td><strong>增強病灶進展</strong></td><td>在類固醇劑量穩定或增加下，增強病灶垂直直徑總和增加至少 25%。</td></tr>
              <tr><td><strong>T2/FLAIR 進展</strong></td><td>在類固醇劑量穩定或增加下，T2/FLAIR 非增強病灶明顯增加。</td></tr>
              <tr><td><strong>新病灶</strong></td><td>出現任何新病灶。</td></tr>
              <tr><td><strong>不可測量病灶</strong></td><td>不可測量病灶明確進展。</td></tr>
              <tr><td><strong>臨床惡化</strong></td><td>明確臨床惡化，且不能由其他原因或類固醇劑量下降解釋。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table comparison-table">
            <caption>假性進展與放射性壞死比較</caption>
            <thead><tr><th scope="col">項目</th><th scope="col">假性進展</th><th scope="col">放射性壞死</th></tr></thead>
            <tbody>
              <tr><td><strong>常見時間</strong></td><td>同步放化療後約 6 個月內。</td><td>放療後約 1 年或更晚。</td></tr>
              <tr><td><strong>機轉</strong></td><td>放療造成暫時性腫瘤血管通透性增加與發炎，TMZ 可加重此現象。</td><td>放射線誘發組織壞死。</td></tr>
              <tr><td><strong>自然病程</strong></td><td>常會自行緩解。</td><td>不太可能自行完全消退。</td></tr>
              <tr><td><strong>影像提示</strong></td><td>投影片提到可見「肥皂泡樣」效果。</td><td>可與真正復發難以區分。</td></tr>
              <tr><td><strong>MGMT 關聯</strong></td><td>MGMT 甲基化病人較容易出現；回溯資料中約 91%。</td><td>沒有同樣明確的預測關聯。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>復發性 GBM 治療選項</caption>
            <thead><tr><th scope="col">選項</th><th scope="col">適用情境</th><th scope="col">證據與重點</th></tr></thead>
            <tbody>
              <tr><td><strong>再次切除</strong></td><td>局部復發、造成腫塊效應，且病人體能狀態尚可。</td><td>可減壓、取得病理並改善症狀。</td></tr>
              <tr><td><strong>再次照射</strong></td><td>局部復發、與前次放療間隔足夠，且正常器官劑量可接受。</td><td>常用 35 Gy / 10 次或其他寡分割方案。</td></tr>
              <tr><td><strong>GammaTile / Cs-131</strong></td><td>手術床局部近接治療或手術靶向放射治療。</td><td>GammaTile 含 Cs-131 放射源；投影片列出每片 4 顆 seed，每顆 3.5 U。</td></tr>
              <tr><td><strong>Bevacizumab</strong></td><td>症狀性水腫、依賴類固醇或復發性 GBM。</td><td>抗 VEGF-A 單株抗體；基於 BRAIN 第 II 期獲准用於復發 GBM。</td></tr>
              <tr><td><strong>Bevacizumab 加再次照射</strong></td><td>局部復發且需改善局部控制與無進展生存期。</td><td>RTOG 1205 使用 bevacizumab 10 mg/kg 每 2 週，加或不加 35 Gy / 10 次；無進展生存期 7.1 對 3.8 個月，但總生存期無差異。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <p>About 80% of GBM recurrences occur within 2 cm of the primary tumor. After completing radiotherapy, the first post-treatment brain MRI is recommended at 2–8 weeks, then every 2–4 months for 3 years, then every 3–6 months indefinitely. Recurrent GBM and pseudoprogression are often difficult to distinguish on MRI; pseudoprogression after chemoradiotherapy can occur in up to 30–40% of patients.</p>

        <div class="table-wrap">
          <table class="oncology-table criteria-table">
            <caption>2020 RANO criteria for progression or recurrence</caption>
            <thead><tr><th scope="col">Criterion</th><th scope="col">Definition</th></tr></thead>
            <tbody>
              <tr><td><strong>Enhancing lesion progression</strong></td><td>At least 25% increase in the sum of perpendicular diameters of enhancing lesions while corticosteroid dose is stable or increasing.</td></tr>
              <tr><td><strong>T2/FLAIR progression</strong></td><td>Significant increase in T2/FLAIR non-enhancing lesion while corticosteroid dose is stable or increasing.</td></tr>
              <tr><td><strong>New lesion</strong></td><td>Any new lesion.</td></tr>
              <tr><td><strong>Nonmeasurable lesion</strong></td><td>Definite progression of a nonmeasurable lesion.</td></tr>
              <tr><td><strong>Clinical deterioration</strong></td><td>Clear clinical deterioration not explained by other causes or decreasing corticosteroid dose.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table comparison-table">
            <caption>Pseudoprogression versus radiation necrosis</caption>
            <thead><tr><th scope="col">Item</th><th scope="col">Pseudoprogression</th><th scope="col">Radiation necrosis</th></tr></thead>
            <tbody>
              <tr><td><strong>Typical timing</strong></td><td>Within about 6 months after chemoradiotherapy.</td><td>About 1 year or later after radiotherapy.</td></tr>
              <tr><td><strong>Mechanism</strong></td><td>Radiotherapy-induced transient increase in tumor vascular permeability and inflammation, which can be intensified by TMZ.</td><td>Radiation-induced tissue necrosis.</td></tr>
              <tr><td><strong>Natural history</strong></td><td>Often improves spontaneously.</td><td>Unlikely to completely resolve spontaneously.</td></tr>
              <tr><td><strong>Imaging clue</strong></td><td>The slide mentions a “soap-bubble” effect.</td><td>Can be difficult to distinguish from true recurrence.</td></tr>
              <tr><td><strong>MGMT association</strong></td><td>More common in MGMT-methylated patients; retrospective data report about 91%.</td><td>No similarly clear predictive association.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Treatment options for recurrent GBM</caption>
            <thead><tr><th scope="col">Option</th><th scope="col">Appropriate setting</th><th scope="col">Evidence and key point</th></tr></thead>
            <tbody>
              <tr><td><strong>Re-resection</strong></td><td>Focal recurrence with mass effect and adequate performance status.</td><td>Can decompress, provide tissue diagnosis, and improve symptoms.</td></tr>
              <tr><td><strong>Reirradiation</strong></td><td>Focal recurrence with sufficient interval from prior radiotherapy and acceptable organ-at-risk dose.</td><td>Commonly 35 Gy / 10 fractions or other hypofractionated regimens.</td></tr>
              <tr><td><strong>GammaTile / Cs-131</strong></td><td>Local surgical-bed brachytherapy or surgically targeted radiotherapy.</td><td>GammaTile contains Cs-131 sources; the slide lists 4 seeds per tile and 3.5 U per seed.</td></tr>
              <tr><td><strong>Bevacizumab</strong></td><td>Symptomatic edema, steroid dependence, or recurrent GBM.</td><td>Anti-VEGF-A monoclonal antibody; FDA approved for recurrent GBM based on BRAIN phase II.</td></tr>
              <tr><td><strong>Bevacizumab plus reirradiation</strong></td><td>Focal recurrence where local control and PFS improvement are needed.</td><td>RTOG 1205 used bevacizumab 10 mg/kg every 2 weeks with or without 35 Gy / 10 fractions; PFS 7.1 versus 3.8 months, without OS difference.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "GBM 靶區/OAR",
        "label_en": "GBM TARGETS/OAR",
        "h2_zh": "GBM 靶區描繪、劑量限制、升劑量與進行中試驗",
        "h2_en": "GBM target delineation, dose constraints, dose escalation, and ongoing trials",
        "body_zh": """
        <ul>
          <li><strong>不建議常規升劑量</strong>：18F-DOPA-PET 引導升劑量研究顯示部分訊號，但 NRG-BN001 初步結果未顯示 75 Gy / 30 次相較 60 Gy / 30 次有無進展或總生存期效益。臨床試驗外不應常規使用強度調控升劑量。</li>
          <li><strong>不建議常規 SRS boost</strong>：RTOG 9305 比較 SRS boost 加放療與 BCNU 對比標準放療加 BCNU，中位總生存期幾乎相同，13.5 對 13.6 個月。</li>
          <li><strong>不建議常規近接治療 boost</strong>：BTSG NIH Trial 87-01 與 Laperriere 隨機試驗未顯示明確效益。</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table contour-table">
            <caption>EORTC/Stupp 與 RTOG GBM 靶區描繪</caption>
            <thead><tr><th scope="col">方法</th><th scope="col">體積定義</th><th scope="col">劑量</th></tr></thead>
            <tbody>
              <tr><td><strong>EORTC / Stupp</strong></td><td>肉眼腫瘤體積為術後 T1 腔或殘存病灶；臨床靶體積為肉眼腫瘤體積加 2 公分；計畫靶體積再加 0.5 公分。</td><td>60 Gy。</td></tr>
              <tr><td><strong>RTOG 第一階段</strong></td><td>第一肉眼腫瘤體積為 T2/FLAIR 水腫；第一臨床靶體積加 2 公分；第一計畫靶體積再加 0.3–0.5 公分。</td><td>46 Gy / 23 次。</td></tr>
              <tr><td><strong>RTOG 加量階段</strong></td><td>第二肉眼腫瘤體積為術後 T1 腔或增強病灶；第二臨床靶體積加 2 公分；第二計畫靶體積再加 0.3–0.5 公分。</td><td>再加 14 Gy / 7 次，總劑量 60 Gy。</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>GBM 正常器官劑量限制</caption>
            <thead><tr><th scope="col">正常器官</th><th scope="col">投影片劑量限制</th><th scope="col">RTOG 0825 參考</th></tr></thead>
            <tbody>
              <tr><td><strong>視神經／視交叉</strong></td><td>最大劑量 52 Gy；計畫風險體積 54 Gy。</td><td>視神經 55 Gy；視交叉 56 Gy。</td></tr>
              <tr><td><strong>腦幹</strong></td><td>最大劑量 54 Gy；計畫風險體積 60 Gy。</td><td>60 Gy。</td></tr>
              <tr><td><strong>眼球</strong></td><td>15 Gy。</td><td>視網膜 50 Gy。</td></tr>
              <tr><td><strong>耳蝸</strong></td><td>平均劑量低於 40–45 Gy，並盡量降低。</td><td>未列出。</td></tr>
              <tr><td><strong>水晶體</strong></td><td>6 Gy。</td><td>未列出。</td></tr>
            </tbody>
          </table>
        </div>
        <p>覆蓋目標：100% 肉眼腫瘤體積由 60 Gy 處方劑量覆蓋；95% 計畫靶體積由處方劑量覆蓋。RTOG 方法中，第二計畫靶體積至少 95% 由 60 Gy 覆蓋，且 99% 由 54 Gy 覆蓋。</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>投影片提到的 GBM 進行中或當代試驗概念</caption>
            <thead><tr><th scope="col">試驗或平台</th><th scope="col">概念</th></tr></thead>
            <tbody>
              <tr><td><strong>GBM AGILE</strong></td><td>全球適應性第 II/III 期平台試驗，分新診斷與復發 GBM cohort；新診斷 cohort 為 TMZ 加或不加研究藥物，復發 cohort 為 lomustine 加或不加研究藥物。</td></tr>
              <tr><td><strong>NRG BN010</strong></td><td>復發情境中立體定位放射手術加免疫治療。</td></tr>
              <tr><td><strong>AZD1390</strong></td><td>將 ATM 抑制劑加入 GBM 治療。</td></tr>
              <tr><td><strong>EF32</strong></td><td>評估 Optune / 腫瘤治療電場在同步放化療階段的角色。</td></tr>
              <tr><td><strong>EF41 / KEYNOTE D58</strong></td><td>輔助 Optune 加或不加 pembrolizumab。</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "body_en": """
        <ul>
          <li><strong>No routine dose escalation</strong>: 18F-DOPA-PET-guided dose escalation showed some signals, but preliminary NRG-BN001 results did not show PFS or OS benefit for 75 Gy / 30 fractions compared with 60 Gy / 30 fractions. Dose intensification should not be routine outside clinical trials.</li>
          <li><strong>No routine SRS boost</strong>: RTOG 9305 compared SRS boost plus radiotherapy and BCNU with standard radiotherapy plus BCNU; median OS was essentially identical, 13.5 versus 13.6 months.</li>
          <li><strong>No routine brachytherapy boost</strong>: BTSG NIH Trial 87-01 and the Laperriere randomized trial did not show clear benefit.</li>
        </ul>

        <div class="table-wrap">
          <table class="oncology-table contour-table">
            <caption>EORTC/Stupp and RTOG GBM target delineation</caption>
            <thead><tr><th scope="col">Method</th><th scope="col">Volume definition</th><th scope="col">Dose</th></tr></thead>
            <tbody>
              <tr><td><strong>EORTC / Stupp</strong></td><td>GTV is postoperative T1 cavity or residual disease; CTV is GTV plus 2 cm; PTV is CTV plus 0.5 cm.</td><td>60 Gy.</td></tr>
              <tr><td><strong>RTOG phase 1</strong></td><td>GTV1 is T2/FLAIR edema; CTV1 is GTV1 plus 2 cm; PTV1 is CTV1 plus 0.3–0.5 cm.</td><td>46 Gy / 23 fractions.</td></tr>
              <tr><td><strong>RTOG boost</strong></td><td>GTV2 is postoperative T1 cavity or enhancing disease; CTV2 is GTV2 plus 2 cm; PTV2 is CTV2 plus 0.3–0.5 cm.</td><td>Additional 14 Gy / 7 fractions, total dose 60 Gy.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>GBM organ-at-risk dose constraints</caption>
            <thead><tr><th scope="col">Organ at risk</th><th scope="col">Constraint in slide</th><th scope="col">RTOG 0825 reference</th></tr></thead>
            <tbody>
              <tr><td><strong>Optic nerves / chiasm</strong></td><td>Maximum dose 52 Gy; PRV 54 Gy.</td><td>Optic nerves 55 Gy; chiasm 56 Gy.</td></tr>
              <tr><td><strong>Brainstem</strong></td><td>Maximum dose 54 Gy; PRV 60 Gy.</td><td>60 Gy.</td></tr>
              <tr><td><strong>Eyes</strong></td><td>15 Gy.</td><td>Retina 50 Gy.</td></tr>
              <tr><td><strong>Cochlea</strong></td><td>Mean dose less than 40–45 Gy, as low as reasonably achievable.</td><td>Not listed.</td></tr>
              <tr><td><strong>Lens</strong></td><td>6 Gy.</td><td>Not listed.</td></tr>
            </tbody>
          </table>
        </div>
        <p>Coverage goal: 100% of the GTV covered by the 60 Gy prescription dose and 95% of the PTV covered by the prescription dose. In the RTOG approach, at least 95% of PTV2 is covered by 60 Gy and 99% of PTV2 is covered by 54 Gy.</p>

        <div class="table-wrap">
          <table class="oncology-table trial-table">
            <caption>Ongoing or contemporary GBM trial concepts mentioned in the slides</caption>
            <thead><tr><th scope="col">Trial or platform</th><th scope="col">Concept</th></tr></thead>
            <tbody>
              <tr><td><strong>GBM AGILE</strong></td><td>Global adaptive phase II/III platform trial with newly diagnosed and recurrent GBM cohorts; newly diagnosed cohort uses TMZ with or without investigational drugs, and recurrent cohort uses lomustine with or without investigational drugs.</td></tr>
              <tr><td><strong>NRG BN010</strong></td><td>Stereotactic radiosurgery plus immunotherapy for recurrence.</td></tr>
              <tr><td><strong>AZD1390</strong></td><td>Addition of an ATM inhibitor to GBM treatment.</td></tr>
              <tr><td><strong>EF32</strong></td><td>Evaluation of Optune / tumor treating fields during the chemoradiotherapy portion.</td></tr>
              <tr><td><strong>EF41 / KEYNOTE D58</strong></td><td>Adjuvant Optune with or without pembrolizumab.</td></tr>
            </tbody>
          </table>
        </div>
        """
      },

      {
        "label_zh": "GBM 決策",
        "label_en": "GBM DECISION",
        "h2_zh": "GBM 臨床決策總表與最重要訊息",
        "h2_en": "GBM clinical decision table and key take-home messages",
        "body_zh": """
        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>GBM 臨床決策總表</caption>
            <thead><tr><th scope="col">臨床情境</th><th scope="col">合理策略</th><th scope="col">核心依據</th></tr></thead>
            <tbody>
              <tr><td><strong>體能狀態佳的新診斷成人 GBM</strong></td><td>最大安全切除後，60 Gy / 30 次放療加同步 TMZ，再接輔助 TMZ，可討論電場治療。</td><td>BTSG、Stupp trial、電場治療試驗。</td></tr>
              <tr><td><strong>MGMT 啟動子甲基化 GBM</strong></td><td>TMZ 效益較明顯；可考慮 Stupp 方案；CCNU 加 TMZ 需慎選。</td><td>Stupp 次群分析、CeTeG/NOA-09。</td></tr>
              <tr><td><strong>MGMT 未甲基化但體能狀態佳</strong></td><td>Stupp 方案仍常作為標準；強烈鼓勵臨床試驗。</td><td>Stupp trial 建立標準治療，並未以 MGMT 作為完全排除條件。</td></tr>
              <tr><td><strong>同步放化療後幕上 GBM</strong></td><td>可討論維持 TMZ 加電場治療。</td><td>JAMA 2017 電場治療試驗。</td></tr>
              <tr><td><strong>高齡但體能狀態佳</strong></td><td>60 Gy / 30 次加 TMZ，或 40 Gy / 15 次加 TMZ。</td><td>標準療程若可耐受；Perry trial。</td></tr>
              <tr><td><strong>高齡或虛弱且功能狀態差</strong></td><td>40 Gy / 15 次、34 Gy / 10 次、25 Gy / 5 次，可依 MGMT 甲基化狀態考慮 TMZ；若 MGMT 甲基化且功能差，可考慮 TMZ 單藥。</td><td>Canadian、Nordic、IAEA、Perry trials。</td></tr>
              <tr><td><strong>同步放化療後 6 個月內疑似早期復發</strong></td><td>小心假性進展；需整合類固醇劑量、臨床病程、RANO 判準與進階影像。</td><td>RANO 與假性進展教學內容。</td></tr>
              <tr><td><strong>復發 GBM 且有局部腫塊效應</strong></td><td>若可行，考慮再次切除。</td><td>症狀緩解與取得組織診斷。</td></tr>
              <tr><td><strong>局部復發 GBM</strong></td><td>可考慮再次照射，例如 35 Gy / 10 次。</td><td>RTOG 1205 與回溯資料。</td></tr>
              <tr><td><strong>復發 GBM 有水腫或依賴類固醇</strong></td><td>可用 bevacizumab。</td><td>BRAIN 第 II 期與復發 GBM 核准依據。</td></tr>
              <tr><td><strong>任何 GBM</strong></td><td>盡可能考慮臨床試驗。</td><td>投影片反覆強調。</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>第三級少突與第三級星形不能混在一起</strong>：第三級少突膠質細胞瘤是 IDH 突變且 1p/19q 共同缺失，最強證據支持 59.4 Gy / 33 次加 PCV。</li>
          <li><strong>第三級星形重點是 CATNON</strong>：IDH 突變、1p/19q 未共同缺失、ATRX 或 TP53 改變；真正提供總生存期效益的是輔助 TMZ，而不是同步 TMZ。</li>
          <li><strong>GBM 標準治療</strong>：最大安全切除後 60 Gy / 30 次放療合併同步 TMZ，再接輔助 TMZ，可依情境討論電場治療。</li>
          <li><strong>高齡或虛弱 GBM</strong>：需個人化，可使用 40/15、34/10、25/5，並依 MGMT 啟動子甲基化決定 TMZ 的價值。</li>
          <li><strong>GBM 不常規升劑量或 boost</strong>：放療升劑量、立體定位加量或近接治療加量的隨機證據未顯示明確生存效益。</li>
          <li><strong>復發 GBM</strong>：必須先區分真正復發、假性進展與放射性壞死；治療選項包括臨床試驗、再次切除、再次照射、bevacizumab 與症狀導向處置。</li>
        </ul>
        """,
        "body_en": """
        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>GBM clinical decision table</caption>
            <thead><tr><th scope="col">Clinical scenario</th><th scope="col">Reasonable strategy</th><th scope="col">Core basis</th></tr></thead>
            <tbody>
              <tr><td><strong>Fit adult with newly diagnosed GBM</strong></td><td>Maximal safe resection followed by 60 Gy / 30 fractions with concurrent TMZ, then adjuvant TMZ, with discussion of tumor treating fields.</td><td>BTSG, Stupp trial, and tumor treating fields trial.</td></tr>
              <tr><td><strong>MGMT promoter methylated GBM</strong></td><td>TMZ benefit is more pronounced; consider Stupp regimen; CCNU plus TMZ requires careful selection.</td><td>Stupp subgroup and CeTeG/NOA-09.</td></tr>
              <tr><td><strong>MGMT unmethylated but fit</strong></td><td>Stupp regimen remains commonly used as standard; clinical trial is strongly encouraged.</td><td>Stupp established standard therapy without excluding patients solely by MGMT status.</td></tr>
              <tr><td><strong>Supratentorial GBM after chemoradiotherapy</strong></td><td>Discuss maintenance TMZ plus tumor treating fields.</td><td>JAMA 2017 tumor treating fields trial.</td></tr>
              <tr><td><strong>Elderly but fit</strong></td><td>60 Gy / 30 fractions plus TMZ, or 40 Gy / 15 fractions plus TMZ.</td><td>Standard therapy if tolerated; Perry trial.</td></tr>
              <tr><td><strong>Elderly or frail with poor performance status</strong></td><td>40 Gy / 15 fractions, 34 Gy / 10 fractions, or 25 Gy / 5 fractions, with TMZ based on MGMT methylation; TMZ alone can be considered if MGMT-methylated and performance status is poor.</td><td>Canadian, Nordic, IAEA, and Perry trials.</td></tr>
              <tr><td><strong>Suspected early recurrence within 6 months after chemoradiotherapy</strong></td><td>Beware of pseudoprogression; integrate steroid dose, clinical course, RANO criteria, and advanced imaging.</td><td>RANO and pseudoprogression teaching content.</td></tr>
              <tr><td><strong>Recurrent GBM with focal mass effect</strong></td><td>Consider re-resection if feasible.</td><td>Symptom relief and tissue diagnosis.</td></tr>
              <tr><td><strong>Focal recurrent GBM</strong></td><td>Consider reirradiation, such as 35 Gy / 10 fractions.</td><td>RTOG 1205 and retrospective data.</td></tr>
              <tr><td><strong>Recurrent GBM with edema or steroid dependence</strong></td><td>Use bevacizumab when appropriate.</td><td>BRAIN phase II and recurrent GBM approval basis.</td></tr>
              <tr><td><strong>Any GBM</strong></td><td>Consider clinical trial whenever possible.</td><td>Repeated emphasis in the teaching slides.</td></tr>
            </tbody>
          </table>
        </div>

        <ul>
          <li><strong>Grade III oligodendroglioma and grade III astrocytoma should not be grouped together</strong>: grade III oligodendroglioma is IDH-mutant and 1p/19q-codeleted; the strongest evidence supports 59.4 Gy / 33 fractions plus PCV.</li>
          <li><strong>CATNON is key for grade III astrocytoma</strong>: IDH-mutant, 1p/19q-intact, ATRX or TP53 altered disease benefits from adjuvant TMZ, not clearly from concurrent TMZ alone.</li>
          <li><strong>GBM standard therapy</strong>: maximal safe resection followed by 60 Gy / 30 fractions with concurrent TMZ, then adjuvant TMZ, with tumor treating fields discussed when appropriate.</li>
          <li><strong>Elderly or frail GBM</strong>: individualize treatment using 40/15, 34/10, or 25/5 regimens, and use MGMT promoter methylation to judge TMZ value.</li>
          <li><strong>No routine dose escalation or boost for GBM</strong>: randomized evidence has not shown clear survival benefit for radiotherapy dose escalation, stereotactic boost, or brachytherapy boost.</li>
          <li><strong>Recurrent GBM</strong>: first distinguish true recurrence from pseudoprogression and radiation necrosis; options include clinical trial, re-resection, reirradiation, bevacizumab, and symptom-directed management.</li>
        </ul>
        """
      }

    ],
    "excel_sheet": "CNS",
    "trial_filter": [
        "CNS", "central nervous system", "glioma", "low-grade glioma", "LGG",
        "glioblastoma", "GBM", "astrocytoma", "oligodendroglioma",
        "anaplastic glioma", "anaplastic astrocytoma", "anaplastic oligodendroglioma",
        "WHO 2021", "IDH", "IDH-mutant", "IDH-wildtype", "1p/19q",
        "ATRX", "TP53", "MGMT", "TERT", "EGFR", "CDKN2A", "CDKN2B",
        "EORTC 22844", "EORTC 22845", "RTOG 9110", "NCCTG 86-72-51",
        "RTOG 9802", "RTOG 0424", "Pignatti", "SATAN", "PCV", "TMZ",
        "temozolomide", "procarbazine", "lomustine", "CCNU", "vincristine",
        "RTOG 9402", "EORTC 26951", "CODEL", "POLA", "NOA-04", "CATNON",
        "BTSG", "Stupp", "Tumor Treating Fields", "TTFields", "Optune", "NovoTAL",
        "CeTeG", "NOA-09", "Canadian trial", "Roa", "Nordic trial", "Malmstrom",
        "IAEA", "Perry", "NRG BN001", "RTOG 9305", "brachytherapy boost",
        "SRS boost", "RANO", "pseudoprogression", "radiation necrosis", "Brandes",
        "bevacizumab", "BRAIN", "RTOG 1205", "GammaTile", "Cs-131", "EORTC contouring",
        "RTOG contouring", "RTOG 0825", "GBM AGILE", "NRG BN010", "AZD1390",
        "EF32", "EF41", "KEYNOTE D58"
    ],
    "prev": ["radbio.html", "放射生物", "RadBio"],
    "next": ["headneck.html", "頭頸癌", "Head & Neck"],
})




PAGES.append({
    "slug": "brain-mets",
    "emoji": "🧠",
    "title_zh": "腦轉移、全腦放療與立體定位放射手術",
    "title_en": "Brain Metastases, WBRT, and SRS",
    "sub_zh": "腦轉移診斷、預後工具、手術/SRS/WBRT 選擇、WBRT 認知保護、SRS 劑量與放射壞死管理。",
    "sub_en": "Brain metastasis workup, prognostication, surgery/SRS/WBRT selection, WBRT neuroprotection, SRS dosing, and radionecrosis management.",
    "sections": [

      {
        "label_zh": "概觀",
        "label_en": "OVERVIEW",
        "h2_zh": "腦轉移概觀、病理生理與常見原發癌",
        "h2_en": "Overview, pathogenesis, and common primary tumors",
        "body_zh": """
        <p><strong>腦轉移</strong>是成人最常見的顱內腫瘤，占成人腦腫瘤超過 50%；約 20–40% 癌症病人會發生顱內轉移。成人常見原發癌包括 <strong>lung、breast、kidney、colorectal、melanoma</strong>；兒童常見來源包括 sarcoma、neuroblastoma、germ-cell tumors。</p>
        <ul>
          <li><strong>傳播方式</strong>：最常見為 hematogenous spread。</li>
          <li><strong>典型位置</strong>：gray-white matter junction，因血管直徑變小而 trapping tumor emboli。</li>
          <li><strong>分布</strong>：約 80% cerebral hemispheres、15% cerebellum、5% brainstem。</li>
          <li><strong>多發性</strong>：許多病人表現為 multiple brain metastases。</li>
        </ul>
        """,
        "body_en": """
        <p><strong>Brain metastases</strong> are the most common intracranial tumors in adults, accounting for more than 50% of adult brain tumors. About 20–40% of cancer patients develop intracranial metastases. Common adult primaries include <strong>lung, breast, kidney, colorectal cancer, and melanoma</strong>; pediatric sources include sarcomas, neuroblastoma, and germ-cell tumors.</p>
        <ul>
          <li><strong>Mechanism</strong>: usually hematogenous spread.</li>
          <li><strong>Typical location</strong>: gray-white matter junction, where narrowing vessels trap tumor emboli.</li>
          <li><strong>Distribution</strong>: approximately 80% cerebral hemispheres, 15% cerebellum, and 5% brainstem.</li>
          <li><strong>Multiplicity</strong>: many patients present with multiple lesions.</li>
        </ul>
        """
      },

      {
        "label_zh": "診斷",
        "label_en": "DIAGNOSIS",
        "h2_zh": "臨床表現、影像與 leptomeningeal disease",
        "h2_en": "Presentation, imaging, and leptomeningeal disease",
        "body_zh": """
        <p>症狀主要來自腫瘤本身與周邊水腫：headache 40–50%、focal neurologic dysfunction 20–40%、cognitive dysfunction 30–50%、seizure 10–20%、stroke-like presentation 5–10%。較少見表現包括 intratumoral hemorrhage、obstructive hydrocephalus、tumor embolization。</p>
        <ul>
          <li><strong>初始評估</strong>：完整病史、身體檢查與 focused neurologic exam。</li>
          <li><strong>CT head without contrast</strong>：可先排除急性出血。</li>
          <li><strong>MRI brain with and without contrast</strong>：gold standard。T1 pre-contrast 常 iso/hypointense；T1 post-contrast 可 uniform、punctate 或 ring-enhancing；T2/FLAIR 通常 hyperintense，顯示 peritumoral edema。</li>
          <li><strong>Pathology</strong>：原則上需要 tissue diagnosis；若已知 metastatic cancer 且影像典型，可依臨床脈絡判斷。若無癌症病史，需 CT CAP、腦影像，並考慮 extracranial site biopsy 或 maximal safe resection。</li>
        </ul>
        <p><strong>Leptomeningeal carcinomatosis</strong> 是癌細胞侵犯 CSF 並附著於 meninges。症狀可包括 pain、seizure、nausea/vomiting、ataxia、incontinence、sensory symptoms、cranial nerve deficits。診斷依 MRI 的 nodular meningeal tumor/thickening/strong enhancement，以及 CSF cytology、opening pressure、leukocytes、protein。</p>
        """,
        "body_en": """
        <p>Symptoms are caused by tumor expansion and edema: headache 40–50%, focal neurologic dysfunction 20–40%, cognitive dysfunction 30–50%, seizures 10–20%, and stroke-like presentation 5–10%. Less common presentations include intratumoral hemorrhage, obstructive hydrocephalus, and tumor embolization.</p>
        <ul>
          <li><strong>Initial assessment</strong>: full history and physical examination with focused neurologic exam.</li>
          <li><strong>CT head without contrast</strong>: useful to rule out acute bleeding.</li>
          <li><strong>MRI brain with and without contrast</strong>: gold standard. T1 pre-contrast lesions are often iso/hypointense; T1 post-contrast lesions may be uniform, punctate, or ring-enhancing; T2/FLAIR is usually hyperintense and highlights peritumoral edema.</li>
          <li><strong>Pathology</strong>: tissue diagnosis is generally required. If metastatic cancer is known and imaging is typical, management may proceed in context. Without known malignancy, obtain CT CAP, brain imaging, and pursue biopsy of another metastatic site or maximal safe resection.</li>
        </ul>
        <p><strong>Leptomeningeal carcinomatosis</strong> occurs when cancer invades CSF and attaches to meninges. Symptoms include pain, seizures, nausea/vomiting, ataxia, incontinence, sensory symptoms, and cranial nerve deficits. Diagnosis uses MRI findings of nodular meningeal tumor/thickening/strong enhancement plus CSF cytology, opening pressure, leukocytes, and protein.</p>
        """
      },

      {
        "label_zh": "初始處置",
        "label_en": "INITIAL MANAGEMENT",
        "h2_zh": "Supportive care 與治療選擇",
        "h2_en": "Supportive care and treatment selection",
        "body_zh": """
        <p>腦轉移的治療通常先處理症狀，再依預後與病灶負荷選擇 surgery、SRS、WBRT 或 combination。</p>
        <ul>
          <li><strong>Steroid</strong>：dexamethasone 可在 3 天內改善約 75% 症狀。常用 IV 10 mg loading，之後 4 mg q6h；開始腫瘤導向治療後 taper。</li>
          <li><strong>Steroid supportive care</strong>：給 PPI 作 GI prophylaxis，監測/處理 hyperglycemia，並告知 steroid side effects。</li>
          <li><strong>Surgery</strong>：large tumor、significant edema/mass effect、或 histologic diagnosis 不確定。</li>
          <li><strong>SRS</strong>：small tumors、limited-volume disease、位於 eloquent/inaccessible areas，或 pre/postoperative local control。</li>
          <li><strong>WBRT</strong>：multiple tumors，例如 >10、high intracranial volume、leptomeningeal disease，或 SCLC brain-metastasis prophylaxis/PCI。</li>
        </ul>
        """,
        "body_en": """
        <p>Management usually begins with symptom control, then selection among surgery, SRS, WBRT, or combined-modality treatment according to prognosis and intracranial disease burden.</p>
        <ul>
          <li><strong>Steroids</strong>: dexamethasone improves symptoms in about 75% of patients within 3 days. A common regimen is IV 10 mg loading dose, then 4 mg q6h, followed by taper after tumor-directed therapy begins.</li>
          <li><strong>Steroid supportive care</strong>: give PPI for GI prophylaxis, monitor/manage hyperglycemia, and counsel on steroid adverse effects.</li>
          <li><strong>Surgery</strong>: large tumor, significant edema/mass effect, or uncertain histologic diagnosis.</li>
          <li><strong>SRS</strong>: small tumors, limited-volume disease, surgically inaccessible/eloquent locations, or pre/postoperative local control.</li>
          <li><strong>WBRT</strong>: multiple tumors, for example >10, high intracranial volume, leptomeningeal disease, or prophylaxis of brain metastases in SCLC/PCI.</li>
        </ul>
        """
      },

      {
        "label_zh": "預後",
        "label_en": "PROGNOSIS",
        "h2_zh": "RPA、GPA 與 Diagnosis-specific GPA",
        "h2_en": "RPA, GPA, and diagnosis-specific GPA",
        "body_zh": """
        <p>治療策略需先估計預後，尤其是 performance status、年齡、extracranial disease、腦轉移數量與總體積。</p>
        <ul>
          <li><strong>KPS/ECOG</strong>：ECOG 2 約等於 KPS 70%，表示可自我照顧與完成 ADL，但不能工作。</li>
          <li><strong>RTOG RPA</strong>：Class I = KPS ≥70、age &lt;65、controlled primary、no extracranial metastases，median survival 7.1 months；Class II median survival 4.2 months；Class III = KPS &lt;70，median survival 2.3 months。</li>
          <li><strong>GPA 2008</strong>：在 age、KPS、extracranial metastases 外，加入 number of CNS metastases；score 3.5–4 median survival 約 11 months，0–1 約 2.6 months。</li>
          <li><strong>Diagnosis-specific GPA 2020</strong>：基於多機構 6,984 位 newly diagnosed brain metastases 病人，排除 recurrent brain metastasis 與 leptomeningeal disease，用於 survival estimation、treatment individualization 與 trial stratification。</li>
        </ul>
        """,
        "body_en": """
        <p>Treatment selection requires prognostication, especially performance status, age, extracranial disease, number of brain metastases, and total intracranial volume.</p>
        <ul>
          <li><strong>KPS/ECOG</strong>: ECOG 2 roughly corresponds to KPS 70%, meaning the patient can care for self and perform ADLs but cannot work.</li>
          <li><strong>RTOG RPA</strong>: Class I = KPS ≥70, age &lt;65, controlled primary, no extracranial metastases, median survival 7.1 months; class II median survival 4.2 months; class III = KPS &lt;70, median survival 2.3 months.</li>
          <li><strong>GPA 2008</strong>: adds number of CNS metastases to age, KPS, and extracranial disease. Score 3.5–4 has median survival around 11 months; score 0–1 around 2.6 months.</li>
          <li><strong>Diagnosis-specific GPA 2020</strong>: based on a multi-institutional cohort of 6,984 newly diagnosed brain-metastasis patients, excluding recurrent brain metastasis and leptomeningeal disease; used to estimate survival, individualize treatment, and stratify trials.</li>
        </ul>
        """
      },

      {
        "label_zh": "WBRT",
        "label_en": "WBRT",
        "h2_zh": "全腦放療：適應症與常用劑量",
        "h2_en": "Whole-brain radiotherapy: indications and dose regimens",
        "body_zh": """
        <p><strong>WBRT</strong> 照射整個腦部，可同時處理 macroscopic brain metastasis 與 microscopic disease。</p>
        <ul>
          <li><strong>標準 regimen</strong>：30 Gy/10 fx。</li>
          <li><strong>較好預後</strong>：35 Gy/14 fx，可考慮用於減少 late toxicity。</li>
          <li><strong>較差預後</strong>：20 Gy/5 fx。</li>
          <li><strong>SCLC PCI</strong>：25 Gy/10 fx。</li>
          <li><strong>WBRT alone</strong>：不適合 SRS/surgery、poor PS、病灶太多或體積太大、leptomeningeal disease。</li>
          <li><strong>WBRT adjunct</strong>：可用於 surgery 或 SRS 之後改善 intracranial control。</li>
        </ul>
        """,
        "body_en": """
        <p><strong>WBRT</strong> treats the entire brain, including macroscopic brain metastases and microscopic disease.</p>
        <ul>
          <li><strong>Standard regimen</strong>: 30 Gy/10 fx.</li>
          <li><strong>Better prognosis</strong>: 35 Gy/14 fx, considered to minimize late toxicity.</li>
          <li><strong>Worse prognosis</strong>: 20 Gy/5 fx.</li>
          <li><strong>SCLC PCI</strong>: 25 Gy/10 fx.</li>
          <li><strong>WBRT alone</strong>: patients not eligible for SRS/surgery because of poor PS, too many/too large metastases, or leptomeningeal disease.</li>
          <li><strong>WBRT adjunct</strong>: after surgery or SRS to improve intracranial control.</li>
        </ul>
        """
      },

      {
        "label_zh": "WBRT 證據",
        "label_en": "WBRT EVIDENCE",
        "h2_zh": "Patchell、QUARTZ 與 WBRT 劑量研究",
        "h2_en": "Patchell, QUARTZ, and WBRT dose evidence",
        "body_zh": """
        <ul>
          <li><strong>Cairncross/MSKCC 1980</strong>：steroid + WBRT 後約 74% neurological improvement；多數死亡來自 systemic disease，而非 CNS progression。</li>
          <li><strong>Patchell I</strong>：48 位 single brain metastasis，surgery → WBRT 36 Gy/12 fx vs needle biopsy → WBRT。Surgery + WBRT 改善 recurrence 20% vs 52%、OS 40 vs 15 weeks、KPS 維持 38 vs 8 weeks。</li>
          <li><strong>Patchell II</strong>：97 位 resected single brain metastasis，postop WBRT 50.4 Gy/28 fx vs observation。WBRT 降低原位 recurrence 10% vs 46%、其他腦部 recurrence 14% vs 37%、neurologic death 14% vs 44%，但 OS 無差異，48 vs 43 weeks。</li>
          <li><strong>QUARTZ</strong>：538 位不適合 surgery/SRS 的 NSCLC brain metastases，dexamethasone + WBRT 20 Gy/5 fx vs supportive care alone。OS 與 QALY 無顯著差異，median OS 約 2 months；支持 limited life expectancy 時 hospice/best supportive care。</li>
          <li><strong>RTOG 6901/7361/9104</strong>：建立 30 Gy/10 fx 為最常用標準；20 Gy/5 fx 對 palliation 與較長療程相近；accelerated hyperfractionation 未改善 survival 或 toxicity。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Cairncross/MSKCC 1980</strong>: steroids + WBRT produced neurologic improvement in about 74%; most deaths were driven by systemic disease rather than CNS progression.</li>
          <li><strong>Patchell I</strong>: 48 patients with single brain metastasis randomized to surgery → WBRT 36 Gy/12 fx vs needle biopsy → WBRT. Surgery + WBRT improved recurrence 20% vs 52%, OS 40 vs 15 weeks, and KPS maintenance 38 vs 8 weeks.</li>
          <li><strong>Patchell II</strong>: 97 patients after resection of a single brain metastasis randomized to postop WBRT 50.4 Gy/28 fx vs observation. WBRT reduced original-site recurrence 10% vs 46%, other-brain recurrence 14% vs 37%, and neurologic death 14% vs 44%, but did not improve OS, 48 vs 43 weeks.</li>
          <li><strong>QUARTZ</strong>: 538 NSCLC patients unsuitable for surgery/SRS randomized to dexamethasone + WBRT 20 Gy/5 fx vs supportive care alone. No significant OS or QALY difference; median OS was about 2 months, supporting hospice/best supportive care for limited life expectancy.</li>
          <li><strong>RTOG 6901/7361/9104</strong>: established 30 Gy/10 fx as the most common standard; 20 Gy/5 fx is similarly palliative to longer schedules; accelerated hyperfractionation did not improve survival or toxicity.</li>
        </ul>
        """
      },

      {
        "label_zh": "WBRT 毒性",
        "label_en": "WBRT TOXICITY",
        "h2_zh": "WBRT 毒性、memantine 與 hippocampal avoidance",
        "h2_en": "WBRT toxicity, memantine, and hippocampal avoidance",
        "body_zh": """
        <p>WBRT 的主要限制是 4–6 個月後的 neurocognitive decline，尤其是 delayed recall/short-term memory。</p>
        <ul>
          <li><strong>急性毒性</strong>：fatigue、alopecia/scalp irritation、otitis/pressure-like sensation、nausea/vomiting、headache、dry eye/vision change、xerostomia、worsening cerebral edema。</li>
          <li><strong>晚期毒性</strong>：short-term memory loss、leukoencephalopathy、brain atrophy、neurocognitive deterioration/dementia、radiation necrosis、cataracts。每分次 &gt;3 Gy 時 radiation necrosis 風險較高。</li>
          <li><strong>RTOG 0614</strong>：WBRT 37.5 Gy/15 fx + memantine vs placebo。Primary delayed recall endpoint 未達顯著，但 memantine 延長 time to cognitive decline，改善 executive function、processing speed、delayed recognition；無 PFS/OS 差異，無額外 toxicity。</li>
          <li><strong>Memantine regimen</strong>：Week 1 5 mg daily；Week 2 5 mg bid；Week 3 10 mg morning + 5 mg evening；Week 4 10 mg bid，持續 24 weeks。CrCl &lt;30 mL/min 停在 5 mg BID；CrCl &lt;5 mL/min hold。</li>
          <li><strong>RTOG 0933</strong>：HA-WBRT 30 Gy/10 fx，brain metastasis 必須距 hippocampus &gt;5 mm。Hippocampus constraints：D100% &lt;9 Gy、Dmax &lt;16 Gy、mean &lt;10 Gy。4-month delayed recall decline 7% vs historical 30%。</li>
          <li><strong>NRG CC001</strong>：518 位 phase III，HA-WBRT + memantine vs WBRT + memantine，皆 30 Gy/10 fx。HA-WBRT + memantine 降低 cognitive failure，4–6 個月 executive function、total recall、delayed recognition 較佳。</li>
        </ul>
        """,
        "body_en": """
        <p>The main limitation of WBRT is neurocognitive decline at 4–6 months, especially delayed recall and short-term memory.</p>
        <ul>
          <li><strong>Acute toxicity</strong>: fatigue, alopecia/scalp irritation, otitis/pressure-like sensation, nausea/vomiting, headache, dry eye/vision change, xerostomia, and worsening cerebral edema.</li>
          <li><strong>Late toxicity</strong>: short-term memory loss, leukoencephalopathy, brain atrophy, neurocognitive deterioration/dementia, radiation necrosis, and cataracts. Radiation necrosis risk is higher with &gt;3 Gy/fraction.</li>
          <li><strong>RTOG 0614</strong>: WBRT 37.5 Gy/15 fx + memantine vs placebo. The primary delayed recall endpoint was not significant, but memantine prolonged time to cognitive decline and improved executive function, processing speed, and delayed recognition; no PFS/OS difference and no excess toxicity.</li>
          <li><strong>Memantine regimen</strong>: week 1 5 mg daily; week 2 5 mg bid; week 3 10 mg morning + 5 mg evening; week 4 10 mg bid, continued for 24 weeks. If CrCl &lt;30 mL/min, stop at 5 mg BID; if CrCl &lt;5 mL/min, hold.</li>
          <li><strong>RTOG 0933</strong>: HA-WBRT 30 Gy/10 fx for brain metastases &gt;5 mm from hippocampus. Hippocampal constraints: D100% &lt;9 Gy, Dmax &lt;16 Gy, mean &lt;10 Gy. Four-month delayed recall decline was 7% vs 30% historical control.</li>
          <li><strong>NRG CC001</strong>: 518-patient phase III trial of HA-WBRT + memantine vs WBRT + memantine, both 30 Gy/10 fx. HA-WBRT + memantine reduced cognitive failure and improved 4–6 month executive function, total recall, and delayed recognition.</li>
        </ul>
        """
      },

      {
        "label_zh": "WBRT 技術",
        "label_en": "WBRT TECHNIQUE",
        "h2_zh": "Conventional WBRT、HA-WBRT 與 plan evaluation",
        "h2_en": "Conventional WBRT, HA-WBRT, and plan evaluation",
        "body_zh": """
        <ul>
          <li><strong>傳統 German helmet field</strong>：supine、head neutral、3-point thermoplastic mask；gantry 90/270；collimator 旋轉使 inferior border 平行 skull base。</li>
          <li><strong>Field borders</strong>：anterior/superior/posterior 超出 skull 約 2 cm；inferior border 從 bony canthus 到 C1–C2 intervertebral space，需 cover skull base + 1 cm margin。</li>
          <li><strong>Technique</strong>：two opposed lateral fields，shield lens and upper airway；light field 從 lateral canthus 到 ear lobe；energy 4–6 MV。</li>
          <li><strong>CT-based planning</strong>：可用 opposed laterals 加 wedges 或 field-in-field 改善 homogeneity；MLC 可保護 scalp、lens 與 face。</li>
          <li><strong>HA-WBRT contouring</strong>：T1-weighted MRI 上 contour hippocampal subgranular zone；hypointense signal medial to temporal horn，quadrigeminal cistern 作 superior-medial landmark，至 splenium of corpus callosum 附近結束。加 5 mm margin 為 hippocampal avoidance zone。</li>
          <li><strong>Plan evaluation</strong>：95% brain receives 95% dose；hot spot &lt;110%。Lens Dmax &lt;6–8 Gy；parotid V20 Gy &lt;47%；hippocampus D100% &lt;9 Gy、Dmax &lt;16 Gy、mean &lt;10 Gy。NRG CC001：whole brain D2% ≤37.5 Gy、D98% ≥25 Gy、V30 Gy ≥95%；optic nerves/chiasm Dmax ≤30 Gy。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Traditional German helmet field</strong>: supine, head neutral, 3-point thermoplastic mask; gantry 90/270; collimator rotated so the inferior border parallels the skull base.</li>
          <li><strong>Field borders</strong>: anterior/superior/posterior borders extend about 2 cm beyond skull; inferior border from bony canthus to C1–C2 intervertebral space, covering skull base with 1 cm margin.</li>
          <li><strong>Technique</strong>: two opposed lateral fields, shield lens and upper airway; light field from lateral canthus to ear lobe; energy 4–6 MV.</li>
          <li><strong>CT-based planning</strong>: opposed laterals can use wedges or field-in-field to improve homogeneity; MLCs can spare scalp, lenses, and facial structures.</li>
          <li><strong>HA-WBRT contouring</strong>: use T1-weighted MRI to contour the hippocampal subgranular zone; hypointense signal medial to temporal horn, quadrigeminal cistern as superior-medial landmark, ending near splenium of corpus callosum. Add 5 mm margin to create hippocampal avoidance zone.</li>
          <li><strong>Plan evaluation</strong>: 95% of brain receives 95% dose; hot spot &lt;110%. Lens Dmax &lt;6–8 Gy; parotid V20 Gy &lt;47%; hippocampus D100% &lt;9 Gy, Dmax &lt;16 Gy, mean &lt;10 Gy. NRG CC001: whole brain D2% ≤37.5 Gy, D98% ≥25 Gy, V30 Gy ≥95%; optic nerves/chiasm Dmax ≤30 Gy.</li>
        </ul>
        """
      },

      {
        "label_zh": "SRS 原則",
        "label_en": "SRS PRINCIPLES",
        "h2_zh": "SRS 基本原理、歷史與適應症",
        "h2_en": "SRS principles, history, and indications",
        "body_zh": """
        <p><strong>SRS</strong> 是以 stereotactic precision 將高劑量 photon beam 聚焦於腦內 target，通常 1–5 fractions；可治療 brain metastases，也可治療 meningioma、vestibular schwannoma、pituitary adenoma、AVM、trigeminal neuralgia 等。</p>
        <ul>
          <li><strong>歷史重點</strong>：1908 Horsley/Clarke stereotactic apparatus；1947 Spiegel/Wycis human stereotactic application；1951 Lars Leksell 提出 stereotactic radiosurgery；1968 Stockholm 第一台 gamma unit；1987 美國第一台 Gamma Knife；1997 CyberKnife；1983 LINAC-based SRS 首篇報告。</li>
          <li><strong>Gamma Knife</strong>：192 cobalt sources，8 sectors，每 sector 24 sources；collimator 4/8/16 mm 或 block；通常 prescribed to 50% isodose line。</li>
          <li><strong>LINAC-based SRS</strong>：用 X-ray photons，以 convergent beams/arcs 造成 steep dose gradient；可用 static IMRT 或 VMAT。</li>
          <li><strong>適合族群</strong>：預期壽命 &gt;4–6 months、good PS、合理 lesion number/size/total volume，可避免或延後 WBRT toxicity。SRS 可重複，但 WBRT 的 whole-brain control 較強。</li>
          <li><strong>常見技術限制</strong>：number 通常 &lt;15–20；single fraction 通常 lesion &lt;2–2.5 cm；3 fractions 通常 &lt;5 cm；需符合 normal brain constraints。</li>
        </ul>
        """,
        "body_en": """
        <p><strong>SRS</strong> uses stereotactic precision to focus high-dose photon radiation on intracranial targets, usually in 1–5 fractions. It treats brain metastases and also benign/vascular entities such as meningioma, vestibular schwannoma, pituitary adenoma, AVM, and trigeminal neuralgia.</p>
        <ul>
          <li><strong>History</strong>: 1908 Horsley/Clarke stereotactic apparatus; 1947 Spiegel/Wycis human stereotactic application; 1951 Lars Leksell described stereotactic radiosurgery; 1968 first gamma unit in Stockholm; 1987 first US Gamma Knife; 1997 CyberKnife; 1983 first LINAC-based SRS report.</li>
          <li><strong>Gamma Knife</strong>: 192 cobalt sources, 8 sectors, 24 sources per sector; 4/8/16 mm collimators or block; usually prescribed to the 50% isodose line.</li>
          <li><strong>LINAC-based SRS</strong>: uses X-ray photons with convergent beams/arcs and steep dose gradients; delivered with static IMRT or VMAT.</li>
          <li><strong>Candidate profile</strong>: expected life expectancy &gt;4–6 months, good PS, reasonable lesion number/size/total volume, aiming to avoid or delay WBRT toxicity. SRS can be repeated, but WBRT gives stronger whole-brain control.</li>
          <li><strong>Common technical limits</strong>: number usually &lt;15–20; single fraction usually for lesions &lt;2–2.5 cm; 3 fractions usually for lesions &lt;5 cm; normal-brain constraints must be met.</li>
        </ul>
        """
      },

      {
        "label_zh": "SRS 劑量",
        "label_en": "SRS DOSE",
        "h2_zh": "SRS 劑量、local control 與 fractionation",
        "h2_en": "SRS dosing, local control, and fractionation",
        "body_zh": """
        <ul>
          <li><strong>RTOG 90-05</strong>：reirradiation phase I toxicity study，建立 single-fraction MTD：≤2 cm = 24 Gy，2–3 cm = 18 Gy，3–4 cm = 15 Gy。</li>
          <li><strong>Cleveland Clinic retrospective</strong>：依 RTOG 90-05 dosing，1-year local control：24 Gy (&lt;2 cm) 85%，18 Gy (2–3 cm) 49%，15 Gy (3–4 cm) 45%。提示 &gt;2 cm 病灶應考慮 fractionated SRS。</li>
          <li><strong>Minniti 2016</strong>：&gt;2 cm brain mets，27 Gy/3 fx 較 single fraction 改善 1-year local control 91% vs 77%，並降低 radiation necrosis 8% vs 20%。</li>
          <li><strong>HYTEC</strong>：≤2 cm 腫瘤約 18 Gy 可達 &gt;85% 1-year local control；melanoma 可能需 ≥21 Gy；&gt;2 cm 建議 fractionate。</li>
          <li><strong>Definitive SRS common dosing</strong>：24 Gy ×1 for &lt;2 cm；18 Gy ×1 for 2–3 cm；15 Gy ×1 for 3–4 cm。</li>
          <li><strong>Preop SRS</strong>：通常比 definitive dose 減少約 20%。&lt;2 cm 可用 21 Gy ×1；melanoma ≥21 Gy；靠近 OAR 可考慮 20 Gy。&gt;2 cm 可用 27 Gy/3 fx，靠近 OAR 可用 24 Gy/3 fx；&gt;30–50 cc 可考慮 30 Gy/5 fx。</li>
          <li><strong>Postop SRS</strong>：因 cavity 較大，常用 27 Gy/3 fx。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>RTOG 90-05</strong>: reirradiation phase I toxicity study establishing single-fraction MTD: ≤2 cm = 24 Gy, 2–3 cm = 18 Gy, 3–4 cm = 15 Gy.</li>
          <li><strong>Cleveland Clinic retrospective</strong>: using RTOG 90-05 dosing, 1-year local control was 85% for 24 Gy (&lt;2 cm), 49% for 18 Gy (2–3 cm), and 45% for 15 Gy (3–4 cm), suggesting lesions &gt;2 cm should be considered for fractionated SRS.</li>
          <li><strong>Minniti 2016</strong>: for brain mets &gt;2 cm, 27 Gy/3 fx improved 1-year local control 91% vs 77% and reduced radionecrosis 8% vs 20% compared with single fraction.</li>
          <li><strong>HYTEC</strong>: for tumors ≤2 cm, around 18 Gy can achieve &gt;85% 1-year local control; melanoma may require ≥21 Gy; lesions &gt;2 cm should be fractionated.</li>
          <li><strong>Definitive SRS common dosing</strong>: 24 Gy ×1 for &lt;2 cm; 18 Gy ×1 for 2–3 cm; 15 Gy ×1 for 3–4 cm.</li>
          <li><strong>Preop SRS</strong>: usually about 20% dose reduction from definitive dosing. &lt;2 cm can receive 21 Gy ×1; melanoma ≥21 Gy; 20 Gy if near OAR. &gt;2 cm can receive 27 Gy/3 fx, or 24 Gy/3 fx near OAR; &gt;30–50 cc may receive 30 Gy/5 fx.</li>
          <li><strong>Postop SRS</strong>: often 27 Gy/3 fx because cavities are larger.</li>
        </ul>
        """
      },

      {
        "label_zh": "SRS vs WBRT",
        "label_en": "SRS VS WBRT",
        "h2_zh": "Limited brain metastases：SRS alone 或加 WBRT？",
        "h2_en": "Limited brain metastases: SRS alone or with WBRT?",
        "body_zh": """
        <ul>
          <li><strong>RTOG 9508</strong>：1–3 brain metastases，WBRT 37.5 Gy/15 fx vs WBRT + SRS。整體 OS 無顯著改善，5.7 vs 6.5 months；single metastasis subgroup UVA 有 OS benefit；local control 改善 71% vs 82%。</li>
          <li><strong>JSROG-99</strong>：1–4 metastases ≤3 cm，WBRT 30 Gy/10 fx + SRS vs SRS alone。OS 無差異 7.5 vs 8 months；SRS alone new brain metastasis 較高 64% vs 42%，1-year local control 較差 73% vs 89%，但 neurologic death、functional preservation、MMSE 無差異。</li>
          <li><strong>Chang/MDACC 2009</strong>：1–3 brain mets，SRS + WBRT 30 Gy/12 fx vs SRS alone。因 SRS + WBRT 組 neurocognitive decline 較多而提前停止；HVLT-R decline 52% vs 24%。</li>
          <li><strong>Alliance N0574/RTOG 0671</strong>：1–3 brain mets，SRS alone vs SRS + WBRT 30 Gy/12 fx。3-month cognitive deterioration 較低於 SRS alone，64% vs 92%；但 intracranial control 較差 51% vs 84%。OS 無差異，10.4 vs 7.4 months。</li>
          <li><strong>實務重點</strong>：good PS 且預期存活 &gt;4 months 的 selected patients，通常偏向 SRS alone 以保護 cognition，但必須密切 MRI follow-up，因 distant brain failure 風險較高。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>RTOG 9508</strong>: 1–3 brain metastases, WBRT 37.5 Gy/15 fx vs WBRT + SRS. No significant OS improvement overall, 5.7 vs 6.5 months; single-metastasis subgroup showed OS benefit on UVA; local control improved 71% vs 82%.</li>
          <li><strong>JSROG-99</strong>: 1–4 metastases ≤3 cm, WBRT 30 Gy/10 fx + SRS vs SRS alone. No OS difference, 7.5 vs 8 months; SRS alone had more new brain metastases 64% vs 42% and worse 1-year local control 73% vs 89%, but no difference in neurologic death, functional preservation, or MMSE.</li>
          <li><strong>Chang/MDACC 2009</strong>: 1–3 brain mets, SRS + WBRT 30 Gy/12 fx vs SRS alone. Trial closed early due to more neurocognitive decline with SRS + WBRT; HVLT-R decline 52% vs 24%.</li>
          <li><strong>Alliance N0574/RTOG 0671</strong>: 1–3 brain mets, SRS alone vs SRS + WBRT 30 Gy/12 fx. Three-month cognitive deterioration was lower with SRS alone, 64% vs 92%; intracranial control was worse, 51% vs 84%. No OS difference, 10.4 vs 7.4 months.</li>
          <li><strong>Practice point</strong>: in selected patients with good PS and expected survival &gt;4 months, SRS alone is usually favored to preserve cognition, but close MRI follow-up is essential because distant brain failure risk is higher.</li>
        </ul>
        """
      },

      {
        "label_zh": "多發腦轉移",
        "label_en": "MULTIPLE METS",
        "h2_zh": "多發腦轉移：number vs volume",
        "h2_en": "Multiple brain metastases: number versus volume",
        "body_zh": """
        <ul>
          <li><strong>JLGK0901</strong>：1194 位 1–10 brain metastases，single tumor &lt;10 cc 且 &lt;3 cm，total cumulative tumor volume &lt;15 cc，無 WBRT。</li>
          <li><strong>Dose</strong>：&lt;4 cc 給 22 Gy；4–10 cc 給 20 Gy。</li>
          <li><strong>結果</strong>：2–4 顆與 5–10 顆 OS 無顯著差異，達 non-inferiority；toxicity 無顯著差異。OS：1 顆 13.9 months，2–4 顆 10.8 months，5–10 顆 10.8 months。</li>
          <li><strong>概念</strong>：腦轉移 <strong>total volume</strong> 對 OS 與 toxicity 通常比 number 更重要。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>JLGK0901</strong>: 1194 patients with 1–10 brain metastases; single tumor &lt;10 cc and &lt;3 cm; total cumulative tumor volume &lt;15 cc; no WBRT.</li>
          <li><strong>Dose</strong>: 22 Gy for &lt;4 cc; 20 Gy for 4–10 cc.</li>
          <li><strong>Results</strong>: no significant OS difference between 2–4 and 5–10 metastases, meeting non-inferiority; no significant toxicity difference. OS: 1 lesion 13.9 months, 2–4 lesions 10.8 months, 5–10 lesions 10.8 months.</li>
          <li><strong>Concept</strong>: total brain-metastasis <strong>volume</strong> is usually more important than number for OS and toxicity.</li>
        </ul>
        """
      },

      {
        "label_zh": "術前/術後 SRS",
        "label_en": "PERIOP SRS",
        "h2_zh": "Surgery + SRS：術後與術前策略",
        "h2_en": "Surgery plus SRS: postoperative and preoperative strategies",
        "body_zh": """
        <ul>
          <li><strong>Mahajan/MDACC</strong>：132 位 resected 1–3 brain mets，postop SRS within 30 days vs observation。12-month freedom from local recurrence 改善：43% observation vs 72% SRS；OS 無差異，18 vs 17 months；SRS 組無 radiation necrosis evidence。</li>
          <li><strong>NCCTG N107C/CEC-3</strong>：194 位 resected brain met cavity &lt;5 cm，WBRT 30/10 or 37.5/15 vs postop SRS 12–20 Gy by volume。SRS 組 6-month cognitive decline 較少，52% vs 85%；OS 無差異，11.6 vs 12.2 months；但 intracranial tumor progression 較快，6.4 vs 27.5 months，6-month surgical bed control 較差，80% vs 87%；SRS radionecrosis 4%。</li>
          <li><strong>Preop vs postop retrospective Patel</strong>：preop SRS 與 postop SRS 的 OS、local recurrence、distant recurrence 類似；postop SRS 有較高 LMD 16.6% vs 3.2% at 2 years，symptomatic radionecrosis 16.4% vs 4.9%。</li>
          <li><strong>Preop SRS potential advantages</strong>：較小 PTV margin、減少 cavity delineation uncertainty、較少 treatment delay、理論上可降低 surgical tumor spillage/CSF seeding 風險。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Mahajan/MDACC</strong>: 132 patients with resected 1–3 brain mets randomized to postop SRS within 30 days vs observation. Twelve-month freedom from local recurrence improved: 43% observation vs 72% SRS; no OS difference, 18 vs 17 months; no evidence of radionecrosis in the SRS group.</li>
          <li><strong>NCCTG N107C/CEC-3</strong>: 194 patients with resected brain-met cavity &lt;5 cm randomized to WBRT 30/10 or 37.5/15 vs postop SRS 12–20 Gy by volume. SRS had less 6-month cognitive decline, 52% vs 85%; no OS difference, 11.6 vs 12.2 months; but shorter time to intracranial progression, 6.4 vs 27.5 months, worse 6-month surgical-bed control, 80% vs 87%, and 4% radionecrosis.</li>
          <li><strong>Preop vs postop retrospective Patel</strong>: OS, local recurrence, and distant recurrence were similar; postop SRS had higher LMD, 16.6% vs 3.2% at 2 years, and symptomatic radionecrosis, 16.4% vs 4.9%.</li>
          <li><strong>Potential preop SRS advantages</strong>: smaller PTV margin, less cavity-delineation uncertainty, less treatment delay, and theoretical reduction in surgical tumor spillage/CSF seeding.</li>
        </ul>
        """
      },

      {
        "label_zh": "SRS Planning",
        "label_en": "SRS PLANNING",
        "h2_zh": "SRS simulation、target volume、plan evaluation 與 constraints",
        "h2_en": "SRS simulation, target volume, plan evaluation, and constraints",
        "body_zh": """
        <ul>
          <li><strong>Simulation</strong>：thermoplastic mask 或 head frame；CT head without contrast，slice thickness ≤1.25 mm。</li>
          <li><strong>MRI fusion</strong>：post-contrast T1-weighted MRI，1 mm slice thickness，gadolinium contrast，orthogonal/no gantry tilt，3D T1 echo-gradient sequence，例如 FSPGR 或 MPRAGE。MRI 到治療時間盡量不要超過 2 weeks。</li>
          <li><strong>Volumes</strong>：GTV = contrast-enhancing tumor 或 cavity on MRI；CTV = GTV；PTV = GTV + 0–2 mm。Intact lesions 常用 1 mm；postop 或 very small lesions 可考慮 2 mm。</li>
          <li><strong>OARs</strong>：brain、optic nerves/chiasm、brainstem、cochlea、eyes/lens。</li>
          <li><strong>Plan evaluation</strong>：99–100% PTV covered by prescription dose。Conformity index = volume covered by 100% isodose / PTV volume，goal 1–1.2。Gradient index = volume covered by 50% isodose / volume covered by 100% isodose，goal &lt;3。</li>
          <li><strong>HYTEC brain constraints</strong>：single fraction V12 &lt;5 cc 約 10% RN risk、V12 &lt;10 cc 約 15%、V12 &lt;15 cc 約 20%；3-fraction V20 &lt;20 cc；5-fraction V24 &lt;20 cc。</li>
          <li><strong>Selected OAR constraints</strong>：single fraction brainstem &lt;12.5 Gy，3-fraction brainstem &lt;18 Gy；single fraction optic structures &lt;10 Gy，3-fraction optic structures &lt;20 Gy；scalp &lt;8 Gy。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Simulation</strong>: thermoplastic mask or head frame; CT head without contrast, slice thickness ≤1.25 mm.</li>
          <li><strong>MRI fusion</strong>: post-contrast T1-weighted MRI, 1 mm slice thickness, gadolinium contrast, orthogonal/no gantry tilt, 3D T1 echo-gradient sequence such as FSPGR or MPRAGE. Try not to exceed 2 weeks between MRI and treatment.</li>
          <li><strong>Volumes</strong>: GTV = contrast-enhancing tumor or cavity on MRI; CTV = GTV; PTV = GTV + 0–2 mm. Intact lesions often use 1 mm; postop or very small lesions may use 2 mm.</li>
          <li><strong>OARs</strong>: brain, optic nerves/chiasm, brainstem, cochlea, eyes/lens.</li>
          <li><strong>Plan evaluation</strong>: 99–100% of PTV covered by prescription dose. Conformity index = volume covered by 100% isodose / PTV volume, goal 1–1.2. Gradient index = volume covered by 50% isodose / volume covered by 100% isodose, goal &lt;3.</li>
          <li><strong>HYTEC brain constraints</strong>: single-fraction V12 &lt;5 cc ≈ 10% RN risk, V12 &lt;10 cc ≈ 15%, V12 &lt;15 cc ≈ 20%; 3-fraction V20 &lt;20 cc; 5-fraction V24 &lt;20 cc.</li>
          <li><strong>Selected OAR constraints</strong>: single-fraction brainstem &lt;12.5 Gy, 3-fraction brainstem &lt;18 Gy; single-fraction optic structures &lt;10 Gy, 3-fraction optic structures &lt;20 Gy; scalp &lt;8 Gy.</li>
        </ul>
        """
      },

      {
        "label_zh": "放射壞死",
        "label_en": "RADIONECROSIS",
        "h2_zh": "SRS 後追蹤與 radiation necrosis 管理",
        "h2_en": "Post-SRS follow-up and radiation necrosis management",
        "body_zh": """
        <ul>
          <li><strong>Follow-up</strong>：SRS 後 brain MRI q2–3 months；2 年後可逐漸延長至 q4 months、q6 months。</li>
          <li><strong>Pathophysiology</strong>：vascular injury 造成 free radicals、inflammation、VEGF production、small-vessel narrowing/fibrinoid necrosis、ischemia/cell death；glial/endothelial damage 可造成 hypoxia、HIF-1α、VEGF、leaky capillaries、edema 與 contrast extravasation。</li>
          <li><strong>Risk factors</strong>：dose-volume、PTV margin、large tumors、prior radiation、concurrent systemic therapy。</li>
          <li><strong>Imaging differentiation</strong>：T1/T2 mismatch 較支持 radiation necrosis；T1/T2 match 較支持 recurrent tumor。快速進展 &lt;3 months 與 serial MRI 也可輔助判斷。</li>
          <li><strong>CTCAE v5 CNS necrosis</strong>：G1 asymptomatic observation；G2 moderate symptoms, corticosteroids；G3 severe symptoms medical intervention；G4 life-threatening urgent intervention；G5 death。</li>
          <li><strong>Management</strong>：symptomatic patients first-line corticosteroids，例如 dexamethasone 4–8 mg/day with gradual taper。其他選項包括 bevacizumab、pentoxifylline + vitamin E；Trental 400 mg + Vitamin E 400 IU BID ×6 months。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Follow-up</strong>: brain MRI every 2–3 months after SRS; after 2 years, may space to every 4 months and then every 6 months.</li>
          <li><strong>Pathophysiology</strong>: vascular injury causes free radicals, inflammation, VEGF production, small-vessel narrowing/fibrinoid necrosis, ischemia, and cell death; glial/endothelial injury can cause hypoxia, HIF-1α, VEGF, leaky capillaries, edema, and contrast extravasation.</li>
          <li><strong>Risk factors</strong>: dose-volume, PTV margin, large tumors, prior radiation, and concurrent systemic therapy.</li>
          <li><strong>Imaging clues</strong>: T1/T2 mismatch is more consistent with radiation necrosis; T1/T2 match is more consistent with recurrent tumor. Rapid imaging progression &lt;3 months and serial MRI trends help.</li>
          <li><strong>CTCAE v5 CNS necrosis</strong>: G1 asymptomatic observation; G2 moderate symptoms requiring corticosteroids; G3 severe symptoms requiring medical intervention; G4 life-threatening requiring urgent intervention; G5 death.</li>
          <li><strong>Management</strong>: corticosteroids first line for symptomatic patients, for example dexamethasone 4–8 mg/day with gradual taper. Other options include bevacizumab and pentoxifylline + vitamin E; Trental 400 mg + Vitamin E 400 IU BID ×6 months.</li>
        </ul>
        """
      },

      {
        "label_zh": "速記",
        "label_en": "QUICK FACTS",
        "h2_zh": "考試速記：腦轉移、WBRT、SRS",
        "h2_en": "Exam quick facts: brain metastases, WBRT, and SRS",
        "body_zh": """
        <ul>
          <li><strong>Brain mets location</strong>：gray-white matter junction；80% cerebrum、15% cerebellum、5% brainstem。</li>
          <li><strong>Most common adult primaries</strong>：lung、breast、kidney、colorectal、melanoma。</li>
          <li><strong>WBRT standard</strong>：30 Gy/10 fx；poor prognosis 20 Gy/5 fx；better prognosis 35 Gy/14 fx；SCLC PCI 25 Gy/10 fx。</li>
          <li><strong>Memantine</strong>：titrate to 10 mg BID，continue 24 weeks。</li>
          <li><strong>HA-WBRT hippocampus constraints</strong>：D100% &lt;9 Gy、Dmax &lt;16 Gy、mean &lt;10 Gy。</li>
          <li><strong>SRS RTOG 90-05</strong>：≤2 cm 24 Gy、2–3 cm 18 Gy、3–4 cm 15 Gy。</li>
          <li><strong>Large lesion</strong>：&gt;2 cm 考慮 27 Gy/3 fx；&gt;30–50 cc 可考慮 30 Gy/5 fx。</li>
          <li><strong>SRS constraints</strong>：single fraction V12 &lt;5 cc 約 10% RN risk；3 fx V20 &lt;20 cc；5 fx V24 &lt;20 cc。</li>
          <li><strong>Follow-up</strong>：SRS 後 MRI q2–3 months。</li>
          <li><strong>Radiation necrosis first-line</strong>：dexamethasone；refractory 可考慮 bevacizumab。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Brain mets location</strong>: gray-white matter junction; 80% cerebrum, 15% cerebellum, 5% brainstem.</li>
          <li><strong>Most common adult primaries</strong>: lung, breast, kidney, colorectal cancer, melanoma.</li>
          <li><strong>WBRT standard</strong>: 30 Gy/10 fx; poor prognosis 20 Gy/5 fx; better prognosis 35 Gy/14 fx; SCLC PCI 25 Gy/10 fx.</li>
          <li><strong>Memantine</strong>: titrate to 10 mg BID and continue 24 weeks.</li>
          <li><strong>HA-WBRT hippocampal constraints</strong>: D100% &lt;9 Gy, Dmax &lt;16 Gy, mean &lt;10 Gy.</li>
          <li><strong>SRS RTOG 90-05</strong>: ≤2 cm 24 Gy, 2–3 cm 18 Gy, 3–4 cm 15 Gy.</li>
          <li><strong>Large lesion</strong>: &gt;2 cm consider 27 Gy/3 fx; &gt;30–50 cc consider 30 Gy/5 fx.</li>
          <li><strong>SRS constraints</strong>: single-fraction V12 &lt;5 cc ≈ 10% RN risk; 3 fx V20 &lt;20 cc; 5 fx V24 &lt;20 cc.</li>
          <li><strong>Follow-up</strong>: MRI every 2–3 months after SRS.</li>
          <li><strong>Radiation necrosis first line</strong>: dexamethasone; refractory cases may use bevacizumab.</li>
        </ul>
        """
      },

    ],
    "excel_sheet": "CNS",
    "trial_filter": [
        "brain metastases", "brain mets", "WBRT", "whole brain radiotherapy",
        "SRS", "stereotactic radiosurgery", "FSRT", "hypofractionated SRS",
        "leptomeningeal", "leptomeningeal carcinomatosis",
        "Patchell", "QUARTZ", "RTOG 0614", "RTOG 0933", "NRG CC001",
        "RTOG 90-05", "RTOG 9508", "JSROG-99", "JLGK0901",
        "Alliance N0574", "RTOG 0671", "NCCTG N107C", "CEC-3",
        "Mahajan", "Brown", "Chang", "Minniti", "HYTEC",
        "memantine", "hippocampal avoidance", "radiation necrosis",
        "dexamethasone", "bevacizumab", "SCLC PCI"
    ],
    "prev": ["cns.html", "原發性中樞神經系統腫瘤", "CNS"],
    "next": ["headneck.html", "頭頸癌", "Head & Neck"],
})

PAGES.append({
    "slug": "headneck",
    "emoji": "🗣️",
    "title_zh": "頭頸癌",
    "title_en": "Head & Neck Cancer",
    "sub_zh": "頭頸部解剖、淋巴結分區、一般放療原則、口腔癌、口咽癌、鼻咽癌與喉癌。",
    "sub_en": "Head and neck anatomy, nodal levels, general RT principles, oral cavity, oropharynx, nasopharynx, and laryngeal cancer.",
    "sections": [

      {
        "label_zh": "解剖",
        "label_en": "ANATOMY",
        "h2_zh": "頭頸部 disease sites 與重要邊界",
        "h2_en": "Head and neck disease sites and key anatomic boundaries",
        "body_zh": """
        <p>頭頸部腫瘤的治療高度依賴解剖與淋巴引流。主要 disease sites 包含 <strong>nasal cavity/sinuses、oral cavity、nasopharynx、oropharynx、larynx、hypopharynx</strong>。</p>
        <ul>
          <li><strong>Oral cavity</strong>：lip、gingiva/alveolar ridges、oral tongue anterior 2/3、floor of mouth、buccal mucosa、retromolar trigone、hard palate。</li>
          <li><strong>Nasopharynx</strong>：anterior = posterior nares/posterior nasal septum；posterior = C1/C2；superior = skull base/basosphenoid；inferior = soft palate；lateral = eustachian tube、torus tubarius、fossa of Rosenmüller。NPC 最常源自 fossa of Rosenmüller。</li>
          <li><strong>Oropharynx</strong>：base of tongue、palatine tonsils、soft palate、posterior pharyngeal wall。Anterior boundary 為 circumvallate papillae/anterior tonsillar pillars；inferior 到 vallecula/tip of epiglottis。</li>
          <li><strong>Supraglottic larynx</strong>：tip of epiglottis 到 laryngeal ventricle；包含 epiglottis、false vocal cords、arytenoids、aryepiglottic folds。</li>
          <li><strong>Glottic larynx</strong>：true vocal cords、anterior/posterior commissures；淋巴較少，所以早期 glottic cancer 頸部淋巴轉移風險低。</li>
          <li><strong>Subglottic larynx</strong>：true vocal cords inferior surface 到 cricoid cartilage inferior surface/first tracheal ring，淋巴較豐富，需注意 level VI。</li>
          <li><strong>Hypopharynx</strong>：pyriform sinus、posterior pharyngeal wall、postcricoid region，通常 nodal risk 高。</li>
        </ul>
        """,
        "body_en": """
        <p>Head and neck treatment is anatomy-driven. Major disease sites include <strong>nasal cavity/sinuses, oral cavity, nasopharynx, oropharynx, larynx, and hypopharynx</strong>.</p>
        <ul>
          <li><strong>Oral cavity</strong>: lip, gingiva/alveolar ridges, anterior two-thirds of oral tongue, floor of mouth, buccal mucosa, retromolar trigone, and hard palate.</li>
          <li><strong>Nasopharynx</strong>: anterior = posterior nares/posterior nasal septum; posterior = C1/C2; superior = skull base/basosphenoid; inferior = soft palate; lateral = eustachian tube, torus tubarius, and fossa of Rosenmüller. NPC most commonly arises from the fossa of Rosenmüller.</li>
          <li><strong>Oropharynx</strong>: base of tongue, palatine tonsils, soft palate, and posterior pharyngeal wall. The anterior boundary is circumvallate papillae/anterior tonsillar pillars; inferior boundary reaches vallecula/tip of epiglottis.</li>
          <li><strong>Supraglottic larynx</strong>: tip of epiglottis to laryngeal ventricle; includes epiglottis, false vocal cords, arytenoids, and aryepiglottic folds.</li>
          <li><strong>Glottic larynx</strong>: true vocal cords and anterior/posterior commissures; sparse lymphatics explain low nodal risk in early glottic cancer.</li>
          <li><strong>Subglottic larynx</strong>: inferior surface of true vocal cords to inferior cricoid/first tracheal ring; richer lymphatics and level VI relevance.</li>
          <li><strong>Hypopharynx</strong>: pyriform sinus, posterior pharyngeal wall, and postcricoid region; nodal risk is usually high.</li>
        </ul>
        """
      },

      {
        "label_zh": "淋巴結",
        "label_en": "NODES",
        "h2_zh": "Cervical lymph node levels 與照射原則",
        "h2_en": "Cervical lymph-node levels and coverage principles",
        "body_zh": """
        <p>頭頸癌 elective nodal coverage 需根據 primary site、laterality、midline involvement、既有陽性淋巴結與相鄰 level 風險決定。</p>
        <ul>
          <li><strong>Level Ia/Ib</strong>：submental/submandibular。Lower lip、anterior oral tongue、anterior floor of mouth 需考慮 Ia；upper lip 需注意 facial lymphatics。</li>
          <li><strong>Levels II–IV</strong>：多數 HNSCC 幾乎都會納入 elective coverage。</li>
          <li><strong>Level V</strong>：nasopharynx 常需納入；若 level II 陽性，可考慮同側 V 低劑量或中劑量納入。</li>
          <li><strong>Level VI</strong>：central compartment；subglottic extension 或 subglottic primary 需納入。</li>
          <li><strong>Retropharyngeal nodes / Level VII</strong>：所有 pharynx sites 通常需 cover，特別是 nasopharynx、oropharynx、hypopharynx。</li>
          <li><strong>Bilateral vs unilateral</strong>：大多數頭頸癌需 bilateral neck coverage；例外是 well-lateralized tonsil 且無 BOT/soft palate involvement，以及部分 well-lateralized oral cavity tumors。</li>
          <li><strong>Adjacent-level rule</strong>：若某 nodal level involved，該 level 常給 intermediate/high dose，鄰近 levels 納入 low-dose elective volume。</li>
        </ul>
        """,
        "body_en": """
        <p>Elective nodal coverage depends on primary site, laterality, midline involvement, positive nodal levels, and adjacent-level risk.</p>
        <ul>
          <li><strong>Level Ia/Ib</strong>: submental/submandibular. Lower lip, anterior oral tongue, and anterior floor of mouth require level Ia consideration; upper lip requires facial lymphatics consideration.</li>
          <li><strong>Levels II–IV</strong>: commonly covered for most HNSCC sites.</li>
          <li><strong>Level V</strong>: routinely relevant for nasopharynx; if level II is involved, consider ipsilateral level V coverage.</li>
          <li><strong>Level VI</strong>: central compartment; cover for subglottic extension or subglottic primary.</li>
          <li><strong>Retropharyngeal nodes / Level VII</strong>: generally covered for pharyngeal sites, especially nasopharynx, oropharynx, and hypopharynx.</li>
          <li><strong>Bilateral vs unilateral</strong>: most head and neck cases receive bilateral neck coverage; exceptions include selected well-lateralized tonsil without BOT/soft-palate involvement and selected well-lateralized oral cavity tumors.</li>
          <li><strong>Adjacent-level rule</strong>: if a nodal level is involved, treat that level to intermediate/high dose and include adjacent levels in the elective low-dose volume.</li>
        </ul>
        """
      },

      {
        "label_zh": "一般 RT",
        "label_en": "GENERAL RT",
        "h2_zh": "Definitive RT、postoperative RT 與 fractionation",
        "h2_en": "Definitive RT, postoperative RT, and fractionation",
        "body_zh": """
        <p>許多 HNSCC disease sites 可用相似的 dose-volume framework，但仍需依 subsite、pathology、surgery status 與 OAR 調整。</p>
        <ul>
          <li><strong>Definitive RT SIB</strong>：常用 <strong>70/63/56 Gy in 35 fx</strong>。70 Gy 給 primary and gross nodes；63 Gy 給 mucosal margin 與 involved nodal levels；56 Gy 給 elective neck。</li>
          <li><strong>Alternative definitive schedules</strong>：可使用 sequential boost 50/60/70 Gy、hyperfractionation 或 accelerated regimens。RTOG 9003 顯示 hyperfractionation 與 accelerated concomitant boost 改善 LRC，但此研究屬 pre-IMRT、無 concurrent chemotherapy 時代。</li>
          <li><strong>Overall treatment time</strong>：tonsillar SCC retrospective data 顯示每延遲 1 天 RT，local control 約下降 1%；治療中斷應盡量避免。</li>
          <li><strong>Postoperative RT indication</strong>：pT3–T4、pN2–N3、ENE/ECE、close or positive surgical margin、LVSI、PNI。</li>
          <li><strong>Postoperative RT SIB</strong>：常用 <strong>60/57/54 Gy in 30 fx</strong>。60 Gy 給 tumor bed/involved nodal bed；57 Gy 給 operative bed/dissected neck；54 Gy 給 elective neck。</li>
          <li><strong>Positive margin or ENE/ECE</strong>：boost 到 <strong>66 Gy/33 fx</strong>，可用 sequential 6 Gy/3 fx。</li>
          <li><strong>Early glottic exception</strong>：T1N0 glottic larynx 63 Gy/28 fx；T2N0 glottic larynx 65.25 Gy/29 fx，皆 2.25 Gy/fx。</li>
        </ul>
        """,
        "body_en": """
        <p>Many HNSCC sites use a similar dose-volume framework, modified by subsite, pathology, surgical status, and organs at risk.</p>
        <ul>
          <li><strong>Definitive RT SIB</strong>: commonly <strong>70/63/56 Gy in 35 fx</strong>. Give 70 Gy to primary and gross nodes, 63 Gy to mucosal margin and involved nodal levels, and 56 Gy to elective neck.</li>
          <li><strong>Alternative definitive schedules</strong>: sequential boost 50/60/70 Gy, hyperfractionation, or accelerated regimens may be used. RTOG 9003 showed improved LRC with hyperfractionation and accelerated concomitant boost, but it was pre-IMRT and without concurrent chemotherapy.</li>
          <li><strong>Overall treatment time</strong>: retrospective tonsillar SCC data showed about 1% loss of local control per day of RT delay; treatment breaks should be minimized.</li>
          <li><strong>Postoperative RT indications</strong>: pT3–T4, pN2–N3, ENE/ECE, close or positive surgical margin, LVSI, or PNI.</li>
          <li><strong>Postoperative RT SIB</strong>: commonly <strong>60/57/54 Gy in 30 fx</strong>. Give 60 Gy to tumor bed/involved nodal bed, 57 Gy to operative bed/dissected neck, and 54 Gy to elective neck.</li>
          <li><strong>Positive margin or ENE/ECE</strong>: boost to <strong>66 Gy/33 fx</strong>, often using a sequential 6 Gy/3 fx boost.</li>
          <li><strong>Early glottic exception</strong>: T1N0 glottic larynx 63 Gy/28 fx; T2N0 glottic larynx 65.25 Gy/29 fx, both 2.25 Gy/fx.</li>
        </ul>
        """
      },

      {
        "label_zh": "系統治療",
        "label_en": "SYSTEMIC TX",
        "h2_zh": "Concurrent chemotherapy、cetuximab 與 immunotherapy",
        "h2_en": "Concurrent chemotherapy, cetuximab, and immunotherapy",
        "body_zh": """
        <ul>
          <li><strong>Definitive setting</strong>：cT3–T4 或 cN2+ 通常加 concurrent chemotherapy。</li>
          <li><strong>Postoperative setting</strong>：positive margin 或 ENE/ECE 加 concurrent chemotherapy；RTOG 9501/EORTC 22931 pooled analysis 支持這兩個 high-risk factors 最能預測 chemoRT benefit。</li>
          <li><strong>Cisplatin</strong>：標準 concurrent agent。High-dose 100 mg/m² q3 weeks 為傳統 category 1；weekly 40 mg/m² 常用且 toxicity 較低。30 mg/m² weekly 太低，不建議等同標準。</li>
          <li><strong>Cisplatin-ineligible</strong>：可考慮 cetuximab 或 carboplatin/paclitaxel；但 HPV-positive OPSCC 中，cetuximab 取代 cisplatin 結果較差。</li>
          <li><strong>Cetuximab</strong>：Bonner trial 顯示 cetuximab + RT 優於 RT alone；但 RTOG 1016、De-ESCALaTE、ARTSCAN III 顯示 HPV-positive OPSCC 中 cetuximab + RT inferior to cisplatin + RT。</li>
          <li><strong>Immunotherapy</strong>：HN004、JAVELIN、KEYNOTE-412 等 definitive chemoRT + ICI trials 未顯示明確 benefit；目前 chemoIO 主要 role 在 recurrent/metastatic disease。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Definitive setting</strong>: add concurrent chemotherapy for cT3–T4 or cN2+ disease.</li>
          <li><strong>Postoperative setting</strong>: add concurrent chemotherapy for positive margin or ENE/ECE; pooled RTOG 9501/EORTC 22931 analysis supports these as the strongest predictors of chemoRT benefit.</li>
          <li><strong>Cisplatin</strong>: standard concurrent agent. High-dose 100 mg/m² q3 weeks is the traditional category 1 regimen; weekly 40 mg/m² is commonly used with lower toxicity. Weekly 30 mg/m² is too low to be considered equivalent.</li>
          <li><strong>Cisplatin-ineligible</strong>: consider cetuximab or carboplatin/paclitaxel; however, in HPV-positive OPSCC, cetuximab substitution is inferior to cisplatin.</li>
          <li><strong>Cetuximab</strong>: Bonner showed cetuximab + RT better than RT alone, but RTOG 1016, De-ESCALaTE, and ARTSCAN III showed HPV-positive OPSCC outcomes are inferior with cetuximab + RT compared with cisplatin + RT.</li>
          <li><strong>Immunotherapy</strong>: HN004, JAVELIN, and KEYNOTE-412 did not establish a benefit for adding ICI to definitive chemoRT; chemoIO is mainly for recurrent/metastatic disease.</li>
        </ul>
        """
      },

      {
        "label_zh": "口腔癌",
        "label_en": "ORAL CAVITY",
        "h2_zh": "Oral cavity cancer：手術為主的疾病",
        "h2_en": "Oral cavity cancer: primarily surgical management",
        "body_zh": """
        <p>Oral cavity cancer 約占頭頸部惡性腫瘤 30%，約 95% 為 SCC，oral tongue 與 lip 是美國常見 subsites。主要風險因子包括 smoking、alcohol、chewing tobacco、poor oral hygiene、periodontal disease、ill-fitting dentures、betel nut、lip cancer 的 chronic sun exposure、immunosuppression、Fanconi anemia 與 dyskeratosis congenita。</p>
        <ul>
          <li><strong>Presentation</strong>：pain、nonhealing ulcer、bleeding、dysphagia、ill-fitting dentures、halitosis；advanced disease 可有 facial numbness、tongue protrusion difficulty、trismus。</li>
          <li><strong>Workup</strong>：H&P、visual inspection、palpation、cranial nerve/cervical LN exam、flexible nasolaryngoscopy 排除 second primary；CT neck with contrast、CT chest、PET/CT if nodal/distant staging needed、MRI if PNI concern；biopsy；dental/speech/swallow/nutrition/smoking cessation。</li>
          <li><strong>Primary treatment</strong>：oral cavity cancers should generally be managed with <strong>surgery</strong> rather than definitive chemoRT when resectable。</li>
          <li><strong>Elective neck</strong>：cN0 常做 elective dissection levels I–III；oral tongue 常 I–IV。Well-lateralized tumors 可 ipsilateral；central tumors 應 bilateral。</li>
          <li><strong>Low-risk omission</strong>：少數 early-stage low-risk tumors 可考慮不做 elective LND，例如 T1 upper lip、upper alveolar ridge、hard palate。</li>
          <li><strong>Sentinel lymph node biopsy</strong>：T1–T2 cN0 可考慮；floor of mouth、gingiva、hard palate 技術上較困難。</li>
          <li><strong>DOI/tumor thickness</strong>：≥4 mm 代表約 28% nodal involvement risk，且 regional recurrences 中約 40% 可為 contralateral。</li>
          <li><strong>Adjuvant RT</strong>：pT3–T4、pN2–3，或 pT1–2 N0–1 但有 LVSI、PNI、positive/close margin ≤5 mm、DOI ≥4–5 mm。</li>
          <li><strong>Adjuvant dose</strong>：60/57/54 Gy in 30 fx；positive margin 或 ENE boost 到 66 Gy/33 fx；positive margin 或 ENE 加 concurrent cisplatin。</li>
        </ul>
        """,
        "body_en": """
        <p>Oral cavity cancer accounts for about 30% of head and neck malignancies, with about 95% being SCC. Oral tongue and lip are common US subsites. Risk factors include smoking, alcohol, chewing tobacco, poor oral hygiene, periodontal disease, ill-fitting dentures, betel nut, chronic sun exposure for lip cancer, immunosuppression, Fanconi anemia, and dyskeratosis congenita.</p>
        <ul>
          <li><strong>Presentation</strong>: pain, nonhealing ulcer, bleeding, dysphagia, ill-fitting dentures, and halitosis; advanced disease can cause facial numbness, difficulty protruding the tongue, and trismus.</li>
          <li><strong>Workup</strong>: H&P, visual inspection, palpation, cranial nerve/cervical LN exam, flexible nasolaryngoscopy to rule out second primary; CT neck with contrast, CT chest, PET/CT if nodal/distant staging needed, MRI if PNI concern; biopsy; dental/speech/swallow/nutrition/smoking cessation.</li>
          <li><strong>Primary treatment</strong>: resectable oral cavity cancers should generally be managed with <strong>surgery</strong> rather than definitive chemoRT.</li>
          <li><strong>Elective neck</strong>: cN0 usually receives elective dissection of levels I–III; oral tongue often levels I–IV. Well-lateralized tumors may receive ipsilateral dissection; central tumors require bilateral management.</li>
          <li><strong>Low-risk omission</strong>: selected early low-risk tumors may omit elective LND, such as T1 upper lip, upper alveolar ridge, and hard palate.</li>
          <li><strong>Sentinel lymph node biopsy</strong>: option for T1–T2 cN0 disease; technically challenging in floor of mouth, gingiva, and hard palate.</li>
          <li><strong>DOI/tumor thickness</strong>: ≥4 mm implies around 28% nodal risk, and about 40% of regional recurrences may be contralateral.</li>
          <li><strong>Adjuvant RT</strong>: pT3–T4, pN2–3, or pT1–2 N0–1 with LVSI, PNI, positive/close margin ≤5 mm, or DOI ≥4–5 mm.</li>
          <li><strong>Adjuvant dose</strong>: 60/57/54 Gy in 30 fx; boost positive margin or ENE to 66 Gy/33 fx; add concurrent cisplatin for positive margin or ENE.</li>
        </ul>
        """
      },

      {
        "label_zh": "口咽癌",
        "label_en": "OROPHARYNX",
        "h2_zh": "Oropharyngeal cancer：HPV/p16 與 de-escalation",
        "h2_en": "Oropharyngeal cancer: HPV/p16 and de-escalation",
        "body_zh": """
        <p>Oropharyngeal cancer 是 HNSCC 常見 site，subsites 包括 <strong>base of tongue、palatine tonsil、soft palate、posterior pharyngeal wall</strong>。&gt;90% 為 SCC，男性較多。AJCC 8 將 HPV/p16-positive 與 HPV-negative OPSCC 視為不同疾病；HPV-positive 預後較佳。</p>
        <ul>
          <li><strong>Presentation</strong>：最常見為 painless neck mass；也可有 dysphagia、odynophagia、otalgia。Oral tongue fixation 暗示 deep muscle involvement；trismus 暗示 medial pterygoid invasion。</li>
          <li><strong>HPV+ profile</strong>：younger、non/light smoker、Caucasian、高風險性行為、tonsil/BOT、nonkeratinizing、basaloid、p16 upregulated、poorly differentiated。</li>
          <li><strong>HPV− profile</strong>：older、heavy smoking/drinking、keratinizing、p53 mutation、EGFR amplified。</li>
          <li><strong>Mechanism</strong>：HPV E7 binds pRB → cell-cycle deregulation and p16 overexpression；E6 binds p53 → p53 degradation。p16 可作 HPV surrogate marker。</li>
          <li><strong>Workup</strong>：H&P、nutrition/risk factors、BOT palpation、dental/neuro exam、flexible laryngoscopy、CBC/CMP、CT neck with contrast、PET/CT、MRI if PNI/skull-base concern、FNA suspicious node with HPV testing、EUA with tonsillectomy or BOT biopsy。</li>
          <li><strong>Referrals</strong>：dentistry before RT、fluoride、speech/swallow、nutrition、feeding tube if unable to eat/drink or &gt;10% weight loss during RT、audiogram if indicated。</li>
          <li><strong>Definitive RT</strong>：70/63/56 Gy in 35 fx。OPSCC elective volume 至少包含 RP + II–IV；若 adjacent level involved，加入 IB/V；well-lateralized tonsil with ≤1 cm soft palate/BOT invasion 可考慮 ipsilateral coverage。</li>
          <li><strong>Postop RT</strong>：60/57/54 Gy in 30 fx；positive margin 或 ECE/ENE 時 66 Gy/33 fx；elective coverage 同樣至少 RP + II–IV。</li>
          <li><strong>RTOG 0129</strong>：HPV+/p16+ 有明顯較佳 OS/PFS；HPV 與 p16 一致性佳。</li>
          <li><strong>RTOG 1016 / De-ESCALaTE</strong>：cetuximab 取代 cisplatin 未降低毒性，且 OS/PFS/recurrence 較差。</li>
          <li><strong>HN002</strong>：60 Gy + weekly cisplatin arm 達 prespecified endpoints；RT alone 未達標。</li>
          <li><strong>HN005</strong>：definitive dose de-escalation to 60 Gy ± nivolumab 未達 noninferiority，為 negative trial。</li>
          <li><strong>Postop TORS de-escalation</strong>：ECOG 3311 phase II promising；ADEPT/PATHOS 仍屬 trial context。Off trial 目前 HPV+ 與 HPV− 多數仍同強度治療。</li>
        </ul>
        """,
        "body_en": """
        <p>Oropharyngeal cancer is a common HNSCC site, with subsites including <strong>base of tongue, palatine tonsil, soft palate, and posterior pharyngeal wall</strong>. More than 90% are SCC, with male predominance. AJCC 8 separates HPV/p16-positive and HPV-negative OPSCC; HPV-positive disease has better prognosis.</p>
        <ul>
          <li><strong>Presentation</strong>: painless neck mass is most common; dysphagia, odynophagia, and otalgia may occur. Oral tongue fixation suggests deep muscle involvement; trismus suggests medial pterygoid invasion.</li>
          <li><strong>HPV+ profile</strong>: younger, non/light smoker, Caucasian, high-risk sexual behavior, tonsil/BOT, nonkeratinizing, basaloid, p16 upregulated, poorly differentiated.</li>
          <li><strong>HPV− profile</strong>: older, heavy smoking/drinking, keratinizing, p53 mutation, EGFR amplified.</li>
          <li><strong>Mechanism</strong>: HPV E7 binds pRB, causing cell-cycle deregulation and p16 overexpression; E6 binds p53, causing p53 degradation. p16 can act as an HPV surrogate marker.</li>
          <li><strong>Workup</strong>: H&P, nutrition/risk factors, BOT palpation, dental/neuro exam, flexible laryngoscopy, CBC/CMP, CT neck with contrast, PET/CT, MRI if PNI/skull-base concern, FNA suspicious node with HPV testing, and EUA with tonsillectomy or BOT biopsy.</li>
          <li><strong>Referrals</strong>: dentistry before RT, fluoride, speech/swallow, nutrition, feeding tube if unable to eat/drink or &gt;10% weight loss during RT, and audiogram if indicated.</li>
          <li><strong>Definitive RT</strong>: 70/63/56 Gy in 35 fx. OPSCC elective volume includes at least RP + II–IV; add IB/V if adjacent levels are involved; well-lateralized tonsil with ≤1 cm soft-palate/BOT invasion can be considered for ipsilateral coverage.</li>
          <li><strong>Postop RT</strong>: 60/57/54 Gy in 30 fx; 66 Gy/33 fx for positive margin or ECE/ENE; elective coverage similarly includes at least RP + II–IV.</li>
          <li><strong>RTOG 0129</strong>: HPV+/p16+ status strongly improves OS/PFS; HPV and p16 correlate well.</li>
          <li><strong>RTOG 1016 / De-ESCALaTE</strong>: replacing cisplatin with cetuximab did not reduce toxicity and worsened OS/PFS/recurrence.</li>
          <li><strong>HN002</strong>: 60 Gy + weekly cisplatin met prespecified endpoints; RT alone did not.</li>
          <li><strong>HN005</strong>: definitive de-escalation to 60 Gy ± nivolumab failed noninferiority.</li>
          <li><strong>Postop TORS de-escalation</strong>: ECOG 3311 phase II is promising; ADEPT/PATHOS remain trial-context strategies. Off trial, HPV+ and HPV− disease are usually treated with similar intensity.</li>
        </ul>
        """
      },

      {
        "label_zh": "鼻咽癌",
        "label_en": "NASOPHARYNX",
        "h2_zh": "Nasopharyngeal cancer：EBV、skull base 與 chemoRT",
        "h2_en": "Nasopharyngeal cancer: EBV, skull base, and chemoRT",
        "body_zh": """
        <p>Nasopharyngeal cancer 在美國少見，但在 South China、Southeast Asia、North Africa 流行，常與 EBV 相關，通常以 non-operative treatment 為主。</p>
        <ul>
          <li><strong>Risk factors</strong>：EBV、salt-preserved fish、preserved foods、low fruit/vegetable diet、tobacco smoke、family history、HPV。</li>
          <li><strong>Presentation</strong>：painless neck mass、nasal/ear fullness/congestion、headache、diplopia、facial numbness、dysphagia、hoarseness、Horner syndrome、CN XI deficits。</li>
          <li><strong>Cranial nerve patterns</strong>：CN VI 常最早受壓；cavernous sinus invasion 可有 Jacod triad：vision loss、ophthalmoplegia、trigeminal neuralgia；lateral RPN/jugular foramen involvement 可造成 CN IX–XII deficits。</li>
          <li><strong>Stage at diagnosis</strong>：LN involvement 非常常見，約 75–90%；約 50% bilateral；5–11% diagnosis 時已有 distant metastasis，常見 bone、lung、liver。</li>
          <li><strong>Workup</strong>：H&P with full neurologic exam、nasopharyngoscopy、CBC/CMP、EBV DNA PCR、CT skull base/neck with contrast、MRI skull base、PET/CT for T3–T4 or N+、primary biopsy 或 neck FNA、EBER ISH/LMP IHC、dental/speech/swallow/nutrition/audiology、smoking cessation。</li>
          <li><strong>T-staging concept</strong>：T1 confined to NPX or extension to OPX/nasal cavity without parapharyngeal involvement；T2 parapharyngeal/adjacent soft tissue；T3 skull base/cervical vertebra/pterygoid/paranasal sinus；T4 intracranial、CN、hypopharynx、orbit、parotid or extensive soft tissue。</li>
          <li><strong>N-staging concept</strong>：N1 unilateral cervical or uni/bilateral RP ≤6 cm above caudal cricoid；N2 bilateral cervical ≤6 cm；N3 &gt;6 cm or below caudal border of cricoid。</li>
          <li><strong>Intergroup 0099</strong>：RT + concurrent cisplatin + adjuvant cisplatin/5-FU 改善 OS/PFS，建立 locally advanced NPC chemoRT basis。</li>
          <li><strong>MAC-NPC</strong>：chemotherapy 加到 RT 帶來約 5-year OS absolute benefit 6%、10-year 8%；concurrent chemotherapy benefit 最大，induction/adjuvant 加到 chemoRT 也可改善 tumor control/survival。</li>
          <li><strong>Induction chemotherapy</strong>：locally advanced endemic-type NPC 可用 GP q3 weeks ×3 或 TPF q3 weeks ×3。Zhang NEJM/JCO 顯示 induction gem/cis → chemoRT 改善 OS、FFS、DMFS、LRFS，EBV DNA &gt;4000 copies/mL benefit 較明顯。</li>
          <li><strong>Concurrent chemotherapy</strong>：cisplatin 40 mg/m² weekly 或 100 mg/m² q3 weeks；induction 後再用 high-dose q3 week cisplatin toxicity concern 較高。</li>
        </ul>
        """,
        "body_en": """
        <p>Nasopharyngeal cancer is rare in the US but endemic in South China, Southeast Asia, and North Africa. It is commonly EBV-related and usually treated non-operatively.</p>
        <ul>
          <li><strong>Risk factors</strong>: EBV, salt-preserved fish, preserved foods, low fruit/vegetable diet, tobacco smoke, family history, and HPV.</li>
          <li><strong>Presentation</strong>: painless neck mass, nasal/ear fullness or congestion, headache, diplopia, facial numbness, dysphagia, hoarseness, Horner syndrome, and CN XI deficits.</li>
          <li><strong>Cranial nerve patterns</strong>: CN VI is often compressed first; cavernous sinus invasion can cause Jacod triad of vision loss, ophthalmoplegia, and trigeminal neuralgia; lateral RPN/jugular foramen involvement can cause CN IX–XII deficits.</li>
          <li><strong>Stage at diagnosis</strong>: nodal involvement is very common, around 75–90%; about 50% bilateral; 5–11% have distant metastasis at diagnosis, commonly bone, lung, and liver.</li>
          <li><strong>Workup</strong>: H&P with full neurologic exam, nasopharyngoscopy, CBC/CMP, EBV DNA PCR, CT skull base/neck with contrast, MRI skull base, PET/CT for T3–T4 or N+, primary biopsy or neck FNA, EBER ISH/LMP IHC, dental/speech/swallow/nutrition/audiology, and smoking cessation.</li>
          <li><strong>T-staging concept</strong>: T1 confined to NPX or extension to OPX/nasal cavity without parapharyngeal involvement; T2 parapharyngeal/adjacent soft tissue; T3 skull base/cervical vertebra/pterygoid/paranasal sinus; T4 intracranial, CN, hypopharynx, orbit, parotid, or extensive soft tissue.</li>
          <li><strong>N-staging concept</strong>: N1 unilateral cervical or uni/bilateral RP ≤6 cm above caudal cricoid; N2 bilateral cervical ≤6 cm; N3 &gt;6 cm or below caudal border of cricoid.</li>
          <li><strong>Intergroup 0099</strong>: RT + concurrent cisplatin + adjuvant cisplatin/5-FU improved OS/PFS and established the chemoRT basis for locally advanced NPC.</li>
          <li><strong>MAC-NPC</strong>: adding chemotherapy to RT gives an absolute OS benefit of about 6% at 5 years and 8% at 10 years; concurrent chemotherapy gives the largest benefit, and induction/adjuvant additions to chemoRT can also improve tumor control/survival.</li>
          <li><strong>Induction chemotherapy</strong>: locally advanced endemic-type NPC can receive GP q3 weeks ×3 or TPF q3 weeks ×3. Zhang NEJM/JCO showed induction gem/cis → chemoRT improved OS, FFS, DMFS, and LRFS, with strongest benefit when EBV DNA &gt;4000 copies/mL.</li>
          <li><strong>Concurrent chemotherapy</strong>: cisplatin 40 mg/m² weekly or 100 mg/m² q3 weeks; high-dose q3-week cisplatin after induction raises toxicity concerns.</li>
        </ul>
        """
      },

      {
        "label_zh": "喉癌",
        "label_en": "LARYNX",
        "h2_zh": "Laryngeal cancer：early glottic RT 與 organ preservation",
        "h2_en": "Laryngeal cancer: early glottic RT and organ preservation",
        "body_zh": """
        <p>Laryngeal cancer 男性較多；約 2/3 為 glottis、1/3 supraglottis、1–2% subglottis。Glottis 淋巴少，supraglottis/subglottis 淋巴豐富。</p>
        <ul>
          <li><strong>Presentation</strong>：hoarseness 尤其 early glottic；dysphagia/globus、cough、hemoptysis、stridor、otalgia。Supraglottic larynx 由 superior laryngeal nerve branches 支配，referred otalgia 可經 CN X/Arnold nerve。</li>
          <li><strong>Workup</strong>：H&P、cranial nerve and cervical LN exam、flexible nasolaryngoscopy 評估 primary and vocal cord mobility、videostroboscopy 評估 mucosal wave、CT neck with contrast、CT chest、PET/CT if needed、MRI if PNI concern、EUA with triple endoscopy and biopsy、dental/speech/swallow/nutrition/audiology/smoking cessation。</li>
          <li><strong>Early glottic RT</strong>：classically 3D-CRT opposed laterals；通常不做 elective nodal coverage，但 opposed laterals 會 incidentally cover level III。</li>
          <li><strong>Early glottic dose</strong>：T1N0 63 Gy/28 fx；T2N0 65.25 Gy/29 fx，皆 2.25 Gy/fx。T1 field 約 5×5 cm，T2 約 6×6 cm，依 tumor extent 調整。</li>
          <li><strong>Hypofractionation evidence</strong>：Japanese hypofractionation/KROG 0201 支持 early glottic cancer 使用 2.25 Gy/fx；KROG 0201 顯示 hypofractionation 至少不劣於 conventional fractionation，並可能縮短 OTT/改善 LC。</li>
          <li><strong>IMRT vs 3D-CRT</strong>：early glottic 使用 IMRT 仍有爭議，但現代 retrospective data 顯示 local/regional control 相近，可減少 carotid dose。</li>
          <li><strong>Early supraglottic/subglottic</strong>：T1–T2 N0、selected T3 N0 可用 definitive RT 70 Gy/35 fx；bulky T2 或 T3 可考慮 concurrent chemotherapy，或 larynx-preserving surgery 後依 pathology adjuvant。</li>
          <li><strong>Locally advanced</strong>：functional larynx → definitive chemoRT；nonfunctional larynx → total laryngectomy。</li>
          <li><strong>RTOG 91-11</strong>：concurrent chemoRT 改善 larynx preservation 82% vs induction 68% vs RT alone 64%，並改善 local control；OS 差異不顯著。</li>
          <li><strong>Elective nodes</strong>：locally advanced larynx 通常 bilateral II–IV；N+ 時同側/雙側 involved side level V；subglottic extension cover level VI。</li>
        </ul>
        """,
        "body_en": """
        <p>Laryngeal cancer is more common in men; about two-thirds arise in the glottis, one-third in the supraglottis, and 1–2% in the subglottis. The glottis has sparse lymphatics, whereas the supraglottis/subglottis have richer lymphatics.</p>
        <ul>
          <li><strong>Presentation</strong>: hoarseness, especially in early glottic disease; dysphagia/globus, cough, hemoptysis, stridor, and otalgia. Supraglottic innervation via superior laryngeal nerve branches explains referred otalgia through CN X/Arnold nerve.</li>
          <li><strong>Workup</strong>: H&P, cranial nerve and cervical LN exam, flexible nasolaryngoscopy to assess primary and vocal cord mobility, videostroboscopy for mucosal wave, CT neck with contrast, CT chest, PET/CT if needed, MRI if PNI concern, EUA with triple endoscopy and biopsy, and dental/speech/swallow/nutrition/audiology/smoking cessation.</li>
          <li><strong>Early glottic RT</strong>: classically 3D-CRT opposed laterals; no elective nodal coverage, although opposed laterals incidentally cover level III.</li>
          <li><strong>Early glottic dose</strong>: T1N0 63 Gy/28 fx; T2N0 65.25 Gy/29 fx, both 2.25 Gy/fx. T1 field is about 5×5 cm; T2 about 6×6 cm, adjusted to tumor extent.</li>
          <li><strong>Hypofractionation evidence</strong>: Japanese hypofractionation/KROG 0201 support 2.25 Gy/fx for early glottic cancer; KROG 0201 suggests hypofractionation is at least not inferior and may shorten OTT/improve LC.</li>
          <li><strong>IMRT vs 3D-CRT</strong>: IMRT for early glottic remains debated, but modern retrospective data show similar local/regional control and lower carotid dose.</li>
          <li><strong>Early supraglottic/subglottic</strong>: T1–T2 N0 and selected T3 N0 can receive definitive RT 70 Gy/35 fx; bulky T2 or T3 can receive concurrent chemotherapy, or larynx-preserving surgery followed by pathology-tailored adjuvant therapy.</li>
          <li><strong>Locally advanced</strong>: functional larynx → definitive chemoRT; nonfunctional larynx → total laryngectomy.</li>
          <li><strong>RTOG 91-11</strong>: concurrent chemoRT improved larynx preservation, 82% vs 68% induction vs 64% RT alone, and improved local control; OS was not significantly different.</li>
          <li><strong>Elective nodes</strong>: locally advanced larynx usually bilateral II–IV; if N+, include ipsilateral/bilateral level V as appropriate; cover level VI for subglottic extension.</li>
        </ul>
        """
      },

      {
        "label_zh": "檢查流程",
        "label_en": "WORKUP",
        "h2_zh": "頭頸癌共同 workup 與 referral checklist",
        "h2_en": "Common H&N workup and referral checklist",
        "body_zh": """
        <ul>
          <li><strong>History</strong>：症狀、weight loss/nutrition、smoking、alcohol、betel nut、sexual history when relevant、family history、hearing baseline、renal function/cisplatin eligibility。</li>
          <li><strong>Exam</strong>：cranial nerve exam、cervical lymph-node exam、oral cavity palpation、BOT palpation when OPSCC suspected、flexible nasolaryngoscopy。</li>
          <li><strong>Labs</strong>：CBC、CMP；NPC 加 EBV DNA PCR；cisplatin 前注意 creatinine。</li>
          <li><strong>Imaging</strong>：CT neck with contrast 為常見起點；CT chest for lung metastasis/second primary；PET/CT for stage III–IV、nodal/distant staging；MRI for PNI、skull base、neural involvement、soft-tissue extent。</li>
          <li><strong>Pathology</strong>：primary biopsy 或 suspicious node FNA；OPSCC 需 HPV/p16 testing；NPC 可做 EBER ISH 或 LMP IHC。</li>
          <li><strong>Referrals before RT</strong>：dentistry/tooth extraction before RT、fluoride、speech/swallow evaluation、nutrition、feeding tube if unable to eat/drink or severe weight loss、audiology before cisplatin、smoking cessation。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>History</strong>: symptoms, weight loss/nutrition, smoking, alcohol, betel nut, sexual history when relevant, family history, hearing baseline, renal function/cisplatin eligibility.</li>
          <li><strong>Exam</strong>: cranial nerve exam, cervical lymph-node exam, oral cavity palpation, BOT palpation when OPSCC suspected, and flexible nasolaryngoscopy.</li>
          <li><strong>Labs</strong>: CBC and CMP; add EBV DNA PCR for NPC; pay attention to creatinine before cisplatin.</li>
          <li><strong>Imaging</strong>: CT neck with contrast is a common starting point; CT chest for lung metastasis/second primary; PET/CT for stage III–IV or nodal/distant staging; MRI for PNI, skull base, neural involvement, and soft-tissue extent.</li>
          <li><strong>Pathology</strong>: primary biopsy or suspicious-node FNA; HPV/p16 testing for OPSCC; EBER ISH or LMP IHC for NPC.</li>
          <li><strong>Referrals before RT</strong>: dentistry/tooth extraction before RT, fluoride, speech/swallow evaluation, nutrition, feeding tube if unable to eat/drink or severe weight loss, audiology before cisplatin, and smoking cessation.</li>
        </ul>
        """
      },

      {
        "label_zh": "速記",
        "label_en": "QUICK FACTS",
        "h2_zh": "考試速記：頭頸癌放療劑量與關鍵原則",
        "h2_en": "Exam quick facts: H&N RT doses and key principles",
        "body_zh": """
        <ul>
          <li><strong>Definitive HNSCC</strong>：70/63/56 Gy in 35 fx SIB。</li>
          <li><strong>Postop HNSCC</strong>：60/57/54 Gy in 30 fx SIB；positive margin/ENE → 66 Gy/33 fx。</li>
          <li><strong>Concurrent chemo definitive</strong>：cT3–T4 或 cN2+。</li>
          <li><strong>Concurrent chemo postop</strong>：positive margin 或 ENE/ECE。</li>
          <li><strong>Cisplatin</strong>：100 mg/m² q3 weeks 或 weekly 40 mg/m²；weekly 30 mg/m² 太低。</li>
          <li><strong>Early glottic</strong>：T1N0 63 Gy/28 fx；T2N0 65.25 Gy/29 fx。</li>
          <li><strong>Oral cavity</strong>：手術為主；cN0 elective neck I–III，oral tongue I–IV；DOI ≥4 mm 高風險。</li>
          <li><strong>OPSCC</strong>：HPV+ 預後佳但 off-trial 不應隨意 de-escalate；cetuximab 不可常規取代 cisplatin。</li>
          <li><strong>NPC</strong>：EBV DNA 有 prognostic value；locally advanced 可 induction GP/TPF → chemoRT。</li>
          <li><strong>Larynx</strong>：functional locally advanced larynx → organ-preserving chemoRT；nonfunctional larynx → total laryngectomy。</li>
          <li><strong>Nodal rule</strong>：II–IV 常見；pharynx cover RP；NPC cover V；subglottic cover VI；anterior oral cavity/lower lip consider Ia。</li>
          <li><strong>IO</strong>：definitive chemoRT + ICI 目前未建立標準 benefit；主要用於 recurrent/metastatic disease。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Definitive HNSCC</strong>: 70/63/56 Gy in 35 fx SIB.</li>
          <li><strong>Postop HNSCC</strong>: 60/57/54 Gy in 30 fx SIB; positive margin/ENE → 66 Gy/33 fx.</li>
          <li><strong>Concurrent chemo definitive</strong>: cT3–T4 or cN2+.</li>
          <li><strong>Concurrent chemo postop</strong>: positive margin or ENE/ECE.</li>
          <li><strong>Cisplatin</strong>: 100 mg/m² q3 weeks or weekly 40 mg/m²; weekly 30 mg/m² is too low.</li>
          <li><strong>Early glottic</strong>: T1N0 63 Gy/28 fx; T2N0 65.25 Gy/29 fx.</li>
          <li><strong>Oral cavity</strong>: surgery-first; cN0 elective neck I–III, oral tongue I–IV; DOI ≥4 mm is high risk.</li>
          <li><strong>OPSCC</strong>: HPV+ has better prognosis but should not be routinely de-escalated off trial; cetuximab should not routinely replace cisplatin.</li>
          <li><strong>NPC</strong>: EBV DNA is prognostic; locally advanced disease can receive induction GP/TPF → chemoRT.</li>
          <li><strong>Larynx</strong>: functional locally advanced larynx → organ-preserving chemoRT; nonfunctional larynx → total laryngectomy.</li>
          <li><strong>Nodal rule</strong>: II–IV common; pharynx cover RP; NPC cover V; subglottic cover VI; anterior oral cavity/lower lip consider Ia.</li>
          <li><strong>IO</strong>: definitive chemoRT + ICI has not established standard benefit; main role is recurrent/metastatic disease.</li>
        </ul>
        """
      }

    ],
    "excel_sheet": "H&N",
    "trial_filter": [
        "head and neck", "HNSCC", "oral cavity", "oropharynx", "OPSCC",
        "HPV", "p16", "nasopharynx", "NPC", "EBV", "larynx", "glottic",
        "supraglottic", "subglottic", "hypopharynx", "sinonasal",
        "lymph node levels", "retropharyngeal", "level II", "level III",
        "level IV", "level V", "level VI", "definitive RT", "postoperative RT",
        "chemoRT", "cisplatin", "cetuximab", "carboplatin paclitaxel",
        "RTOG 9003", "Withers", "RTOG 9501", "EORTC 22931",
        "Bonner", "KEYNOTE-412", "JAVELIN", "HN004",
        "Tata Memorial", "Senti-MERORL", "Ganly", "RTOG 0920",
        "ORATOR", "RTOG 0129", "RTOG 1016", "De-ESCALaTE",
        "HN002", "HN005", "ECOG 3311", "ADEPT", "PATHOS",
        "Intergroup 0099", "MAC-NPC", "gemcitabine cisplatin",
        "TPF", "DIPPER", "VA Larynx", "RTOG 91-11",
        "KROG 0201", "early glottic", "larynx preservation"
    ],
    "prev": ["brain-mets.html", "腦轉移", "Brain Mets"],
    "next": ["lung.html", "肺癌", "Lung"],
})
PAGES.append({
    "slug": "lung",
    "emoji": "🫁",
    "title_zh": "肺癌",
    "title_en": "Lung Cancer",
    "sub_zh": "早期 / 局部晚期 / 轉移性 NSCLC 與局限 / 廣泛期 SCLC。",
    "sub_en": "Early / locally advanced / metastatic NSCLC, and limited / extensive SCLC.",
    "sections": [
      {"label_zh":"早期 NSCLC","label_en":"EARLY NSCLC","h2_zh":"早期 NSCLC (I–IIA)","h2_en":"Early NSCLC (I–IIA)",
       "body_zh":"<p>手術優先 (lobectomy + lymph node dissection)。<strong>醫學上無法手術者</strong> → <strong>SBRT</strong>。</p><p><strong>SBRT 劑量:</strong> peripheral 54 Gy/3 fx；central 50 Gy/5 fx；ultracentral 60 Gy/8 fx。</p><p><strong>RTOG 0236:</strong> 55 Gy/5 fx (BED &gt; 100) 3-yr LC 98%。</p>",
       "body_en":"<p>Surgery is preferred (lobectomy + LN dissection). <strong>Medically inoperable</strong> → <strong>SBRT</strong>.</p><p><strong>SBRT doses:</strong> peripheral 54 Gy/3 fx; central 50 Gy/5 fx; ultracentral 60 Gy/8 fx.</p><p><strong>RTOG 0236:</strong> 55 Gy/5 fx (BED &gt; 100) — 3-yr LC 98%.</p>"},
      {"label_zh":"局部晚期 NSCLC","label_en":"LA NSCLC","h2_zh":"局部晚期 NSCLC (III)","h2_en":"Locally advanced NSCLC (Stage III)",
       "body_zh":"<p><strong>標準:</strong> concurrent chemoRT 60 Gy/30 fx + weekly carboplatin/paclitaxel 或 cisplatin/etoposide。</p><p><strong>RTOG 0617:</strong> 74 Gy 沒有比 60 Gy 好，反而 OS 較差 → <strong>60 Gy 是標準</strong>。</p><p><strong>PACIFIC:</strong> chemoRT 之後 durvalumab consolidation 提升 5-yr OS (43% vs 33%) — Stage III unresectable 標準。</p>",
       "body_en":"<p><strong>Standard:</strong> Concurrent chemoRT 60 Gy/30 fx + weekly carbo/paclitaxel or cisplatin/etoposide.</p><p><strong>RTOG 0617:</strong> 74 Gy was inferior to 60 Gy (OS worse) → <strong>60 Gy is standard</strong>.</p><p><strong>PACIFIC:</strong> Durvalumab consolidation after chemoRT improves 5-yr OS (43% vs 33%) — standard for Stage III unresectable.</p>"},
      {"label_zh":"SCLC","label_en":"SCLC","h2_zh":"小細胞肺癌 (SCLC)","h2_en":"Small-cell lung cancer (SCLC)",
       "body_zh":"<p><strong>Limited-stage:</strong> concurrent chemoRT (cis/etop) with <strong>Turrisi</strong> 45 Gy/1.5 Gy BID/3wk 或標準分次 60–70 Gy (CONVERT 顯示 66 Gy QD 非劣於 BID)。</p><p><strong>PCI:</strong> LS-SCLC 完全反應者，25 Gy/10 fx，降低腦轉率並提升 OS。</p><p><strong>Extensive-stage:</strong> platinum/etoposide + <strong>atezolizumab</strong> (IMpower133)，胸部 consolidation RT 30 Gy/10 fx (CREST) 可考慮。</p>",
       "body_en":"<p><strong>Limited-stage:</strong> concurrent chemoRT (cis/etop) with <strong>Turrisi</strong> 45 Gy BID/3wk or QD 60–70 Gy (CONVERT — 66 Gy QD non-inferior to BID).</p><p><strong>PCI:</strong> Complete responders in LS-SCLC — 25 Gy/10 fx reduces brain mets and improves OS.</p><p><strong>Extensive-stage:</strong> platinum/etoposide + <strong>atezolizumab</strong> (IMpower133); consolidative thoracic RT 30 Gy/10 fx (CREST) may be considered.</p>"},
    ],
    "excel_sheet": "Lung",
    "prev": ["headneck.html", "頭頸", "H&N"],
    "next": ["breast.html", "乳癌", "Breast"],
})

PAGES.append({
    "slug": "breast",
    "emoji": "🎀",
    "title_zh": "乳癌",
    "title_en": "Breast Cancer",
    "sub_zh": "乳癌概觀、DCIS、早期乳癌、局部晚期乳癌、PMRT、RNI、放療分割、APBI 與 reirradiation。",
    "sub_en": "Breast cancer overview, DCIS, early-stage breast cancer, locally advanced disease, PMRT, RNI, fractionation, APBI, and reirradiation.",
    "sections": [

      {
        "label_zh": "概觀",
        "label_en": "OVERVIEW",
        "h2_zh": "乳癌概觀、分型與風險因子",
        "h2_en": "Breast cancer overview, subtypes, and risk factors",
        "body_zh": """
        <p>乳癌是女性最常見惡性腫瘤之一，若排除 non-melanoma skin cancer，終生風險約 <strong>1/8</strong>。乳癌臨床上依 <strong>hormone receptor, HR</strong> 與 <strong>HER2</strong> 表現分類。</p>
        <ul>
          <li><strong>常見分型</strong>：HER2−/HR+ 約 72%，HER2+/HR+ 約 10%，HER2+/HR− 約 5%，triple-negative 約 13%。</li>
          <li><strong>最常見病理</strong>：invasive mammary carcinoma, not otherwise specified，也就是 pure invasive ductal carcinoma；約 80% invasive breast cancers 為 IDC。</li>
          <li><strong>Rarer subtypes</strong>：tubular、medullary、mucinous/colloid、papillary、cribriform。Tubular 常 ER+/PR+ 且 well differentiated；medullary 常與 BRCA1、年輕、TNBC 相關；mucinous 常見於 older patients 且預後較佳。</li>
          <li><strong>Estrogen exposure risk</strong>：female sex、older age、early menarche、nulliparity、first birth age &gt;30、lack of breastfeeding、late menopause &gt;55、hormone replacement therapy。</li>
          <li><strong>Personal/family risk</strong>：family history、prior breast cancer、DCIS、LCIS、atypical ductal hyperplasia、dense breast tissue、childhood/youth chest RT。</li>
          <li><strong>Lifestyle/exposure</strong>：high-fat diet、postmenopausal obesity、sedentary lifestyle。</li>
          <li><strong>Genetic syndromes</strong>：BRCA1、BRCA2、Li-Fraumeni/p53、Cowden/PTEN、ATM、Peutz-Jeghers 等。</li>
        </ul>
        """,
        "body_en": """
        <p>Breast cancer is one of the most common malignancies among women; excluding non-melanoma skin cancer, lifetime risk is about <strong>1 in 8</strong>. Clinically, breast cancer is classified by <strong>hormone receptor, HR</strong>, and <strong>HER2</strong> expression.</p>
        <ul>
          <li><strong>Subtype distribution</strong>: HER2−/HR+ about 72%, HER2+/HR+ about 10%, HER2+/HR− about 5%, and triple-negative about 13%.</li>
          <li><strong>Most common pathology</strong>: invasive mammary carcinoma, not otherwise specified, corresponding to pure invasive ductal carcinoma; about 80% of invasive breast cancers are IDC.</li>
          <li><strong>Rarer subtypes</strong>: tubular, medullary, mucinous/colloid, papillary, and cribriform. Tubular tumors are usually ER+/PR+ and well differentiated; medullary tumors are associated with BRCA1, younger age, and TNBC; mucinous tumors occur in older patients and are favorable.</li>
          <li><strong>Estrogen exposure risk</strong>: female sex, older age, early menarche, nulliparity, first birth age &gt;30, lack of breastfeeding, late menopause &gt;55, and hormone replacement therapy.</li>
          <li><strong>Personal/family risk</strong>: family history, prior breast cancer, DCIS, LCIS, atypical ductal hyperplasia, dense breast tissue, and chest RT during youth.</li>
          <li><strong>Lifestyle/exposure</strong>: high-fat diet, postmenopausal obesity, and sedentary lifestyle.</li>
          <li><strong>Genetic syndromes</strong>: BRCA1, BRCA2, Li-Fraumeni/p53, Cowden/PTEN, ATM, Peutz-Jeghers, among others.</li>
        </ul>
        """
      },

      {
        "label_zh": "檢查",
        "label_en": "WORKUP",
        "h2_zh": "臨床表現、影像、病理與分期檢查",
        "h2_en": "Presentation, imaging, pathology, and staging workup",
        "body_zh": """
        <p>約 90% 乳癌由 screening mammogram 發現，約 10% 由 self/clinical breast exam 發現。常見臨床表現包括 painless mass、pain、nipple discharge、nipple retraction、axillary lymphadenopathy with occult primary。</p>
        <ul>
          <li><strong>Average-risk screening</strong>：ACS 建議 40–44 歲可選擇開始 mammogram，45–54 歲每年，≥55 歲每兩年；USPSTF 40–74 歲每兩年。</li>
          <li><strong>Differential diagnosis</strong>：fibroadenoma、cyst、infection、Mondor’s cord、intraductal papilloma、sclerosing adenosis、lactocele。</li>
          <li><strong>Physical exam</strong>：完整 H&P、breast exam、axillary nodes、supraclavicular nodes。</li>
          <li><strong>Breast anatomy</strong>：乳房分 4 quadrants；upper outer quadrant 乳腺量最多，也是最常見癌症位置；tumor location 以 o’clock position 描述。</li>
          <li><strong>Lymphatic drainage</strong>：主要流向 axilla levels I–III；medial tumors，尤其 LIQ，可流向 internal mammary nodes。SCV 位於 clavicular head 到 cricoid 間、SCM 與 scalene 之間；IMNs 位於前 3 intercostal spaces lateral to sternum，沿 internal mammary artery。</li>
          <li><strong>Imaging</strong>：mammography、ultrasound、MRI if indicated。</li>
          <li><strong>Pathology</strong>：core biopsy strongly preferred；needle aspirate 無法分辨 DCIS 與 invasive ductal carcinoma。</li>
          <li><strong>Pathology report</strong>：需記錄 morphology、grade、ER/PR percentage、HER2 IHC/FISH、Ki67。ER/PR &lt;1% negative，&lt;10% low positive；HER2 IHC 0/1+ negative、2+ equivocal 需 FISH、3+ positive；Ki67 &lt;14% 常視為 low/luminal A-like。</li>
          <li><strong>Systemic staging</strong>：clinical stage IIIA 以上，例如 T3N1、T4、N2，需 CT chest/abdomen/pelvis + bone scan 或 PET/CT；可考慮 brain MRI；若考慮 anthracycline chemotherapy，需 echocardiogram。</li>
        </ul>
        """,
        "body_en": """
        <p>About 90% of breast cancers are detected by screening mammography and about 10% by self or clinical breast examination. Presentations include painless mass, pain, nipple discharge, nipple retraction, and axillary lymphadenopathy with occult primary.</p>
        <ul>
          <li><strong>Average-risk screening</strong>: ACS suggests ages 40–44 as optional mammography start, 45–54 annual mammography, and ≥55 biennial screening; USPSTF recommends biennial screening from 40–74.</li>
          <li><strong>Differential diagnosis</strong>: fibroadenoma, cyst, infection, Mondor’s cord, intraductal papilloma, sclerosing adenosis, and lactocele.</li>
          <li><strong>Physical exam</strong>: complete H&P with breast, axillary node, and supraclavicular node examination.</li>
          <li><strong>Breast anatomy</strong>: the breast is divided into 4 quadrants; the upper outer quadrant has the most tissue volume and is the most common cancer location; tumor position is described by o’clock position.</li>
          <li><strong>Lymphatic drainage</strong>: primarily to axillary levels I–III; medial tumors, especially LIQ, may drain to internal mammary nodes. SCV nodes extend from clavicular head to cricoid between SCM and scalene; IMNs occupy the first 3 intercostal spaces lateral to sternum along the internal mammary artery.</li>
          <li><strong>Imaging</strong>: mammography, ultrasound, and MRI when indicated.</li>
          <li><strong>Pathology</strong>: core biopsy is strongly preferred; needle aspirate cannot distinguish DCIS from invasive ductal carcinoma.</li>
          <li><strong>Pathology report</strong>: document morphology, grade, ER/PR percentage, HER2 IHC/FISH, and Ki67. ER/PR &lt;1% is negative and &lt;10% low positive; HER2 IHC 0/1+ negative, 2+ equivocal requiring FISH, and 3+ positive; Ki67 &lt;14% is often considered low/luminal A-like.</li>
          <li><strong>Systemic staging</strong>: clinical stage IIIA or higher, such as T3N1, T4, or N2, requires CT chest/abdomen/pelvis plus bone scan or PET/CT; consider brain MRI; obtain echocardiogram if anthracycline chemotherapy is planned.</li>
        </ul>
        """
      },

      {
        "label_zh": "分期",
        "label_en": "STAGING",
        "h2_zh": "AJCC TNM 重點",
        "h2_en": "Key AJCC TNM concepts",
        "body_zh": """
        <ul>
          <li><strong>Tis</strong>：DCIS。</li>
          <li><strong>T1</strong>：≤2 cm；T1mi ≤1 mm，T1a &gt;1–5 mm，T1b &gt;5–10 mm，T1c &gt;10–20 mm。</li>
          <li><strong>T2</strong>：&gt;2–5 cm。</li>
          <li><strong>T3</strong>：&gt;5 cm。</li>
          <li><strong>T4</strong>：chest wall invasion、skin ulceration/satellite nodules/edema、T4a+b，或 inflammatory carcinoma。Pectoralis muscle involvement alone 不等於 chest wall invasion。</li>
          <li><strong>cN1</strong>：movable ipsilateral level I/II axillary nodes；cN1mi 為 &gt;0.2–2 mm。</li>
          <li><strong>cN2</strong>：fixed/matted ipsilateral level I/II axillary nodes，或 ipsilateral IMNs without axillary disease。</li>
          <li><strong>cN3</strong>：infraclavicular、IMN + axillary、或 supraclavicular nodes。</li>
          <li><strong>pN1</strong>：1–3 axillary nodes 或 IM sentinel nodes；pN2 = 4–9 axillary nodes 或 clinically positive IMNs with path-negative axilla；pN3 = ≥10 axillary nodes、axillary + clinically positive IMNs、或 SCV nodes。</li>
          <li><strong>M-stage</strong>：M0 no metastases；M0(i+) ≤0.2 mm metastatic deposit；cM1/pM1 為 macroscopic metastasis。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Tis</strong>: DCIS.</li>
          <li><strong>T1</strong>: ≤2 cm; T1mi ≤1 mm, T1a &gt;1–5 mm, T1b &gt;5–10 mm, T1c &gt;10–20 mm.</li>
          <li><strong>T2</strong>: &gt;2–5 cm.</li>
          <li><strong>T3</strong>: &gt;5 cm.</li>
          <li><strong>T4</strong>: chest wall invasion, skin ulceration/satellite nodules/edema, T4a+b, or inflammatory carcinoma. Pectoralis muscle involvement alone is not chest wall invasion.</li>
          <li><strong>cN1</strong>: movable ipsilateral level I/II axillary nodes; cN1mi is &gt;0.2–2 mm.</li>
          <li><strong>cN2</strong>: fixed/matted ipsilateral level I/II axillary nodes or ipsilateral IMNs without axillary disease.</li>
          <li><strong>cN3</strong>: infraclavicular, IMN + axillary, or supraclavicular nodes.</li>
          <li><strong>pN1</strong>: 1–3 axillary nodes or IM sentinel nodes; pN2 = 4–9 axillary nodes or clinically positive IMNs with path-negative axilla; pN3 = ≥10 axillary nodes, axillary + clinically positive IMNs, or SCV nodes.</li>
          <li><strong>M-stage</strong>: M0 no metastases; M0(i+) ≤0.2 mm metastatic deposit; cM1/pM1 macroscopic metastasis.</li>
        </ul>
        """
      },

      {
        "label_zh": "DCIS",
        "label_en": "DCIS",
        "h2_zh": "Ductal carcinoma in situ：RT benefit 與 omission",
        "h2_en": "Ductal carcinoma in situ: RT benefit and omission",
        "body_zh": """
        <p><strong>DCIS</strong> 約占乳癌 20%，屬 <strong>stage 0, pTis</strong>。約 80% DCIS 為 hormone-positive。多數由 screening mammogram 發現 microcalcifications；linear branching calcifications 傾向 high-grade DCIS，fine granular calcifications 傾向 low-grade DCIS。LCIS 通常不視為 malignancy，但 pleomorphic LCIS 需像 high-grade DCIS 處理。</p>
        <ul>
          <li><strong>Natural history</strong>：未治療 DCIS 最多約 30% 於 30 年內進展為 invasive malignancy。</li>
          <li><strong>RT effect</strong>：lumpectomy 後 adjuvant WBI 約將 local recurrence risk 減半；復發中約 50% 為 invasive recurrence。</li>
          <li><strong>NSABP B-17</strong>：lumpectomy ± WBI 50 Gy/25 fx，15-year any recurrence 35% → 20%，invasive recurrence 20% → 10%。</li>
          <li><strong>SweDCIS</strong>：20-year any recurrence 32% → 20%；invasive recurrence 20% → 15%。</li>
          <li><strong>EORTC 10853</strong>：15-year any recurrence 31% → 18%；invasive recurrence 16% → 10%。</li>
          <li><strong>UK/ANZ</strong>：12-year any recurrence 20% → 7%；invasive recurrence 9% → 3%。Tamoxifen 在此 trial 未降低 invasive recurrence，但 NSABP B-24 顯示有 benefit。</li>
          <li><strong>EBCTCG DCIS meta-analysis</strong>：WBI after DCIS lumpectomy halves in situ and invasive recurrence，但無 overall survival benefit。</li>
          <li><strong>ECOG 5194 omission</strong>：excision alone，margin ≥3 mm；12-year IBTR 14% for grade 1–2 and 25% for grade 3；recurrence risk 無 plateau。</li>
          <li><strong>RTOG 9804</strong>：good-risk DCIS 中 RT 仍改善 local control；omission 必須個別化。</li>
          <li><strong>Genomic assays</strong>：DCIS Oncotype 與 DCISionRT 可估計 recurrence risk；DCISionRT 在 PREDICT study 中改變 RT decision 約 42%。</li>
          <li><strong>Mastectomy for DCIS</strong>：即使 close/positive margins，多數情況 observation 即可；但 mastectomy 時應做 SLNB，以防 occult invasive component。</li>
        </ul>
        """,
        "body_en": """
        <p><strong>DCIS</strong> accounts for about 20% of breast cancers and is <strong>stage 0, pTis</strong>. About 80% of DCIS is hormone-positive. It is usually detected on screening mammography as microcalcifications; linear branching calcifications suggest high-grade DCIS, while fine granular calcifications suggest low-grade DCIS. LCIS is usually not considered malignancy, except pleomorphic LCIS, which is treated like high-grade DCIS.</p>
        <ul>
          <li><strong>Natural history</strong>: untreated DCIS may progress to invasive malignancy in up to about 30% over 30 years.</li>
          <li><strong>RT effect</strong>: adjuvant WBI after lumpectomy approximately halves local recurrence; about 50% of recurrences are invasive.</li>
          <li><strong>NSABP B-17</strong>: lumpectomy ± WBI 50 Gy/25 fx; 15-year any recurrence 35% → 20%, invasive recurrence 20% → 10%.</li>
          <li><strong>SweDCIS</strong>: 20-year any recurrence 32% → 20%; invasive recurrence 20% → 15%.</li>
          <li><strong>EORTC 10853</strong>: 15-year any recurrence 31% → 18%; invasive recurrence 16% → 10%.</li>
          <li><strong>UK/ANZ</strong>: 12-year any recurrence 20% → 7%; invasive recurrence 9% → 3%. Tamoxifen did not reduce invasive recurrence in this trial, though NSABP B-24 showed benefit.</li>
          <li><strong>EBCTCG DCIS meta-analysis</strong>: WBI after DCIS lumpectomy halves in situ and invasive recurrence but does not improve overall survival.</li>
          <li><strong>ECOG 5194 omission</strong>: excision alone with margin ≥3 mm; 12-year IBTR 14% for grade 1–2 and 25% for grade 3; recurrence risk does not plateau.</li>
          <li><strong>RTOG 9804</strong>: even in good-risk DCIS, RT improves local control; omission must be individualized.</li>
          <li><strong>Genomic assays</strong>: DCIS Oncotype and DCISionRT estimate recurrence risk; DCISionRT changed RT decisions about 42% of the time in the PREDICT study.</li>
          <li><strong>Mastectomy for DCIS</strong>: observation is usually adequate even with close/positive margins; perform SLNB at mastectomy in case occult invasion is found.</li>
        </ul>
        """
      },

      {
        "label_zh": "早期乳癌",
        "label_en": "EARLY STAGE",
        "h2_zh": "Early-stage invasive breast cancer：BCS + RT、boost 與 omission",
        "h2_en": "Early-stage invasive breast cancer: BCS + RT, boost, and omission",
        "body_zh": """
        <ul>
          <li><strong>NSABP B-04</strong>：radical mastectomy 未比 total mastectomy 改善 DFS/OS；cN0 patients 無 PMRT survival advantage。</li>
          <li><strong>NSABP B-06</strong>：stage I–II，lumpectomy + RT 將 20-year ipsilateral breast recurrence 從 39% 降至 14%，但 DFS/OS 與 mastectomy 類似。</li>
          <li><strong>EBCTCG BCS ± RT</strong>：17 trials, 10,801 patients；10-year recurrence 35% with BCS alone vs 19% with BCS + RT；15-year breast-cancer mortality absolute difference 3.8%。約每避免 4 個 10-year recurrence，可避免 1 個 15-year breast-cancer death。</li>
          <li><strong>Modern local control</strong>：舊研究中 surgery alone 約 30% recurrence，RT 降到約 15%；現代因 screening、better surgery、boost、systemic therapy，LRR 約 15% without RT、8% with RT、2–3% with RT + endocrine therapy。</li>
          <li><strong>Boost</strong>：EORTC 22881 與 Lyon trial 支持 boost 可降低 IBTR，但增加 fibrosis/cosmesis tradeoff。Young age、high grade、close margin、TNBC 等較支持 boost。</li>
          <li><strong>NSABP B-21</strong>：cT1a–bN0，tamoxifen vs RT vs RT+tamoxifen；14-year IBTR 29% tamoxifen alone vs 11% RT alone vs 10% RT+tamoxifen；OS 約 80% 無差異。Tamoxifen 也降低 contralateral breast cancer risk。</li>
          <li><strong>CALGB 9343</strong>：older low-risk ER+ patients，tamoxifen ± RT；RT 改善 local control，但 OS 無差異。</li>
          <li><strong>PRIME II</strong>：≥65 歲、HR+、stage I、tumor ≤3 cm、negative margins；10-year local recurrence 約 10% endocrine therapy alone vs 1% with RT，OS/DFS 類似。</li>
          <li><strong>RT omission rule</strong>：只有 favorable older HR+ stage I patients 且願意服用 5 年 endocrine therapy 時才考慮；若 young、high grade、TNBC 或需 boost，不應輕易 omission。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>NSABP B-04</strong>: radical mastectomy did not improve DFS/OS compared with total mastectomy; cN0 patients had no survival advantage from PMRT.</li>
          <li><strong>NSABP B-06</strong>: in stage I–II disease, lumpectomy + RT reduced 20-year ipsilateral breast recurrence from 39% to 14%, with DFS/OS similar to mastectomy.</li>
          <li><strong>EBCTCG BCS ± RT</strong>: 17 trials and 10,801 patients; 10-year recurrence 35% with BCS alone vs 19% with BCS + RT; 15-year breast-cancer mortality absolute difference 3.8%. About one breast-cancer death by year 15 was avoided for every four recurrences avoided by year 10.</li>
          <li><strong>Modern local control</strong>: older studies showed about 30% recurrence after surgery alone and about 15% with RT; modern LRR is about 15% without RT, 8% with RT, and 2–3% with RT + endocrine therapy due to screening, improved surgery, boost, and systemic therapy.</li>
          <li><strong>Boost</strong>: EORTC 22881 and the Lyon trial support boost for reducing IBTR, with fibrosis/cosmesis tradeoff. Young age, high grade, close margin, and TNBC favor boost.</li>
          <li><strong>NSABP B-21</strong>: cT1a–bN0, tamoxifen vs RT vs RT+tamoxifen; 14-year IBTR 29% tamoxifen alone vs 11% RT alone vs 10% RT+tamoxifen; OS around 80% without difference. Tamoxifen also lowers contralateral breast cancer risk.</li>
          <li><strong>CALGB 9343</strong>: older low-risk ER+ patients, tamoxifen ± RT; RT improved local control but not OS.</li>
          <li><strong>PRIME II</strong>: age ≥65, HR+, stage I, tumor ≤3 cm, negative margins; 10-year local recurrence about 10% with endocrine therapy alone vs 1% with RT, with similar OS/DFS.</li>
          <li><strong>RT omission rule</strong>: consider only for favorable older HR+ stage I patients who will take 5 years of endocrine therapy; do not omit casually in young, high-grade, TNBC, or boost-indicated disease.</li>
        </ul>
        """
      },

      {
        "label_zh": "Axilla/RNI",
        "label_en": "AXILLA/RNI",
        "h2_zh": "Axillary management 與 regional nodal irradiation",
        "h2_en": "Axillary management and regional nodal irradiation",
        "body_zh": """
        <ul>
          <li><strong>NSABP B-32</strong>：SLNB 可安全取代 ALND 於 sentinel node-negative patients，降低 morbidity。</li>
          <li><strong>AMAROS</strong>：positive SLN patients，axillary RT 可替代 ALND，outcomes 類似，lymphedema 較少；slides summary 指出 ALND lymphedema 23% vs SLNB/axillary RT 11%。</li>
          <li><strong>ACOSOG Z0011</strong>：BCS patients with 1–2 positive SLNs receiving WBI/systemic therapy，可 omit ALND；注意此策略不適用 mastectomy 或大量 nodal disease。</li>
          <li><strong>IBCSG 23-01</strong>：SLNB micrometastasis ≤2 mm 可 omit ALND；5-year DFS 類似，ALND 增加 grade 3 events、neuropathy、lymphedema。</li>
          <li><strong>After NAC SLNB</strong>：需 dual tracer 且至少取 ≥2 nodes 才能降低 false-negative rate；Alliance A011202 正在評估 residual nodal disease after NAC 的 axillary RT vs ALND。</li>
          <li><strong>RNI definition</strong>：通常包含 axillary levels I–III、supraclavicular nodes、internal mammary nodes。</li>
          <li><strong>MA.20 / EORTC 22922</strong>：支持 high-risk/node-positive patients 加 RNI，可改善 DFS/DM control；IMNI benefit 小但可能顯著。</li>
          <li><strong>IMN evidence</strong>：French、Korean、DBCG-IMN 等 dedicated IMNI trials 提示 small but significant benefit；需平衡 heart/lung dose。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>NSABP B-32</strong>: SLNB safely replaces ALND in sentinel node-negative patients with lower morbidity.</li>
          <li><strong>AMAROS</strong>: in positive SLN patients, axillary RT can replace ALND with similar outcomes and less lymphedema; slide summary reports lymphedema 23% with ALND vs 11% with SLNB/axillary RT.</li>
          <li><strong>ACOSOG Z0011</strong>: BCS patients with 1–2 positive SLNs receiving WBI/systemic therapy may omit ALND; this should not be generalized to mastectomy or heavy nodal burden.</li>
          <li><strong>IBCSG 23-01</strong>: SLNB micrometastasis ≤2 mm can omit ALND; 5-year DFS was similar, while ALND increased grade 3 events, neuropathy, and lymphedema.</li>
          <li><strong>SLNB after NAC</strong>: use dual tracer and sample at least ≥2 nodes to reduce false-negative rate; Alliance A011202 is evaluating axillary RT vs ALND for residual nodal disease after NAC.</li>
          <li><strong>RNI definition</strong>: usually includes axillary levels I–III, supraclavicular nodes, and internal mammary nodes.</li>
          <li><strong>MA.20 / EORTC 22922</strong>: support RNI in high-risk/node-positive patients, improving DFS/DM control; IMNI benefit is small but may be significant.</li>
          <li><strong>IMN evidence</strong>: French, Korean, and DBCG-IMN trials suggest a small but significant IMNI benefit; balance against heart/lung dose.</li>
        </ul>
        """
      },

      {
        "label_zh": "PMRT/LABC",
        "label_en": "PMRT/LABC",
        "h2_zh": "Locally advanced breast cancer、PMRT 與 NAC",
        "h2_en": "Locally advanced breast cancer, PMRT, and NAC",
        "body_zh": """
        <ul>
          <li><strong>LRR risk after mastectomy</strong>：ECOG pooled analysis 顯示 tumor size &gt;5 cm、≥4 nodes、ER-negative、tumor necrosis、pectoral fascia involvement 為 LRR risk factors。NSABP pooled analysis 中 recurrence 最常在 chest wall/mastectomy scar 57%，其次 SCV 23%、axilla 12%。</li>
          <li><strong>DBCG 82b</strong>：premenopausal high-risk patients，high risk = axillary N+、tumor &gt;5 cm、skin/pectoral fascia invasion；PMRT/RNI 48–50 Gy + CMF 改善 10-year LRR 32% → 9%、DFS 34% → 48%、OS 45% → 54%。</li>
          <li><strong>DBCG 82c</strong>：postmenopausal high-risk patients；PMRT/RNI + tamoxifen 改善 10-year LRR 35% → 8%、DFS 24% → 36%、OS 36% → 45%。</li>
          <li><strong>British Columbia</strong>：pN+ premenopausal after mastectomy/ALND/CMF；PMRT + comprehensive RNI 37.5 Gy/16 fx 改善 20-year DFS 31% → 48%、OS 37% → 47%、LRFFS 61% → 87%。</li>
          <li><strong>EBCTCG PMRT</strong>：PMRT/RNI 對 pN+ disease 改善 recurrence 與 breast-cancer mortality；benefit 需依 nodal burden 與 systemic therapy era 解讀。</li>
          <li><strong>PMRT indications</strong>：一般 stage III、T3–T4、≥4 positive nodes、positive margin 為 absolute/strong indications；T1–2 with 1–3 nodes 需 strongly consider；T3N0 controversial，需看 LVSI、grade、margin、premenopausal status 等。</li>
          <li><strong>NAC role</strong>：允許 downstaging，並依 residual disease 決定 adjuvant systemic therapy。</li>
          <li><strong>CREATE-X</strong>：HER2-negative residual disease after NAC；capecitabine 改善 DFS 74% vs 68%、OS 89% vs 84%，TNBC benefit 較大。</li>
          <li><strong>KATHERINE</strong>：HER2+ residual disease after NAC；T-DM1 vs trastuzumab，3-year DFS 88% vs 77%。</li>
          <li><strong>PMRT after NAC</strong>：BCS 後一定需要 breast RT；NSABP B-51 abstract suggests 若 ypN0 可省略 RNI。Mastectomy 後 PMRT 通常適用 clinical stage III 或 ypN+；PMRT = chest wall irradiation + RNI。</li>
          <li><strong>Bolus PMRT</strong>：bolus 使用需依 skin involvement、scar/chest wall risk、reconstruction 與 toxicity 個別化，不應無差別每天使用。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>LRR risk after mastectomy</strong>: ECOG pooled analysis identified tumor size &gt;5 cm, ≥4 nodes, ER-negative disease, tumor necrosis, and pectoral fascia involvement as LRR risk factors. In the NSABP pooled analysis, recurrence sites were chest wall/mastectomy scar 57%, SCV 23%, and axilla 12%.</li>
          <li><strong>DBCG 82b</strong>: premenopausal high-risk patients, with high risk defined as axillary N+, tumor &gt;5 cm, or skin/pectoral fascia invasion; PMRT/RNI 48–50 Gy + CMF improved 10-year LRR 32% → 9%, DFS 34% → 48%, and OS 45% → 54%.</li>
          <li><strong>DBCG 82c</strong>: postmenopausal high-risk patients; PMRT/RNI + tamoxifen improved 10-year LRR 35% → 8%, DFS 24% → 36%, and OS 36% → 45%.</li>
          <li><strong>British Columbia</strong>: pN+ premenopausal patients after mastectomy/ALND/CMF; PMRT + comprehensive RNI 37.5 Gy/16 fx improved 20-year DFS 31% → 48%, OS 37% → 47%, and LRFFS 61% → 87%.</li>
          <li><strong>EBCTCG PMRT</strong>: PMRT/RNI improves recurrence and breast-cancer mortality in pN+ disease; benefit should be interpreted by nodal burden and systemic therapy era.</li>
          <li><strong>PMRT indications</strong>: stage III, T3–T4, ≥4 positive nodes, and positive margin are absolute/strong indications; strongly consider for T1–2 with 1–3 nodes; T3N0 is controversial and depends on LVSI, grade, margin, and premenopausal status.</li>
          <li><strong>NAC role</strong>: enables downstaging and guides adjuvant systemic therapy according to residual disease.</li>
          <li><strong>CREATE-X</strong>: HER2-negative residual disease after NAC; capecitabine improved DFS 74% vs 68% and OS 89% vs 84%, with larger benefit in TNBC.</li>
          <li><strong>KATHERINE</strong>: HER2+ residual disease after NAC; T-DM1 vs trastuzumab improved 3-year DFS 88% vs 77%.</li>
          <li><strong>PMRT after NAC</strong>: BCS after NAC always requires breast RT; NSABP B-51 abstract suggests RNI may be omitted if ypN0. After mastectomy, PMRT is generally used for clinical stage III or ypN+ disease; PMRT = chest wall irradiation + RNI.</li>
          <li><strong>Bolus PMRT</strong>: bolus use should be individualized according to skin involvement, scar/chest-wall risk, reconstruction, and toxicity rather than applied daily to all patients.</li>
        </ul>
        """
      },

      {
        "label_zh": "分割",
        "label_en": "FRACTIONATION",
        "h2_zh": "Breast RT fractionation：moderate 與 extreme hypofractionation",
        "h2_en": "Breast RT fractionation: moderate and extreme hypofractionation",
        "body_zh": """
        <ul>
          <li><strong>Conventional WBI</strong>：50 Gy/25 fx over 5 weeks。</li>
          <li><strong>Canadian/Whelan</strong>：pT1–2N0 after BCS，negative margins；42.56 Gy/16 fx non-inferior to 50 Gy/25 fx，10-year LR 約 6%、OS 約 85%，toxicity/cosmesis 類似。</li>
          <li><strong>UK START A/B</strong>：40.05 Gy/15 fx over 3 weeks 至少與 50 Gy/25 fx 一樣有效且 late effects 較少；40 Gy/15 fx 成為常用標準。</li>
          <li><strong>DBCG Skagen 1</strong>：pT1–3N0–3 requiring RNI，50 Gy/25 fx vs 40 Gy/15 fx；3-year lymphedema 11.6% vs 11.8%，LRR/DM/death 無差異，支持 RNI 可用 moderate hypofractionation。</li>
          <li><strong>RTOG 1005</strong>：40 Gy/15 fx WBI with SIB to lumpectomy cavity 48 Gy；可縮短療程並整合 boost。</li>
          <li><strong>UK FAST</strong>：28.5 Gy/5 fx once weekly 在 ≥50、low-risk、node-negative BCS patients 中 toxicity 與 conventional RT 類似；30 Gy/5 fx weekly toxicity 較差。</li>
          <li><strong>FAST-Forward</strong>：26 Gy/5 fx daily over 1 week；常用 constraints 包含 ipsilateral lung V8 &lt;15%，heart V7 &lt;5%，V1.5 &lt;30%，PTV 95%-95%，V105 &lt;5%，V107 &lt;2%，Dmax 110%。</li>
          <li><strong>Summary regimens</strong>：42.56 Gy/16 fx、40 Gy/15 fx、40/48 Gy SIB、28.5 Gy/5 weekly、26 Gy/5 daily。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Conventional WBI</strong>: 50 Gy/25 fx over 5 weeks.</li>
          <li><strong>Canadian/Whelan</strong>: pT1–2N0 after BCS with negative margins; 42.56 Gy/16 fx was non-inferior to 50 Gy/25 fx, with 10-year LR about 6%, OS about 85%, and similar toxicity/cosmesis.</li>
          <li><strong>UK START A/B</strong>: 40.05 Gy/15 fx over 3 weeks is at least as effective as 50 Gy/25 fx and produces fewer late effects; 40 Gy/15 fx became a common standard.</li>
          <li><strong>DBCG Skagen 1</strong>: pT1–3N0–3 requiring RNI, 50 Gy/25 fx vs 40 Gy/15 fx; 3-year lymphedema 11.6% vs 11.8%, with no LRR/DM/death difference, supporting moderate hypofractionation for RNI.</li>
          <li><strong>RTOG 1005</strong>: 40 Gy/15 fx WBI with SIB to lumpectomy cavity 48 Gy; shortens treatment and integrates boost.</li>
          <li><strong>UK FAST</strong>: 28.5 Gy/5 fx once weekly had similar toxicity to conventional RT in age ≥50, low-risk, node-negative BCS patients; 30 Gy/5 fx weekly had worse toxicity.</li>
          <li><strong>FAST-Forward</strong>: 26 Gy/5 fx daily over 1 week; commonly used constraints include ipsilateral lung V8 &lt;15%, heart V7 &lt;5%, V1.5 &lt;30%, PTV 95%-95%, V105 &lt;5%, V107 &lt;2%, Dmax 110%.</li>
          <li><strong>Summary regimens</strong>: 42.56 Gy/16 fx, 40 Gy/15 fx, 40/48 Gy SIB, 28.5 Gy/5 weekly, and 26 Gy/5 daily.</li>
        </ul>
        """
      },

      {
        "label_zh": "APBI/再照射",
        "label_en": "APBI/RE-RT",
        "h2_zh": "Partial breast irradiation 與 breast reirradiation",
        "h2_en": "Partial breast irradiation and breast reirradiation",
        "body_zh": """
        <ul>
          <li><strong>Rationale</strong>：許多 ipsilateral breast recurrences 發生在原 tumor bed 附近，因此 selected low-risk patients 可考慮 APBI。</li>
          <li><strong>IMPORT-LOW</strong>：使用 mini-tangents，40 Gy/15 fx partial breast approach；適合 selected lower-risk early breast cancer。</li>
          <li><strong>NSABP B-39</strong>：APBI vs WBI，整體需謹慎解讀；APBI 便利但 patient selection 重要。</li>
          <li><strong>Florence APBI</strong>：30 Gy/5 fx daily 或 QOD，為常用 external-beam APBI regimen。</li>
          <li><strong>APBI candidates</strong>：通常年齡較大、small tumor、negative margins、ER+、node-negative、無 extensive LVSI、無高風險 biology；不適合 extensive DCIS、positive margin、multifocal/multicentric、高 nodal risk。</li>
          <li><strong>Reirradiation indication</strong>：prior ipsilateral BCT + WBI 後，若局部 recurrence 小且可再次 lumpectomy，希望避免 salvage mastectomy，可考慮 partial breast reirradiation。</li>
          <li><strong>RTOG 1014</strong>：&lt;3 cm recurrence，prior WBI &gt;1 year；partial-breast reirradiation 45 Gy/30 fx BID。5-year IBTR 5%，mastectomy rate 10%，OS/DMFS 95%，grade 3 toxicity 7%，無 grade 4–5。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Rationale</strong>: many ipsilateral breast recurrences occur near the original tumor bed, so selected low-risk patients can be considered for APBI.</li>
          <li><strong>IMPORT-LOW</strong>: mini-tangents using a 40 Gy/15 fx partial-breast approach; appropriate for selected lower-risk early breast cancer.</li>
          <li><strong>NSABP B-39</strong>: APBI vs WBI; interpretation requires caution, and patient selection remains essential.</li>
          <li><strong>Florence APBI</strong>: 30 Gy/5 fx daily or every other day, a common external-beam APBI regimen.</li>
          <li><strong>APBI candidates</strong>: generally older age, small tumor, negative margins, ER+, node-negative, no extensive LVSI, and no high-risk biology; avoid in extensive DCIS, positive margins, multifocal/multicentric disease, or high nodal risk.</li>
          <li><strong>Reirradiation indication</strong>: after prior ipsilateral BCT + WBI, if recurrence is small and re-lumpectomy is feasible, partial-breast reirradiation can avoid salvage mastectomy.</li>
          <li><strong>RTOG 1014</strong>: &lt;3 cm recurrence, prior WBI &gt;1 year; partial-breast reirradiation 45 Gy/30 fx BID. Five-year IBTR 5%, mastectomy rate 10%, OS/DMFS 95%, grade 3 toxicity 7%, and no grade 4–5 toxicity.</li>
        </ul>
        """
      },

      {
        "label_zh": "系統治療",
        "label_en": "SYSTEMIC TX",
        "h2_zh": "Endocrine therapy、chemotherapy、HER2 therapy 與 immunotherapy",
        "h2_en": "Endocrine therapy, chemotherapy, HER2 therapy, and immunotherapy",
        "body_zh": """
        <ul>
          <li><strong>Endocrine therapy</strong>：HR+ disease 的核心 systemic therapy。RT omission trials 都要求病人接受 endocrine therapy；若省略 RT，仍需服用約 5 年 endocrine therapy。</li>
          <li><strong>Chemotherapy</strong>：依 stage、nodal status、grade、genomic risk、HR/HER2 subtype 決定；TNBC 與 high-risk HR+ disease 較常需要 chemotherapy。</li>
          <li><strong>HER2-targeted therapy</strong>：HER2+ disease 需 HER2-directed therapy；HER2 IHC 2+ 需 FISH 判定 amplification。</li>
          <li><strong>After NAC residual disease</strong>：HER2-negative residual disease 可用 capecitabine，HER2-positive residual disease 用 T-DM1。</li>
          <li><strong>Immunotherapy</strong>：主要用於 selected TNBC settings；需依 stage、PD-L1/clinical context 與 contemporary systemic therapy standards 決定。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Endocrine therapy</strong>: core systemic therapy for HR+ disease. RT omission trials require endocrine therapy; if RT is omitted, the patient still needs about 5 years of endocrine therapy.</li>
          <li><strong>Chemotherapy</strong>: depends on stage, nodal status, grade, genomic risk, and HR/HER2 subtype; TNBC and high-risk HR+ disease more often require chemotherapy.</li>
          <li><strong>HER2-targeted therapy</strong>: HER2+ disease requires HER2-directed therapy; HER2 IHC 2+ requires FISH to determine amplification.</li>
          <li><strong>Residual disease after NAC</strong>: use capecitabine for HER2-negative residual disease and T-DM1 for HER2-positive residual disease.</li>
          <li><strong>Immunotherapy</strong>: mainly used in selected TNBC settings; use depends on stage, PD-L1/clinical context, and contemporary systemic therapy standards.</li>
        </ul>
        """
      },

      {
        "label_zh": "速記",
        "label_en": "QUICK FACTS",
        "h2_zh": "考試速記：乳癌放療與關鍵 trial",
        "h2_en": "Exam quick facts: breast RT and key trials",
        "body_zh": """
        <ul>
          <li><strong>DCIS</strong>：stage 0；lumpectomy 後 WBI 約 halves recurrence；無 OS benefit；mastectomy 後通常 observation，但需 SLNB。</li>
          <li><strong>BCS + RT</strong>：NSABP B-06 20-year IBTR 39% → 14%；EBCTCG 10-year recurrence 35% → 19%。</li>
          <li><strong>Boost</strong>：降低 IBTR，適合 young/high-grade/close margin/TNBC，但增加 fibrosis/cosmesis issue。</li>
          <li><strong>Older low-risk omission</strong>：CALGB 9343/PRIME II；RT omission 不影響 OS，但 10-year LR 約 10% vs 1–2%。</li>
          <li><strong>PMRT absolute/strong indications</strong>：T3–T4、≥4 positive nodes、positive margin、stage III。</li>
          <li><strong>PMRT 1–3 nodes</strong>：strongly consider，需看 age、grade、LVSI、margin、biology、systemic therapy。</li>
          <li><strong>RNI</strong>：axilla I–III + SCV + IMN；MA.20/EORTC 22922 支持 high-risk/node-positive use。</li>
          <li><strong>AMAROS</strong>：axillary RT 可替代 ALND，lymphedema 23% → 11%。</li>
          <li><strong>NAC residual disease</strong>：HER2− → capecitabine；HER2+ → T-DM1。</li>
          <li><strong>Moderate hypofractionation</strong>：42.56 Gy/16 fx 或 40 Gy/15 fx。</li>
          <li><strong>SIB</strong>：RTOG 1005 = 40 Gy/15 fx + SIB to 48 Gy。</li>
          <li><strong>Ultra-hypofractionation</strong>：FAST = 28.5 Gy/5 fx weekly；FAST-Forward = 26 Gy/5 fx daily。</li>
          <li><strong>APBI</strong>：Florence = 30 Gy/5 fx；IMPORT-LOW = 40 Gy/15 fx mini-tangents。</li>
          <li><strong>Reirradiation</strong>：RTOG 1014 = 45 Gy/30 fx BID partial breast re-RT。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>DCIS</strong>: stage 0; WBI after lumpectomy approximately halves recurrence; no OS benefit; after mastectomy usually observation, but perform SLNB.</li>
          <li><strong>BCS + RT</strong>: NSABP B-06 20-year IBTR 39% → 14%; EBCTCG 10-year recurrence 35% → 19%.</li>
          <li><strong>Boost</strong>: reduces IBTR; favored for young/high-grade/close margin/TNBC, but increases fibrosis/cosmesis issues.</li>
          <li><strong>Older low-risk omission</strong>: CALGB 9343/PRIME II; omission does not affect OS but 10-year LR is about 10% vs 1–2%.</li>
          <li><strong>PMRT absolute/strong indications</strong>: T3–T4, ≥4 positive nodes, positive margin, and stage III.</li>
          <li><strong>PMRT for 1–3 nodes</strong>: strongly consider based on age, grade, LVSI, margin, biology, and systemic therapy.</li>
          <li><strong>RNI</strong>: axilla I–III + SCV + IMN; MA.20/EORTC 22922 support use in high-risk/node-positive disease.</li>
          <li><strong>AMAROS</strong>: axillary RT can replace ALND, with lymphedema 23% → 11%.</li>
          <li><strong>Residual disease after NAC</strong>: HER2− → capecitabine; HER2+ → T-DM1.</li>
          <li><strong>Moderate hypofractionation</strong>: 42.56 Gy/16 fx or 40 Gy/15 fx.</li>
          <li><strong>SIB</strong>: RTOG 1005 = 40 Gy/15 fx + SIB to 48 Gy.</li>
          <li><strong>Ultra-hypofractionation</strong>: FAST = 28.5 Gy/5 fx weekly; FAST-Forward = 26 Gy/5 fx daily.</li>
          <li><strong>APBI</strong>: Florence = 30 Gy/5 fx; IMPORT-LOW = 40 Gy/15 fx mini-tangents.</li>
          <li><strong>Reirradiation</strong>: RTOG 1014 = 45 Gy/30 fx BID partial breast re-RT.</li>
        </ul>
        """
      }

    ],
    "excel_sheet": "Breast",
    "trial_filter": [
        "breast cancer", "breast", "DCIS", "LCIS", "invasive ductal carcinoma",
        "IDC", "invasive lobular carcinoma", "ILC", "HR positive", "ER positive",
        "PR positive", "HER2", "triple negative", "TNBC", "lumpectomy",
        "breast conserving surgery", "BCS", "mastectomy", "SLNB", "ALND",
        "axilla", "regional nodal irradiation", "RNI", "internal mammary",
        "IMN", "supraclavicular", "PMRT", "postmastectomy radiotherapy",
        "neoadjuvant chemotherapy", "NAC", "capecitabine", "T-DM1",
        "trastuzumab", "endocrine therapy", "tamoxifen", "aromatase inhibitor",
        "NSABP B-04", "NSABP B-06", "EBCTCG", "EORTC 22881", "Lyon Trial",
        "NSABP B-21", "NSABP B-32", "AMAROS", "ACOSOG Z0011",
        "IBCSG 23-01", "MA.20", "EORTC 22922", "CALGB 9343", "PRIME II",
        "NSABP B-17", "SweDCIS", "EORTC 10853", "UK ANZ", "ECOG 5194",
        "RTOG 9804", "DCIS Oncotype", "DCISionRT", "DBCG 82b", "DBCG 82c",
        "British Columbia", "NSABP B-18", "NSABP B-27", "CREATE-X",
        "KATHERINE", "NSABP B-51", "Alliance Z1071", "SENTINA",
        "SN FNAC", "Alliance A011202", "DBCG-IMN", "Canadian Trial",
        "Whelan", "UK START A", "UK START B", "DBCG Skagen 1", "FABREC",
        "RTOG 1005", "UK FAST", "FAST Forward", "IMPORT LOW",
        "NSABP B-39", "Florence APBI", "RTOG 1014", "APBI",
        "partial breast irradiation", "reirradiation", "hypofractionation"
    ],
    "prev": ["headneck.html", "頭頸癌", "Head & Neck"],
    "next": ["lung.html", "肺癌", "Lung"],
})

PAGES.append({
    "slug": "gi",
    "emoji": "🧬",
    "title_zh": "胃腸道腫瘤",
    "title_en": "Gastrointestinal Cancers",
    "sub_zh": "食道癌、局部晚期直腸癌、胰臟腺癌與肛門癌：檢查評估、解剖、分期、放療劑量、系統治療、全程新輔助治療（TNT）、器官保留與關鍵臨床試驗。",
    "sub_en": "Esophageal cancer, locally advanced rectal cancer, pancreatic adenocarcinoma, and anal cancer: workup, anatomy, staging, RT dose, systemic therapy, TNT, organ preservation, and key clinical trials.",
    "sections": [

      {
        "label_zh": "GI 總覽",
        "label_en": "GI OVERVIEW",
        "h2_zh": "胃腸道腫瘤放射腫瘤學總覽",
        "h2_en": "Overview of GI radiation oncology",
        "body_zh": """

        <p>本頁整合四個高頻胃腸道放射腫瘤學主題：<strong>食道癌、局部晚期直腸癌、胰臟腺癌與肛門癌</strong>。這四種疾病的共同特色是治療高度依賴解剖位置、淋巴引流、局部侵犯、可切除性、分子分型與多專科治療順序。</p>
        <ul>
          <li><strong>食道癌</strong>：治癒意圖治療主要分成 CROSS／CheckMate 577 路徑與圍手術期 FLOT 路徑；根治性同步放化療則是無法手術或器官保留策略的核心。</li>
          <li><strong>直腸癌</strong>：放療或同步放化療主要提供局部控制效益；現代治療已從固定順序走向依磁振影像風險、分子分型與治療反應調整的策略。</li>
          <li><strong>胰臟腺癌</strong>：核心問題是全身復發風險高、可切除比例低、血管侵犯常見；放療主要選擇性用於邊緣可切除、術後切緣陽性或淋巴結陽性高風險，以及局部晚期不可切除但需局部控制的情境。</li>
          <li><strong>肛門鱗狀細胞癌</strong>：與直腸腺癌最大的不同是標準治療為根治性同步放化療，目標是治癒並保留肛門括約肌功能；救援性腹會陰切除僅用於持續性或復發性疾病。</li>
          <li><strong>胃腸道放療計畫</strong>：需同時平衡腫瘤涵蓋與胃、十二指腸、小腸、結腸、直腸、膀胱、腎臟、肝臟、脊髓、心臟、肺臟等正常器官限制。</li>
        </ul>
        """,
        "body_en": """
        <p>This page integrates four high-yield GI radiation oncology topics: <strong>esophageal cancer, locally advanced rectal cancer, pancreatic adenocarcinoma, and anal cancer</strong>. These diseases are anatomy-driven and require careful integration of nodal drainage, local invasion, resectability, molecular subtype, and multidisciplinary sequencing.</p>
        <ul>
          <li><strong>Esophageal cancer</strong>: curative-intent therapy is mainly divided into the CROSS/CheckMate-577 pathway and the perioperative FLOT pathway; definitive CRT is central for inoperable disease and organ-preservation strategies.</li>
          <li><strong>Rectal cancer</strong>: RT/CRT mainly provides local-control benefit; modern treatment is increasingly MRI-risk-adapted, molecular-adapted, and response-adapted rather than fixed-sequence therapy for everyone.</li>
          <li><strong>Pancreatic adenocarcinoma</strong>: the key problems are high systemic-failure risk, low resectability rate, and frequent vascular involvement; RT is selectively used in borderline resectable disease, postoperative R1/N+ high-risk disease, and locally advanced unresectable local-control settings.</li>
          <li><strong>Anal SCC</strong>: unlike rectal adenocarcinoma, standard treatment is definitive chemoRT with curative and sphincter-preserving intent; salvage APR is reserved for persistent or recurrent disease.</li>
          <li><strong>GI RT planning</strong>: treatment requires balancing tumor coverage against stomach, duodenum, small bowel, colon, rectum, bladder, kidneys, liver, spinal cord, heart, and lung constraints.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道總論",
        "label_en": "ESOPH OVERVIEW",
        "h2_zh": "食道癌總論、臨床表現、危險因子與檢查評估",
        "h2_en": "Esophageal cancer overview, presentation, risk factors, and workup",
        "body_zh": """

        <p>食道癌好發於第 6–7 個十年齡層，男女終身風險約 <strong>0.5%</strong>。主要病理分為 <strong>鱗狀細胞癌（SCC）</strong> 與 <strong>腺癌（ACA）</strong>。全球食道癌以鱗狀細胞癌為主，約占 90%，常位於上段或中段食道，接受同步放化療後的病理完全緩解率較高；西歐與美國則以腺癌為主，約占 70%，多位於下段食道或胃食道交界，同步放化療後的病理完全緩解率相對較低。</p>
        <ul>
          <li><strong>典型臨床表現</strong>：漸進性吞嚥困難、早飽、體重減輕、胃灼熱、黑便與貧血。</li>
          <li><strong>與腫瘤位置相關的症狀</strong>：高位腫瘤或侵犯鄰近構造可造成聲音沙啞與咳嗽；Barrett 食道患者也可能在篩檢性內視鏡中被發現。</li>
          <li><strong>鱗狀細胞癌危險因子口訣 ABCDEF</strong>：A 為賁門失弛緩症；B 為不良飲食、高脂飲食或高溫食物；C 為腐蝕性狹窄或鹼液攝入；另一個 C 為吸菸；D 為異生或憩室；E 為食道蹼或 Plummer-Vinson 症候群；F 為家族性或遺傳因素。</li>
          <li><strong>腺癌危險因子口訣 BOG</strong>：B 為 Barrett 食道；O 為肥胖；G 為胃食道逆流。每週有逆流症狀者風險約增加 5 倍，每日有症狀者約增加 7 倍。</li>
          <li><strong>基本檢查評估</strong>：完整病史與理學檢查、全血球計數、肝腎功能與電解質、生理或解剖性吞嚥攝影、上消化道內視鏡與切片。</li>
          <li><strong>影像與分期</strong>：口服與靜脈顯影胸腹骨盆電腦斷層、氟代葡萄糖正子電腦斷層，以及內視鏡超音波。</li>
          <li><strong>內視鏡超音波角色</strong>：對 T 分期與 N 分期很重要，尤其淋巴結分期通常比正子斷層更適合，也可對可疑淋巴結做細針抽吸。</li>
          <li><strong>支氣管鏡</strong>：若腫瘤位於氣管隆突上方，應考慮支氣管鏡，以排除氣管食道瘻管。</li>
          <li><strong>分子檢測</strong>：所有患者建議做微衛星不穩定性／錯配修復檢測；局部晚期、復發或轉移病人需檢測 PD-L1 與 HER2。</li>
          <li><strong>微衛星不穩定性／錯配修復</strong>：微衛星不穩定性可用聚合酶連鎖反應或次世代定序檢測；錯配修復缺陷可用免疫組織化學評估 MLH1、MSH2、MSH6、PMS2 是否缺失。</li>
          <li><strong>PD-L1 與 HER2</strong>：PD-L1 可用綜合陽性分數 (CPS) 或腫瘤比例分數 (TPS)報告；HER2 免疫染色 3+ 為陽性，2+ 需用原位雜交確認，0–1 為陰性。</li>
        </ul>
        """,
        "body_en": """
        <p>Esophageal cancer peaks in the 6th–7th decades, with lifetime risk around <strong>0.5%</strong>. The two major histologies are <strong>squamous cell carcinoma, SCC</strong>, and <strong>adenocarcinoma, ACA</strong>. SCC accounts for about 90% globally, is more common in the upper/middle esophagus, and has a higher pCR rate after CRT. In Western Europe and the United States, ACA accounts for about 70%, is usually distal esophagus or GEJ, and has a lower pCR rate after CRT.</p>
        <ul>
          <li><strong>Typical presentation</strong>: progressive dysphagia, early satiety, weight loss, heartburn, melena, and anemia.</li>
          <li><strong>Location-related symptoms</strong>: upper tumors or adjacent-structure invasion can cause hoarseness and cough; some Barrett esophagus patients are detected on screening endoscopy.</li>
          <li><strong>SCC risk mnemonic ABCDEF</strong>: A = achalasia; B = bad diet/high-fat/high-temperature foods; C = caustic stricture/lye ingestion; C = cigarette smoking; D = dysplasia/diverticuli; E = esophageal webs/Plummer-Vinson; F = familial/genetic.</li>
          <li><strong>Adenocarcinoma risk mnemonic BOG</strong>: B = Barrett esophagus; O = obesity; G = GERD. Weekly GERD symptoms increase risk about fivefold; daily symptoms about sevenfold.</li>
          <li><strong>Basic workup</strong>: full H&P, CBC/CMP, barium swallow, and upper GI endoscopy with biopsy.</li>
          <li><strong>Imaging and staging</strong>: CT chest/abdomen/pelvis with oral and IV contrast, FDG PET/CT, and EUS.</li>
          <li><strong>EUS role</strong>: important for T/N staging, especially nodal staging, and permits FNA of suspicious nodes.</li>
          <li><strong>Bronchoscopy</strong>: consider for tumors above the carina to rule out tracheoesophageal fistula.</li>
          <li><strong>Molecular testing</strong>: all patients should have MSI/dMMR testing; locally advanced, recurrent, or metastatic patients should have PD-L1 and HER2 testing.</li>
          <li><strong>MSI/dMMR</strong>: MSI can be assessed by PCR/NGS; dMMR by IHC loss of MLH1, MSH2, MSH6, or PMS2.</li>
          <li><strong>PD-L1 / HER2</strong>: PD-L1 can be reported by CPS or TPS; HER2 IHC 3+ is positive, 2+ requires FISH confirmation, and 0–1 is negative.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道解剖/分期",
        "label_en": "ESOPH STAGING",
        "h2_zh": "食道解剖、胃食道交界與 Siewert 分類、淋巴引流與 TNM 分期",
        "h2_en": "Esophageal anatomy, GEJ/Siewert, lymphatic drainage, and TNM",
        "body_zh": """

        <p>食道長約 25 公分，自 <strong>環咽肌</strong> 開始，距門齒約 15–40 公分。食道沒有真正的漿膜，且有豐富的黏膜下淋巴管叢，因此容易發生局部侵犯、縱向黏膜下擴散與跳躍性淋巴結轉移。</p>
        <ul>
          <li><strong>依門齒距離分段</strong>：15–20 公分為頸段食道；20–25 公分為上胸段食道；25–30 公分為中胸段食道；30–40 公分為下胸段食道。</li>
          <li><strong>與脊椎位置關係</strong>：食道大約位於第 6 頸椎到第 10 胸椎前方。</li>
          <li><strong>上皮型態</strong>：上段主要為非角化鱗狀上皮；下段逐漸轉為腺體上皮。</li>
          <li><strong>真正胃食道交界</strong>：指鱗狀上皮與柱狀上皮轉換的位置；胃食道交界腫瘤定義為距真正胃食道交界 5 公分內的腫瘤。</li>
          <li><strong>Siewert 第一型</strong>：腫瘤中心位於胃食道交界上方 1–5 公分。</li>
          <li><strong>Siewert 第二型</strong>：腫瘤中心位於胃食道交界上方 1 公分到下方 2 公分。</li>
          <li><strong>Siewert 第三型</strong>：腫瘤中心位於胃食道交界下方 2–5 公分。</li>
          <li><strong>頸段食道區域淋巴結</strong>：包括鎖骨上淋巴結、斜角肌旁淋巴結、內頸靜脈鏈淋巴結、上頸部與下頸部淋巴結，以及食道周圍淋巴結。</li>
          <li><strong>胸段食道區域淋巴結</strong>：包括上食道旁淋巴結、隆突下淋巴結與下食道旁淋巴結。</li>
          <li><strong>胃食道交界區域淋巴結</strong>：包括下食道淋巴結、膈肌旁淋巴結、心包旁淋巴結、左胃動脈旁淋巴結與腹腔動脈旁淋巴結。</li>
          <li><strong>T1a</strong>：侵犯固有層或黏膜肌層。</li>
          <li><strong>T1b</strong>：侵犯黏膜下層。</li>
          <li><strong>T2</strong>：侵犯固有肌層。</li>
          <li><strong>T3</strong>：侵犯外膜。</li>
          <li><strong>T4a</strong>：侵犯仍可能切除的鄰近構造，例如肋膜、心包膜、奇靜脈、橫膈或腹膜。</li>
          <li><strong>T4b</strong>：侵犯通常不可切除的鄰近構造，例如主動脈、椎體或氣道。</li>
          <li><strong>N 分期</strong>：N1 為 1–2 顆區域淋巴結轉移；N2 為 3–6 顆；N3 為 7 顆以上。</li>
          <li><strong>M1</strong>：遠端轉移，也包括腹膜細胞學陽性。</li>
          <li><strong>AJCC 第 8 版重點</strong>：鱗狀細胞癌與腺癌的 TNM 定義相同，但臨床分期組別依病理型態分開。</li>
        </ul>
        """,
        "body_en": """
        <p>The esophagus is about 25 cm long and begins at the <strong>cricopharyngeus muscle</strong>, spanning about 15–40 cm from the incisors. It has no true serosa and has a rich submucosal lymphatic plexus, explaining local invasion, longitudinal submucosal spread, and skip nodal metastases.</p>
        <ul>
          <li><strong>Anatomic segments by incisors</strong>: 15–20 cm = cervical esophagus; 20–25 cm = upper thoracic; 25–30 cm = middle thoracic; 30–40 cm = lower thoracic esophagus.</li>
          <li><strong>Vertebral relation</strong>: anterior to C6–T10.</li>
          <li><strong>Epithelium</strong>: superiorly nonkeratinized squamous epithelium; inferiorly glandular epithelium.</li>
          <li><strong>True GEJ</strong>: the epithelial transition site; GEJ tumors are within 5 cm of the true GEJ.</li>
          <li><strong>Siewert I</strong>: 1–5 cm above the GEJ.</li>
          <li><strong>Siewert II</strong>: 1 cm above to 2 cm below the GEJ.</li>
          <li><strong>Siewert III</strong>: 2–5 cm below the GEJ.</li>
          <li><strong>Cervical esophagus regional nodes</strong>: supraclavicular, scalene, internal jugular, upper/lower cervical, and periesophageal nodes.</li>
          <li><strong>Thoracic esophagus regional nodes</strong>: upper periesophageal, subcarinal, and lower periesophageal nodes.</li>
          <li><strong>GEJ regional nodes</strong>: lower esophageal, diaphragmatic, pericardial, left gastric, and celiac nodes.</li>
          <li><strong>T1a</strong>: lamina propria or muscularis mucosa invasion.</li>
          <li><strong>T1b</strong>: submucosa invasion.</li>
          <li><strong>T2</strong>: muscularis propria invasion.</li>
          <li><strong>T3</strong>: adventitia invasion.</li>
          <li><strong>T4a</strong>: resectable adjacent structures such as pleura, pericardium, azygous vein, diaphragm, and peritoneum.</li>
          <li><strong>T4b</strong>: unresectable adjacent structures such as aorta, vertebral body, or airway.</li>
          <li><strong>N-stage</strong>: N1 = 1–2 nodes; N2 = 3–6 nodes; N3 = ≥7 nodes.</li>
          <li><strong>M1</strong>: distant metastasis, including positive peritoneal cytology.</li>
          <li><strong>AJCC 8th</strong>: TNM definitions are the same for SCC and ACA, but clinical group staging differs by histology.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道治療",
        "label_en": "ESOPH TX",
        "h2_zh": "食道癌整體治療架構、放療、手術與系統治療",
        "h2_en": "Esophageal cancer treatment framework, RT, surgery, and systemic therapy",
        "body_zh": """

        <ul>
          <li><strong>T1 疾病</strong>：以局部治療為主，優先考慮內視鏡切除，例如內視鏡黏膜切除或內視鏡黏膜下剝離，必要時加上消融；也可選擇食道切除術。</li>
          <li><strong>內視鏡黏膜切除</strong>：較適合小病灶，尤其小於 1.5 公分者，常為分塊切除。</li>
          <li><strong>內視鏡黏膜下剝離</strong>：可用於較大病灶，可整塊切除，並提供較精確的病理分期。</li>
          <li><strong>內視鏡切除後仍有 Barrett 食道</strong>：可考慮射頻消融或冷凍消融。</li>
          <li><strong>T2–T4 或淋巴結陽性</strong>：屬於需多模式治療的族群。</li>
          <li><strong>CROSS／CheckMate 577 路徑</strong>：術前同步放化療 → 食道切除術 → 若 R0 切除後仍有殘餘病理疾病，可給予術後 nivolumab 最多 1 年。</li>
          <li><strong>圍手術期化療路徑</strong>：尤其腺癌或胃食道交界癌，可用 FLOT 4 個療程 → 手術 → FLOT 4 個療程。</li>
          <li><strong>微衛星高度不穩定／錯配修復缺陷</strong>：可考慮術前或圍手術期免疫治療策略。</li>
          <li><strong>不可切除或醫學上無法手術</strong>：採根治性同步放化療，常用 50.4 Gy／28 次合併同步化療。</li>
          <li><strong>放療適應症</strong>：T2–T4 或淋巴結陽性腫瘤。</li>
          <li><strong>術前放療劑量</strong>：41.4–50.4 Gy，每次 1.8 Gy；CROSS 使用 41.4 Gy。</li>
          <li><strong>根治性放療劑量</strong>：通常為 50.4 Gy；證據不支持常規升劑量。</li>
          <li><strong>無同步化療的歷史劑量</strong>：過去曾使用 64 Gy／32 次，但這不是現代根治性同步放化療標準。</li>
          <li><strong>頸段食道癌</strong>：常使用較高劑量，接近頭頸癌劑量，約 66–70 Gy。</li>
          <li><strong>同步化療方案</strong>：每週 carboplatin／paclitaxel；capecitabine 或 5-FU 加 cisplatin；capecitabine 或 5-FU 加 oxaliplatin；或 FOLFOX。</li>
          <li><strong>FLOT</strong>：包含 5-FU、leucovorin、oxaliplatin 與 docetaxel，通常術前每兩週一次共 4 次，術後再 4 次。</li>
          <li><strong>食道切除術方式</strong>：Ivor Lewis 為剖腹加右胸切開；微創 Ivor Lewis 為腹腔鏡加胸腔鏡；McKeown 為右胸切開、剖腹與頸部切口；經裂孔手術為剖腹加頸部切口。</li>
          <li><strong>淋巴結手術</strong>：若未接受誘導同步放化療，手術時建議至少取樣 15 顆淋巴結；若已接受誘導治療，殘餘淋巴結數較難解讀。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>T1 disease</strong>: primarily local therapy, preferably endoscopic resection such as EMR or ESD with ablation when needed; esophagectomy is also an option.</li>
          <li><strong>EMR</strong>: best for small lesions, especially &lt;1.5 cm, and often performed piecemeal.</li>
          <li><strong>ESD</strong>: useful for larger lesions, allows en bloc resection, and provides more accurate pathology staging.</li>
          <li><strong>Residual Barrett esophagus after EMR/ESD</strong>: consider radiofrequency ablation or cryoablation.</li>
          <li><strong>T2–T4 or N+</strong>: requires multimodality therapy.</li>
          <li><strong>CROSS / CheckMate-577 pathway</strong>: preop chemoRT → esophagectomy → adjuvant nivolumab for up to 1 year if R0 resection and residual ypT/N+ disease.</li>
          <li><strong>Perioperative chemotherapy pathway</strong>: especially for ACA/GEJ, use FLOT ×4 → surgery → FLOT ×4.</li>
          <li><strong>MSI-H/dMMR</strong>: consider neoadjuvant or perioperative immunotherapy strategies.</li>
          <li><strong>Unresectable / medically inoperable</strong>: definitive chemoRT, commonly 50.4 Gy/28 fx with concurrent chemotherapy.</li>
          <li><strong>RT indications</strong>: T2–T4 or N+ tumors.</li>
          <li><strong>Preop RT dose</strong>: 41.4–50.4 Gy at 1.8 Gy/fx; CROSS used 41.4 Gy.</li>
          <li><strong>Definitive RT dose</strong>: typically 50.4 Gy; evidence does not support routine dose escalation.</li>
          <li><strong>No concurrent chemo historical dose</strong>: older RT-alone regimens used 64 Gy/32 fx, but this is not the modern definitive CRT standard.</li>
          <li><strong>Cervical esophagus</strong>: often treated to H&N-like doses around 66–70 Gy.</li>
          <li><strong>Concurrent regimens</strong>: weekly carboplatin/paclitaxel; capecitabine/5-FU + cisplatin; capecitabine/5-FU + oxaliplatin; FOLFOX.</li>
          <li><strong>FLOT</strong>: 5-FU, leucovorin, oxaliplatin, and docetaxel, q2 weeks ×4 preop + ×4 postop.</li>
          <li><strong>Esophagectomy approaches</strong>: Ivor Lewis = laparotomy + right thoracotomy; minimally invasive Ivor Lewis = laparoscopy + thoracoscopy; McKeown = right thoracotomy + laparotomy + neck incision; transhiatal = laparotomy + neck incision.</li>
          <li><strong>Nodal surgery</strong>: if no induction chemoRT, sample ≥15 nodes; after induction, residual nodal counts are harder to interpret.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道證據 I",
        "label_en": "ESOPH EVIDENCE I",
        "h2_zh": "術前同步放化療與術後 nivolumab：CROSS、CheckMate 577、POET",
        "h2_en": "Preop chemoRT and adjuvant nivolumab: CROSS, CheckMate 577, and POET",
        "body_zh": """

        <ul>
          <li><strong>CROSS 試驗</strong>：2004–2008 年納入 366 位 T2–T4 或淋巴結陽性的可切除食道／胃食道交界癌，包含鱗狀細胞癌、腺癌與大細胞癌。</li>
          <li><strong>CROSS 方案</strong>：41.4 Gy／23 次，加每週 carboplatin AUC2 與 paclitaxel 50 mg/m²，之後 4–6 週內手術。</li>
          <li><strong>CROSS 生存結果</strong>：術前同步放化療對比單純手術：5 年總生存 47% 對 34%；10 年總生存 38% 對 25%；中位總生存 49 對 24 個月。</li>
          <li><strong>CROSS 病理結果</strong>：R0 切除率 92% 對 69%；手術時淋巴結陽性 31% 對 75%；整體病理完全緩解率 29%。</li>
          <li><strong>CROSS 病理型態差異</strong>：鱗狀細胞癌病理完全緩解率約 49–50%；腺癌約 23%。</li>
          <li><strong>CROSS 毒性</strong>：術後併發症未顯著增加；30 天第 5 級毒性兩組約 6–7%；同步放化療組第 3 級以上血液毒性約 7%。</li>
          <li><strong>CROSS 復發型態</strong>：術前同步放化療降低總復發、局部區域復發，以及遠端合併局部區域失敗。任何復發 35% 對 57%；單純局部區域失敗 3% 對 9%；遠端加局部區域失敗 11% 對 24%。</li>
          <li><strong>CROSS 照野失敗</strong>：同步放化療組多數失敗仍為遠端轉移；照野內復發 5%，照野邊緣復發 2%。術前同步放化療也降低吻合口、縱膈與腹膜復發。</li>
          <li><strong>CheckMate 577</strong>：794 位第二至第三期食道／胃食道交界癌，術前同步放化療後 R0 切除且仍有殘餘病理疾病，以 2:1 隨機分配至 nivolumab 或安慰劑。</li>
          <li><strong>CheckMate 577 方案</strong>：nivolumab 240 mg 每 2 週一次共 16 週，之後 480 mg 每 4 週一次，最多 1 年。</li>
          <li><strong>CheckMate 577 結果</strong>：中位無病生存 22 對 11 個月，p&lt;0.001；鱗狀細胞癌、腺癌與不同 PD-L1 表現族群均有無病生存效益。</li>
          <li><strong>CheckMate 577 毒性</strong>：第 3–4 級治療相關不良事件 13% 對 6%；常見需注意肺炎與皮疹。</li>
          <li><strong>POET</strong>：119 位 T3–T4 Nx 胃食道交界腺癌，比較術前 5-FU／cisplatin 與化療後接 30 Gy／15 次同步放化療加 cisplatin／etoposide。</li>
          <li><strong>POET 結果</strong>：5 年總生存 40% 對 24%，p=0.055；5 年局部控制 38% 對 21%，p=0.03；病理完全緩解 16% 對 2%，p=0.03。</li>
          <li><strong>POET 解讀</strong>：術前同步放化療改善局部控制與病理完全緩解，但因收案不足與早期終止，總生存證據有限。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>CROSS trial</strong>: 2004–2008, 366 patients with T2–T4 or N+ resectable esophagus/GEJ cancer, including SCC, ACA, and large-cell carcinoma.</li>
          <li><strong>CROSS regimen</strong>: 41.4 Gy/23 fx + weekly carboplatin AUC2 + paclitaxel 50 mg/m², followed by surgery within 4–6 weeks.</li>
          <li><strong>CROSS survival</strong>: preop CRT vs surgery alone: 5-year OS 47% vs 34%; 10-year OS 38% vs 25%; median OS 49 vs 24 months.</li>
          <li><strong>CROSS pathology</strong>: R0 resection 92% vs 69%; N+ at surgery 31% vs 75%; overall pCR 29%.</li>
          <li><strong>CROSS histology</strong>: SCC pCR about 49–50%; ACA pCR about 23%.</li>
          <li><strong>CROSS toxicity</strong>: no significant increase in postoperative complications; 30-day grade 5 toxicity about 6–7% in both arms; grade 3+ hematologic toxicity about 7% in the CRT arm.</li>
          <li><strong>CROSS recurrence</strong>: preop CRT reduced total recurrence, locoregional recurrence, and combined distant + locoregional failure. Any recurrence 35% vs 57%; LR failure only 3% vs 9%; combined distant + LR 11% vs 24%.</li>
          <li><strong>CROSS field failure</strong>: most failures in the CRT arm remained distant; infield recurrence 5%, field-edge recurrence 2%. Preop CRT also reduced anastomotic, mediastinal, and peritoneal relapse.</li>
          <li><strong>CheckMate 577</strong>: 794 patients with stage II–III esophageal/GEJ cancer after neoadjuvant chemoRT, R0 resection, and residual pathologic disease, randomized 2:1 to nivolumab vs placebo.</li>
          <li><strong>CheckMate 577 regimen</strong>: nivolumab 240 mg q2 weeks ×16 weeks, then 480 mg q4 weeks, for up to 1 year.</li>
          <li><strong>CheckMate 577 outcome</strong>: median DFS 22 vs 11 months, p&lt;0.001; DFS benefit across SCC, ACA, and PD-L1 subgroups.</li>
          <li><strong>CheckMate 577 toxicity</strong>: grade 3–4 treatment-related AE 13% vs 6%; pneumonitis and rash were notable.</li>
          <li><strong>POET</strong>: 119 patients with T3–T4 Nx GEJ ACA, preop 5-FU/cisplatin vs chemotherapy followed by CRT 30 Gy/15 fx + cisplatin/etoposide.</li>
          <li><strong>POET outcome</strong>: 5-year OS 40% vs 24%, p=0.055; 5-year local control 38% vs 21%, p=0.03; pCR 16% vs 2%, p=0.03.</li>
          <li><strong>POET interpretation</strong>: preop CRT improves local control and pCR, but OS evidence is limited by low accrual and early closure.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道證據 II",
        "label_en": "ESOPH EVIDENCE II",
        "h2_zh": "圍手術期化療、FLOT、ESOPEC 與根治性同步放化療",
        "h2_en": "Perioperative chemotherapy, FLOT, ESOPEC, and definitive CRT",
        "body_zh": """

        <ul>
          <li><strong>MAGIC</strong>：503 位可切除局部晚期第二期以上胃癌、胃食道交界癌或下三分之一食道腺癌，比較單純手術與圍手術期 ECF。ECF 包含 epirubicin、cisplatin 與 5-FU，術前 3 個療程、術後 3 個療程。</li>
          <li><strong>MAGIC 結果</strong>：只有 42% 完成全部 6 個療程，但仍改善總生存與無進展生存。5 年總生存 36% 對 23%；總生存風險比 0.75；無進展生存風險比 0.66。</li>
          <li><strong>FLOT4</strong>：716 位胃或胃食道交界腺癌，臨床 T2 或淋巴結陽性，比較 ECF／ECX 術前 3 次加術後 3 次，與 FLOT 術前 4 次加術後 4 次。</li>
          <li><strong>FLOT4 結果</strong>：中位總生存 50 對 35 個月；中位無病生存 30 對 18 個月。</li>
          <li><strong>FLOT4 毒性</strong>：ECF／ECX 較多噁心嘔吐、血栓事件與貧血；FLOT 較多感染／嗜中性白血球低下、腹瀉與神經病變；住院率相近。</li>
          <li><strong>TOPGEAR</strong>：574 位可切除胃或胃食道交界腺癌，比較圍手術期化療單獨治療，與化療後接 45 Gy／25 次同步放化療再手術與化療。</li>
          <li><strong>TOPGEAR 結果</strong>：加入同步放化療可提高病理完全緩解 8% 到 17%，以及超過 90% 反應 29% 到 50%，但未改善總生存或無進展生存；3 年無進展生存 48% 對 47%，中位總生存 49 對 46 個月。</li>
          <li><strong>NeoAEGIS</strong>：362 位臨床 T2–T3、N0–3、M0 食道或胃食道交界腺癌，比較 CROSS 類術前同步放化療與圍手術期化療；原設計為圍手術期化療優越性試驗，後因無效性停止。</li>
          <li><strong>NeoAEGIS 結果</strong>：3 年總生存 55% 對 57%；中位總生存 48 對 49 個月；病理完全緩解 12% 對 4%；R0 切除 96% 對 82%。</li>
          <li><strong>NeoAEGIS 生活品質</strong>：術前同步放化療 1 年時情緒功能、疼痛與咳嗽較差；圍手術期化療腹瀉較差。</li>
          <li><strong>ESOPEC</strong>：438 位臨床 T2–T4 或淋巴結陽性食道腺癌，比較 CROSS 類術前同步放化療與圍手術期 FLOT。</li>
          <li><strong>ESOPEC 結果</strong>：圍手術期 FLOT 改善 3 年總生存 57% 對 51%，中位總生存 66 對 37 個月，3 年無復發生存 53% 對 37%，病理完全緩解 18% 對 13%。</li>
          <li><strong>ESOPEC 注意事項</strong>：並未與現代「同步放化療 → 手術 → 術後 nivolumab」完整策略比較；FLOT 毒性較高。</li>
          <li><strong>RTOG 8501</strong>：單純放療 64 Gy／32 次對比 50 Gy／25 次同步 cisplatin／5-FU；5 年總生存 26% 對 0%，建立根治性同步放化療地位。</li>
          <li><strong>RTOG 9405／INT 0123</strong>：50.4 Gy 對比 64.8 Gy，兩組皆合併 cisplatin／5-FU；高劑量未改善總生存或局部控制。</li>
          <li><strong>RTOG 9405 毒性問題</strong>：高劑量組治療時間較長，且因毒性導致實際給予 5-FU 劑量較低。</li>
          <li><strong>ARTDECO</strong>：強度調控放療時代比較 50.4 Gy 與 61.6 Gy，合併每週 carboplatin／paclitaxel；3 年局部無進展生存 71% 對 73%，總生存 42% 對 39%，無顯著效益。</li>
          <li><strong>升劑量結論</strong>：根治性食道同步放化療不支持常規超過 50.4 Gy。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>MAGIC</strong>: 503 patients with resectable locally advanced stage II+ gastric/GEJ/lower-third esophageal ACA, surgery alone vs periop ECF. ECF = epirubicin, cisplatin, 5-FU; ×3 preop and ×3 postop.</li>
          <li><strong>MAGIC outcome</strong>: only 42% completed all 6 cycles, but OS/PFS improved. Five-year OS 36% vs 23%; OS HR 0.75; PFS HR 0.66.</li>
          <li><strong>FLOT4</strong>: 716 patients with stomach/GEJ ACA, cT2 and/or cN+, ECF/ECX ×3 preop + ×3 postop vs FLOT ×4 preop + ×4 postop.</li>
          <li><strong>FLOT4 outcome</strong>: median OS 50 vs 35 months; median DFS 30 vs 18 months.</li>
          <li><strong>FLOT4 toxicity</strong>: ECF/ECX had more nausea/vomiting, thromboembolic events, and anemia; FLOT had more infections/neutropenia, diarrhea, and neuropathy; hospitalization was similar.</li>
          <li><strong>TOPGEAR</strong>: 574 patients with resectable stomach/GEJ ACA, periop chemotherapy alone vs chemotherapy → CRT 45 Gy/25 fx → surgery → chemotherapy.</li>
          <li><strong>TOPGEAR outcome</strong>: CRT improved pCR 8%→17% and &gt;90% response 29%→50%, but no OS/PFS benefit: 3-year PFS 48% vs 47%, median OS 49 vs 46 months.</li>
          <li><strong>NeoAEGIS</strong>: 362 patients with cT2–T3 N0–3 M0 esophageal/GEJ ACA, CROSS-like preop CRT vs periop chemotherapy; originally a periop CHT superiority design but stopped for futility.</li>
          <li><strong>NeoAEGIS outcome</strong>: 3-year OS 55% periop CHT vs 57% preop CRT; median OS 48 vs 49 months; pCR 12% vs 4%; R0 96% vs 82%.</li>
          <li><strong>NeoAEGIS QoL</strong>: preop CRT had worse 1-year emotional functioning, pain, and coughing; periop CHT had worse diarrhea.</li>
          <li><strong>ESOPEC</strong>: 438 patients with cT2–T4 or N+ esophageal adenocarcinoma, CROSS-style CRT vs periop FLOT.</li>
          <li><strong>ESOPEC outcome</strong>: periop FLOT improved 3-year OS 57% vs 51%, median OS 66 vs 37 months, 3-year RFS 53% vs 37%, and pCR 18% vs 13%.</li>
          <li><strong>ESOPEC caveat</strong>: not compared with the full modern CRT → surgery → adjuvant nivolumab pathway; FLOT is more toxic.</li>
          <li><strong>RTOG 8501</strong>: RT alone 64 Gy/32 fx vs CRT 50 Gy/25 fx + cisplatin/5-FU; 5-year OS 26% vs 0%, establishing definitive CRT.</li>
          <li><strong>RTOG 9405 / INT 0123</strong>: 50.4 Gy vs 64.8 Gy, both with cisplatin/5-FU; high dose did not improve OS or local control.</li>
          <li><strong>RTOG 9405 toxicity issue</strong>: the high-dose arm had longer treatment time and lower delivered 5-FU dose due to toxicity.</li>
          <li><strong>ARTDECO</strong>: IMRT-era 50.4 Gy vs 61.6 Gy with weekly carbo/taxol; 3-year LPFS 71% vs 73%, OS 42% vs 39%, no significant benefit.</li>
          <li><strong>Dose escalation conclusion</strong>: routine dose escalation beyond 50.4 Gy is not supported for definitive esophageal CRT.</li>
        </ul>
        """
      },

      {
        "label_zh": "食道保留/靶區",
        "label_en": "ESOPH ORGAN/RT",
        "h2_zh": "器官保留、靶區描繪與轉移性疾病第一線治療",
        "h2_en": "Organ preservation, contouring, and metastatic first-line therapy",
        "body_zh": """

        <ul>
          <li><strong>SANO</strong>：第三期器官保留試驗；接受 upfront 同步放化療後 6–12 週若達臨床完全緩解，分配至主動監測或標準手術。</li>
          <li><strong>SANO 結果</strong>：總生存達非劣性；中位無病生存 35 對 49 個月；30 個月遠端轉移 43% 對 34%。主動監測中 35% 維持臨床完全緩解，48% 發生局部區域再生長，17% 發生遠端轉移；短期健康相關生活品質較好。</li>
          <li><strong>CROC 第二期試驗</strong>：可切除第 IB–III 期食道鱗狀細胞癌，先給 DCF 誘導化療 3 次；顯著反應者轉為 50.4 Gy 加 cisplatin／5-FU 根治性同步放化療，反應不足者手術。</li>
          <li><strong>CROC 結果</strong>：58% 達顯著反應；其中 90% 在根治性同步放化療後達臨床完全緩解；1 年無進展生存 90%，3 年總生存 74%，3 年免食道切除生存 45%。</li>
          <li><strong>CROC 毒性</strong>：DCF 毒性高，第 3–4 級嗜中性白血球低下 100%，白血球低下 83%。</li>
          <li><strong>PRESTO／IKF-t057</strong>：進行中的第二期 T1–T2 N0 食道腺癌器官保留試驗；durvalumab 加 FLOT 2 次 → mFOLFOX 加 50 Gy／25 次放療 → 重新評估；持續性疾病手術；完全反應者接受 durvalumab 維持治療。</li>
          <li><strong>原發腫瘤肉眼靶體積</strong>：原發腫瘤。</li>
          <li><strong>淋巴結肉眼靶體積</strong>：受侵犯淋巴結。</li>
          <li><strong>原發腫瘤臨床靶體積</strong>：原發腫瘤肉眼靶體積上下各加 3–4 公分；若延伸到胃，可用 2 公分；徑向加 1 公分，並依心臟、椎體等解剖屏障修正。</li>
          <li><strong>淋巴結臨床靶體積</strong>：受侵犯淋巴結外加 1 公分。</li>
          <li><strong>選擇性淋巴結</strong>：遠端或胃食道交界腫瘤常包含腹腔動脈旁與左胃動脈旁淋巴結；氣管隆突上方病灶可包含雙側鎖骨上淋巴結；縱膈選擇性照射並非一定必要。</li>
          <li><strong>呼吸移動與定位</strong>：依移動評估建立內部靶體積；計畫靶體積通常為內部靶體積外加 0.5–1 公分。模擬定位與每日治療前禁食 2–3 小時。</li>
          <li><strong>轉移性 HER2 陽性腺癌</strong>：5-FU 或 capecitabine 加 oxaliplatin 與 trastuzumab；若 PD-L1 綜合陽性分數至少 1，可加 pembrolizumab。</li>
          <li><strong>轉移性 PD-L1 陽性腺癌</strong>：依綜合陽性分數可用 nivolumab 或 pembrolizumab 加 fluoropyrimidine／oxaliplatin。</li>
          <li><strong>微衛星高度不穩定或錯配修復缺陷</strong>：可考慮單獨免疫治療，例如 pembrolizumab、dostarlimab、ipilimumab／nivolumab，也可使用化療加免疫治療。</li>
          <li><strong>PD-L1 低表現且無可治療突變</strong>：以 fluoropyrimidine 加 oxaliplatin 為主。</li>
          <li><strong>轉移性鱗狀細胞癌</strong>：PD-L1 陽性或微衛星高度不穩定／錯配修復缺陷可用化療免疫治療或單獨免疫治療；PD-L1 低表現可用 fluoropyrimidine／oxaliplatin，可合併或不合併 nivolumab。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>SANO</strong>: phase III organ-preservation trial; after upfront chemoRT, patients with cCR at 6–12 weeks undergo active surveillance vs standard surgery.</li>
          <li><strong>SANO outcome</strong>: OS noninferior; median DFS 35 vs 49 months; 30-month distant metastasis 43% vs 34%. In active surveillance, 35% maintained cCR, 48% had locoregional regrowth, and 17% developed distant metastasis; short-term HRQOL was better.</li>
          <li><strong>CROC phase II</strong>: resectable stage IB–III esophageal SCC, induction DCF ×3; remarkable responders transitioned to definitive CRT 50.4 Gy + cisplatin/5-FU, nonresponders underwent surgery.</li>
          <li><strong>CROC outcome</strong>: 58% remarkable response; 90% of those achieved cCR after dCRT; 1-year PFS 90%, 3-year OS 74%, 3-year esophagectomy-free survival 45%.</li>
          <li><strong>CROC toxicity</strong>: DCF toxicity was high: grade 3–4 neutropenia 100% and leukopenia 83%.</li>
          <li><strong>PRESTO / IKF-t057</strong>: ongoing phase II for T1–T2 N0 esophageal adenocarcinoma organ preservation; durvalumab + FLOT ×2 → mFOLFOX + RT 50 Gy/25 fx → reassessment; persistent disease undergoes surgery; CR receives maintenance durvalumab.</li>
          <li><strong>GTVp</strong>: primary tumor.</li>
          <li><strong>GTVn</strong>: involved lymph nodes.</li>
          <li><strong>CTVp</strong>: GTVp + 3–4 cm superior/inferior; if extending into stomach, 2 cm can be used; radial margin 1 cm, adjusted for barriers such as heart and vertebral body.</li>
          <li><strong>CTVn</strong>: involved node + 1 cm.</li>
          <li><strong>Elective nodes</strong>: distal/GEJ often includes celiac and left gastric nodes; upper lesions above the carina can include bilateral supraclavicular nodes; mediastinal elective coverage is not always required.</li>
          <li><strong>Motion and setup</strong>: use motion study to define ITV; PTV usually ITV + 0.5–1 cm. Keep NPO 2–3 hours before simulation and daily treatment.</li>
          <li><strong>Metastatic ACA HER2+</strong>: 5-FU/capecitabine + oxaliplatin + trastuzumab; if PD-L1 CPS ≥1, add pembrolizumab.</li>
          <li><strong>Metastatic PD-L1+ ACA</strong>: depending on CPS, use nivolumab or pembrolizumab + fluoropyrimidine/oxaliplatin.</li>
          <li><strong>MSI-H/dMMR</strong>: consider IO alone such as pembrolizumab, dostarlimab, or ipilimumab/nivolumab, or chemo + IO.</li>
          <li><strong>PD-L1 low / no targetable mutation</strong>: fluoropyrimidine + oxaliplatin is the backbone.</li>
          <li><strong>Metastatic SCC</strong>: PD-L1+ or MSI-H/dMMR can receive chemoimmunotherapy or IO alone; PD-L1-low disease can receive fluoropyrimidine/oxaliplatin ± nivolumab.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸總論",
        "label_en": "RECTAL OVERVIEW",
        "h2_zh": "直腸癌總論、篩檢、高風險族群與檢查評估",
        "h2_en": "Rectal cancer overview, screening, high-risk groups, and workup",
        "body_zh": """

        <p>大腸直腸癌是男女皆常見的癌症之一，終身風險約 4–5%，也是癌症死亡的重要原因。直腸癌約占所有大腸直腸癌的 40%，定義為發生於<strong>直腸乙狀結腸交界到齒狀線或肛直腸環</strong>之間的癌症。直腸癌與結腸癌治療不同，因為直腸固定於骨盆腔，放療或同步放化療對局部控制與器官保留有重要角色。</p>
        <ul>
          <li><strong>分期分布</strong>：局部疾病約 35%，區域疾病約 36%，遠端轉移約 23%，未知約 6%。</li>
          <li><strong>5 年相對存活</strong>：局部疾病約 91.1%，區域疾病約 73.7%，遠端轉移約 15.7%。</li>
          <li><strong>一般風險篩檢</strong>：美國癌症協會與美國預防服務工作小組建議 45 歲開始；美國預防服務工作小組涵蓋 45–75 歲。</li>
          <li><strong>篩檢工具</strong>：大腸鏡、糞便檢查、軟式乙狀結腸鏡與電腦斷層結腸攝影。</li>
          <li><strong>大腸鏡</strong>：金標準；一般風險通常每 10 年一次；糞便檢查陽性需於 9 個月內接受大腸鏡。</li>
          <li><strong>糞便潛血或免疫化學糞便檢查</strong>：陰性時通常每年一次。</li>
          <li><strong>多標的糞便 DNA 檢測</strong>：陰性時每 3 年一次。</li>
          <li><strong>電腦斷層結腸攝影</strong>：每 5 年一次。</li>
          <li><strong>一等親有大腸直腸癌或進階腺瘤</strong>：40 歲或比親屬診斷年齡早 10 年開始，取較早者；每 5 年一次。</li>
          <li><strong>發炎性腸病</strong>：診斷 8 年後開始大腸鏡，之後每 1–5 年一次。</li>
          <li><strong>曾接受腹骨盆放射線照射</strong>：30 歲或放療後 5 年開始，取較晚者；每 5 年一次。</li>
          <li><strong>Lynch 症候群／遺傳性非瘜肉症大腸直腸癌</strong>：錯配修復基因包括 MLH1、MSH2、MSH6、PMS2；也增加子宮內膜、卵巢、胃、小腸、肝膽、腦、腎盂與輸尿管癌風險；20–25 歲開始大腸鏡，每 1–2 年一次。</li>
          <li><strong>家族性腺瘤性瘜肉症</strong>：APC 自體顯性突變；變異型包括 Gardner 與 Turcot；出現大量瘜肉時考慮預防性結腸切除或全結直腸切除。</li>
          <li><strong>臨床表現</strong>：血便最常見；也可有排便習慣改變、腹瀉或便祕、糞便變細、裏急後重、排便不完全感、疼痛、體重下降、疲倦、腹痛或腹脹；非常局部晚期時可有泌尿症狀。</li>
          <li><strong>檢查評估</strong>：病史理學檢查、個人與家族及篩檢史、肛門指診、男性前列腺評估、女性必要時骨盆檢查、全血球計數、肝腎功能與電解質、癌胚抗原、男性 PSA、生育年齡女性懷孕檢驗、大腸鏡切片、微衛星不穩定性／錯配修復檢測、胸腹骨盆電腦斷層與直腸磁振影像。</li>
          <li><strong>肛門指診加直腸鏡</strong>：判斷腫瘤距肛門緣距離最準確。</li>
          <li><strong>阻塞或瘻管</strong>：非常局部晚期時可能需先做分流性造口，再進行術前治療。</li>
        </ul>
        """,
        "body_en": """
        <p>Colorectal cancer is common in both men and women, with lifetime risk around 4–5%, and remains an important cause of cancer death. Rectal cancer accounts for about 40% of colorectal cancers and is defined as cancer arising between the <strong>rectosigmoid junction and the dentate line / anorectal ring</strong>. Rectal cancer is treated differently from colon cancer because the rectum is fixed in the pelvis, making RT/CRT important for local control and organ preservation.</p>
        <ul>
          <li><strong>Stage distribution</strong>: localized about 35%, regional about 36%, distant about 23%, unknown about 6%.</li>
          <li><strong>5-year relative survival</strong>: localized about 91.1%, regional about 73.7%, distant about 15.7%.</li>
          <li><strong>Average-risk screening</strong>: ACS/USPSTF recommend starting at age 45; USPSTF covers ages 45–75.</li>
          <li><strong>Screening tools</strong>: colonoscopy, stool-based tests, flexible sigmoidoscopy, and CT colonography.</li>
          <li><strong>Colonoscopy</strong>: gold standard; average-risk usually q10 years; positive stool test should be followed by colonoscopy within 9 months.</li>
          <li><strong>FOBT/FIT</strong>: if negative, usually annual.</li>
          <li><strong>Multitarget stool DNA</strong>: if negative, every 3 years.</li>
          <li><strong>CT colonography</strong>: every 5 years.</li>
          <li><strong>First-degree relative CRC/advanced adenoma</strong>: start age 40 or 10 years before the relative’s diagnosis, whichever is earlier; repeat q5 years.</li>
          <li><strong>IBD</strong>: start colonoscopy 8 years after diagnosis, q1–5 years.</li>
          <li><strong>Prior abdominopelvic irradiation</strong>: start at age 30 or 5 years after RT, whichever is later; q5 years.</li>
          <li><strong>Lynch/HNPCC</strong>: MMR genes MLH1, MSH2, MSH6, PMS2; increases risk of endometrial, ovarian, stomach, small bowel, hepatobiliary, brain, renal pelvis, and ureter cancers; colonoscopy age 20–25, q1–2 years.</li>
          <li><strong>FAP</strong>: APC autosomal dominant mutation; variants include Gardner and Turcot; consider elective colectomy or proctocolectomy once polyps develop.</li>
          <li><strong>Presentation</strong>: hematochezia is most common; changes in bowel habits, diarrhea/constipation, narrow stool, tenesmus, incomplete evacuation, pain, weight loss, fatigue, abdominal pain/distension; very locally advanced disease may cause urinary symptoms.</li>
          <li><strong>Workup</strong>: H&P, personal/family/screening history, DRE, male prostate assessment, female pelvic exam when appropriate, CBC/CMP/CEA, PSA in men, pregnancy test in reproductive-age women, colonoscopy with biopsy, MSI/MMR testing, CT CAP, and MRI rectum with contrast.</li>
          <li><strong>DRE with proctoscopy</strong>: one of the most accurate ways to determine distance from the anal verge.</li>
          <li><strong>Obstruction or fistula</strong>: very locally advanced disease may require diverting colostomy before neoadjuvant therapy.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸解剖/分子",
        "label_en": "RECTAL ANAT/MOL",
        "h2_zh": "直腸解剖、淋巴引流、病理、分子檢測與磁振分期",
        "h2_en": "Rectal anatomy, lymphatic drainage, pathology, molecular testing, and MRI staging",
        "body_zh": """

        <ul>
          <li><strong>直腸長度</strong>：從肛門緣往上約 15 公分；臨床試驗常納入距肛門緣 12–16 公分內的腫瘤。</li>
          <li><strong>解剖邊界</strong>：上界為直腸乙狀結腸交界；下界為肛直腸環或括約肌複合體。</li>
          <li><strong>腹膜關係</strong>：上三分之一之前側與外側被腹膜覆蓋；中三分之一只有前方被覆蓋；下三分之一無腹膜覆蓋。</li>
          <li><strong>臨床意義</strong>：腹膜返折會影響局部復發風險、手術困難度與放療靶區設計。</li>
          <li><strong>上段直腸血供</strong>：下腸繫膜動脈至上直腸動脈；淋巴引流至直腸旁、骶前、乙狀結腸旁與下腸繫膜淋巴結。</li>
          <li><strong>中段直腸</strong>：內髂動脈至中直腸動脈；淋巴引流可包含內髂淋巴結。</li>
          <li><strong>下段直腸</strong>：內陰部動脈至下直腸動脈；若侵犯到齒狀線以下，表淺鼠蹊淋巴結風險上升。</li>
          <li><strong>肛直腸環</strong>：包含內括約肌、外括約肌與恥骨直腸肌吊帶。</li>
          <li><strong>齒狀線／梳狀線</strong>：直腸柱狀上皮轉為肛門鱗狀上皮的位置；齒狀線以下的淋巴引流較像肛門。</li>
          <li><strong>放療區域淋巴結</strong>：內髂、骶前與直腸繫膜淋巴結。</li>
          <li><strong>總髂淋巴結</strong>：若已有區域淋巴結受侵犯，可涵蓋總髂淋巴結。</li>
          <li><strong>外髂淋巴結</strong>：若腫瘤向前侵犯膀胱或生殖器官，需納入外髂淋巴結。</li>
          <li><strong>鼠蹊淋巴結</strong>：若腫瘤向下侵犯齒狀線以下，需納入鼠蹊淋巴結。</li>
          <li><strong>病理</strong>：超過 90% 為腺癌；印戒細胞癌約 1–2%，預後較差。</li>
          <li><strong>分化程度</strong>：高分化約 20–25%；中分化約 60–70%；低分化約 15–20%。</li>
          <li><strong>少見病理型態</strong>：小細胞癌、類癌、平滑肌肉瘤與淋巴瘤。</li>
          <li><strong>普遍性微衛星不穩定性／錯配修復檢測</strong>：所有直腸癌病人都應檢測。</li>
          <li><strong>微衛星高度不穩定</strong>：屬於表現型，可用聚合酶連鎖反應或次世代定序檢測，通常定義為超過 30% 位點不穩定。</li>
          <li><strong>錯配修復缺陷</strong>：為潛在原因，可用免疫組織化學評估 MLH1、MSH2、MSH6、PMS2 缺失。</li>
          <li><strong>MLH1 異常</strong>：需檢查 BRAF V600E 突變。</li>
          <li><strong>微衛星高度不穩定／錯配修復缺陷</strong>：對免疫檢查點抑制劑反應佳；第二至第三期大腸直腸癌約 15–20%；一般預後較佳。</li>
          <li><strong>微衛星穩定／錯配修復正常</strong>：通常沒有明顯免疫治療效益。</li>
          <li><strong>轉移性疾病分子檢測</strong>：用次世代定序檢測 RAS、BRAF、HER2、NTRK 融合、POLE／POLD1、RET 融合。NTRK 需要融合，不是單純點突變。</li>
          <li><strong>直腸磁振影像</strong>：局部區域分期標準工具；評估 T 分期、N 分期、直腸繫膜筋膜／環周切緣、壁外血管侵犯、距肛直腸環或肛門緣距離、括約肌複合體與鄰近器官侵犯。</li>
          <li><strong>磁振影像序列</strong>：T2 加權影像最有用；擴散加權影像的受限擴散可幫助分期與反應評估。</li>
          <li><strong>AJCC T 分期</strong>：T1 侵犯黏膜下層；T2 侵犯固有肌層；T3 侵犯結直腸周圍軟組織；T4a 侵犯臟層腹膜；T4b 侵犯鄰近器官或結構。</li>
          <li><strong>AJCC N 分期</strong>：N1 為 1–3 顆淋巴結或腫瘤沉積；N1a 1 顆；N1b 2–3 顆；N1c 腫瘤沉積；N2 為 4 顆以上；N2a 4–6 顆；N2b 7 顆以上。</li>
          <li><strong>AJCC M 分期</strong>：M1a 單一遠端器官或部位；M1b 兩個以上遠端部位；M1c 腹膜轉移。</li>
          <li><strong>轉移型態</strong>：肝臟最常見；上段直腸經上直腸靜脈進入門脈系統；中下段直腸可經全身靜脈回流轉移至肺。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Rectum length</strong>: about 15 cm from the anal verge; trials often include tumors within 12–16 cm of the anal verge.</li>
          <li><strong>Boundaries</strong>: upper = rectosigmoid junction; lower = anorectal ring / sphincter.</li>
          <li><strong>Peritoneal relationship</strong>: upper 1/3 covered anteriorly/laterally by peritoneum; middle 1/3 only anteriorly; lower 1/3 not covered.</li>
          <li><strong>Clinical implication</strong>: the peritoneal reflection affects local-recurrence risk, surgical difficulty, and RT target design.</li>
          <li><strong>Upper rectum blood supply</strong>: inferior mesenteric artery → superior rectal artery; lymph drainage to pararectal, presacral, sigmoidal, and inferior mesenteric nodes.</li>
          <li><strong>Middle rectum</strong>: internal iliac artery → middle rectal artery; lymph drainage can include internal iliac nodes.</li>
          <li><strong>Lower rectum</strong>: internal pudendal artery → inferior rectal artery; extension below the dentate line raises superficial inguinal-node risk.</li>
          <li><strong>Anorectal ring</strong>: internal sphincter, external sphincter, and puborectalis sling.</li>
          <li><strong>Dentate / pectinate line</strong>: transition from rectal columnar epithelium to anal squamous epithelium; below this line, lymphatic behavior is anal-like.</li>
          <li><strong>Regional nodes for RT</strong>: internal iliac, presacral, and mesorectal nodes.</li>
          <li><strong>Common iliacs</strong>: cover if regional nodes are already involved.</li>
          <li><strong>External iliacs</strong>: include if anterior extension into bladder or reproductive organs.</li>
          <li><strong>Inguinal nodes</strong>: include if inferior extension below the dentate line.</li>
          <li><strong>Pathology</strong>: &gt;90% adenocarcinoma; signet-ring 1–2% and poor prognosis.</li>
          <li><strong>Differentiation</strong>: well differentiated 20–25%; moderately differentiated 60–70%; poorly differentiated 15–20%.</li>
          <li><strong>Rare histologies</strong>: small cell, carcinoid, leiomyosarcoma, lymphoma.</li>
          <li><strong>Universal MSI/MMR testing</strong>: all rectal cancer patients should undergo MSI/MMR screening.</li>
          <li><strong>MSI-H</strong>: phenotype; PCR or NGS; usually &gt;30% loci instability.</li>
          <li><strong>dMMR</strong>: underlying cause; IHC loss of MLH1/MSH2/MSH6/PMS2.</li>
          <li><strong>MLH1 abnormal</strong>: check BRAF V600E mutation.</li>
          <li><strong>MSI-H/dMMR</strong>: responds well to checkpoint inhibitors; present in about 15–20% of stage II–III CRC; generally better prognosis.</li>
          <li><strong>MSS/pMMR</strong>: usually no strong immunotherapy benefit.</li>
          <li><strong>Metastatic molecular testing</strong>: RAS, BRAF, HER2, NTRK fusion, POLE/POLD1, RET fusions by NGS panel. NTRK requires fusion, not point mutation.</li>
          <li><strong>Rectal MRI</strong>: standard for locoregional staging; evaluates T stage, N stage, mesorectal fascia/CRM, EMVI, distance to anorectal ring/anal verge, sphincter complex, and adjacent-organ invasion.</li>
          <li><strong>MRI sequences</strong>: T2-weighted sequence is most useful; DWI restricted diffusion helps staging and response assessment.</li>
          <li><strong>AJCC T</strong>: T1 submucosa; T2 muscularis propria; T3 pericolorectal soft tissue; T4a visceral peritoneum; T4b adjacent organs/structures.</li>
          <li><strong>AJCC N</strong>: N1 = 1–3 LNs or tumor deposits; N1a 1 LN; N1b 2–3 LNs; N1c tumor deposits; N2 ≥4 LNs; N2a 4–6; N2b ≥7.</li>
          <li><strong>AJCC M</strong>: M1a single distant site; M1b ≥2 distant sites; M1c peritoneal metastasis.</li>
          <li><strong>Metastatic pattern</strong>: liver is most common; upper rectum drains through the superior rectal vein to the portal system; middle/lower rectum can spread to lung through systemic venous drainage.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸治療",
        "label_en": "RECTAL TX",
        "h2_zh": "直腸癌治療架構、全直腸繫膜切除、低前位切除／腹會陰切除、化療與放療",
        "h2_en": "Rectal cancer treatment framework, TME, LAR/APR, chemotherapy, and RT",
        "body_zh": """

        <ul>
          <li><strong>第一期臨床 T1–T2、淋巴結陰性</strong>：通常以手術單獨治療。</li>
          <li><strong>低風險 T1 局部切除條件</strong>：僅限 T1；小於 3 公分；小於腸腔周徑 30%；切緣大於 3 mm；距肛門緣 8 公分內；中分化或高分化；無神經周圍侵犯、無淋巴血管侵犯；臨床無淋巴結疑慮。</li>
          <li><strong>其他第一期病人</strong>：多數需要全直腸繫膜切除。</li>
          <li><strong>低位 T2 且可能需要腹會陰切除</strong>：可考慮同步放化療後重新評估，再決定手術或觀察等待。</li>
          <li><strong>第二至第三期</strong>：T3–T4、淋巴結陰性，或任何淋巴結陽性，通常需術前治療。</li>
          <li><strong>常見治療順序</strong>：長程同步放化療 → 化療 → 手術或觀察等待；化療 → 長程同步放化療 → 手術或觀察等待；嚴格篩選者單純化療後若反應良好可手術；短程放療 → 手術 → 輔助化療；短程放療 → 化療 → 手術。</li>
          <li><strong>第二至第三期錯配修復缺陷／微衛星高度不穩定</strong>：優先考慮免疫檢查點抑制劑，如 dostarlimab、nivolumab、pembrolizumab；若 6 個月後仍有持續性疾病，再接同步放化療與手術。</li>
          <li><strong>僅有肝或肺寡轉移</strong>：可採治癒意圖；策略可包括化療、放療、全直腸繫膜切除或觀察等待，加上轉移病灶切除或立體定位放療。</li>
          <li><strong>Dutch M1 第二期研究</strong>：肝或肺有限轉移，25 Gy／5 次 → CAPEOX 加 bevacizumab → 直腸手術 → 根治性轉移病灶治療；2 年總生存 80%，8 年存活 32%，無病 28%。</li>
          <li><strong>全直腸繫膜切除</strong>：切除直腸與直腸繫膜，包含周圍脂肪與直腸繫膜淋巴結。</li>
          <li><strong>低前位切除</strong>：保留括約肌，通常可避免永久造口。</li>
          <li><strong>腹會陰切除</strong>：不保留括約肌，移除肛門與括約肌複合體，通常造成永久性結腸造口。</li>
          <li><strong>局部高風險因子</strong>：低位腫瘤、括約肌或肛管侵犯、直腸繫膜筋膜受威脅、T4、預計腹會陰切除，通常更需要術前降期與器官保留討論。</li>
          <li><strong>FOLFOX</strong>：5-FU、leucovorin 與 oxaliplatin。5-FU 抑制胸苷酸合成酶；leucovorin 增強 5-FU 結合；oxaliplatin 造成 DNA 交聯。</li>
          <li><strong>FOLFOX 毒性</strong>：5-FU 可造成手足症候群、噁心與腸胃不適；oxaliplatin 可造成神經病變。</li>
          <li><strong>CAPEOX</strong>：capecitabine 第 1–14 天，每 3 週一循環，合併靜脈 oxaliplatin。</li>
          <li><strong>轉移性微衛星穩定／錯配修復正常疾病</strong>：FOLFOX 或 CAPEOX，可加或不加 bevacizumab。</li>
          <li><strong>轉移性錯配修復缺陷／微衛星高度不穩定或 POLE／POLD 突變</strong>：第一線可用免疫檢查點抑制劑，如 ipilimumab／nivolumab、pembrolizumab、dostarlimab。</li>
          <li><strong>長程同步放化療</strong>：選擇性淋巴結體積 45 Gy；受侵犯直腸繫膜與淋巴結加量至 50.4–54 Gy；同步 5-FU 或 capecitabine。</li>
          <li><strong>Capecitabine 放射增敏</strong>：875 mg/m² 口服每日兩次，週一至週五，僅放療日服用。</li>
          <li><strong>5-FU 放射增敏</strong>：每日 225 mg/m² 或連續輸注。</li>
          <li><strong>手術時間</strong>：通常在術前同步放化療後 5–12 週。</li>
          <li><strong>短程放療</strong>：25 Gy／5 次。</li>
          <li><strong>三維順形或強度調控放療</strong>：皆可使用；強度調控放療有助於降低腸道、膀胱與股骨頭劑量。</li>
          <li><strong>靶區涵蓋</strong>：整個直腸繫膜、骶前、內髂與直腸繫膜淋巴結照射至 45 Gy；前方侵犯時納入外髂；受侵犯直腸繫膜或淋巴結加量至 50.4 Gy，有時 54 Gy。</li>
          <li><strong>三維照野邊界</strong>：上界 L5-S1；側界超出骨盆最寬處 2 公分；下界低於原發腫瘤 3–5 公分，或遠端腫瘤至肛門緣標記。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Stage I cT1–T2N0</strong>: usually surgery alone.</li>
          <li><strong>Selected low-risk T1 local excision criteria</strong>: T1 only, &lt;3 cm, &lt;30% circumference, &gt;3 mm margin, within 8 cm of anal verge, moderately/well differentiated, no PNI/LVSI, no clinical nodal concern.</li>
          <li><strong>Other stage I</strong>: most patients require TME.</li>
          <li><strong>Low-lying T2 requiring APR</strong>: consider chemoRT → restage → surgery or surveillance/W&W.</li>
          <li><strong>Stage II/III</strong>: T3–T4N0 or any N+, usually neoadjuvant therapy.</li>
          <li><strong>Common sequences</strong>: LC-CRT → chemotherapy → surgery/W&W; chemotherapy → LC-CRT → surgery/W&W; selected chemotherapy alone → surgery if good response; SC-RT → surgery → adjuvant chemo; SC-RT → chemotherapy → surgery.</li>
          <li><strong>dMMR/MSI-H stage II/III</strong>: prioritize immune checkpoint inhibitor such as dostarlimab, nivolumab, or pembrolizumab; if persistent disease after about 6 months, proceed to CRT → surgery.</li>
          <li><strong>Oligometastatic liver/lung-only</strong>: potentially curative; strategies include chemotherapy/RT/TME or surveillance plus metastasectomy/SBRT.</li>
          <li><strong>Dutch M1 phase II</strong>: liver/lung-limited metastases, 25 Gy/5 fx → CAPEOX + bevacizumab → rectal surgery → radical metastasis treatment; 2-year OS 80%, 8-year survival 32%, disease-free 28%.</li>
          <li><strong>TME</strong>: total mesorectal excision removes rectum and mesorectum, including surrounding fat and mesorectal LNs.</li>
          <li><strong>LAR</strong>: low anterior resection, sphincter-sparing, usually avoids permanent stoma.</li>
          <li><strong>APR</strong>: abdominoperineal resection, not sphincter-sparing, removes anus/sphincter complex, usually permanent colostomy.</li>
          <li><strong>High-risk local factors</strong>: low tumor, sphincter/anal canal invasion, threatened MRF, T4 disease, planned APR; these usually need neoadjuvant downstaging and organ-preservation discussion.</li>
          <li><strong>FOLFOX</strong>: 5-FU + leucovorin + oxaliplatin. 5-FU inhibits thymidylate synthase; leucovorin enhances 5-FU binding; oxaliplatin causes DNA crosslinks.</li>
          <li><strong>FOLFOX toxicity</strong>: 5-FU hand-foot syndrome and nausea/GI upset; oxaliplatin neuropathy.</li>
          <li><strong>CAPEOX</strong>: capecitabine days 1–14 q3 weeks + IV oxaliplatin.</li>
          <li><strong>pMMR/MSS metastatic</strong>: FOLFOX/CAPEOX ± bevacizumab.</li>
          <li><strong>dMMR/MSI-H or POLE/POLD mutation metastatic</strong>: first-line checkpoint inhibitor such as ipilimumab/nivolumab, pembrolizumab, or dostarlimab.</li>
          <li><strong>LC-CRT</strong>: elective nodal volume 45 Gy; involved mesorectum and involved nodes boosted to 50.4–54 Gy; concurrent 5-FU or capecitabine.</li>
          <li><strong>Capecitabine radiosensitization</strong>: 875 mg/m² PO BID Monday–Friday, only on RT days.</li>
          <li><strong>5-FU radiosensitization</strong>: 225 mg/m² daily or continuous infusion.</li>
          <li><strong>Surgery timing</strong>: usually 5–12 weeks after preop CRT.</li>
          <li><strong>SC-RT</strong>: 25 Gy/5 fractions.</li>
          <li><strong>3D/IMRT</strong>: both usable; IMRT helps bowel/bladder/femoral head sparing.</li>
          <li><strong>Target coverage</strong>: entire mesorectum, presacral, internal iliac, and mesorectal nodes to 45 Gy; anterior invasion includes external iliac; involved mesorectum/nodes boost to 50.4 Gy, sometimes 54 Gy.</li>
          <li><strong>3D borders</strong>: superior L5-S1; lateral margin 2 cm beyond widest pelvis; inferior border 3–5 cm below primary or to anal verge marker for distal tumors.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸觀察等待",
        "label_en": "RECTAL W&W",
        "h2_zh": "觀察等待監測與器官保留基礎",
        "h2_en": "Watch-and-wait surveillance and organ-preservation basis",
        "body_zh": """

        <p>若第二至第三期直腸癌經長程同步放化療加系統治療後達到<strong>臨床完全緩解</strong>，可考慮觀察等待。此策略必須非常密集追蹤，因為局部再生長多發生在前 2 年，且需早期救援全直腸繫膜切除。</p>
        <ul>
          <li><strong>病史理學檢查、癌胚抗原與肛門指診</strong>：前 2 年每 3 個月一次，之後每 6 個月一次直到第 5 年。</li>
          <li><strong>直腸鏡或軟式乙狀結腸鏡</strong>：前 2 年每 3 個月一次，之後每 6 個月一次直到第 5 年。</li>
          <li><strong>直腸磁振影像</strong>：每 6 個月一次，共 3 年。</li>
          <li><strong>胸腹骨盆電腦斷層</strong>：每 6 個月一次，共 5 年。</li>
          <li><strong>大腸鏡</strong>：完成治療後 1 年。</li>
          <li><strong>若發現進階腺瘤</strong>：1 年後重做大腸鏡。</li>
          <li><strong>若未發現進階腺瘤</strong>：3 年後重做，之後每 5 年一次。</li>
          <li><strong>臨床提醒</strong>：觀察等待不是省略治療，而是密集監測加早期救援策略，需要有經驗的磁振影像、內視鏡、肛門指診與多專科團隊判讀。</li>
        </ul>
        """,
        "body_en": """
        <p>If stage II/III rectal cancer reaches <strong>clinical complete response, cCR</strong>, after LC-CRT plus systemic therapy, watch-and-wait can be considered. This strategy requires intensive follow-up because regrowth occurs mainly within the first 2 years and must be salvaged early with TME.</p>
        <ul>
          <li><strong>H&P / CEA / DRE</strong>: every 3 months ×2 years, then every 6 months until 5 years.</li>
          <li><strong>Proctoscopy or flexible sigmoidoscopy</strong>: every 3 months ×2 years, then every 6 months until 5 years.</li>
          <li><strong>MRI rectum</strong>: every 6 months ×3 years.</li>
          <li><strong>CT CAP</strong>: every 6 months ×5 years.</li>
          <li><strong>Colonoscopy</strong>: 1 year after completing therapy.</li>
          <li><strong>If advanced adenoma</strong>: repeat colonoscopy in 1 year.</li>
          <li><strong>If no advanced adenoma</strong>: repeat in 3 years, then every 5 years.</li>
          <li><strong>Clinical caution</strong>: W&W is not treatment omission; it is an intensive surveillance-and-salvage strategy requiring expert MRI, endoscopy, DRE, and multidisciplinary review.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸證據 I",
        "label_en": "RECTAL EVIDENCE I",
        "h2_zh": "局部晚期直腸癌證據：放療局部控制、Dutch TME、FFCD/EORTC、德國試驗",
        "h2_en": "LARC evidence: RT local control, Dutch TME, FFCD/EORTC, and German trial",
        "body_zh": """

        <ul>
          <li><strong>全直腸繫膜切除前時代</strong>：GITSG 7175、NSABP R-01、NCCTG 794751 與 Swedish Rectal Cancer Trial 顯示手術加放療或同步放化療可改善局部復發，部分研究也改善總生存。</li>
          <li><strong>全直腸繫膜切除時代轉變</strong>：全直腸繫膜切除於 1982 年被描述；手術品質提高後，放療主要角色由總生存效益轉為局部控制效益。</li>
          <li><strong>Dutch TME／CKVO 9504</strong>：1861 位距肛門緣小於 15 公分的可切除直腸癌，25 Gy／5 次術前短程放療後接全直腸繫膜切除，對比單純全直腸繫膜切除。</li>
          <li><strong>Dutch TME 結果</strong>：10 年局部復發 5% 對 11%，p&lt;0.001；總生存與無病生存無顯著差異。第三期且切緣陰性亞組 10 年總生存 50% 對 40%，p=0.032。</li>
          <li><strong>FFCD 9203</strong>：術前放療 45 Gy／25 次對比術前同步放化療合併 bolus 5-FU／leucovorin。總生存未改善，但 5 年局部復發 16% 降至 8%，p=0.004；病理完全緩解 4% 升至 11%，p&lt;0.0001。</li>
          <li><strong>EORTC 22921</strong>：長程放療中加入同步化療可改善局部復發；術前同步放化療加術後化療的 5 年局部復發約 7.6%，術前單純放療約 17.1%。</li>
          <li><strong>German CAO/ARO/AIO-94</strong>：823 位距肛門緣小於 16 公分的直腸腺癌，比較術前同步放化療 → 全直腸繫膜切除 → 輔助 5-FU，與全直腸繫膜切除 → 術後同步放化療 → 輔助 5-FU。</li>
          <li><strong>德國試驗方案</strong>：50.4 Gy／28 次加 120 小時 5-FU 輸注；術後組另加術後腫瘤床加量 5.4 Gy。</li>
          <li><strong>德國試驗注意事項</strong>：屬於磁振影像廣泛使用前時代；術後組有 18% 後來發現為 T1–2N0，意味術前組可能約 20% 過度治療。</li>
          <li><strong>德國試驗結果</strong>：5 年局部復發 6% 對 13%，p=0.006；10 年局部復發 7% 對 10%，p=0.048；5 年總生存 76% 對 74%，p=0.80。</li>
          <li><strong>降期與保留括約肌</strong>：術前病理完全緩解約 8%；術後組第三期 40% 對術前組 25%。原預計腹會陰切除病人中，術前組 40% 可保留括約肌，術後組 20%。</li>
          <li><strong>完成率</strong>：術前組放療與化療完成率約 90%，術後組約 50%。</li>
          <li><strong>重點結論</strong>：術前同步放化療優於術後同步放化療，因局部控制較好、毒性較低、完成率較佳，且有更多降期與保留括約肌機會。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Pre-TME era</strong>: GITSG 7175, NSABP R-01, NCCTG 794751, and Swedish Rectal Cancer Trial showed surgery + RT/CRT improves local recurrence, with OS benefit in some trials.</li>
          <li><strong>TME era shift</strong>: TME was described in 1982; after surgical quality improved, the main role of RT became local-control benefit rather than OS benefit.</li>
          <li><strong>Dutch TME / CKVO 9504</strong>: 1861 patients with resectable rectal cancer &lt;15 cm from anal verge, 25 Gy/5 fx preop RT → TME vs TME alone.</li>
          <li><strong>Dutch TME outcome</strong>: 10-year LR 5% vs 11%, p&lt;0.001; no significant OS/DFS difference. Stage III + negative-margin subgroup had 10-year OS 50% vs 40%, p=0.032.</li>
          <li><strong>FFCD 9203</strong>: preop RT alone 45 Gy/25 fx vs preop CRT with bolus 5-FU/leucovorin. No OS benefit, but 5-year LR 16%→8%, p=0.004; pCR 4%→11%, p&lt;0.0001.</li>
          <li><strong>EORTC 22921</strong>: adding concurrent chemotherapy to long-course RT improved local recurrence; preop CRT + postop CHT had 5-year LR around 7.6% vs preop RT alone around 17.1%.</li>
          <li><strong>German CAO/ARO/AIO-94</strong>: 823 patients with rectal adenocarcinoma &lt;16 cm from anal verge, preop CRT → TME → adjuvant 5-FU vs TME → postop CRT → adjuvant 5-FU.</li>
          <li><strong>German regimen</strong>: 50.4 Gy/28 fx + 120-hour 5-FU infusion; postop arm received additional postoperative-bed boost 5.4 Gy.</li>
          <li><strong>German trial caveat</strong>: pre-MRI era; 18% in the postop arm were found to be T1–2N0, implying about 20% potential overtreatment in the preop arm.</li>
          <li><strong>German outcome</strong>: 5-year LR 6% vs 13%, p=0.006; 10-year LR 7% vs 10%, p=0.048; 5-year OS 76% vs 74%, p=0.80.</li>
          <li><strong>Downstaging/sphincter preservation</strong>: preop pCR about 8%; postop arm stage III 40% vs preop 25%. Among patients initially planned for APR, preop arm had 40% sphincter-sparing surgery vs 20% postop.</li>
          <li><strong>Compliance</strong>: preop arm RT/chemo completion about 90% vs postop about 50%.</li>
          <li><strong>Take-home</strong>: preop CRT is preferred over postop CRT because of better local control, lower toxicity, better compliance, and more downstaging/sphincter preservation.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸證據 II",
        "label_en": "RECTAL EVIDENCE II",
        "h2_zh": "短程與長程放療、全程新輔助治療、器官保留、PROSPECT 與錯配修復缺陷 PD-1 治療",
        "h2_en": "Short-course vs long-course, TNT, organ preservation, PROSPECT, and dMMR PD-1 blockade",
        "body_zh": """

        <ul>
          <li><strong>兩種放療典型模式</strong>：長程同步放化療為 50.4–54 Gy，每次 1.8–2 Gy，合併同步化療；短程放療為 25 Gy／5 次，通常不合併同步化療。</li>
          <li><strong>Polish I</strong>：25 Gy／5 次後 7 天內全直腸繫膜切除，對比 50.4 Gy／28 次合併 5-FU／leucovorin 後 4–6 週手術。保留括約肌 61.2% 對 58.0%；總生存、無病生存與局部復發相近；長程同步放化療切緣陽性較低 4.4% 對 12.9%，但急性毒性較高 18% 對 3%。</li>
          <li><strong>TROG 01.04</strong>：T3 直腸腺癌短程放療對比長程同步放化療。3 年局部復發 7.5% 對 4.4%；7 年局部復發 7.5% 對 5.7%；遠端無轉移生存、總生存與晚期毒性相近。遠端腫瘤亞組局部復發 12.5% 對 0%。</li>
          <li><strong>Stockholm III</strong>：比較 25 Gy／5 次後立即手術、25 Gy／5 次後延遲手術，以及 50 Gy／25 次延遲手術且不合併同步化療。5 年局部復發 3–5%，總生存約 75%，無復發生存約 65%。短程放療後延遲手術病理完全緩解 10.4% 對立即手術 0.3%；立即手術術後併發症較多。</li>
          <li><strong>STELLAR</strong>：遠端或中段直腸癌臨床 T3–4 或淋巴結陽性，25 Gy／5 次 → CAPEOX 4 次 → 全直腸繫膜切除 → CAPEOX 2 次，對比長程同步放化療 → 手術 → CAPEOX 6 次。3 年無病生存達非劣性 64.5% 對 62.3%；3 年總生存 86% 對 75%；病理完全緩解 22% 對 12%；第 3–4 級急性毒性 26.5% 對 12.6%。</li>
          <li><strong>RAPIDO</strong>：高風險局部晚期直腸癌，25 Gy／5 次 → CAPEOX 6 次或 FOLFOX4 9 次 → 全直腸繫膜切除，對比長程同步放化療 → 手術 → 選擇性輔助化療。3 年疾病相關治療失敗 23.7% 對 30.4%；遠端轉移 20% 對 27%；病理完全緩解 28% 對 14%；3 年總生存兩組皆 89%。</li>
          <li><strong>RAPIDO 注意事項</strong>：5 年更新顯示短程放療加全程新輔助治療組局部控制較差；局部區域失敗 11.7% 對 8.1%，R0／R1 切除後局部區域復發 10% 對 6%。</li>
          <li><strong>較偏向長程同步放化療的情境</strong>：T4 原發、淋巴結陽性尤其直腸繫膜外淋巴結、直腸繫膜筋膜受侵犯、低位腫瘤、下三分之一腫瘤、括約肌或肛管侵犯，或計畫觀察等待。</li>
          <li><strong>OPRA</strong>：324 位第二至第三期病人，比較誘導 FOLFOX／CAPEOX 後接長程同步放化療，與長程同步放化療後接鞏固 FOLFOX／CAPEOX。8–12 週以肛門指診、軟式乙狀結腸鏡與磁振影像重新評估；完全或近完全反應者進入觀察等待。</li>
          <li><strong>OPRA 結果</strong>：74% 進入觀察等待；再生長多在 2 年內且可用全直腸繫膜切除救援。3 年無病生存約 75%，局部無復發生存約 95%，遠端無轉移生存約 83%，總生存約 94%。器官保留 41% 對 53%，鞏固化療較佳。</li>
          <li><strong>OPERA</strong>：低至中段 T2–T3、N0 或小 N1、腫瘤小於 5 公分；45 Gy／25 次加 capecitabine 後，比較外照射加量 9 Gy／5 次與接觸式 X 光近接治療加量 90 Gy／3 次。3 年器官保留 59% 對 81%；腫瘤小於 3 公分者 63% 對 97%。</li>
          <li><strong>MORPHEUS</strong>：第二／三期高劑量率近接治療加量試驗，基礎為 45 Gy／25 次外照射加 capecitabine 或 5-FU。期中結果：臨床完全緩解 50% 對 90%，2 年免全直腸繫膜切除生存 39% 對 77%。</li>
          <li><strong>JANUS</strong>：長程同步放化療後接 mFOLFOX6／CAPEOX，對比長程同步放化療後接 mFOLFIRINOX；檢驗加強化療是否提高臨床完全緩解、器官保留與無病生存。</li>
          <li><strong>PROSPECT</strong>：1194 位嚴格篩選、適合保留括約肌全直腸繫膜切除的 T2N+ 或 T3N0/+ 病人。先給 FOLFOX6 6 次；若反應至少 20% 則直接手術，反應不足再放療；對比標準術前同步放化療。</li>
          <li><strong>PROSPECT 結果</strong>：5 年無病生存 80.8% 對 78.6%；總生存 89.5% 對 90.2%；局部復發 1.8% 對 1.6%；R0 切除 90.4% 對 91.2%。支持嚴格篩選中等風險病人可先化療並在反應良好時省略放療。</li>
          <li><strong>Cercek dostarlimab</strong>：第二期單臂研究，12 位第二至第三期錯配修復缺陷直腸癌病人。原計畫 dostarlimab → 長程同步放化療 → 全直腸繫膜切除，但中位追蹤 12 個月時，100% 持續臨床完全緩解，無需同步放化療或手術。</li>
          <li><strong>錯配修復缺陷 PD-1 治療毒性</strong>：81% 症狀在 9 週內緩解；無第 3 級以上不良事件；僅見第 1–2 級皮膚炎、搔癢與疲倦。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Two RT paradigms</strong>: LC-CRT = 50.4–54 Gy at 1.8–2 Gy/fx + concurrent chemotherapy; SC-RT = 25 Gy/5 fx without concurrent chemo.</li>
          <li><strong>Polish I</strong>: 25 Gy/5 fx → TME within 7 days vs 50.4 Gy/28 fx + 5-FU/leucovorin → TME 4–6 weeks later. Sphincter preservation 61.2% vs 58.0%, p=0.570; OS/DFS/LR similar; LC-CRT lower positive CRM 4.4% vs 12.9%, but higher acute toxicity 18% vs 3%.</li>
          <li><strong>TROG 01.04</strong>: T3 rectal adenocarcinoma, SC-RT vs LC-CRT. Three-year LR 7.5% vs 4.4%, p=0.24; 7-year LR 7.5% vs 5.7%; DMFS/OS/late toxicity similar. Distal tumors subgroup LR 12.5% SC-RT vs 0% LC-CRT.</li>
          <li><strong>Stockholm III</strong>: 25 Gy/5 fx immediate surgery vs 25 Gy/5 fx delayed surgery vs 50 Gy/25 fx delayed surgery without concurrent chemo. Five-year LR 3–5%, OS about 75%, RFS about 65%. SC-RT delayed TME pCR 10.4% vs 0.3% immediate; immediate surgery had more postop complications.</li>
          <li><strong>STELLAR</strong>: distal/mid rectal cancer cT3–4 and/or N+, 25 Gy/5 fx → CAPEOX ×4 → TME → CAPEOX ×2 vs LC-CRT → TME → CAPEOX ×6. Three-year DFS noninferior 64.5% vs 62.3%; 3-year OS 86% vs 75%; pCR 22% vs 12%; grade 3–4 acute toxicity 26.5% vs 12.6%.</li>
          <li><strong>RAPIDO</strong>: high-risk LARC, 25 Gy/5 fx → CAPEOX ×6 or FOLFOX4 ×9 → TME vs LC-CRT → TME → optional adjuvant chemo. Three-year disease-related treatment failure 23.7% vs 30.4%; DM 20% vs 27%; pCR 28% vs 14%; 3-year OS both 89%.</li>
          <li><strong>RAPIDO caution</strong>: 5-year update showed worse local control with SC-TNT: LRF 11.7% vs 8.1%, and LRR after R0/R1 resection 10% vs 6%.</li>
          <li><strong>When to favor LC-CRT</strong>: T4 primary, N+ especially extra-mesorectal nodes, involved mesorectal fascia, low-lying tumor, lower third rectum, sphincter/anal canal involvement, or planned W&W.</li>
          <li><strong>OPRA</strong>: 324 stage II/III patients, induction FOLFOX/CAPEOX → LC-CRT vs LC-CRT → consolidation FOLFOX/CAPEOX. Restaged at 8–12 weeks with DRE, flex sig, and MRI. cCR/near cCR → W&W.</li>
          <li><strong>OPRA outcome</strong>: 74% entered W&W; regrowth mostly within 2 years and salvageable with TME. Three-year DFS ~75%, LRFS ~95%, DMFS ~83%, OS ~94%. Organ preservation 41% induction vs 53% consolidation.</li>
          <li><strong>OPERA</strong>: low-mid cT2–T3 cN0/small cN1 tumors &lt;5 cm, 45 Gy/25 fx + capecitabine then EBRT boost 9 Gy/5 fx vs contact X-ray BT boost 90 Gy/3 fx. Three-year organ preservation 59% vs 81%; tumors &lt;3 cm: 63% vs 97%.</li>
          <li><strong>MORPHEUS</strong>: phase II/III HDR brachytherapy boost after EBRT 45 Gy/25 fx + capecitabine/5-FU. Interim: cCR 50% vs 90%, 2-year TME-free survival 39% vs 77%.</li>
          <li><strong>JANUS</strong>: LC-CRT → mFOLFOX6/CAPEOX vs LC-CRT → mFOLFIRINOX; testing whether intensified chemotherapy increases cCR/organ preservation and DFS.</li>
          <li><strong>PROSPECT</strong>: 1194 selected cT2N+ or cT3N0/+ patients eligible for sphincter-sparing TME. FOLFOX6 ×6; if ≥20% response → TME, RT reserved for inadequate response; compared with standard preop CRT.</li>
          <li><strong>PROSPECT outcome</strong>: 5-year DFS 80.8% vs 78.6%; OS 89.5% vs 90.2%; LR 1.8% vs 1.6%; R0 90.4% vs 91.2%. Supports RT omission in carefully selected intermediate-risk patients.</li>
          <li><strong>Cercek dostarlimab</strong>: phase II single-arm, 12 stage II–III dMMR rectal cancer patients. Planned dostarlimab → LC-CRT → TME, but at median 12 months, 100% sustained cCR and no CRT/TME needed.</li>
          <li><strong>dMMR PD-1 toxicity</strong>: 81% symptom resolution within 9 weeks; no grade 3+ AEs; only grade 1–2 dermatitis, pruritus, and fatigue.</li>
        </ul>
        """
      },

      {
        "label_zh": "直腸決策",
        "label_en": "RECTAL DECISION",
        "h2_zh": "直腸癌臨床決策總結",
        "h2_en": "Rectal cancer clinical decision framework",
        "body_zh": """

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>直腸癌治療策略：依分期、分子分型與器官保留目標決定</caption>
            <thead>
              <tr>
                <th scope="col">臨床情境</th>
                <th scope="col">主要策略</th>
                <th scope="col">臨床重點</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>臨床 T1–T2、淋巴結陰性</strong></td>
                <td>以手術為主；低風險 T1 病灶可考慮經肛門局部切除，其餘多數需全直腸繫膜切除。</td>
                <td>只有符合低風險條件的 T1 病灶才適合局部切除；其他情況需標準腫瘤學切除。</td>
              </tr>
              <tr>
                <td><strong>低位 T2 腫瘤，可能需要腹會陰切除</strong></td>
                <td>同步放化療後重新評估，再依反應決定手術或觀察等待策略。</td>
                <td>若治療目標包含保留肛門括約肌，可先嘗試術前降期。</td>
              </tr>
              <tr>
                <td><strong>錯配修復正常／微衛星穩定、較高位 T2–T3，且適合括約肌保留手術</strong></td>
                <td>可考慮類似 PROSPECT 策略：先給 FOLFOX 化療；若反應良好，可直接全直腸繫膜切除。</td>
                <td>適合嚴格篩選的中等風險病人；若反應不足，再補放療。</td>
              </tr>
              <tr>
                <td><strong>低位 T2–T3 或 T4 腫瘤</strong></td>
                <td>長程同步放化療後接鞏固性化療，再依反應選擇觀察等待或手術。</td>
                <td>低位腫瘤、T4、直腸繫膜筋膜受威脅、括約肌或肛管侵犯時，較偏向長程同步放化療。</td>
              </tr>
              <tr>
                <td><strong>錯配修復缺陷／微衛星高度不穩定，第二至第三期</strong></td>
                <td>優先考慮 PD-1 免疫檢查點抑制劑，例如 dostarlimab；若仍有殘餘病灶，再考慮同步放化療或手術。</td>
                <td>需早期檢測微衛星不穩定性與錯配修復狀態；此族群可對免疫治療有非常深的反應。</td>
              </tr>
              <tr>
                <td><strong>僅有肝或肺寡轉移</strong></td>
                <td>可採多模式治療，包括化療、放療、直腸手術、轉移病灶切除或立體定位放療。</td>
                <td>部分病人仍可採取治癒意圖治療，不應直接視為單純緩和治療。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="clinical-note"><strong>總結：</strong>直腸癌治療已從「全直腸繫膜切除加固定順序放化療」演進到依 <strong>磁振影像風險、分子分型與治療反應</strong> 調整的個人化策略。錯配修復正常／微衛星穩定病人需平衡局部控制、全身控制與器官保留；錯配修復缺陷／微衛星高度不穩定病人則正在快速走向免疫治療優先。</p>
        """,
        "body_en": """

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Rectal cancer treatment strategy by stage, molecular subtype, and organ-preservation goal</caption>
            <thead>
              <tr>
                <th scope="col">Clinical scenario</th>
                <th scope="col">Main strategy</th>
                <th scope="col">Clinical emphasis</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Clinical T1–T2, node-negative disease</strong></td>
                <td>Surgery alone; selected low-risk T1 tumors may undergo transanal local excision, while most others require total mesorectal excision.</td>
                <td>Local excision is appropriate only for carefully selected low-risk T1 tumors; otherwise, oncologic resection is required.</td>
              </tr>
              <tr>
                <td><strong>Low-lying T2 tumor, likely requiring abdominoperineal resection</strong></td>
                <td>Chemoradiotherapy followed by restaging, then surgery or a watch-and-wait strategy depending on response.</td>
                <td>If sphincter preservation is a goal, neoadjuvant downstaging can be considered.</td>
              </tr>
              <tr>
                <td><strong>Mismatch-repair proficient / microsatellite-stable upper T2–T3 tumor suitable for sphincter-sparing surgery</strong></td>
                <td>Consider a PROSPECT-like strategy: upfront FOLFOX, followed by direct total mesorectal excision if response is adequate.</td>
                <td>Best suited for carefully selected intermediate-risk patients; reserve radiotherapy for inadequate response.</td>
              </tr>
              <tr>
                <td><strong>Low-lying T2–T3 or T4 tumor</strong></td>
                <td>Long-course chemoradiotherapy followed by consolidation chemotherapy, then watch-and-wait or surgery depending on response.</td>
                <td>Favor long-course chemoradiotherapy for low tumors, T4 disease, threatened mesorectal fascia, or sphincter/anal-canal involvement.</td>
              </tr>
              <tr>
                <td><strong>Mismatch-repair deficient / microsatellite instability-high stage II–III disease</strong></td>
                <td>Prioritize PD-1 immune checkpoint blockade, such as dostarlimab; persistent disease can then proceed to chemoradiotherapy or surgery.</td>
                <td>Test microsatellite instability and mismatch-repair status early; this subgroup can have very deep immunotherapy responses.</td>
              </tr>
              <tr>
                <td><strong>Liver-only or lung-only oligometastatic disease</strong></td>
                <td>Use multimodality therapy, including chemotherapy, radiotherapy, rectal surgery, metastasectomy, or stereotactic radiotherapy.</td>
                <td>Some patients can still be managed with curative intent rather than purely palliative intent.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="clinical-note"><strong>Summary:</strong> Rectal cancer treatment has evolved from total mesorectal excision plus fixed-sequence chemoradiotherapy to <strong>MRI-risk-adapted, molecular-adapted, and response-adapted</strong> personalized therapy. Mismatch-repair proficient / microsatellite-stable disease requires balancing local control, systemic control, and organ preservation; mismatch-repair deficient / microsatellite instability-high disease is rapidly moving toward immunotherapy-first management.</p>
        """,
        "body_en": """
        <p>Pancreatic adenocarcinoma is a major cause of cancer death, with average diagnosis in the 60s and higher incidence in males and Black patients. About 50% present with distant metastasis. Overall 5-year survival is about 13%; localized about 44%, locoregional about 16%, metastatic about 3%. Pancreatic tumors include exocrine tumors about 95% and endocrine tumors about 5%; pancreatic adenocarcinoma is the dominant exocrine tumor.</p>
        <ul>
          <li><strong>Less common exocrine tumors</strong>: adenosquamous, acinar cell, and squamous cell carcinoma.</li>
          <li><strong>Endocrine tumors</strong>: neuroendocrine tumors; nonfunctioning tumors are often malignant.</li>
          <li><strong>Clinical challenge</strong>: nonspecific early symptoms, early metastasis, frequent vascular invasion, and low resectability.</li>
          <li><strong>Resectability caveat</strong>: even radiographically resectable disease can reveal occult metastasis/peritoneal disease intraoperatively; upfront resectable presentation is about 20%, and about 20% of those prove unresectable at surgery.</li>
          <li><strong>Symptoms</strong>: upper abdominal pain radiating to the back, weight loss, fatigue, nausea, diarrhea/steatorrhea, jaundice, and new diabetes.</li>
          <li><strong>Pancreatic head tumors</strong>: more likely to cause biliary obstruction, painless jaundice, dark urine, pale stool, and pruritus.</li>
          <li><strong>Body/tail tumors</strong>: present later, often after plexus invasion or metastasis.</li>
          <li><strong>CAPS screening</strong>: high-risk individuals with EUS and/or MRI/MRCP about q12 months.</li>
          <li><strong>Peutz-Jeghers</strong>: STK11/LKB1, start age 40.</li>
          <li><strong>FAMMM</strong>: CDKN2A/p16, start age 40.</li>
          <li><strong>Hereditary pancreatitis</strong>: PRSS1/SPINK1.</li>
          <li><strong>Family history</strong>: 1 first-degree relative with pancreatic cancer; or ≥3 first/second/third-degree relatives with pancreatic cancer.</li>
          <li><strong>BRCA1/2, p16, HNPCC with ≥1 FDR</strong>: start age 45 or 10 years before youngest relative diagnosis.</li>
          <li><strong>Risk factors</strong>: chronic pancreatitis, cigarette smoking, heavy alcohol use, chronic diabetes, high BMI, red meat, hydrocarbons, pesticides, and heavy metals.</li>
          <li><strong>Hereditary syndromes</strong>: PRSS1/SPINK1, STK11/LKB1, CDKN2A/p16, Lynch/HNPCC MLH1/MSH2/MSH6/PMS2, ataxia telangiectasia, BRCA/PALB2-related syndromes.</li>
          <li><strong>Clinical red flags</strong>: new diabetes + weight loss + upper abdominal/back pain; painless jaundice in an older patient.</li>
          <li><strong>Basic workup</strong>: H&P, CBC, CMP, CA19-9.</li>
          <li><strong>Imaging</strong>: CT pancreatic protocol is most important; MRI abdomen/pelvis and MRCP supplement ductal anatomy/liver metastasis evaluation; CT CAP rules out metastasis.</li>
          <li><strong>PET/CT</strong>: controversial; may detect metastasis but cannot replace dedicated pancreatic protocol CT.</li>
          <li><strong>Biopsy</strong>: EUS-guided biopsy, ERCP, or CT-guided biopsy. Upfront resectable disease may not require preop biopsy, but neoadjuvant therapy requires tissue confirmation.</li>
          <li><strong>Staging laparoscopy</strong>: consider before upfront surgery, especially when occult-metastasis risk is high; some centers omit it if high-quality imaging is sufficient.</li>
          <li><strong>Genetic testing after diagnosis</strong>: ATM, BRCA1, BRCA2, CDKN2A, MLH1, MSH2, MSH6, PALB2, PMS2, STK11, TP53.</li>
          <li><strong>Double duct sign</strong>: simultaneous pancreatic duct and common bile duct dilation; highly suspicious for pancreatic-head malignancy and should be treated as malignant until proven otherwise.</li>
        </ul>
        """
      },

      {
        "label_zh": "胰臟解剖/分期",
        "label_en": "PANCREAS STAGING",
        "h2_zh": "胰臟解剖、病理、分子檢測、AJCC 分期與可切除性",
        "h2_en": "Pancreatic anatomy, pathology, molecular testing, AJCC staging, and resectability",
        "body_zh": """

        <ul>
          <li><strong>解剖位置</strong>：胰頭位於第一至第二腰椎前方；胰臟分為頭、頸、體、尾。</li>
          <li><strong>鉤突</strong>：向下呈鉤狀突出的部分；此處腫瘤較難偵測。</li>
          <li><strong>腫瘤位置</strong>：約 60% 在胰頭；15% 在頸部或尾部；20% 為瀰漫性侵犯。</li>
          <li><strong>胰膽管解剖</strong>：胰管與副胰管和總膽管匯合，經 Oddi 括約肌於 Vater 壺腹進入十二指腸。</li>
          <li><strong>腹腔動脈幹</strong>：約位於 T11/T12；分支包括總肝動脈、左胃動脈與脾動脈。</li>
          <li><strong>上腸繫膜動脈</strong>：約位於 L1；分支包括下胰十二指腸動脈、空迴腸動脈、中結腸動脈、右結腸動脈與迴結腸動脈。</li>
          <li><strong>分期重點</strong>：胰臟腺癌分期不只看大小，更重要的是腹腔動脈、上腸繫膜動脈、總肝動脈、上腸繫膜靜脈與門靜脈受侵犯情形。</li>
          <li><strong>淋巴引流</strong>：胰周、腹腔動脈旁、上腸繫膜、肝門與主動脈旁淋巴結。</li>
          <li><strong>靜脈轉移</strong>：經門脈系統，常轉移至肝臟。</li>
          <li><strong>胰頭／頸部引流</strong>：沿總膽管、總肝動脈、門靜脈、胰十二指腸弓、上腸繫膜靜脈與上腸繫膜動脈右側壁。</li>
          <li><strong>胰體／尾部引流</strong>：沿總肝動脈、腹腔動脈、脾動脈與脾門。</li>
          <li><strong>病理</strong>：最常見為腺癌。</li>
          <li><strong>第 1 級</strong>：高分化，超過 95% 為腺體。</li>
          <li><strong>第 2 級</strong>：中分化，50–95% 為腺體。</li>
          <li><strong>第 3 級</strong>：低分化，少於 50% 為腺體。</li>
          <li><strong>變異型</strong>：腺鱗癌、鱗狀細胞癌、膠樣癌、肝樣癌、髓樣癌、侵襲性微乳突癌、印戒細胞或低黏附性癌、未分化或退行性或肉瘤樣或癌肉瘤或類破骨巨細胞癌。</li>
          <li><strong>分子意義</strong>：BRCA1/2 與 PALB2 影響鉑類敏感性與治療選擇；錯配修復基因影響微衛星高度不穩定或錯配修復缺陷可能性。</li>
          <li><strong>BRCA／PALB2 方案</strong>：可考慮 FOLFIRINOX 或 gemcitabine／cisplatin。</li>
          <li><strong>AJCC 第 8 版 T1</strong>：小於等於 2 公分；T1a 小於等於 0.5 公分，T1b 0.5–1 公分，T1c 1–2 公分。</li>
          <li><strong>T2</strong>：大於 2–4 公分。</li>
          <li><strong>T3</strong>：大於 4 公分。</li>
          <li><strong>T4</strong>：侵犯腹腔動脈、上腸繫膜動脈或總肝動脈。</li>
          <li><strong>N0／N1／N2</strong>：N0 無淋巴結轉移；N1 為 1–3 顆淋巴結；N2 為 4 顆以上。</li>
          <li><strong>M1</strong>：遠端轉移，第四期。</li>
          <li><strong>重點</strong>：AJCC 分期與外科可切除性不完全相同；可切除性取決於腫瘤與血管接觸角度、是否可重建、變異血管解剖與腫瘤生物學。</li>
          <li><strong>動脈可切除</strong>：未接觸腹腔動脈、上腸繫膜動脈或總肝動脈。</li>
          <li><strong>靜脈可切除</strong>：未接觸上腸繫膜靜脈或門靜脈，或接觸小於等於 180 度且無血管輪廓不規則。</li>
          <li><strong>胰頭／鉤突邊緣可切除動脈條件</strong>：接觸總肝動脈但未延伸至腹腔動脈或總肝動脈分叉；接觸上腸繫膜動脈小於等於 180 度；變異動脈解剖依接觸程度判斷。</li>
          <li><strong>胰體／尾部邊緣可切除動脈條件</strong>：接觸腹腔動脈小於等於 180 度。</li>
          <li><strong>邊緣可切除靜脈條件</strong>：接觸上腸繫膜靜脈或門靜脈大於 180 度，或小於等於 180 度但有輪廓不規則或血栓，只要近端與遠端血管仍適合重建。</li>
          <li><strong>動脈不可切除</strong>：接觸上腸繫膜動脈或腹腔動脈大於 180 度；腹腔動脈接觸合併主動脈侵犯。</li>
          <li><strong>靜脈不可切除</strong>：上腸繫膜靜脈或門靜脈完全阻塞且無法切除重建。</li>
          <li><strong>生物學邊緣可切除</strong>：日本胰臟學會將 CA19-9 大於等於 500 視為生物學上邊緣可切除。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Anatomy</strong>: pancreatic head anterior to L1–L2; divided into head, neck, body, and tail.</li>
          <li><strong>Uncinate process</strong>: hook-shaped inferior projection; tumors here are harder to detect.</li>
          <li><strong>Tumor location</strong>: about 60% pancreatic head; 15% neck/tail; 20% diffuse involvement.</li>
          <li><strong>Duct anatomy</strong>: pancreatic duct/accessory duct joins the common bile duct and enters the duodenum through the sphincter of Oddi at the ampulla of Vater.</li>
          <li><strong>Celiac trunk</strong>: about T11/T12; branches include common hepatic, left gastric, and splenic artery.</li>
          <li><strong>SMA</strong>: about L1; branches include inferior pancreaticoduodenal, jejunal/ileal, middle colic, right colic, and ileocolic arteries.</li>
          <li><strong>Staging focus</strong>: PDAC staging is not only size; CA, SMA, CHA, and SMV/PV involvement are critical.</li>
          <li><strong>Lymphatic drainage</strong>: peripancreatic, celiac, superior mesenteric, porta hepatic, and para-aortic nodes.</li>
          <li><strong>Venous spread</strong>: through portal venous network, commonly causing liver metastases.</li>
          <li><strong>Head/neck drainage</strong>: along common bile duct, common hepatic artery, portal vein, pancreaticoduodenal arcades, SMV, and right lateral SMA wall.</li>
          <li><strong>Body/tail drainage</strong>: along common hepatic artery, celiac axis, splenic artery, and splenic hilum.</li>
          <li><strong>Pathology</strong>: most commonly adenocarcinoma.</li>
          <li><strong>Grade 1</strong>: well differentiated, &gt;95% glands.</li>
          <li><strong>Grade 2</strong>: moderately differentiated, 50–95% glands.</li>
          <li><strong>Grade 3</strong>: poorly differentiated, &lt;50% glands.</li>
          <li><strong>Variants</strong>: adenosquamous, squamous, colloid, hepatoid, medullary, invasive micropapillary, signet-ring/poorly cohesive, and undifferentiated/anaplastic/sarcomatoid/carcinosarcoma/osteoclast-like giant cells.</li>
          <li><strong>Molecular implication</strong>: BRCA1/2 and PALB2 affect platinum sensitivity and regimen choice; MMR genes affect MSI-H/dMMR possibility.</li>
          <li><strong>BRCA/PALB2 regimen</strong>: consider FOLFIRINOX or gemcitabine/cisplatin.</li>
          <li><strong>AJCC 8 T1</strong>: ≤2 cm; T1a ≤0.5 cm, T1b 0.5–1 cm, T1c 1–2 cm.</li>
          <li><strong>T2</strong>: &gt;2–4 cm.</li>
          <li><strong>T3</strong>: &gt;4 cm.</li>
          <li><strong>T4</strong>: involves celiac axis, SMA, or common hepatic artery.</li>
          <li><strong>N0/N1/N2</strong>: N0 none; N1 1–3 LNs; N2 ≥4 LNs.</li>
          <li><strong>M1</strong>: distant metastasis; stage IV.</li>
          <li><strong>Key point</strong>: AJCC staging and surgical resectability are not identical; resectability depends on tumor-vessel contact angle, reconstructability, variant anatomy, and biology.</li>
          <li><strong>Resectable arterial</strong>: no contact with CA, SMA, or CHA.</li>
          <li><strong>Resectable venous</strong>: no SMV/PV contact or ≤180° contact without contour irregularity.</li>
          <li><strong>Borderline head/uncinate arterial</strong>: CHA contact without extension to CA or CHA bifurcation; ≤180° SMA contact; variant arterial anatomy contact depends on degree.</li>
          <li><strong>Borderline body/tail arterial</strong>: ≤180° CA contact.</li>
          <li><strong>Borderline venous</strong>: &gt;180° SMV/PV contact, or ≤180° contact with contour irregularity/thrombosis if proximal and distal vessel are suitable for reconstruction.</li>
          <li><strong>Unresectable arterial</strong>: &gt;180° SMA or CA contact; CA contact with aortic involvement.</li>
          <li><strong>Unresectable venous</strong>: complete SMV/PV occlusion not amenable to resection/reconstruction.</li>
          <li><strong>Biological borderline</strong>: Japanese Pancreas Society considers CA19-9 ≥500 biologically borderline resectable.</li>
        </ul>
        """
      },

      {
        "label_zh": "胰臟治療",
        "label_en": "PANCREAS TX",
        "h2_zh": "胰臟腺癌治療架構、手術、化療與放療劑量",
        "h2_en": "Pancreatic adenocarcinoma treatment framework, surgery, chemotherapy, and RT dose",
        "body_zh": """

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>胰臟腺癌治療架構：依可切除性分層</caption>
            <thead>
              <tr>
                <th scope="col">臨床情境</th>
                <th scope="col">核心策略</th>
                <th scope="col">放療角色</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>初始可切除</strong></td>
                <td>手術後接輔助化療。</td>
                <td>若有切緣陽性或淋巴結陽性，可在全身治療後考慮術後同步放化療。</td>
              </tr>
              <tr>
                <td><strong>邊緣可切除</strong></td>
                <td>術前化療後重新評估；選擇性加入同步放化療或立體定位放療，再評估是否手術。</td>
                <td>放療可用於處理血管旁切緣與腫瘤血管交界面，提高陰性切緣機會。</td>
              </tr>
              <tr>
                <td><strong>局部晚期不可切除</strong></td>
                <td>先給全身治療；若無進展或遠端轉移，再考慮局部治療。</td>
                <td>同步放化療或立體定位放療主要改善局部控制，不應預設一定能改善總生存。</td>
              </tr>
              <tr>
                <td><strong>遠端轉移</strong></td>
                <td>以全身治療為主。</td>
                <td>放療多用於緩解症狀，例如疼痛、出血、阻塞，或少數寡進展／局部控制情境。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="clinical-note"><strong>邊緣可切除的基本順序：</strong>化療 → 重新評估 → 若適合則同步放化療或立體定位放療 → 再重新評估 → 手術。這個順序反映胰臟腺癌的核心風險：即使局部治療成功，隱性全身性疾病仍常造成失敗。</p>
        <ul>
          <li><strong>手術</strong>：是唯一可能治癒胰臟腺癌的治療。</li>
          <li><strong>日本手術對比同步放化療研究</strong>：可切除胰臟腺癌中，手術優於根治性同步放化療；中位總生存 12 個月對 9 個月；2 年總生存 20% 對 0%。</li>
          <li><strong>胰十二指腸切除術</strong>：用於胰頭癌；切除胰頭、十二指腸、膽囊、部分遠端胃與近端空腸；重建包括胰空腸吻合、肝空腸吻合與胃空腸吻合。</li>
          <li><strong>遠端胰臟切除</strong>：用於胰體或胰尾病灶，常合併或不合併脾臟切除。</li>
          <li><strong>Appleby 手術</strong>：用於胰體／胰尾或腹腔動脈侵犯病灶；切除胰體尾、遠端胃、脾臟與腹腔動脈。</li>
          <li><strong>術前化療</strong>：常用 FOLFIRINOX 或 gemcitabine 加 nab-paclitaxel。</li>
          <li><strong>BRCA1/2 或 PALB2 突變</strong>：可考慮 FOLFIRINOX 或 gemcitabine 加 cisplatin。</li>
          <li><strong>輔助化療</strong>：常用 FOLFIRINOX 或 gemcitabine 加 capecitabine。</li>
          <li><strong>FOLFIRINOX</strong>：包含 5-FU／leucovorin、irinotecan 與 oxaliplatin。Irinotecan 抑制第一型拓樸異構酶；oxaliplatin 造成 DNA 交聯。</li>
          <li><strong>Gemcitabine 加 nab-paclitaxel</strong>：nab-paclitaxel 是白蛋白結合型 paclitaxel，作用於微小管穩定；gemcitabine 是核苷類似物，抑制 DNA 合成。</li>
          <li><strong>Capecitabine</strong>：口服 5-FU 前驅藥。</li>
        </ul>
        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>胰臟癌常用放療劑量與適用情境</caption>
            <thead>
              <tr>
                <th scope="col">治療情境</th>
                <th scope="col">常用劑量／分割</th>
                <th scope="col">同步或搭配治療</th>
                <th scope="col">重點</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>術後傳統分割放療</strong></td>
                <td>45–50.4 Gy／25–28 次</td>
                <td>同步 5-FU 或 capecitabine</td>
                <td>主要考慮於切緣陽性、淋巴結陽性或局部復發高風險病人。</td>
              </tr>
              <tr>
                <td><strong>術前傳統同步放化療</strong></td>
                <td>45–50.4 Gy／25–28 次</td>
                <td>5-FU 或 capecitabine</td>
                <td>CONKO-007 使用 50.4 Gy／28 次。</td>
              </tr>
              <tr>
                <td><strong>PREOPANC 方案</strong></td>
                <td>36 Gy／15 次</td>
                <td>Gemcitabine</td>
                <td>屬於較短療程的同步放化療策略。</td>
              </tr>
              <tr>
                <td><strong>Alliance A021501 立體定位放療</strong></td>
                <td>33–40 Gy／5 次</td>
                <td>通常接在改良 FOLFIRINOX 後</td>
                <td>需要嚴格正常器官限制與呼吸移動管理。</td>
              </tr>
              <tr>
                <td><strong>不可切除病人的根治性同步放化療</strong></td>
                <td>45–50.4 Gy／25–28 次</td>
                <td>5-FU 或 capecitabine</td>
                <td>適用於全身治療後疾病穩定、且局部控制具有臨床意義的病人。</td>
              </tr>
              <tr>
                <td><strong>根治性或鞏固性立體定位放療</strong></td>
                <td>約 40 Gy／5 次</td>
                <td>通常接在誘導性全身治療後</td>
                <td>避免單次 25 Gy，因十二指腸毒性風險較高。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <ul>
          <li><strong>RTOG 9704 參考</strong>：術後 50.4 Gy／28 次；比較放化療前後使用 5-FU 或 gemcitabine；同步放化療期間使用 5-FU；5 年總生存 18% 對 22%，未達顯著差異。</li>
          <li><strong>術後三維順形放療欄位</strong>：前後對照照野，上界 T10/T11、下界 L3/L4，側界包含肝門、胰臟殘端、椎體外 1.5–2 公分以涵蓋主動脈旁區域。</li>
          <li><strong>術後強度調控放療臨床靶體積</strong>：包含殘餘腫瘤或腫瘤床、手術夾、腹腔動脈、上腸繫膜動脈、門靜脈、胰空腸吻合口與主動脈周圍區域。</li>
          <li><strong>立體定位放療模擬定位</strong>：優先放置金標；手術夾或支架可輔助，但金標較佳；治療前禁食 4 小時；可用屏氣或腹部壓迫搭配四維電腦斷層。</li>
          <li><strong>立體定位放療劑量範例</strong>：腫瘤與腫瘤血管交界面給 40 Gy／5 次；腹腔動脈、上腸繫膜動脈與胰周淋巴結等選擇性區域可給 25 Gy／5 次。</li>
          <li><strong>正常器官限制</strong>：十二指腸、胃與小腸應分開描繪；範例限制包括 V33 &lt;1 cc、V20 &lt;3 cc、V15 &lt;9 cc、0.03 cc &lt;36–38 Gy。</li>
          <li><strong>立體定位放療禁忌</strong>：若腫瘤已造成十二指腸穿孔，則不適合立體定位放療。</li>
        </ul>
        """,
        "body_en": """

        <div class="table-wrap">
          <table class="oncology-table decision-table">
            <caption>Pancreatic adenocarcinoma treatment framework by resectability</caption>
            <thead>
              <tr>
                <th scope="col">Clinical scenario</th>
                <th scope="col">Core strategy</th>
                <th scope="col">Role of radiotherapy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Upfront resectable</strong></td>
                <td>Surgery followed by adjuvant chemotherapy.</td>
                <td>Postoperative chemoradiotherapy can be considered after systemic therapy for positive margins or node-positive disease.</td>
              </tr>
              <tr>
                <td><strong>Borderline resectable</strong></td>
                <td>Neoadjuvant chemotherapy followed by restaging; selected patients receive chemoradiotherapy or stereotactic radiotherapy, then restaging and surgery.</td>
                <td>Radiotherapy may help sterilize the vascular margin and tumor-vessel interface, increasing the chance of margin-negative resection.</td>
              </tr>
              <tr>
                <td><strong>Locally advanced unresectable</strong></td>
                <td>Systemic therapy first; if there is no progression or distant metastasis, local therapy can be considered.</td>
                <td>Chemoradiotherapy or stereotactic radiotherapy mainly improves local control; a consistent overall-survival benefit should not be assumed.</td>
              </tr>
              <tr>
                <td><strong>Metastatic</strong></td>
                <td>Systemic therapy is the main treatment.</td>
                <td>Radiotherapy is mainly used for palliation, such as pain, bleeding, obstruction, or selected oligoprogression/local-control situations.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="clinical-note"><strong>Basic sequence for borderline resectable disease:</strong> chemotherapy → restaging → chemoradiotherapy or stereotactic radiotherapy when appropriate → restaging → surgery. This sequence reflects the central risk in pancreatic adenocarcinoma: even when local therapy succeeds, occult systemic disease often drives failure.</p>
        <ul>
          <li><strong>Surgery</strong>: the only potentially curative treatment for pancreatic adenocarcinoma.</li>
          <li><strong>Japanese surgery-versus-chemoradiotherapy study</strong>: in resectable pancreatic adenocarcinoma, surgery was superior to definitive chemoradiotherapy; median overall survival was 12 versus 9 months, and 2-year overall survival was 20% versus 0%.</li>
          <li><strong>Pancreaticoduodenectomy</strong>: used for pancreatic-head cancers; removes the pancreatic head, duodenum, gallbladder, part of the distal stomach, and proximal jejunum; reconstruction includes pancreaticojejunostomy, hepaticojejunostomy, and gastrojejunostomy.</li>
          <li><strong>Distal pancreatectomy</strong>: used for pancreatic body or tail lesions, often with or without splenectomy.</li>
          <li><strong>Appleby procedure</strong>: used for pancreatic body or tail tumors, or celiac-axis involvement; removes the pancreatic body/tail, distal stomach, spleen, and celiac axis.</li>
          <li><strong>Neoadjuvant chemotherapy</strong>: commonly FOLFIRINOX or gemcitabine plus nab-paclitaxel.</li>
          <li><strong>BRCA1/2 or PALB2 mutation</strong>: consider FOLFIRINOX or gemcitabine plus cisplatin.</li>
          <li><strong>Adjuvant chemotherapy</strong>: commonly FOLFIRINOX or gemcitabine plus capecitabine.</li>
          <li><strong>FOLFIRINOX</strong>: includes 5-FU/leucovorin, irinotecan, and oxaliplatin. Irinotecan inhibits topoisomerase I; oxaliplatin causes DNA crosslinks.</li>
          <li><strong>Gemcitabine plus nab-paclitaxel</strong>: nab-paclitaxel is albumin-bound paclitaxel and stabilizes microtubules; gemcitabine is a nucleoside analog that inhibits DNA synthesis.</li>
          <li><strong>Capecitabine</strong>: an oral prodrug of 5-FU.</li>
        </ul>
        <div class="table-wrap">
          <table class="oncology-table dose-table">
            <caption>Common pancreatic radiotherapy doses and treatment settings</caption>
            <thead>
              <tr>
                <th scope="col">Treatment setting</th>
                <th scope="col">Common dose / fractionation</th>
                <th scope="col">Concurrent or paired therapy</th>
                <th scope="col">Key point</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Postoperative conventional radiotherapy</strong></td>
                <td>45–50.4 Gy / 25–28 fractions</td>
                <td>Concurrent 5-FU or capecitabine</td>
                <td>Mainly considered for positive margins, node-positive disease, or high local-recurrence risk.</td>
              </tr>
              <tr>
                <td><strong>Neoadjuvant conventional chemoradiotherapy</strong></td>
                <td>45–50.4 Gy / 25–28 fractions</td>
                <td>5-FU or capecitabine</td>
                <td>CONKO-007 used 50.4 Gy / 28 fractions.</td>
              </tr>
              <tr>
                <td><strong>PREOPANC regimen</strong></td>
                <td>36 Gy / 15 fractions</td>
                <td>Gemcitabine</td>
                <td>A shorter-course chemoradiotherapy strategy.</td>
              </tr>
              <tr>
                <td><strong>Alliance A021501 stereotactic radiotherapy</strong></td>
                <td>33–40 Gy / 5 fractions</td>
                <td>Usually after modified FOLFIRINOX</td>
                <td>Requires strict organ-at-risk constraints and respiratory-motion management.</td>
              </tr>
              <tr>
                <td><strong>Definitive chemoradiotherapy for unresectable disease</strong></td>
                <td>45–50.4 Gy / 25–28 fractions</td>
                <td>5-FU or capecitabine</td>
                <td>For selected patients with stable locally advanced disease after systemic therapy, when local control is clinically meaningful.</td>
              </tr>
              <tr>
                <td><strong>Definitive or consolidative stereotactic radiotherapy</strong></td>
                <td>Approximately 40 Gy / 5 fractions</td>
                <td>Usually after induction systemic therapy</td>
                <td>Avoid single-fraction 25 Gy because of high duodenal-toxicity risk.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <ul>
          <li><strong>RTOG 9704 reference</strong>: postoperative 50.4 Gy / 28 fractions; compared 5-FU versus gemcitabine before and after chemoradiotherapy; concurrent 5-FU was used during chemoradiotherapy; 5-year overall survival was 18% versus 22%, not statistically significant.</li>
          <li><strong>Postoperative three-dimensional conformal fields</strong>: anterior-posterior/posterior-anterior fields with superior border at T10/T11, inferior border at L3/L4, and lateral borders including the porta hepatis, pancreatic remnant, and vertebral bodies plus 1.5–2 cm to cover the para-aortic region.</li>
          <li><strong>Postoperative intensity-modulated radiotherapy clinical target volume</strong>: includes residual tumor or tumor bed, surgical clips, celiac artery, superior mesenteric artery, portal vein, pancreaticojejunostomy, and para-aortic region.</li>
          <li><strong>Stereotactic radiotherapy simulation</strong>: fiducials are preferred; clips or a stent can help but are less ideal; keep patients fasting for 4 hours; use breath-hold or abdominal compression with four-dimensional computed tomography.</li>
          <li><strong>Stereotactic radiotherapy dose example</strong>: 40 Gy / 5 fractions to gross tumor and tumor-vessel interface; 25 Gy / 5 fractions to elective regions including celiac, superior mesenteric, and peripancreatic nodal regions.</li>
          <li><strong>Organ-at-risk constraints</strong>: contour duodenum, stomach, and small bowel separately; example constraints include V33 &lt;1 cc, V20 &lt;3 cc, V15 &lt;9 cc, and 0.03 cc &lt;36–38 Gy.</li>
          <li><strong>Contraindication to stereotactic radiotherapy</strong>: tumor-associated duodenal perforation is not suitable for stereotactic radiotherapy.</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>ESPAC-1</strong>: 289 resected pancreatic adenocarcinoma, 2×2 randomization CRT vs no CRT and CHT vs no CHT. CRT = split-course 40 Gy/20 fx with 2-week break + 5-FU; CHT = 5-FU/leucovorin ×6.</li>
          <li><strong>ESPAC-1 outcome</strong>: adjuvant CHT improved OS: 5-year OS 21% vs 8%; CRT was associated with worse OS: 5-year OS 10% vs 20%.</li>
          <li><strong>ESPAC-1 caveats</strong>: physician-selected randomization arm, background treatment allowed, observation/CHT arms sometimes received RT, RT dose up to 60 Gy, and outdated split-course RT.</li>
          <li><strong>CONKO-001</strong>: adjuvant gemcitabine vs observation after resection. Gemcitabine 1000 mg/m² weekly ×3, q4 weeks ×6.</li>
          <li><strong>CONKO-001 outcome</strong>: 5-year DFS 16% vs 7%, 10-year DFS 14% vs 6%; 5-year OS 21% vs 10%, 10-year OS 12% vs 8%.</li>
          <li><strong>ESPAC-4</strong>: gemcitabine/capecitabine vs gemcitabine; median OS 28 vs 25 months.</li>
          <li><strong>ESPAC-4 margin point</strong>: 60% R1 resection; R1 median OS 23 months vs R0 40 months, highlighting margin status.</li>
          <li><strong>PRODIGE-24</strong>: modified FOLFIRINOX vs gemcitabine; median OS about 55 vs 35 months; preferred for fit patients.</li>
          <li><strong>Postop CRT take-home</strong>: adjuvant chemotherapy is core; postop CRT can be considered for N+ or positive margins, especially after systemic therapy, but is not routine for all patients.</li>
          <li><strong>GITSG/EORTC/ESPAC historical CRT data</strong>: mixed; GITSG suggested benefit but was small/old; ESPAC-1 was negative but methodologically criticized.</li>
          <li><strong>PREOPANC-1</strong>: 246 resectable/borderline resectable patients. Upfront surgery → gemcitabine ×6 vs neoadjuvant gemcitabine-based CRT 36 Gy/15 fx during cycle 2 → surgery → gemcitabine ×4.</li>
          <li><strong>PREOPANC-1 outcome</strong>: R0 resection 41% vs 28%; 5-year OS 21% vs 7%; benefit strongest in borderline resectable disease.</li>
          <li><strong>Alliance A021501</strong>: 126 borderline resectable PDAC. mFOLFIRINOX ×8 → surgery → FOLFOX6 ×4 vs mFOLFIRINOX ×7 → SBRT 33–40 Gy/5 fx → surgery → FOLFOX6 ×4.</li>
          <li><strong>Alliance outcome</strong>: surgery 58% vs 51%; R0 resection 88% vs 74%; 2 pCRs both in RT arm; RT arm closed early because of lower early survival signal, but trial was underpowered/flawed and not definitive against RT.</li>
          <li><strong>CONKO-007</strong>: borderline/unresectable disease after 3 months induction FOLFIRINOX or gemcitabine; randomization to continue chemo vs CRT 50.4 Gy/28 fx + weekly gemcitabine.</li>
          <li><strong>CONKO-007 outcome</strong>: total R0 resection not significantly improved 18% vs 25%, but R0 CRM-negative 9% vs 20%, pCR 0% vs 6%, R1 10% vs 3%. PFS/OS similar.</li>
          <li><strong>PREOPANC-2</strong>: neoadjuvant FOLFIRINOX ×8 vs PREOPANC-1 winning arm. Median OS 22 vs 21 months; resection 77% vs 75%.</li>
          <li><strong>LAP07</strong>: 442 locally advanced pancreatic cancer. Induction gemcitabine ± erlotinib; if nonprogressive, continue chemo vs CRT 54 Gy + capecitabine.</li>
          <li><strong>LAP07 outcome</strong>: erlotinib no OS benefit; chemoRT no OS benefit but improved locoregional control: locoregional progression 46% vs 32%.</li>
          <li><strong>Pancreas SBRT</strong>: single-fraction 25 Gy had unacceptable duodenal toxicity; modern approach uses multifraction SBRT around 33–40 Gy/5 fx.</li>
          <li><strong>SMART / MR-guided adaptive RT</strong>: aims for dose escalation and daily adaptation to improve local control while protecting GI OARs.</li>
          <li><strong>NRG GI-011/LAP100</strong>: ongoing dose-escalated RT/SBRT strategies such as 75 Gy/25 fx or 50 Gy/5 fx in locally advanced disease.</li>
        </ul>
        """
      },

      {
        "label_zh": "肛門總論",
        "label_en": "ANAL OVERVIEW",
        "h2_zh": "肛門癌總論、臨床表現、危險因子與檢查評估",
        "h2_en": "Anal cancer overview, presentation, risk factors, and workup",
        "body_zh": """

        <p>肛門癌相對少見，終身風險約 <strong>1/500</strong>，約占胃腸道惡性腫瘤的 2.5%；直腸癌約比肛門癌常見 5 倍。女性約為男性 2 倍，平均診斷年齡在 60 多歲。多數病人以局部或局部區域疾病表現，因此治癒率相對高。人類乳突病毒與約 85–90% 病例相關，HIV 也是重要危險因子。</p>
        <ul>
          <li><strong>分期分布</strong>：局部疾病約 41%，區域疾病約 36%，遠端轉移約 14%，未知約 8%。</li>
          <li><strong>5 年相對存活</strong>：局部疾病 84.5%，區域疾病 68.2%，遠端轉移 36.3%，未知 66.8%。</li>
          <li><strong>核心概念</strong>：肛門鱗狀細胞癌雖少見，但診斷時多非廣泛轉移，且根治性同步放化療可保留肛門功能。</li>
          <li><strong>臨床表現</strong>：直腸出血最常見；也可有疼痛、直腸腫塊感與排便習慣改變。</li>
          <li><strong>臨床陷阱</strong>：症狀常被誤認為痔瘡、肛裂或良性肛直腸疾病；持續出血、疼痛、腫塊感或免疫抑制者應低門檻做肛門指診、肛門鏡與切片。</li>
          <li><strong>危險因子</strong>：人類乳突病毒，尤其第 16 型；也包括第 18、31、33、45 型；曾有子宮頸、外陰或陰道相關病毒癌症；HIV；免疫抑制；吸菸；接受式肛交。</li>
          <li><strong>病史理學檢查</strong>：詢問症狀持續時間、性質與完整病史。</li>
          <li><strong>肛門指診</strong>：最重要，用於評估腫瘤範圍與括約肌功能。</li>
          <li><strong>女性評估</strong>：婦科檢查與子宮頸篩檢。</li>
          <li><strong>生育功能</strong>：適合的病人應於同步放化療前討論生育保存。</li>
          <li><strong>抽血</strong>：全血球計數、肝腎功能與電解質、癌胚抗原、HIV；若 HIV 陽性，檢查 CD4 數。</li>
          <li><strong>病理</strong>：肛門鏡切片原發腫瘤並檢測人類乳突病毒；可疑淋巴結用切除切片或細針抽吸。</li>
          <li><strong>內視鏡</strong>：乙狀結腸鏡或大腸鏡。</li>
          <li><strong>影像</strong>：胸腹骨盆電腦斷層、骨盆磁振影像加顯影、正子電腦斷層，尤其 T3–T4 或淋巴結陽性病人。</li>
        </ul>
        """,
        "body_en": """
        <p>Anal cancer is relatively rare, with lifetime risk about <strong>1 in 500</strong>, and accounts for about 2.5% of GI malignancies; rectal cancer is about five times more common. It is about twice as common in women, with average diagnosis in the 60s. Most patients present with localized or locoregional disease, so cure rates are relatively high. HPV is associated with about 85–90% of cases, and HIV is an important risk factor.</p>
        <ul>
          <li><strong>Stage distribution</strong>: localized about 41%, regional about 36%, distant about 14%, unknown about 8%.</li>
          <li><strong>5-year relative survival</strong>: localized 84.5%, regional 68.2%, distant 36.3%, unknown 66.8%.</li>
          <li><strong>Key concept</strong>: anal SCC is rare but usually not widely metastatic at diagnosis, and definitive chemoRT can preserve anal function.</li>
          <li><strong>Presentation</strong>: rectal bleeding is most common; pain, rectal mass sensation, and change in bowel habits.</li>
          <li><strong>Clinical pitfall</strong>: symptoms are often mistaken for hemorrhoid, anal fissure, or benign anorectal disease; persistent bleeding, pain, mass sensation, or immunosuppression should trigger DRE, anoscopy, and biopsy.</li>
          <li><strong>Risk factors</strong>: HPV, especially HPV16; also HPV18, 31, 33, 45; history of cervical/vulvar/vaginal HPV-related cancers; HIV; immunosuppression; smoking; receptive anal intercourse.</li>
          <li><strong>H&P</strong>: ask symptom duration/nature and complete history.</li>
          <li><strong>DRE</strong>: most important; assess tumor extent and sphincter function.</li>
          <li><strong>Female evaluation</strong>: gynecologic exam and cervical screening.</li>
          <li><strong>Fertility</strong>: appropriate patients should discuss fertility preservation before chemoRT.</li>
          <li><strong>Labs</strong>: CBC, CMP, CEA, HIV; if HIV-positive, CD4 count.</li>
          <li><strong>Pathology</strong>: anoscopy with biopsy of primary tumor and HPV status; suspicious nodes by excisional biopsy or FNA.</li>
          <li><strong>Procedures</strong>: sigmoidoscopy/colonoscopy.</li>
          <li><strong>Imaging</strong>: CT CAP, MRI pelvis with contrast, PET/CT especially for T3–T4 or N+ disease.</li>
        </ul>
        """
      },

      {
        "label_zh": "肛門解剖/分期",
        "label_en": "ANAL ANAT/STAGE",
        "h2_zh": "肛門解剖、淋巴引流、組織學與 AJCC 第 9 版分期",
        "h2_en": "Anal anatomy, lymphatic drainage, histology, and AJCC 9th edition",
        "body_zh": """

        <ul>
          <li><strong>肛管</strong>：從齒狀線到肛門緣，約 4 公分。</li>
          <li><strong>齒狀線</strong>：分隔直腸柱狀上皮與肛管鱗狀上皮。</li>
          <li><strong>括約肌</strong>：肛管被內括約肌與外括約肌包圍。</li>
          <li><strong>肛門緣</strong>：可觸摸到的無毛鱗狀上皮與有毛鱗狀上皮交界。</li>
          <li><strong>肛門邊緣皮膚</strong>：距肛門緣 5 公分內的會陰周圍皮膚。</li>
          <li><strong>齒狀線以上淋巴引流</strong>：至直腸繫膜與內髂淋巴結。</li>
          <li><strong>齒狀線以下淋巴引流</strong>：至鼠蹊與股淋巴結。</li>
          <li><strong>真正黏膜</strong>：位於齒狀線以上，含 Morgagni 柱，向下形成肛瓣。</li>
          <li><strong>移行區</strong>：從齒狀線開始，含鱗狀上皮。</li>
          <li><strong>肛管病理</strong>：鱗狀細胞癌約 80%，腺癌約 10%。</li>
          <li><strong>腺癌</strong>：通常依直腸腺癌原則處理。</li>
          <li><strong>其他肛管病理</strong>：黑色素瘤、神經內分泌腫瘤、類癌、Kaposi 肉瘤、平滑肌肉瘤與淋巴瘤。</li>
          <li><strong>肛門周圍皮膚腫瘤</strong>：肛門周圍鱗狀細胞癌、基底細胞癌、黑色素瘤、Bowen 病與 Paget 病；若明確源自皮膚，依皮膚癌處理。</li>
          <li><strong>AJCC 第 9 版 T1</strong>：小於等於 2 公分。</li>
          <li><strong>T2</strong>：大於 2–5 公分。</li>
          <li><strong>T3</strong>：大於 5 公分。</li>
          <li><strong>T4</strong>：侵犯鄰近器官，例如陰道、尿道或膀胱。</li>
          <li><strong>N1a</strong>：鼠蹊、直腸繫膜、上直腸、內髂或閉孔淋巴結。</li>
          <li><strong>N1b</strong>：外髂淋巴結。</li>
          <li><strong>N1c</strong>：N1a 加 N1b。</li>
          <li><strong>M1</strong>：遠端轉移。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Anal canal</strong>: from dentate line to anal verge, about 4 cm.</li>
          <li><strong>Dentate line</strong>: separates rectal columnar epithelium from anal canal squamous epithelium.</li>
          <li><strong>Sphincters</strong>: anal canal surrounded by internal and external anal sphincters.</li>
          <li><strong>Anal verge</strong>: palpable junction between non-hair-bearing and hair-bearing squamous epithelium.</li>
          <li><strong>Anal margin</strong>: perianal skin within 5 cm of anal verge.</li>
          <li><strong>Above dentate line drainage</strong>: mesorectal and internal iliac nodes.</li>
          <li><strong>Below dentate line drainage</strong>: inguinal and femoral nodes.</li>
          <li><strong>True mucosa</strong>: above dentate line; contains columns of Morgagni, which form anal valves inferiorly.</li>
          <li><strong>Transitional zone</strong>: starts at the dentate line and contains squamous epithelium.</li>
          <li><strong>Anal canal pathology</strong>: SCC about 80%, adenocarcinoma about 10%.</li>
          <li><strong>Adenocarcinoma</strong>: usually managed like rectal adenocarcinoma.</li>
          <li><strong>Other anal canal histologies</strong>: melanoma, neuroendocrine, carcinoid, Kaposi sarcoma, leiomyosarcoma, lymphoma.</li>
          <li><strong>Perianal skin tumors</strong>: perianal SCC, BCC, melanoma, Bowen disease, Paget disease; managed like skin cancers when clearly skin-based.</li>
          <li><strong>AJCC 9 T1</strong>: ≤2 cm.</li>
          <li><strong>T2</strong>: &gt;2–5 cm.</li>
          <li><strong>T3</strong>: &gt;5 cm.</li>
          <li><strong>T4</strong>: invades adjacent organs such as vagina, urethra, bladder.</li>
          <li><strong>N1a</strong>: inguinal, mesorectal, superior rectal, internal iliac, obturator LNs.</li>
          <li><strong>N1b</strong>: external iliac LNs.</li>
          <li><strong>N1c</strong>: N1a + N1b.</li>
          <li><strong>M1</strong>: distant metastasis.</li>
        </ul>
        """
      },

      {
        "label_zh": "肛門治療/劑量",
        "label_en": "ANAL TX/DOSE",
        "h2_zh": "肛門癌治療架構、放療劑量、5-FU/MMC 與反應評估",
        "h2_en": "Anal cancer treatment framework, RT dose, 5-FU/MMC, and response assessment",
        "body_zh": """

        <ul>
          <li><strong>T1N0 肛門邊緣高分化鱗狀細胞癌</strong>：廣泛局部切除，切緣至少 1 公分。</li>
          <li><strong>廣泛局部切除條件</strong>：病灶源自肛門周圍皮膚且明確與肛管分離；可取得陰性切緣且不影響括約肌；無區域淋巴結侵犯。</li>
          <li><strong>T1N0 肛管鱗狀細胞癌，或 T2–T4，或淋巴結陽性</strong>：根治性同步放化療。</li>
          <li><strong>標準同步化療</strong>：5-FU 加 mitomycin-C。</li>
          <li><strong>5-FU 劑量</strong>：1000 mg/m²，第 1–4 天，每 4 週一循環，共 2 循環。</li>
          <li><strong>Mitomycin-C 劑量</strong>：10 mg/m² 靜脈推注，每 4 週一循環，共 2 循環。</li>
          <li><strong>5-FU 機轉與毒性</strong>：抑制胸苷酸合成酶；常見黏膜炎、口腔炎、噁心、嘔吐與腹瀉。</li>
          <li><strong>Mitomycin-C 機轉與毒性</strong>：DNA 交聯型烷化劑，低氧下活化；主要毒性為嗜中性白血球低下。</li>
          <li><strong>RTOG 0529 T1–T2N0</strong>：原發腫瘤 50.4 Gy／28 次；骨盆 42 Gy／28 次；無淋巴結加量。</li>
          <li><strong>RTOG 0529 T3–T4N0</strong>：原發腫瘤 54 Gy／30 次；骨盆 45 Gy／30 次；無淋巴結加量。</li>
          <li><strong>RTOG 0529 N1</strong>：原發腫瘤 54 Gy／30 次；骨盆 45 Gy／30 次；淋巴結小於等於 3 公分給 50.4 Gy／28 次，大於 3 公分給 54 Gy／30 次。</li>
          <li><strong>反應評估</strong>：不要太早判定治療失敗。ACT II 事後分析顯示，許多 11 週時未完全緩解的病人會在 26 週達臨床完全緩解。</li>
          <li><strong>實務時間點</strong>：若臨床安全，約於放療後 26 週，也就是約 6.5 個月評估反應。</li>
          <li><strong>持續性疾病或局部復發</strong>：救援性腹會陰切除。</li>
          <li><strong>救援手術</strong>：通常為全直腸繫膜切除概念下的腹會陰切除；依直腸癌腹會陰切除原則，且常需較寬的肛門周圍切緣。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>T1N0 anal margin well-differentiated SCC</strong>: wide local excision with ≥1 cm margin.</li>
          <li><strong>Wide local excision requirements</strong>: perianal skin lesion clearly separate from anal canal; negative margin feasible without sphincter compromise; no regional nodes.</li>
          <li><strong>T1N0 anal canal SCC or T2–T4 or N+</strong>: definitive chemoRT.</li>
          <li><strong>Standard concurrent chemo</strong>: 5-FU + mitomycin-C.</li>
          <li><strong>5-FU dose</strong>: 1000 mg/m² days 1–4, q4 weeks ×2 cycles.</li>
          <li><strong>MMC dose</strong>: 10 mg/m² bolus q4 weeks ×2 cycles.</li>
          <li><strong>5-FU mechanism/toxicity</strong>: thymidylate synthase inhibition; mucositis, stomatitis, nausea, vomiting, diarrhea.</li>
          <li><strong>MMC mechanism/toxicity</strong>: DNA-crosslinking alkylator, hypoxic activation; main toxicity neutropenia.</li>
          <li><strong>RTOG 0529 T1–T2N0</strong>: primary 50.4 Gy/28 fx; pelvis 42 Gy/28 fx; no nodal boost.</li>
          <li><strong>RTOG 0529 T3–T4N0</strong>: primary 54 Gy/30 fx; pelvis 45 Gy/30 fx; no nodal boost.</li>
          <li><strong>RTOG 0529 N1</strong>: primary 54 Gy/30 fx; pelvis 45 Gy/30 fx; nodal boost ≤3 cm 50.4 Gy/28 fx; &gt;3 cm 54 Gy/30 fx.</li>
          <li><strong>Response assessment</strong>: do not declare treatment failure too early. ACT II post hoc showed many patients convert from incomplete response at 11 weeks to cCR by 26 weeks.</li>
          <li><strong>Practical timing</strong>: assess response at about 26 weeks after RT, around 6.5 months, if clinically safe.</li>
          <li><strong>Persistent disease or local recurrence</strong>: salvage APR.</li>
          <li><strong>Salvage surgery</strong>: usually APR as part of TME; follow rectal APR principles and often use wider perianal margins.</li>
        </ul>
        """
      },

      {
        "label_zh": "肛門證據",
        "label_en": "ANAL EVIDENCE",
        "h2_zh": "肛門鱗狀細胞癌根治性同步放化療證據：Nigro 到 PLATO",
        "h2_en": "Anal SCC definitive chemoRT evidence: Nigro to PLATO",
        "body_zh": """

        <ul>
          <li><strong>Nigro 方案／Wayne State</strong>：30 Gy／15 次前後對照照射骨盆與鼠蹊淋巴結，加 5-FU／mitomycin-C。原本計畫術後腹會陰切除，但前 5/6 位病人完全緩解，因此改為切片評估。</li>
          <li><strong>Nigro 回溯性資料</strong>：45 位病人，切片時完全緩解 84%，5 年總生存 67%，5 年無造口生存 59%。建立根治性同步放化療概念。</li>
          <li><strong>UK ACT I</strong>：第二至第四期肛門癌，45 Gy／20–25 次放療，加或不加 5-FU／mitomycin-C。</li>
          <li><strong>UK ACT I 結果</strong>：3 年局部失敗 61% 降至 39%；癌症特異存活 61% 升至 72%；總生存未顯著差異。13 年更新：每 100 位病人接受同步放化療可減少 25 次局部區域復發與 12.5 次癌症死亡，且未增加晚期毒性。</li>
          <li><strong>EORTC 22861</strong>：T1–T2N1–3 或 T3–T4N0–3，單純放療對比同步放化療。</li>
          <li><strong>EORTC 結果</strong>：5 年完全緩解 54% 升至 80%；局部控制 50% 升至 68%；無造口生存 40% 升至 72%；總生存無差異。</li>
          <li><strong>ECOG 1289／RTOG 8704</strong>：放療加 5-FU 對比放療加 5-FU／mitomycin-C。</li>
          <li><strong>RTOG 8704 結果</strong>：5 年造口率 22% 降至 9%；無造口生存 59% 升至 71%；無病生存 51% 升至 73%；總生存無差異；第 4–5 級毒性 7% 升至 23%。</li>
          <li><strong>UK ACT II</strong>：50.4 Gy／28 次；5-FU／cisplatin 對比 5-FU／mitomycin-C；維持性 5-FU 對比觀察。</li>
          <li><strong>ACT II 結果</strong>：cisplatin 未優於 mitomycin-C；維持性 5-FU 無效；因便利性與毒性表現，mitomycin-C 仍為標準。</li>
          <li><strong>ACT II 事後分析</strong>：於 11、18、26 週評估臨床完全緩解；許多病人到 26 週才延遲達完全緩解；避免過早救援性腹會陰切除。</li>
          <li><strong>RTOG 9811</strong>：同步 5-FU／mitomycin-C 放化療，對比誘導 5-FU／cisplatin 後接 5-FU／cisplatin 同步放化療。</li>
          <li><strong>RTOG 9811 結果</strong>：5 年總生存 78% 對 71%；無病生存 68% 對 58%；無造口生存 72% 對 65%；支持避免誘導 cisplatin 策略。</li>
          <li><strong>ACCORD 03</strong>：腫瘤至少 4 公分或淋巴結陽性；測試誘導 5-FU／cisplatin 與高劑量加量。無明確無造口生存效益；高劑量加量僅有未達顯著的趨勢。</li>
          <li><strong>RTOG 0529</strong>：第二期劑量繪製強度調控放療；主要終點未達成，但降低急性血液毒性、第 3 級以上皮膚毒性與胃腸毒性。</li>
          <li><strong>RTOG 0529 計畫提醒</strong>：中央審查後 81% 需要重新計畫，表示肛門癌強度調控放療的輪廓描繪、劑量繪製、淋巴結涵蓋與正常器官保護需要高度專業。</li>
          <li><strong>PLATO ACT III</strong>：T1N0/NX 局部切除後，測試小型肛門邊緣腫瘤是否可選擇性同步放化療；主要終點為 3 年局部區域無失敗生存 90%。</li>
          <li><strong>PLATO ACT IV</strong>：T1–T2 小於等於 4 公分、N0/X 早期肛門癌，測試強度調控放療下的減量同步放化療；主要終點為 3 年局部區域無失敗生存 90%。</li>
          <li><strong>PLATO ACT V</strong>：T2N1–3 或 T3–T4 任意 N，測試放療升劑量，目標將 3 年局部區域失敗由 30% 降至 20%。</li>
          <li><strong>未來方向</strong>：依風險調整放療，早期疾病降劑量，局部晚期疾病升劑量。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Nigro regimen / Wayne State</strong>: 30 Gy/15 fx AP/PA to pelvis and inguinal nodes + 5-FU/MMC. APR was originally planned, but the first 5/6 patients had CR, so the approach changed to biopsy assessment.</li>
          <li><strong>Nigro retrospective</strong>: 45 patients, CR at biopsy 84%, 5-year OS 67%, 5-year colostomy-free survival 59%. Established definitive chemoRT concept.</li>
          <li><strong>UK ACT I</strong>: stage II–IV anal cancer, RT 45 Gy/20–25 fx ± 5-FU/MMC.</li>
          <li><strong>UK ACT I outcome</strong>: 3-year local failure 61%→39%; cancer-specific survival 61%→72%; OS not significantly different. Thirteen-year update: per 100 patients, CRT prevented 25 locoregional relapses and 12.5 cancer deaths without increased late toxicity.</li>
          <li><strong>EORTC 22861</strong>: T1–T2N1–3 or T3–T4N0–3, RT alone vs CRT.</li>
          <li><strong>EORTC outcome</strong>: 5-year CR 54%→80%; LC 50%→68%; CFS 40%→72%; OS no difference.</li>
          <li><strong>ECOG 1289 / RTOG 8704</strong>: RT + 5-FU vs RT + 5-FU/MMC.</li>
          <li><strong>RTOG 8704 outcome</strong>: 5-year colostomy 22%→9%; CFS 59%→71%; DFS 51%→73%; OS no difference; grade 4–5 toxicity 7%→23%.</li>
          <li><strong>UK ACT II</strong>: 50.4 Gy/28 fx; 5-FU/cisplatin vs 5-FU/MMC; maintenance 5-FU vs observation.</li>
          <li><strong>ACT II outcome</strong>: cisplatin not superior to MMC; maintenance 5-FU no benefit; MMC remains SOC because of convenience and toxicity profile.</li>
          <li><strong>ACT II post hoc</strong>: cCR assessed at 11, 18, and 26 weeks; many delayed responses occurred by 26 weeks; avoid premature salvage APR.</li>
          <li><strong>RTOG 9811</strong>: concurrent 5-FU/MMC CRT vs induction 5-FU/cisplatin → CRT with 5-FU/cisplatin.</li>
          <li><strong>RTOG 9811 outcome</strong>: 5-year OS 78% vs 71%; DFS 68% vs 58%; CFS 72% vs 65%; supports avoiding induction cisplatin strategy.</li>
          <li><strong>ACCORD 03</strong>: tumor ≥4 cm or N+; tested induction 5-FU/cisplatin and high-dose boost. No clear CFS benefit; high-dose boost only nonsignificant trend.</li>
          <li><strong>RTOG 0529</strong>: phase II dose-painted IMRT; primary endpoint not met, but reduced acute hematologic, grade 3+ dermatologic, and GI toxicity.</li>
          <li><strong>RTOG 0529 planning warning</strong>: 81% required replanning after central review, so anal IMRT contouring/dose painting/nodal coverage/OAR sparing require expertise.</li>
          <li><strong>PLATO ACT III</strong>: T1N0/NX after local excision; tests selective CRT for small anal margin tumors; primary endpoint 3-year LRFFS 90%.</li>
          <li><strong>PLATO ACT IV</strong>: T1–T2 ≤4 cm N0/X early anal cancer; tests reduced-dose CRT using IMRT; primary endpoint 3-year LRFFS 90%.</li>
          <li><strong>PLATO ACT V</strong>: T2N1–3 or T3–T4 any N; tests RT dose escalation to reduce 3-year LRF from 30% to 20%.</li>
          <li><strong>Future direction</strong>: risk-adapted RT, with early-stage dose de-escalation and locally advanced dose escalation.</li>
        </ul>
        """
      },

      {
        "label_zh": "劑量速查",
        "label_en": "DOSE CHECKLIST",
        "h2_zh": "胃腸道腫瘤放療劑量與治療順序速查",
        "h2_en": "GI radiation dose and sequencing checklist",
        "body_zh": """

        <ul>
          <li><strong>食道癌術前 CROSS</strong>：41.4 Gy／23 次，加每週 carboplatin／paclitaxel，之後手術。</li>
          <li><strong>食道癌根治性同步放化療</strong>：50.4 Gy／28 次合併同步化療；不常規升劑量。</li>
          <li><strong>頸段食道癌</strong>：常用 66–70 Gy，接近頭頸癌劑量。</li>
          <li><strong>食道癌原發臨床靶體積</strong>：原發腫瘤上下各加 3–4 公分；若延伸到胃，可用 2 公分；徑向加 1 公分並依解剖修正。</li>
          <li><strong>直腸癌長程同步放化療</strong>：選擇性骨盆 45 Gy，加量至 50.4–54 Gy，合併 capecitabine 或 5-FU。</li>
          <li><strong>直腸癌短程放療</strong>：25 Gy／5 次。</li>
          <li><strong>直腸癌觀察等待追蹤</strong>：肛門指診、軟式乙狀結腸鏡與癌胚抗原前 2 年每 3 個月一次，之後每 6 個月至第 5 年；磁振影像每 6 個月一次共 3 年；胸腹骨盆電腦斷層每 6 個月一次共 5 年。</li>
          <li><strong>胰臟癌術後同步放化療</strong>：45–50.4 Gy／25–28 次，加 5-FU 或 capecitabine。</li>
          <li><strong>胰臟癌術前傳統同步放化療</strong>：45–50.4 Gy／25–28 次；CONKO-007 為 50.4 Gy／28 次。</li>
          <li><strong>胰臟癌 PREOPANC</strong>：36 Gy／15 次加 gemcitabine。</li>
          <li><strong>胰臟癌立體定位放療</strong>：常用 33–40 Gy／5 次；避免單次 25 Gy，因十二指腸毒性風險高。</li>
          <li><strong>肛門癌 T1–T2N0</strong>：原發腫瘤 50.4 Gy／28 次；骨盆 42 Gy／28 次。</li>
          <li><strong>肛門癌 T3–T4N0</strong>：原發腫瘤 54 Gy／30 次；骨盆 45 Gy／30 次。</li>
          <li><strong>肛門癌淋巴結陽性</strong>：原發腫瘤 54 Gy／30 次；骨盆 45 Gy／30 次；淋巴結小於等於 3 公分給 50.4 Gy／28 次，大於 3 公分給 54 Gy／30 次。</li>
          <li><strong>肛門癌同步化療</strong>：第 1 週與第 5 週給 5-FU／mitomycin-C；約 26 週評估反應。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Esophagus preop CROSS</strong>: 41.4 Gy/23 fx + weekly carboplatin/paclitaxel → surgery.</li>
          <li><strong>Esophagus definitive</strong>: 50.4 Gy/28 fx with concurrent chemotherapy; no routine dose escalation.</li>
          <li><strong>Cervical esophagus</strong>: often 66–70 Gy, H&N-like.</li>
          <li><strong>Esophagus RT CTVp</strong>: GTVp + 3–4 cm superior/inferior; if stomach extension, 2 cm; radial 1 cm adjusted anatomically.</li>
          <li><strong>Rectal LC-CRT</strong>: 45 Gy elective pelvis + boost to 50.4–54 Gy with concurrent capecitabine or 5-FU.</li>
          <li><strong>Rectal SC-RT</strong>: 25 Gy/5 fx.</li>
          <li><strong>Rectal W&W surveillance</strong>: DRE/flex sig/CEA q3mo ×2y, then q6mo to 5y; MRI q6mo ×3y; CT CAP q6mo ×5y.</li>
          <li><strong>Pancreas postop CRT</strong>: 45–50.4 Gy/25–28 fx + 5-FU/capecitabine.</li>
          <li><strong>Pancreas neoadjuvant conventional CRT</strong>: 45–50.4 Gy/25–28 fx; CONKO-007 50.4 Gy/28 fx.</li>
          <li><strong>Pancreas PREOPANC</strong>: 36 Gy/15 fx + gemcitabine.</li>
          <li><strong>Pancreas SBRT</strong>: commonly 33–40 Gy/5 fx; avoid single-fraction 25 Gy due to duodenal toxicity.</li>
          <li><strong>Anal T1–T2N0</strong>: primary 50.4 Gy/28 fx; pelvis 42 Gy/28 fx.</li>
          <li><strong>Anal T3–T4N0</strong>: primary 54 Gy/30 fx; pelvis 45 Gy/30 fx.</li>
          <li><strong>Anal N+</strong>: primary 54 Gy/30 fx; pelvis 45 Gy/30 fx; node ≤3 cm 50.4 Gy/28 fx; &gt;3 cm 54 Gy/30 fx.</li>
          <li><strong>Anal chemo</strong>: 5-FU/MMC in weeks 1 and 5; response assessment around 26 weeks.</li>
        </ul>
        """
      },

      {
        "label_zh": "考試速記",
        "label_en": "QUICK FACTS",
        "h2_zh": "考試速記：胃腸道腫瘤核心試驗與重點結論",
        "h2_en": "Exam quick facts: GI oncology core trials and take-home messages",
        "body_zh": """

        <ul>
          <li><strong>食道癌 CROSS</strong>：41.4 Gy／23 次加 carboplatin／paclitaxel 後手術；改善總生存、R0 切除與病理完全緩解；鱗狀細胞癌病理完全緩解高於腺癌。</li>
          <li><strong>食道癌 CheckMate 577</strong>：術前同步放化療加 R0 切除後若仍有殘餘病理疾病，術後 nivolumab 改善無病生存。</li>
          <li><strong>食道癌 FLOT4／ESOPEC</strong>：圍手術期 FLOT 是腺癌與胃食道交界癌重要選項；ESOPEC 支持 FLOT 優於 CROSS 類同步放化療，但未與術後 nivolumab 路徑比較。</li>
          <li><strong>食道癌根治性同步放化療</strong>：RTOG 8501 建立同步放化療；RTOG 9405 與 ARTDECO 顯示不應常規超過 50.4 Gy。</li>
          <li><strong>直腸癌 Dutch TME</strong>：25 Gy／5 次使 10 年局部復發 11% 降至 5%，但整體總生存未改善。</li>
          <li><strong>直腸癌德國試驗</strong>：術前同步放化療優於術後同步放化療。</li>
          <li><strong>直腸癌短程與長程</strong>：Polish、TROG 與 Stockholm 整體相近，但低位、T4、直腸繫膜筋膜受威脅、括約肌侵犯或器官保留時較偏向長程同步放化療。</li>
          <li><strong>直腸癌 OPRA</strong>：同步放化療後鞏固化療改善器官保留。</li>
          <li><strong>直腸癌 PROSPECT</strong>：嚴格篩選 T2N+ 或 T3 病人可先 FOLFOX，若反應至少 20% 可省略放療。</li>
          <li><strong>直腸癌錯配修復缺陷</strong>：PD-1 抑制劑可造成深度臨床完全緩解；需早期檢測微衛星不穩定性／錯配修復。</li>
          <li><strong>胰臟癌可切除性</strong>：由上腸繫膜動脈、腹腔動脈、總肝動脈、上腸繫膜靜脈與門靜脈接觸程度決定可切除、邊緣可切除或不可切除。</li>
          <li><strong>胰臟癌輔助治療</strong>：身體狀況良好者首選改良 FOLFIRINOX；gemcitabine／capecitabine 為替代選項。</li>
          <li><strong>胰臟癌術後同步放化療</strong>：選擇性用於 R1 或淋巴結陽性，通常在系統治療後考慮；不常規給所有病人。</li>
          <li><strong>胰臟癌 PREOPANC</strong>：術前 gemcitabine 為基礎同步放化療改善 R0 與長期總生存訊號，尤其邊緣可切除疾病。</li>
          <li><strong>胰臟癌 LAP07</strong>：不可切除疾病中，同步放化療改善局部控制但不改善總生存。</li>
          <li><strong>肛門癌標準</strong>：以強度調控放療為基礎的根治性同步放化療加 5-FU／mitomycin-C；手術是救援，不是肛管鱗狀細胞癌第一線。</li>
          <li><strong>肛門癌 RTOG 8704</strong>：mitomycin-C 改善無病生存與無造口生存，但增加血液毒性。</li>
          <li><strong>肛門癌 ACT II</strong>：cisplatin 未優於 mitomycin-C；維持性 5-FU 無效。</li>
          <li><strong>肛門癌反應評估</strong>：臨床安全時應等約 26 週再判定持續性疾病。</li>
          <li><strong>肛門癌 RTOG 0529</strong>：強度調控放療降低部分急性毒性，但需要高品質計畫；中央審查後重新計畫很常見。</li>
        </ul>
        """,
        "body_en": """
        <ul>
          <li><strong>Esophagus CROSS</strong>: 41.4 Gy/23 fx + carbo/taxol → surgery; improves OS, R0, and pCR; SCC pCR higher than ACA.</li>
          <li><strong>Esophagus CheckMate 577</strong>: residual disease after neoadj CRT + R0 surgery → adjuvant nivolumab improves DFS.</li>
          <li><strong>Esophagus FLOT4/ESOPEC</strong>: periop FLOT is a major ACA/GEJ option; ESOPEC favored FLOT over CROSS-style CRT but did not compare against the adjuvant nivolumab pathway.</li>
          <li><strong>Esophagus definitive CRT</strong>: RTOG 8501 established CRT; RTOG 9405 and ARTDECO show no routine dose escalation above 50.4 Gy.</li>
          <li><strong>Rectal Dutch TME</strong>: 25 Gy/5 fx improves 10-year LR 11%→5%, without overall OS benefit.</li>
          <li><strong>Rectal German trial</strong>: preop CRT preferred over postop CRT.</li>
          <li><strong>Rectal SC vs LC</strong>: Polish/TROG/Stockholm broadly comparable, but LC-CRT favored for low tumors, T4 disease, threatened MRF, sphincter involvement, or organ preservation.</li>
          <li><strong>Rectal OPRA</strong>: consolidation chemo after CRT improves organ preservation.</li>
          <li><strong>Rectal PROSPECT</strong>: selected cT2N+ or cT3 patients can receive FOLFOX first and omit RT if ≥20% response.</li>
          <li><strong>Rectal dMMR</strong>: PD-1 blockade can produce dramatic cCR; test MSI/MMR early.</li>
          <li><strong>Pancreas resectability</strong>: SMA/CA/CHA/SMV/PV contact defines resectable, borderline, and unresectable disease.</li>
          <li><strong>Pancreas adjuvant</strong>: mFOLFIRINOX preferred for fit patients; gem/cape alternative.</li>
          <li><strong>Pancreas postop CRT</strong>: selective for R1 or N+ after systemic therapy; not routine for all.</li>
          <li><strong>Pancreas PREOPANC</strong>: neoadj gem-based CRT improves R0 and long-term OS signal, especially borderline resectable disease.</li>
          <li><strong>Pancreas LAP07</strong>: chemoRT improves local control but not OS in unresectable disease.</li>
          <li><strong>Anal standard</strong>: definitive IMRT-based chemoRT with 5-FU/MMC; surgery is salvage, not first-line for anal canal SCC.</li>
          <li><strong>Anal RTOG 8704</strong>: MMC improves DFS/CFS but increases hematologic toxicity.</li>
          <li><strong>Anal ACT II</strong>: cisplatin not superior to MMC; maintenance 5-FU no benefit.</li>
          <li><strong>Anal response</strong>: wait until about 26 weeks before declaring persistent disease when clinically safe.</li>
          <li><strong>Anal RTOG 0529</strong>: IMRT reduces some acute toxicities but requires high-quality planning; central-review replanning was common.</li>
        </ul>
        """
      }

    ],
    "excel_sheet": "GI",
    "trial_filter": [
        "GI", "gastrointestinal", "esophageal cancer", "esophagus", "GEJ",
        "gastroesophageal junction", "Siewert", "squamous cell carcinoma",
        "SCC", "adenocarcinoma", "ACA", "Barrett", "GERD", "EUS",
        "FDG PET", "MSI", "dMMR", "PD-L1", "HER2", "CROSS",
        "CheckMate 577", "nivolumab", "POET", "MAGIC", "FLOT",
        "FLOT4", "TOPGEAR", "NeoAEGIS", "ESOPEC", "RTOG 8501",
        "RTOG 9405", "INT 0123", "ARTDECO", "SANO", "CROC",
        "PRESTO", "carboplatin paclitaxel", "FOLFOX", "cisplatin",
        "5-FU", "esophagectomy", "Ivor Lewis", "McKeown",
        "rectal cancer", "locally advanced rectal cancer", "LARC",
        "TME", "total mesorectal excision", "low anterior resection",
        "LAR", "abdominoperineal resection", "APR", "watch and wait",
        "W&W", "short-course RT", "SC-RT", "25 Gy", "long-course CRT",
        "LC-CRT", "capecitabine", "Dutch TME", "CKVO 9504",
        "FFCD 9203", "EORTC 22921", "CAO ARO AIO 94", "German trial",
        "Polish I", "TROG 01.04", "Stockholm III", "STELLAR",
        "RAPIDO", "TNT", "total neoadjuvant therapy", "OPRA",
        "OPERA", "MORPHEUS", "JANUS", "PROSPECT", "dostarlimab",
        "PD-1 blockade", "dMMR rectal cancer", "MSI-H rectal cancer",
        "pancreatic adenocarcinoma", "pancreas", "pancreatic cancer",
        "CA19-9", "double duct sign", "CT pancreatic protocol", "MRCP",
        "EUS FNA", "resectable", "borderline resectable", "unresectable",
        "celiac artery", "CA", "SMA", "CHA", "SMV", "PV", "portal vein",
        "Whipple", "pancreaticoduodenectomy", "distal pancreatectomy",
        "Appleby", "FOLFIRINOX", "modified FOLFIRINOX", "gemcitabine",
        "nab-paclitaxel", "gemcitabine cisplatin", "gemcitabine capecitabine",
        "CONKO-001", "ESPAC-1", "ESPAC-4", "PRODIGE-24", "RTOG 9704",
        "RTOG 0848", "PREOPANC-1", "PREOPANC-2", "Alliance A021501",
        "CONKO-007", "LAP07", "SBRT", "SMART", "MR-guided adaptive",
        "NRG GI-011", "LAP100", "BRCA", "PALB2", "ATM", "STK11",
        "anal cancer", "anal canal", "anal margin", "HPV", "HIV",
        "mitomycin", "MMC", "Nigro", "Wayne State", "UK ACT I",
        "ACT I", "EORTC 22861", "ECOG 1289", "RTOG 8704",
        "UK ACT II", "ACT II", "RTOG 9811", "ACCORD 03",
        "RTOG 0529", "PLATO", "ACT III", "ACT IV", "ACT V",
        "colostomy-free survival", "salvage APR"
    ],
    "prev": ["breast.html", "乳癌", "Breast"],
    "next": ["gu.html", "泌尿", "GU"],
})

PAGES.append({
    "slug": "gu",
    "emoji": "🫘",
    "title_zh": "泌尿生殖癌",
    "title_en": "Genitourinary (non-prostate)",
    "sub_zh": "膀胱癌與睪丸精原細胞瘤的放射治療。",
    "sub_en": "Bladder cancer and testicular seminoma.",
    "sections": [
      {"label_zh":"膀胱癌","label_en":"BLADDER","h2_zh":"肌肉侵犯性膀胱癌 (MIBC)","h2_en":"Muscle-invasive bladder cancer (MIBC)",
       "body_zh":"<p><strong>Radical cystectomy</strong> 為標準；有意保留膀胱者採 <strong>trimodality therapy (TMT)</strong>：TURBT → concurrent chemoRT。</p><p><strong>BC2001:</strong> RT + 5-FU/MMC 相對 RT alone 提升 locoregional DFS。</p><p><strong>劑量:</strong> 64 Gy/32 fx 或 55 Gy/20 fx (英國標準)。</p>",
       "body_en":"<p><strong>Radical cystectomy</strong> is standard; bladder-preservation via <strong>trimodality therapy (TMT)</strong>: TURBT → concurrent chemoRT.</p><p><strong>BC2001:</strong> RT + 5-FU/MMC improves locoregional DFS vs RT alone.</p><p><strong>Dose:</strong> 64 Gy/32 fx or 55 Gy/20 fx (UK).</p>"},
      {"label_zh":"睪丸精原細胞瘤","label_en":"SEMINOMA","h2_zh":"睪丸精原細胞瘤","h2_en":"Testicular seminoma",
       "body_zh":"<p><strong>Stage I:</strong> 手術後可選 surveillance / 單次 carboplatin / RT (20 Gy para-aortic)。</p><p><strong>Stage II A/B:</strong> RT 30 Gy dog-leg (para-aortic + ipsilateral iliac) 或 3–4 週期 BEP 化療。</p>",
       "body_en":"<p><strong>Stage I:</strong> post-orchiectomy — surveillance vs single carboplatin vs RT (20 Gy para-aortic).</p><p><strong>Stage II A/B:</strong> RT 30 Gy dog-leg (para-aortic + ipsilateral iliac) or 3–4 cycles BEP.</p>"},
    ],
    "excel_sheet": "GU",
    "prev": ["gi.html", "消化道", "GI"],
    "next": ["prostate.html", "攝護腺", "Prostate"],
})

PAGES.append({
    "slug": "prostate",
    "emoji": "♂️",
    "title_zh": "攝護腺癌",
    "title_en": "Prostate Cancer",
    "sub_zh": "局限性、術後、轉移性攝護腺癌與系統性治療。",
    "sub_en": "Localized, post-prostatectomy, metastatic; systemic therapy & RT regimens.",
    "sections": [
      {"label_zh":"風險分層","label_en":"RISK","h2_zh":"NCCN 風險分層","h2_en":"NCCN risk stratification",
       "body_zh":"<ul><li><strong>Very low / Low:</strong> PSA &lt; 10, GS ≤ 6, T1c–T2a</li><li><strong>Favorable intermediate (FIR):</strong> single IR factor + &lt; 50% cores + GG 1–2</li><li><strong>Unfavorable IR (UIR):</strong> 2+ IR factors / GG 3 / &gt; 50% cores</li><li><strong>High / Very high:</strong> GS ≥ 8, PSA &gt; 20, T3a+</li></ul>",
       "body_en":"<ul><li><strong>Very low / Low:</strong> PSA &lt; 10, GS ≤ 6, T1c–T2a</li><li><strong>Favorable intermediate (FIR):</strong> single IR factor + &lt; 50% cores + GG 1–2</li><li><strong>Unfavorable IR (UIR):</strong> 2+ IR factors / GG 3 / &gt; 50% cores</li><li><strong>High / Very high:</strong> GS ≥ 8, PSA &gt; 20, T3a+</li></ul>"},
      {"label_zh":"劑量與分次","label_en":"DOSE","h2_zh":"劑量與大分次","h2_en":"Dose & hypofractionation",
       "body_zh":"<p><strong>標準:</strong> 78–80 Gy standard fractionation。</p><p><strong>Moderate hypofx:</strong> CHHiP (60 Gy/20 fx) / PROFIT (60 Gy/20 fx) — 非劣。</p><p><strong>Ultra-hypofx / SBRT:</strong> HYPO-RT-PC (42.7 Gy/7 fx)、PACE-B (36.25 Gy/5 fx) — 非劣。</p><p><strong>ADT + RT (STAMPEDE, Bolla EORTC 22961):</strong><br>· FIR：短程 ADT 4 個月<br>· UIR：ADT 4–6 個月<br>· 高風險：長程 ADT 18–36 個月</p>",
       "body_en":"<p><strong>Standard:</strong> 78–80 Gy standard fractionation.</p><p><strong>Moderate hypofractionation:</strong> CHHiP (60 Gy/20 fx) / PROFIT (60 Gy/20 fx) — non-inferior.</p><p><strong>Ultra-hypofx / SBRT:</strong> HYPO-RT-PC (42.7 Gy/7 fx); PACE-B (36.25 Gy/5 fx) — non-inferior.</p><p><strong>ADT + RT (STAMPEDE, Bolla EORTC 22961):</strong><br>· FIR: short-course ADT 4 mo<br>· UIR: ADT 4–6 mo<br>· High risk: long-course ADT 18–36 mo</p>"},
      {"label_zh":"術後 RT","label_en":"POSTOP","h2_zh":"術後放射治療","h2_en":"Post-prostatectomy RT",
       "body_zh":"<p><strong>Adjuvant vs early salvage (RADICALS-RT, GETUG-17, RAVES):</strong> 早期 salvage 與 adjuvant 相當，且副作用較少。</p><p><strong>RTOG 9601:</strong> Salvage RT + bicalutamide 2 yr 相對 RT alone 提升 OS (但主要獲益在 PSA &gt; 0.7)。</p><p><strong>SPPORT (NRG 0534):</strong> Salvage RT + short-term ADT + pelvic nodal RT 提升 fPFS。</p>",
       "body_en":"<p><strong>Adjuvant vs early salvage (RADICALS-RT, GETUG-17, RAVES):</strong> Early salvage equivalent to adjuvant with less toxicity.</p><p><strong>RTOG 9601:</strong> Salvage RT + 2-yr bicalutamide improves OS vs RT alone (benefit mainly in PSA &gt; 0.7).</p><p><strong>SPPORT (NRG 0534):</strong> Salvage RT + short-term ADT + pelvic nodal RT improves fPFS.</p>"},
    ],
    "excel_sheet": "Prostate",
    "prev": ["gu.html", "泌尿", "GU"],
    "next": ["gyn.html", "婦科", "Gyn"],
})

PAGES.append({
    "slug": "gyn",
    "emoji": "🌸",
    "title_zh": "婦科腫瘤",
    "title_en": "Gynecologic Cancers",
    "sub_zh": "子宮頸、子宮內膜、外陰癌的放射治療原則。",
    "sub_en": "Radiation for cervical, endometrial, and vulvar cancers.",
    "sections": [
      {"label_zh":"子宮頸癌","label_en":"CERVIX","h2_zh":"局部晚期子宮頸癌","h2_en":"Locally advanced cervical cancer",
       "body_zh":"<p><strong>標準治療:</strong> concurrent chemoRT (weekly cisplatin 40 mg/m² × 5–6) + 近接治療 boost。</p><p><strong>近接治療:</strong> HDR / LDR，MRI-guided IGABT (EMBRACE-I) 提升 LC 與降低毒性。</p><p><strong>目標劑量:</strong> HR-CTV D90 ≥ 85 Gy EQD2 (α/β=10)。</p><p><strong>INTERLACE:</strong> Induction chemo → chemoRT 相較 chemoRT alone 提升 PFS 與 OS。</p>",
       "body_en":"<p><strong>Standard:</strong> Concurrent chemoRT (weekly cisplatin 40 mg/m² × 5–6) + brachytherapy boost.</p><p><strong>Brachytherapy:</strong> HDR / LDR; MRI-guided IGABT (EMBRACE-I) improves LC and reduces toxicity.</p><p><strong>Target:</strong> HR-CTV D90 ≥ 85 Gy EQD2 (α/β=10).</p><p><strong>INTERLACE:</strong> Induction chemo → chemoRT improves PFS and OS vs chemoRT alone.</p>"},
      {"label_zh":"子宮內膜癌","label_en":"ENDOMETRIAL","h2_zh":"子宮內膜癌","h2_en":"Endometrial cancer",
       "body_zh":"<p><strong>PORTEC-1/2:</strong> 中風險 endometrioid 子宮內膜癌，vaginal brachytherapy (VBT) 對局部復發相當於 EBRT 且毒性較低。</p><p><strong>PORTEC-3:</strong> 高風險 endometrial (Stage III / serous / clear cell) — chemoRT vs RT alone: chemoRT 提升 OS 於 Stage III。</p><p><strong>GOG 249:</strong> 高中風險 — VBT + chemo 沒有比 pelvic RT 好。</p>",
       "body_en":"<p><strong>PORTEC-1/2:</strong> Intermediate-risk endometrioid — vaginal brachytherapy (VBT) equivalent to EBRT for local recurrence with less toxicity.</p><p><strong>PORTEC-3:</strong> High-risk endometrial (Stage III / serous / clear cell) — chemoRT vs RT alone: OS benefit in Stage III.</p><p><strong>GOG 249:</strong> High-intermediate risk — VBT + chemo not superior to pelvic RT.</p>"},
      {"label_zh":"外陰癌","label_en":"VULVAR","h2_zh":"外陰癌","h2_en":"Vulvar cancer",
       "body_zh":"<p><strong>手術為主</strong>；≥ 2 陽性淋巴結或 ECE 需輔助 RT。GOG 205 顯示 chemoRT (5-FU/cisplatin) 63.6% CR。</p>",
       "body_en":"<p><strong>Surgery-first</strong>; adjuvant RT for ≥ 2 positive nodes or ECE. GOG 205 — chemoRT (5-FU/cisplatin) yields 63.6% CR.</p>"},
    ],
    "excel_sheet": "Gyn",
    "prev": ["prostate.html", "攝護腺", "Prostate"],
    "next": ["lymphoma.html", "淋巴瘤", "Lymphoma"],
})

PAGES.append({
    "slug": "lymphoma",
    "emoji": "🩸",
    "title_zh": "淋巴瘤",
    "title_en": "Lymphoma",
    "sub_zh": "霍奇金與非霍奇金淋巴瘤的放射治療原則。",
    "sub_en": "Radiation for Hodgkin and non-Hodgkin lymphoma.",
    "sections": [
      {"label_zh":"霍奇金","label_en":"HODGKIN","h2_zh":"霍奇金淋巴瘤 (HL)","h2_en":"Hodgkin lymphoma (HL)",
       "body_zh":"<p><strong>Early stage favorable:</strong> ABVD ×2 + ISRT 20 Gy (GHSG HD10)。</p><p><strong>Early stage unfavorable:</strong> ABVD ×4 + ISRT 30 Gy (HD11)。</p><p><strong>Advanced stage:</strong> ABVD ×6 或 escalated BEACOPP；PET-adapted 已成標準 (RATHL、GHSG HD16/17)。</p><p><strong>ISRT / INRT (ILROG):</strong> 從擴大範圍 EFRT → involved-field → involved-site，降低長期毒性 (二次癌、心臟事件)。</p>",
       "body_en":"<p><strong>Early stage favorable:</strong> ABVD ×2 + ISRT 20 Gy (GHSG HD10).</p><p><strong>Early stage unfavorable:</strong> ABVD ×4 + ISRT 30 Gy (HD11).</p><p><strong>Advanced stage:</strong> ABVD ×6 or escalated BEACOPP; PET-adapted approach is standard (RATHL, GHSG HD16/17).</p><p><strong>ISRT / INRT (ILROG):</strong> Volumes reduced from EFRT → involved-field → involved-site, reducing late toxicity (SMN, cardiac events).</p>"},
      {"label_zh":"非霍奇金","label_en":"NHL","h2_zh":"非霍奇金淋巴瘤 (NHL)","h2_en":"Non-Hodgkin lymphoma (NHL)",
       "body_zh":"<p><strong>DLBCL:</strong> R-CHOP ×6 ± ISRT 30 Gy (partial response 或 bulky)；FLYER — 年輕 low-risk 4 週期 R-CHOP 就夠。</p><p><strong>Follicular:</strong> Stage I/II — ISRT 24 Gy (Lowry, Hoskin)。晚期無症狀觀察。</p><p><strong>MALT lymphoma (胃):</strong> H. pylori 根除；持續病灶 24 Gy ISRT。</p>",
       "body_en":"<p><strong>DLBCL:</strong> R-CHOP ×6 ± ISRT 30 Gy (partial response or bulky); FLYER — young low-risk: 4 cycles R-CHOP is sufficient.</p><p><strong>Follicular:</strong> Stage I/II — ISRT 24 Gy (Lowry, Hoskin). Advanced asymptomatic — watch and wait.</p><p><strong>Gastric MALT:</strong> H. pylori eradication; persistent disease — 24 Gy ISRT.</p>"},
    ],
    "excel_sheet": "Lymphoma",
    "prev": ["gyn.html", "婦科", "Gyn"],
    "next": ["sarcoma.html", "肉瘤", "Sarcoma"],
})

PAGES.append({
    "slug": "sarcoma",
    "emoji": "🦴",
    "title_zh": "軟組織肉瘤",
    "title_en": "Soft Tissue Sarcoma",
    "sub_zh": "STS 概論與關鍵證據。",
    "sub_en": "Soft tissue sarcoma overview and key evidence.",
    "sections": [
      {"label_zh":"處置","label_en":"MANAGEMENT","h2_zh":"局部處置","h2_en":"Local management",
       "body_zh":"<p><strong>肢體 STS:</strong> 廣泛切除 + RT 是保肢標準。</p><p><strong>Neoadjuvant vs adjuvant RT (O'Sullivan, Lancet 2002):</strong> Preop 50 Gy 有較多急性 wound complication；Postop 60–66 Gy 有較多長期 fibrosis/edema。</p><p><strong>VORTEX / NRG SARC (Wang):</strong> 減少 CTV margin 至 3 cm 效果相當。</p><p><strong>Retroperitoneal (STRASS):</strong> preop RT 沒有整體 abdominal recurrence 好處，但可能對 liposarcoma 亞群有幫助。</p>",
       "body_en":"<p><strong>Extremity STS:</strong> Wide excision + RT is limb-sparing standard.</p><p><strong>Neo vs adjuvant RT (O'Sullivan, Lancet 2002):</strong> Preop 50 Gy — more acute wound complications; postop 60–66 Gy — more long-term fibrosis/edema.</p><p><strong>VORTEX / NRG SARC (Wang):</strong> Reducing CTV to 3 cm gives equivalent outcomes.</p><p><strong>Retroperitoneal (STRASS):</strong> Preop RT no overall abdominal recurrence benefit, but possible benefit in liposarcoma subgroup.</p>"},
    ],
    "excel_sheet": "Sarcoma",
    "prev": ["lymphoma.html", "淋巴瘤", "Lymphoma"],
    "next": ["skin.html", "皮膚", "Skin"],
})

PAGES.append({
    "slug": "skin",
    "emoji": "🧴",
    "title_zh": "皮膚癌",
    "title_en": "Skin Cancer",
    "sub_zh": "BCC、cSCC 與黑色素瘤的放射治療原則。",
    "sub_en": "Radiation for BCC, cSCC, and melanoma.",
    "sections": [
      {"label_zh":"BCC/SCC","label_en":"BCC/SCC","h2_zh":"BCC 與 cSCC","h2_en":"BCC and cSCC",
       "body_zh":"<p><strong>手術為主</strong> (Mohs)；<strong>Definitive RT</strong> 用於手術困難位置 (眼瞼、鼻尖、耳廓) 或高齡不宜手術。</p><p><strong>術後 RT 適應:</strong> perineural invasion、切緣陽性 或 大結節性淋巴。</p><p><strong>常用劑量:</strong> 66 Gy/33 fx；elderly 55 Gy/20 fx；palliative 30 Gy/5 fx。</p>",
       "body_en":"<p><strong>Surgery-first</strong> (Mohs); <strong>definitive RT</strong> for anatomically difficult sites (eyelid, nasal tip, pinna) or elderly non-surgical candidates.</p><p><strong>Adjuvant RT:</strong> perineural invasion, positive margins, or bulky nodal disease.</p><p><strong>Common doses:</strong> 66 Gy/33 fx; elderly 55 Gy/20 fx; palliative 30 Gy/5 fx.</p>"},
      {"label_zh":"黑色素瘤","label_en":"MELANOMA","h2_zh":"黑色素瘤","h2_en":"Melanoma",
       "body_zh":"<p><strong>ANZMTG 01.02 / TROG 02.01:</strong> 高風險節區術後 RT 降低 LR (~2×) 但無 OS 好處，副作用明顯。</p><p><strong>IMRT / hypofractionation (30 Gy/5 fx 或 48 Gy/20 fx)</strong> 為常用。</p>",
       "body_en":"<p><strong>ANZMTG 01.02 / TROG 02.01:</strong> Adjuvant nodal RT halves LR but no OS benefit and meaningful toxicity.</p><p><strong>IMRT / hypofractionation (30 Gy/5 fx or 48 Gy/20 fx)</strong> commonly used.</p>"},
    ],
    "excel_sheet": "Cutaneous",
    "prev": ["sarcoma.html", "肉瘤", "Sarcoma"],
    "next": ["peds.html", "兒童", "Peds"],
})

PAGES.append({
    "slug": "peds",
    "emoji": "🧒",
    "title_zh": "兒童放射腫瘤",
    "title_en": "Pediatric Radiation Oncology",
    "sub_zh": "髓母、室管膜、Ewing、橫紋肌肉瘤、神經母、Wilms 與 CSI。",
    "sub_en": "Medulloblastoma, ependymoma, Ewing, rhabdomyosarcoma, neuroblastoma, Wilms, and CSI.",
    "sections": [
      {"label_zh":"髓母細胞瘤","label_en":"MEDULLOBLASTOMA","h2_zh":"髓母細胞瘤 (Medulloblastoma)","h2_en":"Medulloblastoma",
       "body_zh":"<p><strong>Average risk:</strong> 23.4 Gy CSI + 後顱窩 boost 至 54 Gy + 化療 (ACNS 0331 顯示不能省略 CSI 或減量 posterior fossa)。</p><p><strong>High risk:</strong> 36 Gy CSI + boost + 化療。</p><p>WNT 亞型可考慮進一步 de-escalation。</p>",
       "body_en":"<p><strong>Average risk:</strong> 23.4 Gy CSI + posterior fossa boost to 54 Gy + chemo (ACNS 0331 — cannot omit CSI or reduce PF).</p><p><strong>High risk:</strong> 36 Gy CSI + boost + chemo.</p><p>WNT subgroup — potential de-escalation ongoing.</p>"},
      {"label_zh":"室管膜瘤","label_en":"EPENDYMOMA","h2_zh":"室管膜瘤 (Ependymoma)","h2_en":"Ependymoma",
       "body_zh":"<p><strong>術後 involved-field RT 54–59.4 Gy</strong>；即使全切除也建議 (ACNS 0121, ACNS 0831)。</p>",
       "body_en":"<p><strong>Postop involved-field RT 54–59.4 Gy</strong>; recommended even after GTR (ACNS 0121, ACNS 0831).</p>"},
      {"label_zh":"Ewing 肉瘤","label_en":"EWING","h2_zh":"Ewing 肉瘤","h2_en":"Ewing sarcoma",
       "body_zh":"<p><strong>Definitive RT:</strong> 55.8 Gy (COG AEWS1031)。<br><strong>術後 R0:</strong> 觀察；<strong>R1:</strong> 50.4 Gy；<strong>R2:</strong> 55.8 Gy。</p>",
       "body_en":"<p><strong>Definitive RT:</strong> 55.8 Gy (COG AEWS1031).<br><strong>Post-op R0:</strong> observe; <strong>R1:</strong> 50.4 Gy; <strong>R2:</strong> 55.8 Gy.</p>"},
      {"label_zh":"橫紋肌肉瘤","label_en":"RHABDO","h2_zh":"橫紋肌肉瘤 (Rhabdomyosarcoma)","h2_en":"Rhabdomyosarcoma",
       "body_zh":"<p><strong>IRSG / COG:</strong> Group I embryonal (favorable): 觀察；其他組別皆需 RT。</p><p>典型劑量 36–50.4 Gy 依 group 與位置。</p>",
       "body_en":"<p><strong>IRSG / COG:</strong> Group I embryonal (favorable): observe; all others need RT.</p><p>Typical doses 36–50.4 Gy by group and site.</p>"},
      {"label_zh":"Wilms & 神經母","label_en":"WILMS/NB","h2_zh":"Wilms 與神經母細胞瘤","h2_en":"Wilms & neuroblastoma",
       "body_zh":"<p><strong>Wilms:</strong> flank RT 10.8 Gy (Stage III/IV or unfavorable histology)；whole-lung 12 Gy for pulmonary mets。</p><p><strong>Neuroblastoma:</strong> 高風險 induction chemo → surgery → 21.6 Gy → immunotherapy (dinutuximab)。</p>",
       "body_en":"<p><strong>Wilms:</strong> Flank RT 10.8 Gy (Stage III/IV or unfavorable histology); whole-lung 12 Gy for pulmonary mets.</p><p><strong>Neuroblastoma:</strong> High-risk — induction chemo → surgery → 21.6 Gy → immunotherapy (dinutuximab).</p>"},
    ],
    "excel_sheet": "Peds",
    "prev": ["skin.html", "皮膚", "Skin"],
    "next": ["palliative.html", "緩和", "Palliative"],
})

PAGES.append({
    "slug": "palliative",
    "emoji": "🕊️",
    "title_zh": "緩和放射治療",
    "title_en": "Palliative Radiation",
    "sub_zh": "骨轉移、脊髓壓迫、SVC 症候群、腫瘤出血的處置。",
    "sub_en": "Bone mets, cord compression, SVC syndrome, and tumor bleeding.",
    "sections": [
      {"label_zh":"骨轉移","label_en":"BONE METS","h2_zh":"骨轉移","h2_en":"Bone metastases",
       "body_zh":"<p><strong>單次 8 Gy vs 30 Gy/10 fx (Chow, RTOG 97-14):</strong> 疼痛控制相當；單次再照射率較高但方便。</p><p><strong>複雜/脊柱/軟組織:</strong> 30 Gy/10 fx or 20 Gy/5 fx。</p><p><strong>SBRT 為骨轉移 (RTOG 0631, SC.24/CCTG SC.24 SORCE):</strong> 脊椎 24 Gy/2 fx 相對 conventional 20 Gy/5 fx 疼痛完全緩解率更高。</p>",
       "body_en":"<p><strong>Single 8 Gy vs 30 Gy/10 fx (Chow, RTOG 97-14):</strong> Equivalent pain control; single-fx has higher retreatment rate but is convenient.</p><p><strong>Complex / spine / soft-tissue extension:</strong> 30 Gy/10 fx or 20 Gy/5 fx.</p><p><strong>Spine SBRT (RTOG 0631, SC.24):</strong> 24 Gy/2 fx improves complete pain response vs conventional 20 Gy/5 fx.</p>"},
      {"label_zh":"脊髓壓迫","label_en":"CORD","h2_zh":"惡性脊髓壓迫","h2_en":"Malignant spinal cord compression",
       "body_zh":"<p><strong>Patchell trial (Lancet 2005):</strong> 手術 + RT 相對 RT alone 顯著提升行走與存活。</p><p><strong>RT alone dose:</strong> 30 Gy/10 fx。<br><strong>Highly selected:</strong> SBRT 為 oligomets 病人的選項。</p>",
       "body_en":"<p><strong>Patchell trial (Lancet 2005):</strong> Surgery + RT significantly improves ambulation and survival vs RT alone.</p><p><strong>RT alone dose:</strong> 30 Gy/10 fx.<br><strong>Highly selected:</strong> SBRT is an option for oligomets patients.</p>"},
      {"label_zh":"SVC / 出血","label_en":"SVC / BLEED","h2_zh":"SVC 症候群與出血","h2_en":"SVC syndrome & tumor bleeding",
       "body_zh":"<p><strong>SVC:</strong> 首選<strong>血管內支架</strong>快速緩解；後續 RT 依原發癌 (SCLC → 化療優先)。</p><p><strong>Hemostatic RT:</strong> 婦科 / 泌尿 / 胸腔出血 — 20–30 Gy/5–10 fx 有效止血。</p>",
       "body_en":"<p><strong>SVC:</strong> <strong>Endovascular stenting</strong> is preferred for rapid relief; subsequent RT depends on primary (SCLC → chemo first).</p><p><strong>Hemostatic RT:</strong> Gyn / GU / thoracic bleeding — 20–30 Gy/5–10 fx effectively stops bleeding.</p>"},
    ],
    "excel_sheet": "Palliation",
    "prev": ["peds.html", "兒童", "Peds"],
    "next": None,
})
