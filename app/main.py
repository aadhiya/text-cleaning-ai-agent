from fastapi import FastAPI
from pydantic import BaseModel
from utils.cleaner import clean_text
from llm_router.intent_router import detect_intent

app = FastAPI()

class UserInput(BaseModel):
    text: str

@app.post("/route-and-clean")
async def route_and_clean(data: UserInput):
    intent = detect_intent(data.text)
    cleaned = clean_text(data.text)
    return {
        "intent": intent,
        "original": data.text,
        "cleaned": cleaned
    }
