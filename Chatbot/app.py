from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# LangSmith tracking (optional)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title('Langchain Demo with Groq API')
input_text = st.text_input("Search the topic you want")

# Groq Chat LLM
llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    model="llama3-8b-8192",  # You can also try "gemma-7b-it", etc.
    temperature=0.7,
    api_key=os.environ["GROQ_API_KEY"]
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
