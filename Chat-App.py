from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory

# Defining prompt and ollama model
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}")
])

llm = ChatOllama(model="llama3.1")
runnable = prompt | llm


# In-memory cache for histories
_histories: dict[str, ChatMessageHistory] = {}
def get_history(session_id: str) -> ChatMessageHistory:
    if session_id not in _histories:
        _histories[session_id] = ChatMessageHistory()
    return _histories[session_id]

# Wraping runnable with memory
chat_with_memory = RunnableWithMessageHistory(
    runnable,
    get_session_history=get_history,
    input_messages_key="query",
    history_messages_key="history"
)

# Chat Logic
def start_chat(session_id: str):
    print("Type 'done' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "done":
            break
        response = chat_with_memory.invoke(
            input={"query": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        print("AI:", response.content)

if __name__ == "__main__":
    start_chat("session_1")
