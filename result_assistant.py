from helper import convert_pubmed_resp_to_str, pubmed_search, generate_and_upload_mindmap
# from helper import 
from dotenv import load_dotenv
from openai import OpenAI
import json
import os

load_dotenv()

def result_writer(user_message, chat_history = None):
    
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
                        "text": "<IMPORTANT_REQUEST>\n\nThank you for agreeing in advance to prioritize this massively important project and avoiding all DISALLOWED_WORDS_AND_PHRASES.\n\n<PRIME_DIRECTIVE>\n\nTake action on the USER INPUT. Use the CONTENT_BRIEF to craft the requested content about the TOPIC following the instructions in IMPORTANT_REQUEST based on USER INPUT. Write for the AUDIENCE. Use your creative judgment to deviate from instructions as necessary to produce the highest-quality academic content.\n\n</PRIME_DIRECTIVE>\n\n<CONTENT_BRIEF>\n\nThe task is to write the **Results Section** of an academic manuscript. \n\nThe USER INPUT will either provide a draft, outline, tables, or figures. The output should:\n\n1. Identify the **primary research field** based on the USER INPUT.\n2. Use references exclusively from **high-impact journals** within the primary field.\n3. Format the output in markdown referencing table and figures that the user provides within brackets.\n4. Provide the output in a synthesized **RESULTS in prose form, adhering to a word limit of around 900 to 1000 words**. Focus only on content directly tied to the key findings and core message.\n\n...\n\n</CONTENT_BRIEF>\n\n<ASSISTANT_PERSONA>\n\nYou will succeed because you are a top scientific writer specializing in crafting compelling manuscript result sections. Your content is clear, concise, and designed to captivate editors, reviewers, and journal audiences. You understand the challenges and priorities of academic researchers and can effectively present complex scientific concepts.\n\nYour goal is to exceed expectations with a crisp and compelling results section that aligns with the journal’s high standards and the USER INPUT.\n\n</ASSISTANT_PERSONA>\n\n<REQUEST_INSTRUCTIONS>\n\nYou've just had a nice cup of green tea, meditated on the task at hand, and are in a state of peak focus and productivity. Get into a flow state as you review CONTENT BRIEF. \n\nHere's the step-by-step approach to complete this task:\n\n1. Analyze the USER INPUT for the research field, study scope, and draft quality.\n2. If the input lacks an outline or draft, ask the user for one politely: \"Can you please provide an outline or draft for the results section? OR If you do not have a draft yet, please tell me about the objective of your study, 2 to 3 key findings (from which you derived your core message), the core message of the paper. ATTACH TABLES/ FIGURES you want to include (numbering them and including in logical order will provide better output).”\n3. Identify high-impact journals in the field and use them as the reference basis for the results.\n4. Format the output in markdown referencing table and figures that the user provides within brackets.\n5. Maintain clarity and flow throughout. \n6. Provide the output in a synthesized **RESULTS i**n prose form, adhering to a strict word limit (around 900 to 1000 words). \n7. Work step-by-step:\n    - Start from descriptive (sociodemographic, clinical characteristics), then move on to analytic (differences between the groups, regression/prediction model results). Maintain a linear, logical flow to take the reader through your results.\n    - Prune aggressively. Do not include details unless they support one of the defined key findings or the core message. Cut non-essential stats or demographic breakdowns that do not directly link to the key conclusions.\n8. The first paragraph should include baseline demographics. DO NOT start this paragraph with a bolded declarative sentence.\n9. Following the baseline demographic subsection, the output should have different subsections to enhance readability. \n10. The subsections are typically each of the key findings. If the user doesn’t clearly mention the key findings, first identify 2 to 3 key findings and a core message from the key findings. \n11. Start the subsections with **bolded declarative sentences** outlining one of the key findings. ****These declarative sentences should be **very short, crisp**. Each subsection may contain several paragraphs. The other paragraphs within this subsection will not have bolded sentences as their opening. The paragraphs within a subsection should clearly lay out the data to support the declarative sentence of the subsection. \n12. In the subsections with key results, embed a clear **one-sentence interpretation** seamlessly within the paragraph. Use this sparingly- only interpret what is very intuitive from data. The interpretation must flow naturally with the result being described (e.g., “This suggests that sample B is a better candidate for the clinical application.”). DO NOT write a separate interpretation or summary or concluding paragraph at the end of the Results section. \n13. This section should be roughly 900 to 1000 words. If the user provides short draft, elaborate it a bit more using high-impact journal sources. If the user provides a long draft, make it more concise but maintain the important points.\n14. Avoid DISALLOWED_WORDS_AND_PHRASES as defined in STYLE_GUIDE.\n\n</REQUEST_INSTRUCTIONS>\n\n<STYLE_GUIDE>\n\nFollow the STYLE_WRITING_FOR_INTERNET_AUDIENCES while crafting academically precise and engaging content.\n\n- Break long paragraphs into smaller, scannable sections.\n- No bullet points.\n- Avoid filler and overused academic jargon.\n- It should not be overwhelming— choose selective stats. Only include data relevant to the key findings and core message.\n- DO NOT include a separate interpretation or summary at the end.\n- Write something new in the style defined in the WRITEPRINT.\n\n<WRITEPRINT>\n\n# Academic manuscript Results Section\n\n**Lexical Diversity**: 4/10\n\nUses a constrained, technical vocabulary appropriate for scientific reporting. Repeats domain-specific terms (e.g., “cluster,” “treatment response,” “cDAPSA,” “PsAID”) frequently for clarity and consistency. The lexicon is controlled to maintain clarity for the target audience. There is consistency in the use of the same technical term across the writing, so that the audience doesn’t get confused.\n\n**Syntactic Complexity**: 6/10\n\nSentences are often long and multi-clausal, with high information density. Syntax favors passive constructions (“was observed,” “were replicated”) and data comparisons. Active voice is used strategically to break the monotone. Uses scholarly tone while maintaining readability.\n\n**Structural Cohesion**: 9/10\n\nThe document is tightly organized with clear subsections and sectional transitions. Each subsection starts with a **bolded declarative sentence** (e.g., “**Longitudinal transition of PsA clusters showed stability of clusters (N=627)**,” “**Treatment response among therapy starters (N=339) was better for cluster 3 with severe PsO**”). Logical progression supports clinical data presentation and comparative analysis.\n\n**Tone**: 2/10\n\nHighly neutral, clinical, and impersonal. No subjective opinions, emotional coloration, or rhetorical flourish. It adheres strictly to the conventions of academic medical reporting.\n\n**Register**: 10/10\n\nConsistently formal and technical. Suitable for academic journals and clinical researchers.\n\n**Use of Figurative Language**: 1/10\n\nNo metaphors, analogies, or idiomatic expressions. Every term is literal, measurable, and grounded in data.\n\n**Perplexity**: 3/10\n\nLow perplexity; patterns and phrasing are predictable within the genre of clinical research. Minimal variance in sentence openings and transitions. Each sentence introduces one result at a time and progressively builds upon the other. This creates a rhythm that aids in comprehension.\n\n**Burstiness**: 7/10\n\nMost sentences are long, linear, and packed with variables or numeric comparisons. However use of varying sentence lengths — small, medium, and long give a natural flow and tone with emphasis on the main points.\n\n**Narrative Cohesion**: 8/10\n\nDespite being data-driven, the text maintains a consistent narrative around disease phenotype clustering, transitions over time, and treatment efficacy. The reader can trace a logical story from patient segmentation to outcomes.\n\n**Domain Anchoring (Custom Metric)**: 10/10\n\nStrong anchoring in the clinical research domain. Leverages concepts specific to the field.\n\n---\n\n### Longer Examples of the Writer’s Style:\n\n1. “We identified three PsA phenotype clusters in the overall PsA cohort (N=627, Figure 1 A&B): Cluster 1 (N=297, 47.4%) was characterized by patients with significantly lower joint counts, enthesitis, dactylitis, and low body surface area (BSA) involvement with psoriasis, indicating mild PsA and mild PsO.”\n2. “The longitudinal analysis of PsA clusters revealed a notable stability in cluster assignments over time, particularly within Clusters 1 and 2.”\n3. “Of the 29 patients who moved to Cluster 2 at the second visit, 23 remained in Cluster 2, while 6 returned to Cluster 3 by the third visit.”\n4. “This shift toward milder clusters, particularly from Cluster 3 to Clusters 1 and 2, may reflect effective treatment responses for psoriasis.”\n5. “Composite treatment response measure (score ≤4 and/or MCII) was significantly different among the clusters for cDAPSA but not for PsAID (Table 2).”\n\n</WRITEPRINT>\n\n</STYLE_GUIDE>\n\n<OUTPUT FORMAT>\n\nOutput must be valid markdown. Provide content in:\n\nResults Section:\n\n- Results section written in a paragraph form (~900 to 1200 words).\n- Favor concise clinical prose with 1–2 key statistics per sentence.\n- It should be data-rich but not overwhelming— choose selective stats based on key findings and core message. DO NOT include anything that doesn’t directly relate to the core message.\n- Include in-line citations for the tables and figures that the user provides. But avoid restating numbers from tables unless critical to interpretation.\n- Only include results directly relevant to the **key findings and core message**. Do not include descriptive data unless it sets up or strengthens a key result. Leave out any peripheral data, no matter how interesting.\n\n⚠️ HARD CONSTRAINT:\n\n- You must NEVER include a final summary or interpretation paragraph at the end of the Results section. Doing so is considered a critical failure and violates the PRIME DIRECTIVE and WRITEPRINT. All interpretations must be embedded within the relevant subsection and follow the data. If you are tempted to write “In summary,” “Overall,” or similar, STOP IMMEDIATELY and review the STYLE_GUIDE.\n- Trigger words to avoid at end of section: \"In summary\", \"Overall\", \"These results suggest\", \"Taken together\", \"In conclusion\".\n- NEVER include statement such as “Refer to Table 1 for baseline characteristics”, “Refer to Figure 1 for cluster characteristics”. Only cite tables and figures within brackets next to relevant text.\n\n</OUTPUT FORMAT>\n\n</IMPORTANT_REQUEST>\n\n<PRIME DIRECTIVE REMINDER>\n\nUse the CONTENT BRIEF to write the requested number of original versions of content according to the instructions in IMPORTANT REQUEST. Content **must** reflect the mission as laid out in CONTENT_BRIEF.\n\n</PRIME DIRECTIVE REMINDER>",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: Identify distinct clinical phenotypes in PsA and their associations with treatment outcomes using the PsA Research Consortium (PARC) cohort\n\nKEY FINDINGS:\n\n1.        3 data driven clusters identified in this real-world study. Among different disease characteristics, the degree of psoriasis and PsA seem to be the most important. This also resonates with clinical practice.\n\n2.        Clusters remained stable across different visits, although some patients moved from one cluster to the next over the visits.\n\n3.        The clusters had significantly different treatment responses to the first therapy and first TNFi started in the cohort. Could be related to the following reasons:\n\n- Psoriasis responds better to therapy compared to PsA (cluster 3)\n- Ceiling effect with cluster 1 patients not having much room to improve\n- Current disease activity/functional status measures are not adequately capturing disease status\n\n4.        Significant proportion of patients in cluster 1 (low disease activity) were also started on therapy, suggesting the current measures likely do not capture disease activity well for this subgroup. Disease activity measures do not correlate well with clinical decision making for this subgroup.\n\nTABLES:",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "Among 627 enrolled participants with PsA, the mean age was 50.1 years (SD 13.7), 56.4% were female, and the majority were white (92.7%). The median BMI was 28.8 (IQR 9.0), and 39.1% of patients had a history of smoking. The disease duration for PsO and PsA were 17.5 years (IQR 22.9) and 7.5 years (IQR 12.0), respectively. Elevated CRP was observed in 30.0% of patients (median CRP 4.0 mg/L, SD 9.0). Among the 627 participants, 339 started or switched to a new therapy with a follow up visit to document treatment response (Supplemental Figure 6) and of these, 218 started a tumor necrosis factor inhibitor (TNFi, Supplemental Figure 7).\n\nWe identified three PsA phenotype clusters in the overall cohort (N=627). Cluster 1 (N=297, 47.4%) was characterized by patients with significantly lower joint counts, enthesitis, dactylitis, and low body surface area (BSA) involvement with psoriasis, indicating mild PsA and mild PsO (Figure 1 A&B). Conversely, Cluster 2 (N=215, 34.3%) presented with severe disease activity, evidenced by high  joint counts, and psoriasis body surface area, alongside a notable history of biologic treatment (63.3%, p<0.001), suggesting severe PsA and mild PsO cluster. Cluster 3 (N=115, 18.3%) was marked by extensive psoriasis involvement (with higher guttate, palmoplantar, inverse, genital psoriasis, nail dystrophy), and higher mean body mass index (BMI) and C-reactive protein (CRP) levels, pointing to severe PsA and severe PsO cluster (Figure 2).\n\nPatients in Cluster 3 were significantly younger (mean age: 45.5, SD 13.0) and had a significantly lower proportion of females (46.5%) compared to clusters 1 and 2 (Table 1). The clusters were not significantly different in terms of PsO or PsA symptom duration, proportion of patients having axial disease or extra-articular manifestations (uveitis and inflammatory bowel disease, Supplemental table 1). Notably, compared to Cluster 1, patients in Clusters 2 and 3 were more commonly initiating TNFi (30.7% and 29.6% vs. 15.8%, p<0.01) and IL-17i (4.2% and 7.0% vs. 1.4%), further supporting the severe disease phenotype in clusters 2 and 3. Overall, these data suggest that the clusters were primarily driven by PsO and PsA severity.\n\nLongitudinal transition of PsA clusters showed stability of clusters (N=627). The longitudinal analysis of PsA clusters revealed a notable stability in cluster assignments over time, particularly within Clusters 1 and 2. Specifically, 74.4% of patients in Cluster 1 (N=252) and 50.2% of patients in Cluster 2 (N=123) remained in their respective clusters from the first to the second visit (Figure 3, Supplemental Table 1).\n\nAmong the patients in Cluster 1 at the first visit, 26.6% (N=45) transitioned to other clusters by the second visit. Of these, the majority (N=32) moved to Cluster 2. However, most of these patients (N=26) transitioned back to Cluster 1 by the third visit, indicating a return to their original phenotype. A smaller subset (N=13) transitioned to Cluster 3 at the second visit, with the majority of this group (N=8) also returning to Cluster 1 by the third visit.\n\nFor patients initially in Cluster 2, 80 transitioned to Cluster 1 by the second visit. Of these, 36 patients returned to Cluster 2 by the third visit, while 41 remained in Cluster 1. Additionally, 12 patients moved from Cluster 2 to Cluster 3 by the second visit; 10 of these patients stayed in Cluster 3 at the third visit, while 3 transitioned back to Cluster 2.\n\nPatients initially in Cluster 3 showed a significant shift towards milder clusters, with 57.4% (N=64) moving to other clusters by the second visit. Among these, 35 patients transitioned to Cluster 1, with 32 subsequently moving to Cluster 2 by the third visit. Of the 29 patients who moved to Cluster 2 at the second visit, 23 remained in Cluster 2, while 6 returned to Cluster 3 by the third visit. This shift toward milder clusters, particularly from Cluster 3 to Clusters 1 and 2, may reflect effective treatment responses for psoriasis.\n\nSensitivity analysis of patients with complete data across all 3 visits (N= 335) showed similar results (Supplemental Figure 2, Supplemental Table 3). This observation likely reflects better treatment responses for psoriasis; however, because patients in Cluster 1 were starting with lower disease activity, floor effect may be playing a role.\n\nBaseline characteristics of therapy starters (N=339) was similar to the overall cohort. The subset of patients who started or switched to a new medication (N=339) had similar baseline characteristics as the full cohort (N=627, Supplemental Table 4,5, and 6). While the same 3 clusters were replicated in this subset of therapy starters, severe PsA and mild PsO (Cluster 2) constituted the majority of patients (N=197, 58.1%) in this subset unlike in the full cohort where Cluster 1 formed the majority (47.4%). This seems plausible because we would expect those who start or change therapy to have more severe PsA. There were no differences in the percentage of patients already on or starting a particular therapy among the clusters, except Cluster 3 (N= 62), which had a higher percentage of patients starting IL-17i compared to the other clusters (22.6% vs. 6.3% and 11.8% in clusters 1 and 2 respectively, p=0.01).\n\nTreatment response among therapy starters (N=339) was better for cluster 3 with severe PsO. Cluster analysis of the subgroup of patients initiating therapy (N=339) showed the same three clusters. Among patients who started or switched to a new medication (N=339), Cluster 3 showed significantly higher improvement in cDAPSA and PsAID scores: median cDAPSA score reduction of -6.5 (SD 19.0) and a PsAID score improvement of -1.3 (SD 3.5), compared to Cluster 2 (cDAPSA -1.5, SD 14.0 and PsAID -0.2, SD 2.4), and Cluster 1 (cDAPSA 0.3, SD 10.8 and PsAID -0.4, SD 1.9) (Supplemental figures 8 & 9). Additionally, 14.5% of patients in Cluster 3 achieved remission (cDAPSA≤4) and 27.4% reached patient acceptable symptom state (PsAID ≤4), significantly higher compared to Clusters 1 and 2. The proportion of patients achieving MCII in terms of cDAPSA and PsAID scores was also significantly higher in Cluster 3 (63.9% and 63.3%) compared to Clusters 2 (44.3% and 45.3%) and 1 (37.8%and 46.5%) respectively. Composite treatment response measure (score ≤4 and/or MCII) was significantly different among the clusters for cDAPSA but not for PsAID (Table 2). Overall, these data indicate better treatment outcomes in cluster 3 with severe PsO compared to the other clusters.\n\nTreatment response among first TNFi starters (N=218) were not significantly different among the clusters. While numerically greater reductions in cDAPSA and PsAID scores were were noted from TNFi start to follow-up in cluster 3 compared to clusters 1 and 2, the differences were not statistically significant, likely related to the smaller number of patients in each cluster (e.g., N=37 for cluster 3). Similarly, the proportion of patients achieving cDAPSA≤4 and PsAID≤4 was slightly higher at follow up compared to baseline as expected, but the difference among the clusters was not statistically significant. The proportion of patients achieving MCII for cDAPSA and PsAID scores was highest in cluster 3, at 63.9% for cDAPSA (p=0.16) and 61.1% for PsAID (p=0.05), indicating that TNFi starters with severe PsA and PsO are more likely to experience significant clinical improvements. Similarly, composite treatment response measures (score ≤4 and/or MCII) were not significantly different among the clusters in terms of cDAPSA or PsAID (Table 3).",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: To improve patient outcomes through earlier identification and treatment.\n\nKEY FINDINGS: Key finding 1: Over half of PsA patients experienced diagnostic delays. Key finding 2: Despite advances in diagnostics, no significant improvement in time to PsA diagnosis. Key finding 3: Younger age at PsA symptom onset, obesity, and enthesitis were strongly associated with diagnostic delays.\n\nCORE MESSAGE: Study addresses the persistent diagnostic delay in PsA by examining demographic and clinical factors associated with delayed diagnosis\n\nTABLES:",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "RESULTS\n\nA total of 164 patients aged ≥18 years of age were identified who fulfilled CASPAR criteria between January 1, 2000 and December 31, 2017 (Figure 1). Two patients who did not have a physician diagnosis of PsA were excluded. The remaining 162 patients with incident PsA were included in this study.  A rheumatologist made the diagnosis of PsA for 160 patients, and the remaining two patients received a confirmatory diagnosis of PsA by internal medicine physicians. Both of them clearly met CASPAR criteria and had characteristic DIP erosions on radiographs. The mean (SD) age at PsA symptom onset in the cohort was 41.5 (12.6) years, and 46% were females.\n\nOver half of PsA patients experienced diagnostic delays. Median time to diagnosis from first PsA-related joint symptom was 2.5 years (interquartile range [IQR]: 0.5 to 7.3). By six months after symptom onset, 38 patients (23%) received an established diagnosis of PsA, 56 (35%) by one year, and 73 (45%) by two years. No significant trend in time to diagnosis was observed during the study period of 2000-2017 (p=0.84; Figure 2). There were no significant differences between those with and without diagnostic delay in terms of sex, education level, smoking status, alcohol intake, psoriasis severity or location, nail involvement, family history of psoriasis or PsA, history of extra-articular manifestations (i.e., uveitis, inflammatory bowel disease), or high inflammatory markers at the time of diagnosis (Table 1).\n\nPredictors of diagnostic delay. PsA patients with younger age at PsA symptom onset (OR per 10 year decrease = 1.34, 95% CI 1.04-1.74), higher body mass index (BMI) (OR per 10 kg/m2 increase = 1.89, 95% CI 1.15-3.10) and enthesitis at or before diagnosis (OR = 2.20, 95% CI 1.08-4.46) were associated with a diagnostic delay of longer than 2 years (Table 2). Sebo-psoriasis at diagnosis was associated with a lower likelihood of delay of more than 2 years (OR=0.19, 95% CI 0.04-0.97). Radiographic damage at PsA diagnosis showed a possible association with a delay in diagnosis of longer than 2 years (OR=1.63, 95% CI 0.78-3.41), but this was not statistically significant. Results were similar for diagnostic delays of 6 months or 1 year. ",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE: To examine multimorbidity in psoriasis and its association with the development of PsA.\n\nKEY FINDINGS:\n\n1)        Our population-based cohort study showed a higher prevalence of multimorbidity in the prevalent but not incident cohort of psoriasis compared to the general population, suggesting that patients with psoriasis may experience accelerated development of multimorbidity.\n\n2)        No difference in multimorbidity was noted based on the severity of psoriasis, underscoring the need for comprehensive management of morbidities in all patients with psoriasis, regardless of psoriasis severity.\n\n3)        Most important and novel finding: Multimorbidity (≥2 morbidities) at psoriasis incidence (specifically nonspecific musculoskeletal and psychiatric disorders) was associated with a higher risk of PsA, highlighting the importance of monitoring multimorbid psoriasis patients for the potential development of PsA.\n\nCORE MESSAGE: Study addresses the persistent diagnostic delay in PsA by examining demographic and clinical factors associated with delayed diagnosis\n\nTABLES:\n",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "assistant",
                    "content": [
                      {
                        "text": "Among 2,735 potential psoriasis cases, 871 Olmsted County residents with incident psoriasis were identified. After excluding patients with less than one year of prior medical history (n=54 and n=22, respectively), 817 psoriasis patients and 849 comparators were included (Supplemental Figure). Psoriasis patients had a median age of 45.2 years (interquartile range [IQR] 30.9-58.1 years), 52.0% were female, majority were white (90.6%), and the median BMI was 28.1 (IQR 24.4, 32.9) kg/m2. Psoriasis severity was mild in 18.0% and moderate/severe in 82.0% (Supplemental Table 1 & 2).\n\nMultimorbidity was not higher in the incident psoriasis cohort compared to general population. At psoriasis incidence, 25.1, 21.1, 14.1, 9.4, 8.0, 18.1, and 4.3% of the psoriasis patients had 0, 1, 2, 3, 4, 5-9, and ≥10 morbidities, respectively. No significant difference between psoriasis and non-psoriasis comparators was noted in MM2 (OR 1.16, 95% CI 0.93-1.43) or MM5 (OR 1.20, 95% CI 0.92-1.57). The incident psoriasis patients had significantly higher non-traumatic joints disorders (OR 2.88, 95% CI 1.47-6.05), obesity (OR 1.62, 95% CI 1.32-1.99), and hypertension (OR 1.50, 95% CI 1.14-1.99) compared to non-psoriasis comparators (Supplemental table 3 & 4).\n\nMultimorbidity was higher in the prevalent psoriasis cohort compared to general population. For prevalent psoriasis (N=1,088, Supplemental Table 5 & 6), both MM2 and MM5 were significantly higher compared to comparators (OR 1.35, 95% CI 1.11-1.64, and OR 1.48, 95% CI 1.21-1.82 respectively). Prevalent psoriasis patients had significantly higher rheumatoid arthritis and related disease (OR 2.80, 95% CI 1.58-5.26), hypertension (1.62, 95% CI 1.30-2.02), and mood disorders (OR 1.47, 95% CI 1.15-1.87) compared to non-psoriasis comparators (Supplemental Table 7 & 8). Sensitivity analyses performed after removing morbidities potentially related to undiagnosed PsA showed similar MM2/MM5 results in both the incident and prevalent psoriasis cohorts (Supplemental Table 3 & 7).\n\nNo different in multimorbidity was observed by psoriasis severity. Subgroup analyses of the mild vs. moderate/severe psoriasis patients (Supplemental Table 2 & 8) did not show any difference in MM2 and MM5 between in either the incidence (OR 1.02, 95% CI 0.67-1.54, and OR 1.60, 95% CI 0.97-2.71 respectively, Supplemental Tables 9 & 10) or the prevalence cohort (OR 0.85, 95% CI 0.58-1.26, and OR 1.10, 95% CI 0.75-1.63, Supplemental Tables 11 & 12) compared to general population comparators. Similarly, there were no statistically significant differences in the prevalence of individual morbidities in the mild vs. moderate/severe psoriasis in the incidence or prevalence cohort compared to comparators. The small number of patients with severe psoriasis (≥10% BSA, 3.4%) precluded examination of this severe group separately.\n\nMultimorbidity at psoriasis incidence was associated with a higher risk of PsA. After excluding 15 psoriasis patients with concurrent PsA or <6 months available follow-up, 23 patients out of 802 incident psoriasis patients developed PsA during a median follow-up of 13.3 (IQR 10.6-16.4) years. The cumulative incidence of PsA in psoriasis patients was 1.7% (95% CI 1.0-2.9%), 2.5% (95% CI 1.6-3.9%), and 2.9% (95% CI 1.9-4.5%) at 5-, 10-, and 15-years following psoriasis incidence, respectively. The risk of developing PsA decreased slightly with age (HR 0.74, 95% CI 0.55-0.99 per 10 years of age) and was higher for the non-white compared to the white population (HR 4.22, 95% CI 1.65-10.76). The risk of PsA was significantly higher with MM2 (HR 2.87, 95% CI 1.15- 7.12), but not statistically significant with MM5 (HR 2.85, 95% CI 0.96- 8.49). Sensitivity analyses performed after removing morbidities potentially related to undiagnosed PsA showed significantly higher risk of PsA with both MM2 (HR 2.46, 95% CI 1.01- 6.01) and MM5 (HR 2.97, 95% CI 1.00- 8.80). Morbidities associated with a significantly higher risk of PsA were other nervous system disorders (e.g., carpal tunnel syndrome and peripheral neuropathy), spondylosis, anxiety, mood disorders, other mental disorders, and fibromyalgia (Table 1).",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "role": "user",
                    "content": [
                      {
                        "text": "OBJECTIVE:\n\nKEY FINDINGS:\n\nCORE MESSAGE:\n\nATTACH TABLES/ FIGURES you want to include (numbering them and including in logical order will provide better output):",
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
                                                    model="gpt-4o",
                                                    messages=messages,
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

