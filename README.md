# 🧠 Ollama Personal Chatbot with Short-Term Memory

A sleek, dark-themed personal AI chatbot built using **FastAPI**, **LangChain**, and **Ollama**, enhanced with short-term memory using `RunnableWithMessageHistory`. Includes a simple, responsive web UI and session handling logic that ends conversations cleanly when the user says "bye".

---

## 🔍 Features

* ✅ Chatbot powered by `llama3.1` from Ollama
* ✅ Maintains short-term context across messages using LangChain memory
* ✅ Simple frontend with a modern dark UI (HTML + CSS)
* ✅ Session termination: saying "bye" ends the chat and disables further messages
* ✅ Supports CORS and static file serving with FastAPI

---

## 🖼️ UI Preview

> Dark-mode chat layout with colored user and bot messages
> *(Insert screenshot or demo GIF here)*

---

## 🚀 Getting Started

### 1. Prerequisites

* Python 3.10+
* [Ollama](https://ollama.com) installed and running
* Required Python packages

### 2. Clone & Install

```bash
git clone https://github.com/yourusername/ollama-chatbot.git
cd ollama-chatbot
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
fastapi
uvicorn
langchain
langchain-ollama
httpx
```

### 3. Start the Server

```bash
uvicorn main:app --reload
```

### 4. Access the App

Open your browser and go to:

```
http://localhost:8000
```

---







