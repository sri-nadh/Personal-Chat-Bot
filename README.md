# Personal ChatBot with Short-Term Memory using Ollama and LangChain

This project is a lightweight personal chatbot built using the [LangChain](https://www.langchain.com/) framework and [Ollama](https://ollama.com/) for running local LLMs. The chatbot supports short-term memory via `RunnableWithMessageHistory`, allowing it to remember the conversation context within a session.

## Features

* **Local LLM Inference**: Powered by `llama3.1` via the `ChatOllama` interface.
* **Session-Based Memory**: Remembers user interaction within a session using in-memory chat history.
* **Lightweight CLI Interface**: Interact with the chatbot directly in your terminal.

## How It Works

1. A prompt template is defined with a system message, a placeholder for chat history, and a dynamic user query.
2. `ChatOllama` serves as the backend LLM.
3. `RunnableWithMessageHistory` from LangChain wraps the pipeline to add memory support.
4. The chatbot runs in a loop and remembers messages as long as the session is active.

## Installation

Make sure you have the following installed:

* Python 3.8+
* [Ollama](https://ollama.com/download)
* Required Python libraries:

```bash
pip install langchain langchain_community
```

## Usage

1. Start the Ollama server and ensure `llama3.1` model is available:

```bash
ollama run llama3.1
```

2. Run the chatbot:

```bash
python Chat-App.py
```

3. Type your messages. Type `done` to exit the chat session.




