from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_profile: dict = {}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    msg = request.message.lower()
    
    if "career" in msg:
        reply = "Career guidance kavala? Edhi field interest?"
    elif "course" in msg:
        reply = "Course kavala? Em nerchukovali?"
    elif "college" in msg:
        reply = "College info kavala? E college?"
    else:
        reply = "Hello! Nenu ela help cheyyali?"
    
    return {"reply": reply, "intent": "ok"}

@app.get("/")
def home():
    return {"status": "ok"}