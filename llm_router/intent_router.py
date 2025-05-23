import subprocess

def detect_intent(prompt: str) -> str:
    system_prompt = (
        "You're an AI assistant that classifies text processing tasks. "
        "Respond with one of the following INTENTS:\n"
        "CRM_CLEANING\nSURVEY_CLEANING\nMODEL_PREPROCESSING\n\n"
        "Example 1:\nUser: I can't log in to the CRM system.\nIntent: CRM_CLEANING\n\n"
        "Example 2:\nUser: This is another test. It’s okay I guess.\nIntent: SURVEY_CLEANING\n\n"
        "Example 3:\nUser: Reset password and prepare logs for model training.\nIntent: MODEL_PREPROCESSING\n\n"
        f"User: {prompt}\nIntent:"
    )

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=system_prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = result.stdout.decode('utf-8').strip()

    if not output:
        return "UNKNOWN"

    lines = output.splitlines()
    if not lines:
        return "UNKNOWN"

    return lines[-1].strip().upper()
