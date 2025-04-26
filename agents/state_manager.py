# agents/state_manager.py

import json
from pathlib import Path

STATE_FOLDER = Path("logs")
STATE_FOLDER.mkdir(parents=True, exist_ok=True)

def load_state(filename: str) -> dict:
    path = STATE_FOLDER / filename
    if not path.exists():
        path.write_text(json.dumps({"cleaned": []}))
    with open(path, 'r') as f:
        return json.load(f)

def save_state(filename: str, state: dict):
    path = STATE_FOLDER / filename
    with open(path, 'w') as f:
        json.dump(state, f, indent=2)

def add_cleaned_entry(filename: str, cleaned_text: str):
    state = load_state(filename)
    if cleaned_text not in state["cleaned"]:
        state["cleaned"].append(cleaned_text)
        save_state(filename, state)
