# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model=genai.GenerativeModel("gemini-2.5-flash")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = model.generate_content(question,stream=True)
    return response

st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot_face:")
st.header("Gemini LLM Application")


if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
        
input=st.text_input("input:", key="input")
submit=st.button("Ask the question")
        
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("you", input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot", chunk.text))
            
st.write("Chat History:")
for role,text in st.session_state['chat_history']:
            st.write(f"{role}: {text}")
        
 