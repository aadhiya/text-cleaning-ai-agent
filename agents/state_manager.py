import os
import json

def load_state(state_file):
    """Load the cleaned memory state."""
    if not os.path.exists(state_file):
        # Create an empty state if missing
        with open(state_file, "w") as f:
            json.dump({"cleaned": []}, f)
        return {"cleaned": []}

    try:
        with open(state_file, "r") as f:
            state = json.load(f)
    except (json.JSONDecodeError, ValueError):
        # If file corrupted, reset it safely
        state = {"cleaned": []}
        with open(state_file, "w") as f:
            json.dump(state, f)
    return state

def save_state(state_file, state):
    """Save the memory state back."""
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)

def add_cleaned_entry(state_file, cleaned_text):
    """Add a cleaned entry if it's not already in the state."""
    state = load_state(state_file)
    if cleaned_text not in state["cleaned"]:
        state["cleaned"].append(cleaned_text)
        save_state(state_file, state)
