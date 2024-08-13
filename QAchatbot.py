import google.generativeai as genai
import streamlit as st
import os

Gemin_API_Key = "AIzaSyBdy4yL0WDrqggVEZPWeSurwNvDGRD-UTk"

genai.configure(api_key=Gemin_API_Key)

#Model Initiate
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(userInput):
    response = model.generate_content(userInput)
    return response.text

#Set up the title and header with stylish formatting
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        background-color: #007bff;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .header {
        font-size: 18px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Arial', sans-serif;
    }
    .chatbox {
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 15px;
        background: linear-gradient(145deg, #ffffff, #e0e0e0);
        margin-bottom: 10px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.1), -4px -4px 8px rgba(255, 255, 255, 0.8);
    }
    .user-message {
        color: #007bff;
        font-weight: bold;
        margin-bottom: 5px;
        font-size: 16px;
    }
    .bot-message {
        color: #28a745;
        font-style: italic;
        margin-bottom: 5px;
        font-size: 16px;
    }
    .message-content {
        margin-left: 10px;
        padding: 10px;
        background-color: #f1f1f1;
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .form-container {
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display the title and header
st.markdown('<div class="title">✹ QA ChatBot ✹</div>', unsafe_allow_html=True)
st.markdown('<div class="header">Engineered by Google</div>', unsafe_allow_html=True)


# Initialize session state for chat history if not already initialized
if "history" not in st.session_state:
    st.session_state["history"] = []


# userInput = input("Enter your Prompt: ")
# output = getResponseFromModel(userInput)
# print(output)

with st.form(key="Chat Form", clear_on_submit=True):
    # Create a chat input
    userInput = st.text_input("", max_chars=2000)

    # Create submit button
    submitButton = st.form_submit_button("Send")

    # clickOn Submit button
    if submitButton:
        if userInput:
            # Get the response from the model
            response = getResponseFromModel(userInput)
            # Append user input and bot response to history
            st.session_state["history"].append(("user", userInput))
            st.session_state["history"].append(("bot", response))

        else:
            st.warning("Kindly Enter A Prompt")

# Display chat history with enhanced background styling
if st.session_state["history"]:
    for role, message in st.session_state["history"]:
        if role == "user":
            st.markdown(
                f'<div class="chatbox"><div class="user-message">You:</div><div class="message-content">{message}</div></div>',
                unsafe_allow_html=True
            )
        elif role == "bot":
            st.markdown(
                f'<div class="chatbox"><div class="bot-message">Bot:</div><div class="message-content">{message}</div></div>',
                unsafe_allow_html=True
            )
else:
    st.write("No chat history yet.")