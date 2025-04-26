# agents/survey_clean_mod.py

from utils.cleaner import clean_text
import json
from pathlib import Path

STATE_FILE = Path("logs/cleaned_survey_state.json")

# Initialize the state file if it doesn’t exist
if not STATE_FILE.exists():
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"cleaned": []}))

def load_state():
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def run_agent(input_texts):
    state = load_state()
    new_cleaned = []

    for text in input_texts:
        cleaned = clean_text(text)
        if cleaned not in state["cleaned"]:
            state["cleaned"].append(cleaned)
            new_cleaned.append({"original": text, "cleaned": cleaned})

    save_state(state)
    return new_cleaned
