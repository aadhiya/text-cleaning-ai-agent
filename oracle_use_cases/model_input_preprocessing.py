import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.cleaner import clean_text

def model_demo():
    print("🤖 Oracle Model Input Preprocessing Demo\n")

    raw_inputs = [
        "URGENT!!! Cannot access server logs since 2am. NEED HELP ASAP!!",
        "how do I reset the root password on linux?",
        "What’s the best way to backup Oracle DB?",
        "Server logs not accessible – getting 403 error!",
        "can’t ssh into staging box. tried restarting"
    ]

    print("Raw input text for model:\n")
    for text in raw_inputs:
        print(f"- {text}")
    print("\nCleaned text for training-ready input:\n")

    for i, text in enumerate(raw_inputs, 1):
        cleaned = clean_text(text)
        print(f"[Example {i}]\nRaw:    {text}\nCleaned:{cleaned}\n")

if __name__ == "__main__":
    model_demo()
