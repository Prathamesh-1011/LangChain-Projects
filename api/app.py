from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Demo Server",
    version="1.0",
    description="A simple API Server"
)

# Groq-compatible ChatOpenAI setup
model = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)

# Ollama local model
llm = Ollama(model="gemma3:1b")

prompt1 = ChatPromptTemplate.from_template("Give me detailed information of {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Give me a recipe of {topic} with 100 words")

add_routes(app, prompt1 | model, path="/anything")
add_routes(app, prompt2 | llm, path="/recipe")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)