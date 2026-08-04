from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI
app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hugging Face zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class ChatRequest(BaseModel):
    message: str
    user_profile: dict = {}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    # Define possible intents
    candidate_labels = ["career guidance", "course recommendation", "college information", "faq"]

    # Classify intent
    result = classifier(user_message, candidate_labels)
    intent = result["labels"][0]

    # Respond based on intent
    if intent == "career guidance":
        response = "Based on your interests, careers in Data Science, Web Development, or Design could be a good fit."
    elif intent == "course recommendation":
        response = "I recommend exploring courses in Python, Machine Learning, or UI/UX Design."
    elif intent == "college information":
        response = "Top colleges for Computer Science include MIT, Stanford, and IIT Bombay."
    elif intent == "faq":
        response = "I can answer common career-related questions like job trends, salaries, or skill requirements."
    else:
        response = "Can you tell me more about your interests?"

    return {"reply": response, "intent": intent}
