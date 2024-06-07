import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Set up the Google Generative AI Client
api_key = os.getenv('API_KEY')
if not api_key:
    st.error("API key is missing. Please set the API key in the .env file.")
    st.stop()

# Configure the Generative AI client
genai.configure(api_key=api_key)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_bot_response(user_input):
    response = model.generate_content(user_input)  # Assuming user_input is the correct parameter
    return response.text

# Streamlit App
st.set_page_config(page_title="Simple LLM Chatbot", page_icon="🤖")

st.title("🤖 Simple LLM Chatbot")
st.write("Ask me anything!")

# Sidebar for user instructions
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    This is a simple chatbot using Google Generative AI. 
    Type your message in the input box and press Enter.
    """
)

if 'history' not in st.session_state:
    st.session_state['history'] = []

with st.form(key='chat_form'):
    user_input = st.text_input("You: ", "")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    response = get_bot_response(user_input)
    st.session_state['history'].append((user_input, response))

if st.session_state['history']:
    for chat in st.session_state['history']:
        st.write(f"**You**: {chat[0]}")
        st.write(f"**Bot**: {chat[1]}")

st.markdown("""
<style>
.stTextInput > div > div > input {
    background-color: #f0f2f6;
    color: #FF6347; /* Change this to your desired font color */
}
</style>
""", unsafe_allow_html=True)
