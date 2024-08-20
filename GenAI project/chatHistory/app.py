from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history and chat object if they don't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'chat' not in st.session_state:
    model = genai.GenerativeModel("gemini-pro")
    st.session_state['chat'] = model.start_chat(history=[])

# Function to get a response from the Gemini model
def get_gemini_response(question):
    chat = st.session_state['chat']  # Reference chat from session state
    response = chat.send_message(question, stream=True)
    
    # Iterate over the response and collect the chunks
    full_response = ""
    for chunk in response:
        st.write(chunk.text)  # Display each chunk as it's received
        full_response += chunk.text
    
    # Resolve the response to ensure iteration is complete
    response.resolve()

    return full_response

# Text input for the user's question
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


# Handle user input and display the response
if submit and input:
    st.subheader("Rsponse: ")
    full_response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.session_state['chat_history'].append(("Bot", full_response))
    
seeHistory = st.button("See Chat History")
if seeHistory:
    # Display the chat history
    st.subheader("The Chat History is")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
