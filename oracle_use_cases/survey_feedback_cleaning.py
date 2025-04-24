import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.cleaner import clean_text

def survey_demo():
    print("📋 Oracle Survey Feedback Cleaning Demo\n")

    raw_feedback = [
        "It’s okay, I guess. Not bad.",
        "Okay I guess. Not bad.",
        "Not bad. It's okay.",
        "Not bad at all! I’m pretty happy with the service.",
        "Pretty happy with the service. Not bad at all!",
        "I can’t say I’m satisfied…"
    ]

    print("Raw survey entries:\n")
    for feedback in raw_feedback:
        print(f"- {feedback}")
    print("\nCleaning and deduplicating...\n")

    cleaned_feedback = [clean_text(entry) for entry in raw_feedback]
    df = pd.DataFrame({"cleaned": cleaned_feedback})
    unique_cleaned = df.drop_duplicates()["cleaned"].tolist()

    for i, entry in enumerate(unique_cleaned, 1):
        print(f"[Cleaned Entry {i}] {entry}")

if __name__ == "__main__":
    survey_demo()
