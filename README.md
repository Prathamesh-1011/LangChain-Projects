# LangChain Projects – Chatbot & API Integration with Groq and Ollama

This project demonstrates how to build interactive AI-powered applications using [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/), [FastAPI](https://fastapi.tiangolo.com/), and large language models from Groq and Ollama.


## 🔧 Project Structure

```bash
LangchainProjects/
│
├── chatbot/
│   ├── app.py          # Chatbot with Groq API via Streamlit
│   └── locallama.py    # Chatbot using Ollama local LLM (e.g., Gemma3)
│
├── api/
│   ├── app.py          # FastAPI server exposing Groq and Ollama models
│   └── client.py       # Streamlit client interacting with the API
│
├── .env                # Environment variables (GROQ_API_KEY, LANGCHAIN_API_KEY)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```


## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd LangchainProjects
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the root directory with the following content:

```
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

### 4. Run Applications

#### 💬 Chatbot with Groq LLM

```bash
cd chatbot
streamlit run app.py
```

#### 💻 Chatbot with Local Ollama Model

Ensure [Ollama](https://ollama.com/) is installed and the model `gemma3:1b` is available.

```bash
ollama pull gemma3:1b
streamlit run locallama.py
```

#### 🌐 FastAPI Server (Groq + Ollama APIs)

```bash
cd api
uvicorn app:app --reload --port 9000
```

#### 🧑‍💻 Streamlit Client (Calling FastAPI)

```bash
streamlit run client.py
```

---
## 📡 LangSmith Real-Time Tracking

LangSmith is a powerful tool for **observability and debugging** in LangChain applications. It helps you:

* View your prompt chains in real time
* Inspect inputs, outputs, and intermediate steps
* Analyze performance and latency

### Enable Tracking

To enable LangSmith tracking, the following environment variables must be set:

```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Tracking is already integrated in your chatbot and API scripts using:

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
```

## 🔍 Sample LangSmith Dashboard
![LangSmith Dashboard](https://github.com/Prathamesh-1011/LangChain-Projects/blob/main/LangSmith%20Dashboard.png?raw=true)

## LangSmith RunnableSequences
![LangSmith Responses](https://github.com/Prathamesh-1011/LangChain-Projects/blob/main/Responses.png?raw=true)

## 🔌 API Endpoints

| Route       | Method | Model Used      | Description                     |
| ----------- | ------ | --------------- | ------------------------------- |
| `/anything` | POST   | Groq (LLaMA3)   | Detailed topic info (100 words) |
| `/recipe`   | POST   | Ollama (Gemma3) | Recipe generation (100 words)   |


## 📦 Sample `requirements.txt`

```
langchain
langchain-openai
langchain-community
langserve
streamlit
fastapi
uvicorn
python-dotenv
requests
```


## ✅ Features

* 🔗 LangChain integration with both Groq and Ollama LLMs
* 🧠 Multiple prompt templates
* 🧪 Streamlit frontends for easy user interaction
* 🔄 FastAPI backend for scalable API endpoints


## 📍 Notes

* You need a valid [Groq API key](https://console.groq.com/keys) to use Groq's hosted LLaMA3 models.
* Install and run [Ollama](https://ollama.com/) locally to use Gemma3 or other models.
* LangSmith tracking is optional; remove the `LANGCHAIN_TRACING_V2` line if unused.
