from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# CORS add chey - frontend nunchi call cheyyadaniki
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IMPORTANT: Model ni global ga okkasari matrame load chey
print("Loading model...")
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
print("Model loaded!")

class ChatRequest(BaseModel):
    message: str
    user_profile: dict

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    message = request.message
    candidate_labels = ["career guidance", "course recommendation", "college information"]
    
    result = classifier(message, candidate_labels)
    intent = result["labels"][0]
    
    reply = f"Based on your message, I think you need {intent}."
    
    return {"reply": reply, "intent": intent}

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running"}