from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    user_profile: dict

def detect_intent(message: str):
    message = message.lower()
    if "career" in message or "job" in message:
        return "career guidance"
    elif "course" in message or "learn" in message or "skill" in message:
        return "course recommendation" 
    elif "college" in message or "university" in message or "admission" in message:
        return "college information"
    else:
        return "general"

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    message = request.message
    intent = detect_intent(message)
    
    replies = {
        "career guidance": "I can help you with career guidance. What field are you interested in?",
        "course recommendation": "I can recommend courses for you. What do you want to learn?",
        "college information": "I can provide college information. Which college or course?",
        "general": "How can I help you today?"
    }
    
    return {"reply": replies[intent], "intent": intent}

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running"}