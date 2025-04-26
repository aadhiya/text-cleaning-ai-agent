from fastapi import FastAPI
from pydantic import BaseModel
from utils.cleaner import clean_text
from llm_router.intent_router import detect_intent
from agents import clean_survery_mod  # new

app = FastAPI()

# Existing route input
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

# New toggle-based agent
class ToggleInput(BaseModel):
    agent: str
    texts: list[str]

@app.post("/toggle-agent")
async def toggle_agent(data: ToggleInput):
    if data.agent == "survey_clean_mod":
        result = clean_survery_mod.run_agent(data.texts)
        return {"agent": data.agent, "result": result}
    return {"error": "Unknown agent"}

@app.get("/")
async def root():
    return {"message": "Toggle-based and LLM-based AI endpoints are ready."}
