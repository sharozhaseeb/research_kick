from research_ideas_assistant import research_ideas_chatbot
import json

if __name__ == "__main__":
    print("--------------------------------------------")
    print("Welcome to Research Boost's Command Line Interface")
    print("--------------------------------------------")
    print("\nStarting Research Ideas Assistant...\n")
    chat_history = []

    while True:
        # get input from user
        user_message = input("User: ")
        assistant_response, chat_history = research_ideas_chatbot(user_message, chat_history)
        # print(f"Assistant: {chat_history[-1]['content']}")
        print(f"\nAssistant: {assistant_response}\n")
        print("--------------------------------------------")



