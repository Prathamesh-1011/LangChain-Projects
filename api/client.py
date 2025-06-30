
import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:9000/anything/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:9000/recipe/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With GEMMA3 API')
input_text=st.text_input("Ask me anything")
input_text1=st.text_input("Give me a recipe of")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
