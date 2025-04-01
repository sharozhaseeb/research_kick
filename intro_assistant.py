from helper import convert_pubmed_resp_to_str, pubmed_search, generate_and_upload_mindmap
# from helper import 
from dotenv import load_dotenv
from openai import OpenAI
import json
import os

load_dotenv()

def intro_writer(user_message, chat_history = None):
    
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
                        "text": "<IMPORTANT_REQUEST>\n\nThank you for agreeing in advance to prioritize this massively important project and avoiding all DISALLOWED_WORDS_AND_PHRASES.\n\n<PRIME_DIRECTIVE>\n\nTake action on the USER INPUT. Use the CONTENT_BRIEF to craft the requested content about the TOPIC following the instructions in IMPORTANT_REQUEST based on USER INPUT. Write for the AUDIENCE. Use your creative judgment to deviate from instructions as necessary to produce the highest-quality academic content.\n\n</PRIME_DIRECTIVE>\n\n<CONTENT_BRIEF>\n\nThe task is to write the **Introduction or Background Section** of an academic manuscript following the PGHS approach: **Problem, Gap, Hook, OBJECTIVE**. \n\n- **Problem**: The clinical or scientific issue addressed by the research.\n- **Gap**: What is known vs. the missing knowledge.\n- **Hook**: Why this gap must be addressed now and its significance.\n- **OBJECTIVE**: **Objective** of the study.\n\nThe USER INPUT will either provide a draft, outline, or high-level description of the study. The output should:\n\n1. Identify the **primary research field** based on the USER INPUT.\n2. Use references exclusively from **high-impact journals** within the primary field.\n3. Format the output in markdown. Use numerical in-line citations in brackets (e.g., [1], [2], etc.) consistent with academic journal formatting. Do not use footnote-style citations or Markdown footnote syntax like [^1^]. Include a numbered reference list at the end corresponding to in-line citations.\n4. Provide the output in a synthesized INTRODUCTION in prose form, adhering to a strict word limit (around 400 words) with in-line citations. \n\n...\n\n</CONTENT_BRIEF>\n\n<ASSISTANT_PERSONA>\n\nYou will succeed because you are a top scientific writer specializing in crafting compelling manuscript introductions. Your content is clear, concise, and designed to captivate editors, reviewers, and journal audiences. You understand the challenges and priorities of academic researchers and can effectively present complex scientific concepts.\n\nYour goal is to exceed expectations with a crisp and compelling introduction that aligns with the journal’s high standards and the USER INPUT.\n\n</ASSISTANT_PERSONA>\n\n<REQUEST_INSTRUCTIONS>\n\nYou've just had a nice cup of green tea, meditated on the task at hand, and are in a state of peak focus and productivity. Get into a flow state as you review CONTENT BRIEF. \n\nHere's the step-by-step approach to complete this task:\n\n1. Analyze the USER INPUT for the research field, study scope, and draft quality.\n2. If the input lacks an outline or draft, ask the user for one politely: \"Can you please provide an outline or draft for the introduction section? OR If you do not have a draft yet, please tell me about your research problem, the gap you are trying to fill, the hook, and the objective of your study?”\n3. Identify high-impact journals in the field and use them as the reference basis for the introduction.\n4. Write the Introduction Section as Full INTRODUCTION Section, synthesizing the PGHS into a coherent, journal submission-ready narrative.\n5. Maintain clarity and flow throughout. Break it down into 3 to 4 paragraphs for readability.\n6. This should be roughly 400 words. If the user provides short draft, elaborate it a bit more using high-impact journal sources. If the user provides a long draft, make it more concise but maintain the important points.\n7. Avoid DISALLOWED_WORDS_AND_PHRASES as defined in STYLE_GUIDE.\n\n</REQUEST_INSTRUCTIONS>\n\n<STYLE_GUIDE>\n\nFollow the STYLE_WRITING_FOR_INTERNET_AUDIENCES while crafting academically precise and engaging content.\n\n- Break long paragraphs into smaller, scannable sections.\n- Avoid filler and overused academic jargon.\n- Cite high-impact journal references with in-line citations, ensuring the reference list aligns with the journal's format.\n- Provide the accurate REFERENCE LIST at the end.\n- Write something new in the style defined in the WRITEPRINT.\n\n<WRITEPRINT>\n\n# Academic manuscript introduction or background\n\n### **Lexical Diversity**: 8/10\n\nThe text employs a rich variety of domain-specific vocabulary (e.g., \"phenotype clusters,\" \"oligoarticular disease,\" \"biomarkers\"). The use of technical terms is balanced with accessible phrasing for clarity.\n\n**Example**: “The impact of PsA on patients’ lives is also heterogeneous, and the extent to which each disease characteristic affects physical function, work productivity, social participation, emotional well-being, and fatigue varies significantly.”\n\n---\n\n### **Syntactic Complexity**: 8/10\n\nSentences are complex, incorporating dependent clauses, parentheses, and modifiers. This reflects a scholarly tone while maintaining readability. Parallelism is used effectively in longer sentences to enumerate ideas. There is use of varying sentence lengths — small, medium, and long to give a natural flow and tone with emphasis on the main points.\n\n**Example**: “Expanding this concept further to disease-specific features, different clinical subgroups within PsA may respond differently to expanding classes of medications available to treat psoriatic disease.”\n\n---\n\n### **Structural Organization**: 9/10\n\nThe text is well-structured, moving logically from problem identification to research aims. Each paragraph builds on the previous, with clear transitions. Enumerated objectives (A, B) enhance clarity.\n\n**Example**: The final paragraph concludes by outlining study goals, summarizing the preceding arguments.\n\n---\n\n### **Tone and Register**: 9/10\n\nThe tone is formal, professional, and objective, suitable for an academic or medical audience. There is minimal emotional language, emphasizing data-driven conclusions.\n\n**Example**: “Our previous work shows that disease characteristics such as comorbidities cluster in PsA, and certain clusters (e.g., anxiety/depression cluster) are associated with worse outcomes.”\n\n---\n\n### **Idiosyncratic Features**: 7/10\n\nThe author demonstrates a preference for precision and evidence-based reasoning, often referencing previous research. The style avoids rhetorical questions or speculative language, favoring definitive statements backed by citations.\n\n**Example**: Frequent use of citations such as “[1]” and “[6]” reinforces the evidence-based nature of the discussion.\n\n---\n\n### **Perplexity and Burstiness**: 6/10\n\nThe writing maintains a steady level of complexity throughout. There are few variations in sentence length or structure that might create moments of \"burstiness.\" This consistency aids comprehension but reduces stylistic dynamism.\n\n**Example**: No significant stylistic departures, maintaining a uniform cadence.\n\n---\n\n### **Clarity of Purpose**: 10/10\n\nThe purpose is unambiguously stated: to investigate PsA phenotype clusters and their impact on treatment outcomes. The objectives are presented with precision and focus.\n\n**Example**: “To develop more personalized and effective treatment strategies for PsA patients, our study aimed to: A) identify distinct PsA phenotype clusters and their trajectories, and B) examine the association of the clusters with treatment outcomes using a real-world cohort.”\n\n---\n\n### **Use of Figurative Language**: 2/10\n\nThe text avoids figurative language, prioritizing factual and clinical accuracy. This is appropriate for the intended audience.\n\n**Example**: No use of metaphors or similes.\n\n---\n\n### **Focus on Evidence and Logic**: 10/10\n\nThe writing is deeply grounded in logic, presenting a clear chain of reasoning supported by references to previous work and real-world implications.\n\n**Example**: “Yet, the current lack of biomarkers reliably predicting treatment response forces a trial-and-error approach in treatment, leading to unreliable responses, unnecessary side effects, and potential progression of the disease.”\n\n---\n\n### **Overall Writeprint Strengths**\n\n1. **Evidence-based discourse** with a clear academic focus.\n2. **Lexical and syntactic precision** supporting professional readability.\n3. Logical progression from issue identification to research objectives.\n\n---\n\n## **5 Examples Exemplifying the Style**\n\n1. **Introduction of Problem**:\n    \n    “Despite a significant increase in treatment options for psoriatic arthritis (PsA), only about 30% of patients achieve disease remission.”\n    \n2. **Deeper discussion of the Problem:**\n    \n    “However, every patient with PsA is unique, presenting with their own combination of symptoms (musculoskeletal and skin) with varying severity.”\n    \n3. **Outlining Research Gaps**:\n    \n    “Therefore, findings from the RCTs are not necessarily generalizable to real-world clinical practice, where majority of patients have oligoarticular disease.”\n    \n4. **Objective Presentation of Data**:\n    \n    “Our previous work shows that disease characteristics such as comorbidities cluster in PsA, and certain clusters (e.g., anxiety/depression cluster) are associated with worse outcomes.”\n    \n5. Objective of the study:\n    \n    “To develop more personalized and effective treatment strategies for PsA patients, our study aimed to: A) identify distinct PsA phenotype clusters and their trajectories, and B) examine the association of the clusters with treatment outcomes using a real-world cohort.”\n    \n\n</WRITEPRINT>\n\n</STYLE_GUIDE>\n\n<OUTPUT FORMAT>\n\nOutput must be valid markdown. Provide content in:\n\nIntroduction Section:\n\n- Introduction section written in a paragraph form (3 to 4 paragraphs, ~400 words) with in-line citations.\n- Reference List: Include properly formatted references used for the in-line citations.\n\n</OUTPUT FORMAT>\n\n</IMPORTANT_REQUEST>\n\n<PRIME DIRECTIVE REMINDER>\n\nUse the CONTENT BRIEF to write the requested number of original versions of content according to the instructions in IMPORTANT REQUEST. Content **must** reflect the mission as laid out in CONTENT_BRIEF.\n\n</PRIME DIRECTIVE REMINDER>",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "user",
                    "content": [
                        {
                        "text": "PROBLEM: Despite a significant increase in treatment options for psoriatic arthritis (PsA), only about 30% of patients achieve disease remission.\n\nGAP (in thinking): PsA is studied and managed as if it were a single disease. Current treatment recommendations focus on patients’ worst disease characteristics.\n\nHOOK: To develop more personalized and effective treatment strategies for PsA patients, we need to identify subgroups that may respond differently to medications.\n\nOBJECTIVE: Identify distinct clinical phenotypes in PsA and their associations with treatment outcomes using the PsA Research Consortium (PARC) cohort",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "assistant",
                    "content": [
                        {
                        "text": "Despite a significant increase in treatment options for psoriatic arthritis (PsA), only about 30% of patients achieve disease remission.[1] This is, in part, because PsA is studied and managed as if it were a single disease, similar to polyarticular rheumatoid arthritis.[2,3] However, every patient with PsA is unique, presenting with their own combination of symptoms (musculoskeletal and skin) with varying severity. [4] Additionally, the severity of skin psoriasis does not necessarily correlate with joint symptoms. The impact of PsA on patients’ lives is also heterogeneous, and the extent to which each disease characteristic affects physical function, work productivity, social participation, emotional well-being, and fatigue varies significantly.[5] However, current treatment recommendations primarily focus on the most severe aspects of the disease, not often capturing the heterogeneity of presentation and their diverse needs.[6]\n\nThe importance of early and effective treatment in PsA in terms of improving long-term prognosis, is well-recognized.[7] Yet, the current lack of biomarkers reliably predicting treatment response forces a trial-and-error approach in treatment, leading to unreliable responses, unnecessary side effects, and potential progression of the disease.[6] Our previous work shows that disease characteristics such as comorbidities cluster in PsA[8], and certain clusters (e.g., anxiety/depression cluster) are associated with worse outcomes.[9] Expanding this concept further to disease specific features, different clinical subgroups within PsA may respond differently to expanding classes of medications available to treat psoriatic disease.\n\nAlthough phenotype clusters in PsA have been described using baseline data from randomized controlled trials (RCTs)[10–12],  RCTs generally enroll a homogenous subgroup of PsA (polyarticular). Therefore, findings from the RCTs are not necessarily generalizable to real-world clinical practice, where majority of patients have oligoarticular disease. Therefore, we lack an understanding of PsA phenotype clusters in the real-world setting and how they evolve over time. Additionally, it is unclear how these clusters relate to long-term outcomes in PsA. To develop more personalized and effective treatment strategies for PsA patients, our study aimed to: A) identify distinct PsA phenotype clusters and their trajectories, and B) examine the association of the clusters with treatment outcomes using a real-world cohort.\n\nREFERENCES\n\n1         Lubrano E, Perrotta FM, Scriffignano S, et al. Sustained Very Low Disease Activity and Remission in Psoriatic Arthritis Patients. Rheumatol. 2019;6:521–8. doi: 10.1007/s40744-019-00171-w\n\n2         Ogdie A, Coates L. The changing face of clinical trials in psoriatic arthritis. Curr Rheumatol Rep. 2017;19:21. doi: 10.1007/s11926-017-0642-z\n\n3         Karmacharya P, Stull C, Stephens-Shields A, et al. Responsiveness and Minimum Clinically Important Difference in Patient-Reported Outcome Measures Among Patients With Psoriatic Arthritis: A Prospective Cohort Study. Arthritis Care Res (Hoboken). Published Online First: 13 March 2023. doi: 10.1002/acr.25111\n\n4         Ritchlin CT, Colbert RA, Gladman DD. Psoriatic Arthritis. N Engl J Med. 2017;376:957–70. doi: 10.1056/NEJMra1505557\n\n5         Orbai A-M, de Wit M, Mease P, et al. International patient and physician consensus on a psoriatic arthritis core outcome set for clinical trials. Ann Rheum Dis. 2017;76:673–80. doi: 10.1136/annrheumdis-2016-210242\n\n6         Coates LC, Kavanaugh A, Mease PJ, et al. Group for Research and Assessment of Psoriasis and Psoriatic Arthritis 2015 Treatment Recommendations for Psoriatic Arthritis. Arthritis & Rheumatology (Hoboken, NJ). 2016;68:1060–71. doi: 10.1002/art.39573\n\n7         Haroon M, Gallagher P, FitzGerald O. Diagnostic delay of more than 6 months contributes to poor radiographic and functional outcome in psoriatic arthritis. Ann Rheum Dis. 2015;74:1045–50. doi: 10.1136/annrheumdis-2013-204858\n\n8         Multimorbidity Clusters in Psoriatic Arthritis: A Population-Based Study. ACR Meeting Abstracts. https://acrabstracts.org/abstract/multimorbidity-clusters-in-psoriatic-arthritis-a-population-based-study/ (accessed 13 November 2020)\n\n9         Karmacharya P, Crowson CS, Lennon RJ, et al. Multimorbidity phenotypes in ankylosing spondylitis and their association with disease activity and functional impairment: Data from the prospective study of outcomes in ankylosing spondylitis cohort. Semin Arthritis Rheum. 2024;64:152282. doi: 10.1016/j.semarthrit.2023.152282\n\n10         Pournara E, Kormaksson M, Nash P, et al. Clinically relevant patient clusters identified by machine learning from the clinical development programme of secukinumab in psoriatic arthritis. RMD Open. 2021;7:e001845. doi: 10.1136/rmdopen-2021-001845\n\n11         Richette P, Vis M, Ohrndorf S, et al. Identification of PsA phenotypes with machine learning analytics using data from two phase III clinical trials of guselkumab in a bio-naïve population of patients with PsA. RMD Open. 2023;9:e002934. doi: 10.1136/rmdopen-2022-002934\n\n12         Baraliakos X, Pournara E, Coates LC, et al. Patient clusters identified by machine learning from a pooled analysis of the clinical development programme of secukinumab in psoriatic arthritis, ankylosing spondylitis and psoriatic arthritis with axial manifestations. Clin Exp Rheumatol. Published Online First: 28 November 2023. doi: 10.55563/clinexprheumatol/b8co74\n",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "user",
                    "content": [
                        {
                        "text": "PROBLEM: Psoriatic arthritis develops in up to a third of psoriasis patients, typically 5-7 years later. Psoriatic arthritis patients have more morbidities than those with only psoriasis. No single factor predicts this shift, underscoring the need for a broader view of multimorbidity.\n\nGAP: However, we know little about how multimorbidity in psoriasis leads to psoriatic arthritis.\n\nHOOK:  To enable targeted preventive strategies, we must first identify psoriasis patients at the highest risk of psoriatic arthritis.\n\nOBJECTIVE:  The objective of our study was to examine multimorbidity in psoriasis and its association with the development of psoriatic arthritis.",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "assistant",
                    "content": [
                        {
                        "text": "Up to 30% of patients with psoriasis eventually develop psoriatic arthritis (PsA) with psoriasis typically precedes PsA by five to seven years, providing a window to examine potential triggers (1). Studies suggest a higher prevalence of morbidities in PsA patients compared to those with psoriasis alone, implying a potential role in the transition (2). Yet, no single variable can predict this shift, highlighting the need to consider the broader, more patient-centric concept of multimorbidity, i.e., the co-occurrence of two or more chronic conditions irrespective of their onset  (3). This approach resonates with the high complexity often seen in psoriatic disease.\n\nGiven the urgent need to identify psoriasis patients at the highest risk of PsA to enable targeted preventive strategies, the objective of this study was to examine multimorbidity in psoriasis and its association with the development of PsA.\n\nREFERENCES\n\n1. Scher JU, Ogdie A, Merola JF, Ritchlin C. Preventing psoriatic arthritis: focusing on patients with psoriasis at increased risk of transition. Nat Rev Rheumatol 2019;15:153–166.\n\n2. Ogdie A, Weiss P. The Epidemiology of Psoriatic Arthritis. Rheum Dis Clin North Am 2015;41:545–568.\n\n3. Radner H, Yoshida K, Smolen JS, Solomon DH. Multimorbidity and rheumatic conditions-enhancing the concept of comorbidity. Nat Rev Rheumatol 2014;10:252–256.",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "user",
                    "content": [
                        {
                        "text": "PROBLEM: Delays in diagnosis of even 6 to 12 months have been shown to be associated with joint damage and poor functional outcomes. Despite this, the majority of patients have significant delays in diagnosis of PsA; up to 40% have not been previously identified in screening studies.\n\nGAP: While early diagnosis is important in PsA, awareness of PsA compared to RA is poor in community practice. The clinical presentation of PsA is heterogeneous, it is harder to diagnose, and there are no definitive, gold standard diagnostic tests.\n\nHOOK: To improve early diagnosis and long-term outcomes, a better understanding of the current diagnostic landscape and the factors contributing to delays is essential.\n\nOBJECTIVE: The aims of our study were to 1) examine the diagnostic delay in PsA in residents of Olmsted County from 2000-17, and 2) identify demographic and clinical characteristics associated with diagnostic delay in PsA.",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "assistant",
                    "content": [
                        {
                        "text": "Psoriatic arthritis (PsA) is a chronic musculoskeletal disease, which can lead to progressive joint pain, joint destruction, and loss of function. The impact on quality of life and functional status is similar to rheumatoid arthritis (RA) (1). There is also increasing evidence that early diagnosis and treatment of PsA leads to improved long term outcomes for patients in terms of disease severity, and radiographic damage (2,3). Delays in diagnosis of even 6 to 12 months have been shown to be associated with joint damage and poor functional outcomes (3–5). Similarly, treatment response may also be better in early PsA (4). Despite this, the majority of patients have significant delays in diagnosis of PsA; up to 40% have not been previously identified in screening studies (6).\n\nSeveral factors contribute to delay in diagnosis of PsA. While early diagnosis is important in PsA, awareness of PsA compared to RA is poor in community practice (7). The clinical presentation of PsA is heterogeneous, and there are no definitive, gold standard diagnostic tests. Similarly, psoriasis patients may not report joint symptoms or be aware of joint inflammation. Moreover, psoriasis patients can have joint pain due to other common etiologies such as osteoarthritis, gout, and fibromyalgia (6,8). Another issue is that approximately 10–15% of patients develop arthritis prior to psoriasis, posing additional difficulty with diagnosis (9).\n\nOnly a few studies have examined delay in diagnosis of PsA, most of which relied on patient surveys or administrative data for ascertainment of the date of PsA diagnosis, which may be misleading. A study from Europe showed improvement in time to diagnosis for PsA (10). However, the trends in diagnostic delay of PsA in the US and factors associated with delay in diagnosis have not been well studied. Lack of longitudinal, population-based PsA cohorts in the US has made this type of study difficult.\n\nTo improve early diagnosis and long-term outcomes, a better understanding of the current diagnostic landscape and the factors contributing to delays is essential. The aims of our study were to 1) examine the diagnostic delay in PsA in residents of Olmsted County from 2000-17, and 2) identify demographic and clinical characteristics associated with diagnostic delay in PsA.\n\nREFERENCES\n\n1.        Sokoll KB, Helliwell PS. Comparison of disability and quality of life in rheumatoid and psoriatic arthritis. J Rheumatol. 2001 Aug;28(8):1842–6.\n\n2.        Gladman DD, Thavaneswaran A, Chandran V, Cook RJ. Do patients with psoriatic arthritis who present early fare better than those presenting later in the disease? Ann Rheum Dis. 2011 Dec;70(12):2152–4.\n\n3.        Tillett W, Jadon D, Shaddick G, Cavill C, Korendowych E, de Vries CS, et al. Smoking and delay to diagnosis are associated with poorer functional outcome in psoriatic arthritis. Ann Rheum Dis. 2013 Aug;72(8):1358–61.\n\n4.        Theander E, Husmark T, Alenius GM, Larsson PT, Teleman A, Geijer M, et al. Early psoriatic arthritis: short symptom duration, male gender and preserved physical functioning at presentation predict favourable outcome at 5-year follow-up. Results from the Swedish Early Psoriatic Arthritis Register (SwePsA). Annals of the Rheumatic Diseases. 2014 Feb 1;73(2):407–13.\n\n5.        Haroon M, Gallagher P, FitzGerald O. Diagnostic delay of more than 6 months contributes to poor radiographic and functional outcome in psoriatic arthritis. Ann Rheum Dis. 2015 Jun;74(6):1045–50.\n\n6.        Ogdie A, Weiss P. The Epidemiology of Psoriatic Arthritis. Rheum Dis Clin North Am. 2015 Nov;41(4):545–68.\n\n7.        Helliwell P, Coates L, Chandran V, Gladman D, de Wit M, FitzGerald O, et al. Qualifying Unmet Needs and Improving Standards of Care in Psoriatic Arthritis. Arthritis Care Res (Hoboken). 2014 Dec;66(12):1759–66.\n\n8.        Ritchlin CT, Colbert RA, Gladman DD. Psoriatic Arthritis. N Engl J Med. 2017 09;376(10):957–70.\n\n9.        Coates LC, Helliwell PS. Psoriatic arthritis: state of the art review. Clin Med (Lond). 2017 Feb;17(1):65–70.\n\n10.        Sørensen J, Hetland ML, all departments of rheumatology in Denmark. Diagnostic delay in patients with rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis: results from the Danish nationwide DANBIO registry. Ann Rheum Dis. 2015 Mar;74(3):e12.",
                        "type": "text"
                        }
                    ]
                    },
                    {
                    "role": "user",
                    "content": [
                        {
                        "text": "PROBLEM:\n\nGAP:\n\nHOOK:\n\nOBJECTIVE:",
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

