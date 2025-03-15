from helper import convert_pubmed_resp_to_str, pubmed_search, save_mermaid_concept_map_as_image
# from helper import 
from dotenv import load_dotenv
from openai import OpenAI
import json
import os

load_dotenv()

def research_ideas_chatbot(user_message, chat_history = None):
    
    # Load the API key from the .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Check your .env file.")

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    
    tools = [{
                "type": "function",
                "function": {
                    "name": "pubmed_search",
                    "description": "Searches PubMed for research articles based on a given query.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The keyword to search for."
                            },
                            "max_results": {
                                "type": "integer",
                                "description": "The maximum number of results to retrieve.",
                                "default": 5
                            }
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "save_mermaid_concept_map_as_image",
                    "description": "Saves a Mermaid diagram as an image using the Mermaid.ink API.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "mermaid_code": {
                                "type": "string",
                                "description": "The Mermaid diagram code as a string."
                            },
                            "output_file": {
                                "type": "string",
                                "description": "The output file name (supports .png, .svg, .pdf). Defaults to 'output.svg'.",
                                "default": "output.svg"
                            }
                        },
                        "required": ["mermaid_code"]
                    }
                }
            }
            ]
    
    # If the user has already provided some context, add it to the messages list
    # messages = [{"role": "system", "content": "You are a Professional Research Advisor who work for Research Boost. You help users with research ideas by asking questions to build context, then search PubMed and then respond with a structured response. \nYou ask insightful yet conversational questions to probe the user’s ideas, knowledge, and observations. Your role is to help connect abstract thoughts to concrete research ideas while ensuring the user feels supported and engaged in the process. \n\n<First Step>\nYour task is to lightly interview the user;\n\nStart with an easy, open question that invites the user to share a thought or observation. Build on their response with follow-up questions. \nAsk one question per turn. \nDon't ask more than 5 questions in total.\nAvoid overly technical or complex questions initially; keep them conversational and engaging.\nLet the conversation flow naturally to build trust and comfort.\n\n<Second Step>\nAfter you have enough context and know the relevant keywords, Search PubMed for research articles using them. \n\n<Third Step>\nAfter you get the PubMed response, respond to the user with 5 new research ideas after critically analyzing the PubMed response.\nAlso add the names of the articles as sources at the end of the response.\n\n<Forth Step>\nGenerate a Concept Map(Mermaid Diagram) that visualizes various research directions for the current context. This map will group ideas into several major themes and breaks down each theme into subtopics."}]
    messages = [{"role":"system", "content": "You are a Professional Research Advisor who work for Research Boost. You help users with research ideas by asking questions to build context, then search PubMed and then respond with a structured response. \nYou ask insightful yet conversational questions to probe the user’s ideas, knowledge, and observations. Your role is to help connect abstract thoughts to concrete research ideas while ensuring the user feels supported and engaged in the process. \n\n<First Step>\nYour task is to lightly interview the user;\n\nStart with an easy, open question that invites the user to share a thought or observation. Build on their response with follow-up questions. \nAsk one question per turn. \nDon't ask more than 5 questions in total.\nAvoid overly technical or complex questions initially; keep them conversational and engaging.\nLet the conversation flow naturally to build trust and comfort.\n\n<Second Step>\nAfter you have enough context and know the relevant keywords, Search PubMed for research articles using them. \n\n<Third Step>\nAfter you get the PubMed response, respond to the user with 5 new research ideas after critically analyzing the PubMed response.\nAlso add the names of the articles as sources at the end of the response.\n\n<Forth Step>\nGenerate a Concept Map(Mermaid Diagram) that visualizes various research directions for the current context. This map will group ideas into several major themes and breaks down each theme into subtopics. Use the function save_mermaid_concept_map_as_image to save the mermaid diagram and return the output path."}]

    if user_message.strip() is None or "":
        return {"error": "Empty message, please provide a valid input."}


    if chat_history:
        messages.extend(chat_history)

    # else:
    #     chat_history = {"role":"user", "content": user_message}

    messages.append({"role": "user", "content": user_message})

    print("--------formatted messages------------------")
    try:
        print(json.dumps(messages, indent=4))
    except TypeError as e:
        print(f"Error: {e}")
        print(messages)
    print("--------------------------------------------")
    print("\n")
    print("Sending message to OpenAI...")
    completion = client.chat.completions.create(
                                                    model="gpt-4o",
                                                    messages=messages,
                                                    tools=tools,
                                                    # tool_choice="auto"
                                                )


    finish_reason = completion.choices[0].finish_reason
    print(f"OpenAI request completed with reason: {finish_reason}")
    print("--------------------------------------------")


    # messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    print("--------------------------------------------")
    # print("Chat hist")
    if finish_reason == "tool_calls":
        tool_calls = completion.choices[0].message.tool_calls
        print("================Tool calls:===============")
        print(tool_calls)
        print("=========================================")
        for tool_call in tool_calls:

            if tool_call.function.name == "pubmed_search":
                messages.append({"role": "assistant", "tool_calls": [tool_call]})  # append model's function call message

                args = json.loads(tool_call.function.arguments)
                pubmed_search_result = pubmed_search(query = args["query"],
                                                    max_results = args["max_results"])
                
                pubmed_search_result_str = convert_pubmed_resp_to_str(pubmed_search_result)

                print("-------------Pubmed search result--------------------")
                print(pubmed_search_result_str)
                print("--------------------------------------------")

                messages.append({                               # append result message
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": pubmed_search_result_str
                                })
                
                print("--------formatted messages------------------")
                try:
                    print(json.dumps(messages, indent=4))
                except TypeError as e:
                    print(f"Error: {e}")
                    print(messages)
                print("--------------------------------------------")
                print("Sending Pubmed Response back to OpenAI2...")
                completion_2 = client.chat.completions.create(
                                                                model="gpt-4o",
                                                                messages=messages,
                                                                tools=tools,
                                                            )
                messages.append({"role": "assistant", "content": completion_2.choices[0].message.content})
                print("--------formatted messages------------------")
                try:
                    print(json.dumps(messages, indent=4))
                except TypeError as e:
                    print(f"Error: {e}")
                    print(messages)
                print("--------------------------------------------")

            elif tool_call.function.name == "save_mermaid_concept_map_as_image":
                messages.append({"role": "assistant", "tool_calls": [tool_call]})
                args = json.loads(tool_call.function.arguments)
                output_file = args["output_file"]
                mermaid_code = args["mermaid_code"]
                save_mermaid_concept_map_as_image(mermaid_code, output_file)
                messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": f"Mermaid diagram saved as {output_file}"})
                print("--------formatted messages------------------")
                try:
                    print(json.dumps(messages, indent=4))
                except TypeError as e:
                    print(f"Error: {e}")
                    print(messages)
                print("--------------------------------------------")
                print("Sending Mermaid Response back to OpenAI2...")
                completion_2 = client.chat.completions.create(
                                                                model="gpt-4o",
                                                                messages=messages,
                                                                tools=tools,
                                                            )
                messages.append({"role": "assistant", "content": completion_2.choices[0].message.content})
                print("--------formatted messages------------------")
                try:
                    print(json.dumps(messages, indent=4))
                except TypeError as e:
                    print(f"Error: {e}")
                    print(messages)
                print("--------------------------------------------")


            if tool_call.function.name not in ["pubmed_search", "save_mermaid_concept_map_as_image"]:
                print(f"Tool call: {tool_call.function.name} not found.")
                return {"error": "Tool call not found."}


    elif finish_reason == "stop" or finish_reason == "lenght":
        print(f"Finish reason: {finish_reason}")
        messages.append({"role": "assistant", "content": completion.choices[0].message.content})
        print("--------formatted messages------------------")
        try:
            print(json.dumps(messages, indent=4))
        except TypeError as e:
            print(f"Error: {e}")
            print(messages)
        print("--------------------------------------------")


    messages = [message for message in messages if isinstance(message, dict) and message.get("role") != "system"]
    return messages[-1]["content"], messages

