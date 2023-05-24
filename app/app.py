import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import openai
openai.api_key = st.secrets['api_key']

model_name = st.secrets['model_name']

chat_history = []

st.title('trump chat')

prompt = st.text_input("Enter prompt here")
  
if st.button("Send"):
    # print("done")
    # st.text("\n".join(chat_history))
    completion = openai.Completion.create(model = model_name, prompt = f"""You are Donald Trump. {prompt}.""", max_tokens = 40, temperature=1.0)
    # print(completion.choices)
    st.empty()
    st.text(completion.choices[0].text)
