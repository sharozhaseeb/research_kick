import gradio as gr
# from helper import convert_pubmed_resp_to_str, pubmed_search
from dotenv import load_dotenv
from openai import OpenAI
import json
import os
from research_ideas_assistant import research_ideas_chatbot

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Check your .env file.")
client = OpenAI(api_key=api_key)

# Wrapper function for Gradio
def gradio_chatbot(user_input, chat_history=[]):
    """
    Gradio-compatible chatbot wrapper.
    
    Parameters:
        user_input (str): User's message input.
        chat_history (list): Gradio's conversation history [(user, bot), ...].
    
    Returns:
        list: Updated chat history in [(user, bot), ...] format.
        str: Empty string to clear input field.
    """
    
    # Convert Gradio history to OpenAI API format
    formatted_history = []
    for i, msg in enumerate(chat_history):
        if i % 2 == 0:  # User message
            formatted_history.append({"role": "user", "content": msg[0]})
        else:  # Assistant message
            formatted_history.append({"role": "assistant", "content": msg[1]})

    # Call your chatbot function
    try:
        response, updated_history = research_ideas_chatbot(user_input, formatted_history)
    except Exception as e:
        return chat_history + [(user_input, f"Error: {str(e)}")], ""

    # Convert OpenAI API response back to Gradio format
    chat_history.append((user_input, response))
    
    return chat_history, ""

# Create the Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 💡 Research Ideas Chatbot")
    chatbot_ui = gr.Chatbot()
    msg = gr.Textbox(label="Ask your research question:")
    clear = gr.Button("Clear")

    msg.submit(gradio_chatbot, [msg, chatbot_ui], [chatbot_ui, msg])
    clear.click(lambda: ([], ""), [], [chatbot_ui, msg])

demo.launch()


#####3-------------------------
# import gradio as gr
# import openai
# import os

# # Initialize OpenAI client
# client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Ensure your API key is set

# # Chatbot function
# def chatbot(user_input, history):
#     # Convert Gradio history format [(user, bot), ...] → OpenAI API format [{"role": "user", "content": ...}, ...]
#     messages = [{"role": "user", "content": msg[0]} if i % 2 == 0 else {"role": "assistant", "content": msg[1]}
#                 for i, msg in enumerate(history)]

#     messages.append({"role": "user", "content": user_input})

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=messages
#     )
    
#     bot_reply = response.choices[0].message.content
#     history.append((user_input, bot_reply))  # Ensure history is stored as (user, bot) tuples

#     return history, ""  # Clear input box after sending

# # Gradio UI
# with gr.Blocks() as demo:
#     chatbot_ui = gr.Chatbot()
#     msg = gr.Textbox(label="Type your message here:")
#     clear = gr.Button("Clear")

#     msg.submit(chatbot, [msg, chatbot_ui], [chatbot_ui, msg])
#     clear.click(lambda: ([], ""), [], [chatbot_ui, msg])

# demo.launch()

##################---

# import gradio as gr

# from research_ideas_assistant import research_ideas_chatbot

# with gr.Blocks() as demo:

#     chatbot = gr.Chatbot(label='Openai Chatbot', height=750)
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])
    
#     msg.submit(research_ideas_chatbot, [msg, chatbot], [msg, chatbot])

# demo.launch()



# import random
# import gradio as gr

# def random_response(message, history):
#     return random.choice(["Yes", "No"])

# demo = gr.ChatInterface(random_response, type="messages", autofocus=False)

# if __name__ == "__main__":
#     demo.launch()