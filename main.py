from research_ideas_assistant import research_ideas_chatbot
from interview_research_ideas_assistant import research_ideas_interview_chatbot
from intro_assistant import intro_writer
from discussion_assistant import disc_writer
from method_assistant import method_writer
from result_assistant import result_writer
import json

if __name__ == "__main__":
    print("--------------------------------------------")
    print("Welcome to Research Boost's Command Line Interface")
    print("--------------------------------------------")
    
    chat_history = []

    while True:
        # print("\nStarting Research Ideas Assistant...\n")
        # # get input from user
        # user_message = input("User: ")

        # # assistant_response, chat_history = research_ideas_chatbot(user_message, chat_history)
        # assistant_response, chat_history = research_ideas_interview_chatbot(user_message, chat_history)
        

        # # print(f"Assistant: {chat_history[-1]['content']}")
        # print(f"\nAssistant: {assistant_response}\n")
        # print("--------------------------------------------")



        #INTRO WRITER
        #-------------------------------------

        # print("\nStarting Intro writer Assistant...\n")
        # # get input from user
        # user_message = input("User: ")
        # assistant_response, chat_history = intro_writer(user_message, chat_history)
        # print(f"\nAssistant: {assistant_response}\n")
        # print(f"type of response: {type(assistant_response)}")
        # print("--------------------------------------------")


        # load response as json
        # try:
        #     response_dict = json.loads(assistant_response)
        #     print("Parsed Response (Indented):")
        #     print(json.dumps(response_dict, indent=4))
        #     print("type of response_dict: ", type(response_dict))
        # except json.JSONDecodeError:
        #     print("Response is not valid JSON.")
        # print("--------------------------------------------")




        #DISCUSSION WRITER
        #-------------------------------------

        # print("\nStarting Discussion writer Assistant...\n")
        # # get input from user
        # user_message = input("User: ")
        # assistant_response, chat_history = disc_writer(user_message, chat_history)
        # print(f"\nAssistant: {assistant_response}\n")
        # print(f"type of response: {type(assistant_response)}")
        # print("--------------------------------------------")


        # # load response as json
        # try:
        #     response_dict = json.loads(assistant_response)
        #     print("Parsed Response (Indented):")
        #     print(json.dumps(response_dict, indent=4))
        #     print("type of response_dict: ", type(response_dict))
        # except json.JSONDecodeError:
        #     print("Response is not valid JSON.")
        # print("--------------------------------------------")





        #METHOD WRITER
        #-------------------------------------
        
        # print("\nStarting Methods writer Assistant...\n")
        # # get input from user
        # user_message = input("User: ")
        # assistant_response, chat_history = method_writer(user_message, chat_history)
        # print(f"\nAssistant: {assistant_response}\n")
        # print(f"type of response: {type(assistant_response)}")
        # print("--------------------------------------------")


        # # load response as json
        # try:
        #     response_dict = json.loads(assistant_response)
        #     print("Parsed Response (Indented):")
        #     print(json.dumps(response_dict, indent=4))
        #     print("type of response_dict: ", type(response_dict))
        # except json.JSONDecodeError:
        #     print("Response is not valid JSON.")
        # print("--------------------------------------------")




        # #RESULT WRITER
        # #-------------------------------------
        
        print("\nStarting Results writer Assistant...\n")
        # get input from user
        user_message = input("User: ")
        assistant_response, chat_history = result_writer(user_message, chat_history)
        print(f"\nAssistant: {assistant_response}\n")
        print(f"type of response: {type(assistant_response)}")
        print("--------------------------------------------")

