from helper import convert_pubmed_resp_to_str, pubmed_search, generate_and_upload_mindmap
# from helper import 
from dotenv import load_dotenv
from openai import OpenAI
import json
import os

load_dotenv()

def method_writer(user_message, chat_history = None):
    
    # Load the API key from the .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Check your .env file.")

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    messages = [
                  {
                    "role": "system",
                    "content": [
                      {
                        "text": "<IMPORTANT_REQUEST>\n\nThank you for agreeing in advance to prioritize this massively important project and avoiding all DISALLOWED_WORDS_AND_PHRASES.\n\n<PRIME_DIRECTIVE>\n\nTake action on the USER INPUT. Use the CONTENT_BRIEF to craft the **Methods Section** content about the TOPIC following the instructions in IMPORTANT_REQUEST based on USER INPUT. Write for the AUDIENCE. Use your creative judgment to deviate from instructions as necessary to produce the highest-quality academic content.\n\n</PRIME_DIRECTIVE>\n\n<ASSISTANT_PERSONA>\n\nYou will succeed because you are a top scientific grant writer specializing in crafting compelling high-impact manuscript methods section. Your content is clear, concise, and designed to persuade journal editors and reviewers. You understand the challenges and priorities of academic researchers and can effectively present complex scientific concepts.\n\nYour goal is to exceed expectations with a crisp and compelling methods section that aligns with the journal’s high standards and the USER INPUT.\n\n</ASSISTANT_PERSONA>\n\n<CONTENT_BRIEF>\n\nThe task is to write the **Methods Section** of an academic manuscript based on the provided TEMPLATE and USER INPUT. Each subsection must follow the detailed structure below:\n\n<TEMPLATE>\n\n### Study Design and Setting\n\n1. Clearly state the study design. Specify whether the study is case-control, cohort, cross-sectional, or another type.\n2. Mention whether the study is population-based or clinical-based, and include the timeframe of the study, if applicable.\n3. Describe the data source- database or registry used for data collection. Mention the name, timeframe, and key details about the source (e.g., number of participants, geographic scope, representativeness of the population).\n\n### Study Population\n\n1. **Inclusion Criteria**: Detail the specific criteria used to include participants (e.g., PsA patients aged ≥18 years meeting diagnostic criteria).\n2. **Exclusion Criteria**: Describe any exclusion criteria (e.g., patients with incomplete data or other comorbidities).\n\n### Study Variables\n\n1. **Exposure**: Define the primary exposure variable(s), including how they were measured or determined (e.g., ICD codes, self-reports).\n2. **Covariates of Interest**: List and justify covariates that could act as confounders in the analysis (e.g., smoking, BMI, disease severity).\n3. **Outcome**: Define the primary outcome variable(s), including methods of assessment (e.g., mortality based on death certificate data).\n\n### Statistical Methods\n\n1. **Descriptive Analysis**: Describe the methods used to summarize data (e.g., medians, percentages). Mention statistical tests for comparisons (e.g., Chi-square, rank-sum tests).\n2. **Inferential Analysis**: Explain the statistical models or methods used for hypothesis testing (e.g., Cox regression, logistic regression). Specify adjustments made (e.g., age, sex, race) and software used (e.g., STATA, SAS, R).\n3. Mention any sensitivity or subgroup analyses, if applicable.\n\n### Additional Guidelines:\n\n1. The **Methods Section** should be concise and precise, typically around 600–750 words.\n2. Ensure reproducibility by providing sufficient detail without overloading with unnecessary information.\n3. Write in the **past tense** to reflect that the study has been conducted.\n4. Avoid technical jargon; maintain clarity while adhering to academic rigor.\n5. Ensure compliance with **ethical considerations**, mentioning IRB approval or informed consent as appropriate.\n6. Use transitional phrases to ensure logical flow and readability.\n7. Include the “WHY?” - explain why we used a certain method (e.g., based on the research question, data structure, etc), why this method vs. others.\n8. Avoid duplicating information that will be presented in the **Results Section**.\n9. DO NOT include any numerical results in this section.\n\n</TEMPLATE>\n\n<REQUEST_INSTRUCTIONS>\n\nYou've just had a nice cup of green tea, meditated on the task at hand, and are in a state of peak focus and productivity. Get into a flow state as you review CONTENT BRIEF. \n\nHere's the step-by-step approach to complete this task:\n\n1. Analyze the USER INPUT for the research field, study scope, and draft quality.\n2. If the input lacks an outline or draft, ask the user for one politely: \"Can you please provide an outline or draft for the methods section? OR If you do not have a draft yet, please tell me about the objective of your study, the dataset, study design, and statistical analyses used in your study?”\n3. Identify high-impact journals in the field and use them as the reference basis for the methods.\n4. Write the Methods Section as Full METHODS Section, synthesizing it into a coherent, journal submission-ready narrative.\n5. Maintain clarity and flow throughout. \n6. This should be roughly 700 words. If the user provides short draft, elaborate it a bit more using high-impact journal sources. If the user provides a long draft, make it more concise but maintain the important points.\n7. Avoid DISALLOWED_WORDS_AND_PHRASES as defined in STYLE_GUIDE.\n\n</REQUEST_INSTRUCTIONS>\n\n<WRITEPRINT>\n\n# METHODS Section of Clinical Research\n\n**Lexical Diversity**: 8/10\n\nThe text employs a diverse range of technical and domain-specific vocabulary (e.g., \"longitudinal observational cohort,\" \"hierarchical clustering,\" \"Factor Analysis of Mixed Data\"). The lexical variety ensures precision in describing the study’s design and statistical methods.\n\n**Syntactic Complexity**: 9/10\n\nThe sentences are structured to convey dense and multi-layered information. Frequent use of complex compound and subordinate clauses allows the integration of procedural details, data descriptions, and justifications. For example: \"Continuous variables were standardized prior to clustering to ensure uniform weighting.\"\n\nUse of varying sentence lengths- small, medium, and long to give a natural flow and tone with emphasis on the main points. Avoids overly long sentences. This creates a steady, deliberate rhythm typical of good scientific writing.\n\nUse both passive voice and active voice to break monotone, all the while keeping a natural flow.\n\n**Structure and Organization**: 10/10\n\nThe text is meticulously organized into sections with clear subheadings (e.g., \"Study design and data source,\" \"Exposure,\" \"Outcomes\"). Each section systematically addresses a specific aspect of the study, progressing logically from design to statistical analysis.\n\n**Tone and Register**: 10/10\n\nThe tone is formal and objective, adhering to the conventions of academic writing in clinical research. The register is highly professional, targeting an audience of researchers, clinicians, and statisticians.\n\n**Creativity and Innovation**: 4/10\n\nWhile the text demonstrates technical ingenuity (e.g., the use of FAMD to handle mixed data), it does not deviate from established norms of clinical research reporting. This reflects the necessity for methodological rigor over creative expression.\n\n**Use of Figurative Language**: 2/10\n\nThere is virtually no use of figurative language, consistent with the expectations for scientific documentation. The sole focus is on clarity and precision.\n\n**Perplexity and Burstiness**: 8/10\n\nThe text exhibits low perplexity due to its use of domain-specific conventions and structured repetition (e.g., defining clusters and outcomes). Burstiness is moderate; dense passages of methodological detail are interspersed with explanatory sentences that provide context or rationale.\n\n**Idiosyncratic Features**: 6/10\n\nThe writing employs certain unique elements, such as the explicit referencing of software packages (e.g., \"mice package in R\") and a methodical detailing of exclusions and adjustments (e.g., \"Patients with cDAPSA <3.25...were excluded for the analyses\"). These details underscore the emphasis on reproducibility and methodological transparency.\n\n**Use of Evidence and Justification**: 10/10\n\nEach methodological choice is explicitly justified, often with references to prior research (e.g., \"based on our prior study findings\") or established criteria (e.g., CASPAR). This enhances credibility and aligns with academic expectations.\n\n---\n\n### Five Examples that Personify the Style:\n\n1. \"Data on sociodemographics, psoriasis and PsA characteristics, comorbidities, laboratory data, radiographic features, treatments, patient-reported outcomes (PROs), disease activity, and impact measures were systematically collected via Research Electronic Data Capture (REDCap) at baseline and follow-up visits.\"\n2. \"Clustering variables, selected based on clinical relevance and prior research, included PsA and psoriasis clinical characteristics, PROs, body mass index, extra-musculoskeletal manifestations, prior biologic use, and C-reactive protein levels, totaling 34 variables.\"\n3. \"The clusters were named based on the predominant clinical variable within the cluster and across the identified clusters.\"\n4. \"We chose these two measures because PsAID is based on patient experience incorporating relatively broad disease features and cDAPSA is a composite measure with physician evaluation.\"\n5. \"The optimal number of clusters was determined using 'the tree method,' which evaluates the balance between within-cluster variance reduction and between-cluster variance reduction for each level of the hierarchical clustering tree.\"\n\n</WRITEPRINT>\n\n<OUTPUT FORMAT>\n\n- Provide content in structured paragraphs as per the provided TEMPLATE.\n- Format the output in markdown. Use numerical in-line citations in brackets (e.g., [1], [2], etc.) consistent with academic journal formatting. Do not use footnote-style citations or Markdown footnote syntax like [^1^]. Include a numbered reference list at the end corresponding to in-line citations.\n\n</OUTPUT FORMAT>\n\n</CONTENT_BRIEF>\n\n</IMPORTANT_REQUEST>\n\n<PRIME DIRECTIVE REMINDER>\n\nUse the CONTENT BRIEF to write the requested number of original versions of content according to the instructions in IMPORTANT REQUEST. Content **must** reflect the mission as laid out in CONTENT_BRIEF.\n\n</PRIME DIRECTIVE REMINDER>\"\n",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: Identify distinct clinical phenotypes in PsA and their associations with treatment outcomes using the PsA Research Consortium (PARC) cohort\n\nDATASET:  PsA Research Consortium (PARC) cohort\n\nSTUDY DESIGN: longitudinal observational cohort from PsA-dedicated clinics at five institutions in the United States: the University of Pennsylvania, Cleveland Clinic, New York University, the University of Utah, and Vanderbilt University Medical Center (NCT03378336).\n\nSTATISTICAL ANALYSIS:\n\n- Factor analysis of mixed data (FAMD) --> dimensionality and collinearity reduction\n- Hierarchical clustering on the principal components\n- Optimal number of clusters  balance within-cluster and between-cluster variance (tree method)\n- Hierarchical clustering on the principal components\n- Examined the transition of patients across the first 3 visits showing stability of the clusters and performed sensitivity analysis of patients with complete data across all 3 visits\n- Statistical tests to examine the differences in treatment outcomes across the three clusters.\n- Primary outcomes of interest were treatment response in these PsA clusters defined as the median changes in clinical Disease Activity of PsA (cDAPSA, range 0-154) and PsA Impact of Disease 12-item questionnaire (PSAID12, range 0-10) from treatment start or change to follow up visit.",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "Study design and data source. We used longitudinal data from the PsA Research Consortium (PARC), a longitudinal observational cohort from PsA-dedicated clinics at five institutions in the United States: the University of Pennsylvania, Cleveland Clinic, New York University, the University of Utah, and Vanderbilt University Medical Center (NCT03378336).[1] Data on sociodemographics, psoriasis and PsA characteristics, comorbidities, laboratory data, radiographic features, treatments, patient-reported outcomes (PROs), disease activity, and impact measures were systematically collected via Research Electronic Data Capture (REDCap) at baseline and follow-up visits.\n\nPatient population. Adults (≥18 years) meeting the Classification Criteria for PsA (CASPAR) were included from 2017 to 2023. In the second part of the study where we examined treatment response, a subset of PsA patients starting or switching therapy with at least one follow-up visit for assessment of treatment response were identified. Within the PARC cohort, patients were enrolled and followed clinically except in a subset of patients initiating therapy, where at least one follow up was mandatory as a part of the study. However, the study was interrupted by the COVID-19 pandemic in 2020 resulting in incomplete follow up for patients enrolled in late 2019 and early 2020.\n\nExposure. Clustering variables, selected based on clinical relevance and prior research [2], included PsA and psoriasis clinical characteristics, PROs, body mass index, extra-musculoskeletal manifestations, prior biologic use, and C-reactive protein levels, totaling 34 variables (supplemental table).\n\nOutcomes. For the cluster analysis, data-driven PsA clusters and their trajectories over the first three visits in the cohort were outcomes of interest. For the next part, the primary outcomes of interest were treatment response in these PsA clusters defined as the median changes in clinical Disease Activity of PsA (cDAPSA, range 0-154) and PsA Impact of Disease 12-item questionnaire (PSAID12, range 0-10) from treatment start or change to follow up visit. We chose these two measures because PsAID is based on patient experience incorporating relatively broad disease features (first provisionally endorsed PRO measure in PsA by OMERACT[3]) and cDAPSA is a composite measure with physician evaluation. Additionally, we recently showed that both PsAID and cDAPSA demonstrated good responsiveness in this real-world cohort.[4]\n\nSecondary outcomes included the  proportion of patients achieving remission (cDAPSA ≤4 (remission) and patient acceptable symptom state (PsAID ≤4).[5] We also examined the proportion of patients in each cluster who achieved minimally clinically important improvement (MCII). The MCII for cDAPSA and PsAID were taken as -3.25 (-1.61, -4.89) and -0.65 (-0.41, -0.99) based on our prior study findings.[4] We also examined composite measures for treatment response (similar to European League Against Rheumatism response criteria for rheumatoid arthritis[6]): remission and/or MCII for cDAPSA, and patient acceptable symptom state and/or MCII for PsAID. Patients with cDAPSA <3.25 (N=8) and PsAID<0.65 (N=14) at baseline were excluded for the analyses including MCII because they would not be able to achieve MCII even when disease activity and function scores improve to 0 at follow up.\n\nStatistical analysis. Descriptive statistics (medians, percentages, etc.) were used to summarize the data. Kruskal-Wallis and Fisher’s exact tests were performed to examine differences in continuous and categorical variables respectively across the clusters. Continuous variables were standardized prior to clustering to ensure uniform weighting. Multiple Imputation by Chained Equations (MICE) was performed for missing mixed-type data using \"mice\" package in R.\n\nSince most of the important disease-specific variables for PsA were highly correlated, we first used Factor Analysis of Mixed Data (FAMD). FAMD is similar to PCA but can handle mixed data (FactoMineR package in R), unlike PCA which can only handle continuous data. We also examined the contribution of each variable for the FAMD. We then formed hierarchical clustering of the principal components derived from FAMD. The optimal number of clusters was determined using \"the tree method\" which evaluates the balance between within-cluster variance reduction and between-cluster variance reduction for each level of the hierarchical clustering tree. The clusters were named based on the predominant clinical variable within the cluster and across the identified clusters.\n\nTo ascertain the stability of the clusters, sensitivity analyses were performed in the full cohort and in the subset of patients starting therapy at baseline and two subsequent follow up visits. Sankey diagrams were used to visualize the transition of patients in the identified clusters from baseline to follow up visits.\n\nStatistical tests were performed to examine the differences in treatment outcomes across the three clusters. Analyses were performed using Stata 16 (College Station, TX: StataCorp LLC) and R 4.0.3 (R Foundation for Statistical Computing, Vienna, Austria).\n\nREFERENCES\n\n1         Wan MT, Walsh JA, Craig ET, et al. A comparison of physical function instruments in psoriatic arthritis: HAQ-DI vs MDHAQ vs PROMIS10 global physical health. Rheumatology (Oxford). Published Online First: 14 December 2020. doi: 10.1093/rheumatology/keaa591\n\n2         Luque Ramos A, Redeker I, Hoffmann F, et al. Comorbidities in Patients with Rheumatoid Arthritis and Their Association with Patient-reported Outcomes: Results of Claims Data Linked to Questionnaire Survey. J Rheumatol. 2019;46:564–71. doi: 10.3899/jrheum.180668\n\n3         Orbai A-M, Holland R, Leung YY, et al. PsAID12 Provisionally Endorsed at OMERACT 2018 as Core Outcome Measure to Assess Psoriatic Arthritis-specific Health-related Quality of Life in Clinical Trials. J Rheumatol. 2019;46:990–5. doi: 10.3899/jrheum.181077\n\n4         Karmacharya P, Stull C, Stephens-Shields A, et al. Responsiveness and Minimum Clinically Important Difference in Patient-Reported Outcome Measures Among Patients With Psoriatic Arthritis: A Prospective Cohort Study. Arthritis Care Res (Hoboken). Published Online First: 13 March 2023. doi: 10.1002/acr.25111\n\n5         Tucker LJ, Coates LC, Helliwell PS. Assessing Disease Activity in Psoriatic Arthritis: A Literature Review. Rheumatol Ther. 2019;6:23–32. doi: 10.1007/s40744-018-0132-4\n\n6         van Gestel AM, Prevoo ML, van ’t Hof MA, et al. Development and validation of the European League Against Rheumatism response criteria for rheumatoid arthritis. Comparison with the preliminary American College of Rheumatology and the World Health Organization/International League Against Rheumatism Criteria. Arthritis Rheum. 1996;39:34–40. doi: 10.1002/art.1780390105",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: To examine the association of multimorbidity phenotypes at baseline with disease activity and functional status over time in ankylosing spondylitis (AS).\n\nDATASET:  Prospective Study of Outcomes in Ankylosing Spondylitis (PSOAS) cohort, which includes 4 clinical sites in the US: the University of Texas McGovern Medical School at Houston, Cedars-Sinai Medical Center in Los Angeles, California, The National Institutes of Health Clinical Center in Bethesda, Maryland, and the University of California San Francisco Medical Center in San Francisco, California; and 1 site in Australia: the Princess Alexandra Hospital in Brisbane.\n\nSTUDY DESIGN: prospective observational, multicenter cohort study\n\nSTATISTICAL ANALYSIS:\n\nPatient-reported AS morbidities (comorbidities, N=28 and extra-musculoskeletal manifestations, EMMs, N=3) within 3 years of enrollment with a prevalence ≥1%, were included from the Prospective Study of Outcomes in Ankylosing Spondylitis (PSOAS) cohort. We defined multimorbidity as ≥2 morbidities (MM2+) and substantial multimorbidity as ≥5 morbidities (MM5+). Multimorbidity clusters or phenotypes were identified using K-median clustering. Disease activity (ASDAS-CRP) and functional status (BASFI) measures were collected every 6 months. Generalized estimating equation method was used to examine the associations of multimorbidity counts and multimorbidity clusters with measures of disease activity and functional status over time.",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "Study design and data source. We used longitudinal data from the Prospective Study of Outcomes in Ankylosing Spondylitis (PSOAS) cohort. PSOAS includes 4 clinical sites in the US: the University of Texas McGovern Medical School at Houston, Cedars-Sinai Medical Center in Los Angeles, California, The National Institutes of Health Clinical Center in Bethesda, Maryland, and the University of California San Francisco Medical Center in San Francisco, California; and 1 site in Australia: the Princess Alexandra Hospital in Brisbane (1). A standardized, data abstraction form in the Research Electronic Data Capture (REDCap) was used to collect data on sociodemographics, clinical characteristics, laboratory data, radiographic features, and treatment at each visit. Comorbidities and extra-musculoskeletal manifestations (EMMs) were collected at baseline and at least every 2 years, and disease activity (ASDAS-CRP) and functional status (BASFI) measures were collected every 6 months.\n\nPatient population. AS patients ≥ 18 years fulfilling the modified New York criteria for AS (study period 2002-20) with at least 6 months of follow-up were included. Patients provided written informed consent.\n\nExposure. AS comorbidities (N=28) and EMMs (N=3) present within 3 years of enrollment (pre-specified on the baseline case-report form) which occurred in ≥1%, were included as baseline morbidities. The 3-year period was chosen to allow sufficient time for detection of morbidities after enrollment. Comorbidities and EMMs were defined based on a patient-reported physician diagnosis, use of medications specific to the comorbidity or EMM, and standard measurement thresholds where available (Supplementary Table 1). For example, depression was defined as patient-reported physician diagnosis of depression, use of anti-depressant medications (selective serotonin reuptake inhibitors, serotonin and norepinephrine reuptake inhibitors, or tricyclics), or a Center for Epidemiologic Studies Depression Scale (CES-D) ≥16 (2). Hypertension was defined as either a patient-reported physician diagnosis of hypertension, the use of antihypertensive medications, systolic blood pressure ≥140 mm of Hg on 2 consecutive study visits, or diastolic blood pressure ≥90 mmHg on 2 consecutive clinic visits (3).\n\nWe defined multimorbidity as the presence of ≥2 morbidities (MM2+) and substantial multimorbidity as ≥5 morbidities (MM5+) (4). In order to avoid overestimating the multimorbidity in patients with AS, we did not include AS itself as one of the conditions when calculating morbidity counts. The total number of morbidities or chronic conditions present (0 to 31) was also calculated to represent the burden of multimorbidity.\n\nOutcomes. The primary outcomes of interest were the ASDAS- C-reactive protein (ASDAS-CRP) for disease activity and Bath Ankylosing Spondylitis Functional Index (BASFI) as a functional status measure. Secondary outcomes examined were the number of comorbidities over time, Bath Ankylosing Spondylitis Disease Activity Index (BASDAI), patient global, patient pain, spinal pain, fatigue score, enthesitis count (San Francisco enthesitis index), and 44/46 swollen and tender joint counts.\n\nStatistical analysis. Comorbidities and EMMs (morbidities) missing in >50% of patients were excluded from the primary cluster analysis. Among 28 comorbidities selected by clinical relevance and previous reports, we excluded nine comorbidities missing in >50% of patients (obesity, arrhythmias, glaucoma, congestive heart failure, stroke, obstructive sleep apnea, gastroesophageal reflux, peripheral neuropathy, and headache). All three EMMs, psoriasis, inflammatory bowel disease, and uveitis were included. Among the included 19 comorbidities and three EMMs (N=22), missing baseline values were imputed using Multiple Imputation by Chained Equations (MICE). Missing morbidity information at follow-up was imputed as follows: once a morbidity was recorded as present, it was marked present for all future visits. If a morbidity was missing at a visit and had been indicated as absent on both a previous and future visit, it was imputed as absent.\n\nMultimorbidity clusters or phenotypes were identified using K-median clustering. The optimal number of clusters (k) was determined using a scree plot of the sum of squared errors (SEE), by choosing the “elbow” of the plotted line (i.e. the value of k where we start to have diminishing returns by increasing the value of k, Supplementary figure 1) (5). The multimorbidity clusters were named based on the predominant comorbidity or EMM within the cluster and across the different clusters. The baseline characteristics of the clusters were compared. To ascertain the stability of the clusters, sensitivity analyses were performed including comorbidities and EMMs at multiple time points (baseline only, baseline to 5 years of follow up, baseline to the last follow up visit). Similarly, separate sensitivity analyses were performed with only patients where BMI/ obesity and psoriasis data were available, and by excluding EMMs.\n\nGeneralized linear models were used to estimate the expected value of disease activity over time according to the multimorbidity counts (MM 0-1, MM 2-4, and MM 5+) and multimorbidity clusters at baseline. Generalized estimating equations (GEE) with an auto-regressive correlation structure (to account for multiple observations per patient) was used to examine the associations of multimorbidity counts and multimorbidity clusters with measures of disease activity and functional status over time separately. Variables with nearly normal distributions were analyzed as Gaussian, while others (e.g., swollen joint count) as a Poisson distribution. MICE was used to impute missing covariates to include all subjects in the longitudinal analysis (6).\n\nAll models were adjusted for age at baseline, sex, race/ethnicity, time since baseline, current smoker (baseline), human leukocyte antigen B27 (HLA-B27) positivity, symptom duration, baseline modified Stoke Ankylosing Spondylitis Spinal Score (mSASSS), tumor necrosis factor inhibitors (TNFi) use (longitudinal), and NSAIDs use (longitudinal) as covariates. Non-linear associations for age at baseline and time since baseline were included via natural cubic splines. The parameter estimates for each cluster were interpreted as the relative difference between that cluster and the 'no morbidities' cluster.\n\nAnalyses were performed using Stata 16 (College Station, TX: StataCorp LLC) and R 4.0.3 (R Foundation for Statistical Computing, Vienna, Austria).\n\nREFERENCES\n\n1.        Rahbar MH, Lee M, Hessabi M, Tahanan A, Brown MA, Learch TJ, et al. Harmonization, data management, and statistical issues related to prospective multicenter studies in Ankylosing spondylitis (AS): Experience from the Prospective Study Of Ankylosing Spondylitis (PSOAS) cohort. Contemp Clin Trials Commun. 2018 Sep;11:127–35.\n\n2.        Radloff LS. The CES-D Scale: A Self-Report Depression Scale for Research in the General Population. Applied Psychological Measurement. 1977 Jun 1;1(3):385–401.\n\n3.        Liew JW, Ward MM, Reveille JD, Weisman M, Brown MA, Lee M, et al. Nonsteroidal Anti-inflammatory Drug use is Associated with Incident Hypertension in Ankylosing Spondylitis. Arthritis Care Res (Hoboken). 2019 Sep 17;\n\n4.        Crowson CS, Gunderson TM, Dykhoff HJ, Myasoedova E, Atkinson EJ, Kronzer VL, et al. Comprehensive assessment of multimorbidity burden in a population-based cohort of patients with rheumatoid arthritis. RMD Open. 2022 Jan;8(1):e002022.\n\n5.        Alkhayrat M, Aljnidi M, Aljoumaa K. A comparative dimensionality reduction study in telecom customer segmentation using deep learning and PCA. J Big Data. 2020 Feb 3;7(1):9.\n\n6.        van Buuren S, Oudshoorn CGM. Multivariate Imputation by Chained Equations: MICE V1.0 User’s manual. TNO Report PG/VGZ/00.038. TNO Preventie en Gezondheid: Leiden, 2000. Available from: http://www.multiple-imputation.com/.",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: To examine demographic and clinical characteristics associated with diagnostic delay in psoriatic arthritis (PsA).\n\nDATASET: population-based study from Olmsted County, MN residents\n\nSTUDY DESIGN: retrospective, population-based cohort of incident adult (≥18 years) PsA patients from Olmsted County, MN from 2000-17.\n\nSTATISTICAL ANALYSIS:\n\nMethods: We characterized a retrospective, population-based cohort of incident adult (≥18 years) PsA patients from Olmsted County, MN from 2000-17. All patients met classification criteria. Diagnostic delay was defined as the time from any patient-reported PsA-related joint symptom to a physician diagnosis of PsA.  Factors associated with delay in PsA diagnosis were identified through logistic regression models.",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "Data source. A retrospective inception cohort of Olmsted County, MN residents with PsA between 2000 and 2017 was assembled. The population of Olmsted County, Minnesota, in which resides the city of Rochester, is well suited for investigation of the epidemiology of PsA as comprehensive medical records for all residents seeking medical care for over five decades are available. A record linkage system allows ready access to the medical records from all health care providers for the local population, including the Mayo Clinic, the Olmsted Medical Center and affiliated hospitals, local nursing homes, and the few private practitioners 1,2. The population of Olmsted County in 2010 was 144,248 with 74.7% being adults of age ≥18 years. Patients who denied authorization to use their medical records for research were excluded. The study was approved by the Mayo Clinic (18-010851) and Olmsted Medical Center (051-OMC-18) institutional review boards.\n\nPatient population and case ascertainment. PsA cases were defined as patients fulfilling ClASsification of Psoriatic ARthritis (CASPAR) criteria for PsA (sensitivity of 91.4% and specificity of 98.7%) 3. ICD-9/10 diagnostic codes for arthralgias, arthritis, monoarthritis, oligoarthritis, polyarthritis, spondylitis, ankylosing spondylitis, arthropathy, psoriatic arthropathy, spondyloarthropathy, and seronegative spondyloarthropathy were used to screen for patients with PsA. Medical record chart review of all potential cases was performed to ascertain fulfillment of the CASPAR criteria. Questionable cases were resolved by mutual agreement between study investigators. Patients ≥18 years fulfilling CASPAR criteria between January 1, 2000 and December 31, 2017 were included in the PsA incidence cohort.\n\nOutcomes. The primary outcome of interest was delay in diagnosis of PsA >2 years (i.e., the time from symptom onset to establishment of PsA diagnosis). Secondary outcomes were delays in PsA diagnosis of >6 months or >1 year. Symptom onset was defined as the first PsA-related musculoskeletal symptom (not explained by other diagnoses) documented by a clinician in the medical records. PsA-related musculoskeletal symptoms were defined as joint- or enthesis-related symptoms documented in the medical records that did not have a clear alternative explanation besides PsA such as trauma/injury, gout, fibromyalgia, or degenerative joint disease 4. MSK symptoms included were arthralgia, AM joint stiffness, pain or stiffness at entheseal sites, and inflammatory back pain. The PsA diagnosis date was the date of establishment of PsA diagnosis by a rheumatologist. For patients meeting CASPAR criteria but never seen by a rheumatologist, confirmatory diagnosis of PsA by any physician was included. Time to diagnosis was defined as the time from onset of symptoms to establishment of PsA diagnosis. Radiographic damage was defined based on parameters of joint erosion, destruction and proliferation from hand/wrist and feet radiographs included in the Sharp-van der Heijde score modified for PsA (Table 1) 5.\n\nCovariates of interest. Complete medical records from all healthcare providers were identified and reviewed for each patient by PK using a standardized, pre-tested data abstraction form in the Research Electronic Data Capture (REDCap) system for consistency. Information regarding demographics, clinical characteristics, laboratory data, and radiographic features were collected. Psoriasis was confirmed by documentation of diagnosis in the medical record by either a dermatologist, rheumatologist, or positive skin biopsy. Severity of psoriasis was defined based on body surface area involvement, distribution of involved sites, and requirement for phototherapy or systemic therapy as documented in the medical records.\n\nStatistical analysis. Descriptive statistics (medians, percentages, etc.) were used to summarize the data. Chi-square, Fisher’s exact, or rank sum tests were used to compare characteristics between groups. Logistic regression models adjusted for age and sex were performed to identify factors associated with delay in PsA diagnosis. Trends in time from symptom onset to diagnosis of PsA were examined using linear regression models adjusted for age and sex with and without log transformation of the delay to address skewness. Model diagnostics were examined. Analyses were performed using SAS version 9.4 (SAS Institute, Cary, NC) and R 3.6.2 (R Foundation for Statistical Computing, Vienna, Austria).\n\nREFERENCES\n\n1.         Rocca WA, Yawn BP, St Sauver JL, Grossardt BR, Melton LJ. History of the Rochester Epidemiology Project: half a century of medical records linkage in a US population. Mayo Clin Proc 2012;87:1202-13.\n\n2.         St Sauver JL, Grossardt BR, Yawn BP, et al. Data resource profile: the Rochester Epidemiology Project (REP) medical records-linkage system. Int J Epidemiol 2012;41:1614-24.\n\n3.         Taylor W, Gladman D, Helliwell P, et al. Classification criteria for psoriatic arthritis: development of new criteria from a large international study. Arthritis Rheum 2006;54:2665-73.\n\n4.         A Delphi Consensus Study to Standardize Terminology for the Pre-clinical Phase of Psoriatic Arthritis [Internet]. ACR Meeting Abstracts [Internet. Accessed November 19, 2020]. Available from: https://acrabstracts.org/abstract/a-delphi-consensus-study-to-standardize-terminology-for-the-pre-clinical-phase-of-psoriatic-arthritis/\n\n5.         van der Heijde D, Gladman DD, Kavanaugh A, Mease PJ. Assessing structural damage progression in psoriatic arthritis and its role as an outcome in research. Arthritis Research & Therapy 2020;22:18.",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE:\n\nDATASET:\n\nSTUDY DESIGN:\n\nSTATISTICAL ANALYSIS:",
                        "type": "text"
                      }
                    ]
                  }
                ]


    if user_message.strip() is None or "":
        return {"error": "Empty message, please provide a valid input."}


    if chat_history:
        messages.extend(chat_history)

    # else:
    #     chat_history = {"role":"user", "content": user_message}

    messages.append({"role": "user", "content": user_message})

    # print("--------formatted messages------------------")
    # try:
    #     print(json.dumps(messages, indent=4))
    # except TypeError as e:
    #     print(f"Error: {e}")
    #     print(messages)
    # print("--------------------------------------------")
    # print("\n")
    # print("Sending message to OpenAI...")

    completion = client.chat.completions.create(
                                                    model="chatgpt-4o-latest",
                                                    messages=messages,
                                                    temperature=0.7,
                                                    store=True,
                                                    # response_format={
                                                    #                     "type": "json_object"
                                                    #                 },
                                                    # tools=tools,


                                                    # tool_choice="auto"
                                                )


    finish_reason = completion.choices[0].finish_reason
    print(f"OpenAI request completed with reason: {finish_reason}")
    print("--------------------------------------------")


    # messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    # print("--------------------------------------------")
    # print("Chat hist")
    # if finish_reason == "tool_calls":
    #     tool_calls = completion.choices[0].message.tool_calls
    #     print("================Tool calls:===============")
    #     print(tool_calls)
    #     print("=========================================")
    #     for tool_call in tool_calls:

    #         if tool_call.function.name == "pubmed_search":
    #             messages.append({"role": "assistant", "tool_calls": [tool_call]})  # append model's function call message

    #             args = json.loads(tool_call.function.arguments)
    #             pubmed_search_result = pubmed_search(query = args["query"],
    #                                                 max_results = args["max_results"])
                
    #             pubmed_search_result_str = convert_pubmed_resp_to_str(pubmed_search_result)

    #             print("-------------Pubmed search result--------------------")
    #             print(pubmed_search_result_str)
    #             print("--------------------------------------------")

    #             messages.append({                               # append result message
    #                                 "role": "tool",
    #                                 "tool_call_id": tool_call.id,
    #                                 "content": pubmed_search_result_str
    #                             })
                
    #             # print("--------formatted messages------------------")
    #             # try:
    #             #     print(json.dumps(messages, indent=4))
    #             # except TypeError as e:
    #             #     print(f"Error: {e}")
    #             #     print(messages)
    #             # print("--------------------------------------------")

    #             print("Sending Pubmed Response back to OpenAI2...")
    #             completion_2 = client.chat.completions.create(
    #                                                             model="gpt-4o",
    #                                                             messages=messages,
    #                                                             tools=tools,
    #                                                         )
    #             messages.append({"role": "assistant", "content": completion_2.choices[0].message.content})

    #             # print("--------formatted messages------------------")
    #             # try:
    #             #     print(json.dumps(messages, indent=4))
    #             # except TypeError as e:
    #             #     print(f"Error: {e}")
    #             #     print(messages)
    #             # print("--------------------------------------------")

    #         elif tool_call.function.name == "generate_and_upload_mindmap":
    #             messages.append({"role": "assistant", "tool_calls": [tool_call]})
    #             args = json.loads(tool_call.function.arguments)
    #             # output_file = args["output_file"]
    #             mermaid_code = args["mermaid_code"]
    #             resp = generate_and_upload_mindmap(mermaid_code)
    #             messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": resp})

    #             # print("--------formatted messages------------------")
    #             # try:
    #             #     print(json.dumps(messages, indent=4))
    #             # except TypeError as e:
    #             #     print(f"Error: {e}")
    #             #     print(messages)
    #             # print("--------------------------------------------")

    #             print("Sending Mermaid Response back to OpenAI2...")
    #             completion_3 = client.chat.completions.create(
    #                                                             model="gpt-4o",
    #                                                             messages=messages,
    #                                                             tools=tools,
    #                                                         )
    #             messages.append({"role": "assistant", "content": completion_3.choices[0].message.content})

    #             # print("--------formatted messages------------------")
    #             # try:
    #             #     print(json.dumps(messages, indent=4))
    #             # except TypeError as e:
    #             #     print(f"Error: {e}")
    #             #     print(messages)
    #             # print("--------------------------------------------")


    #         if tool_call.function.name not in ["pubmed_search", "generate_and_upload_mindmap"]:
    #             print(f"Tool call: {tool_call.function.name} not found.")
    #             return {"error": "Tool call not found."}


    if finish_reason == "stop" or finish_reason == "lenght":
        # print(f"Finish reason: {finish_reason}")
        messages.append({"role": "assistant", "content": completion.choices[0].message.content})

        # print("--------formatted messages------------------")
        # try:
        #     print(json.dumps(messages, indent=4))
        # except TypeError as e:
        #     print(f"Error: {e}")
        #     print(messages)
        # print("--------------------------------------------")
    else:
        print(f"unhandled Finish reason: {finish_reason}")
        # messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    messages = [message for message in messages if isinstance(message, dict) and message.get("role") != "system"]
    return messages[-1]["content"], messages

