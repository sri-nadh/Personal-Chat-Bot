from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory
import uvicorn


app = FastAPI()

class RequestSchema(BaseModel):
    user_message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}")
])

llm = ChatOllama(model="llama3.1")
runnable = prompt | llm

_histories: dict[str, ChatMessageHistory] = {}
def get_history(session_id: str) -> ChatMessageHistory:
    if session_id not in _histories:
        _histories[session_id] = ChatMessageHistory()
    return _histories[session_id]

chat_with_memory = RunnableWithMessageHistory(
    runnable,
    get_session_history=get_history,
    input_messages_key="query",
    history_messages_key="history"
)

_terminated_sessions: set[str] = set() #terminated session is added to this, to check and issue session over message to the user.
SESSION_ID="session_1"

@app.post("/chat_bot")
async def chat_bot(request: RequestSchema):
    user_input = request.user_message.strip()
    
    if not user_input:
        raise HTTPException(status_code=400, detail="Empty input not allowed.")
    
    if SESSION_ID in _terminated_sessions:
        return JSONResponse(
            content={"response": "This session has ended. Please refresh or start a new session to chat again."}
        )
    
    if user_input.lower() == "bye":
        _histories.pop(SESSION_ID, None)
        _terminated_sessions.add(SESSION_ID)
        return JSONResponse(
            content={"response": "Ok bye, it was nice chatting with you. Have a good rest of the day!"}
        )
    
    response = chat_with_memory.invoke(
        input={"query": user_input},
        config={"configurable": {"session_id":SESSION_ID }}
    )
    
    return JSONResponse(content={"response": response.content})


if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=8000)



