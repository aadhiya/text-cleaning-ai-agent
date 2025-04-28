<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.100.0-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Streamlit-1.19.0-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Ollama-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-Async-lightgrey?style=for-the-badge" />
</p>

# Oracle Text Cleaning AI Agent

## 🚀 Why Your Architecture is Modular Agent-Based

| Feature | How You Built It |
|---------|------------------|
| **Agents separated into modules** | You have different agents like `survey_clean_mod`, `crm_clean_mod` (or ready for more) each in their own file (`agents/`). |
| **Each agent handles a specific task** | Survey cleaning, CRM cleaning, etc., without overlapping. |
| **Agents can be toggled ON or OFF** | In Streamlit, user chooses which agent to activate. |
| **Central logic stays the same** | Your main FastAPI server doesn't change if you add/remove agents. |
| **New agents can be added easily** | Just drop a new file in `agents/`, register a route — done ✅. |
| **Shared utility functions** | You use `utils/cleaner.py` — multiple agents reuse same tools without duplication. |
| **Smart memory and state per agent** | Each agent maintains its own log/memory like `cleaned_survey_state.json`. |
| **Extensible** | You can add 5, 10, 20 more specialized agents without rewriting the core app. |

### 📋 In Short:

✅ You separated the "what" (agents) from the "how" (FastAPI, Streamlit UI, file uploads).  
✅ You allowed modular control by toggles and API endpoints.  
✅ You enabled scalability: add more specialized agents without touching frontend/backend logic heavily.

✅ This is exactly what companies like OpenAI, Cohere, and Anthropic talk about when they discuss Modular Agent Frameworks!

### 📢 Even More Powerful:

> “Our system uses **Modular AI Agents** designed for independent task execution, user-controlled activation, and seamless backend orchestration, fully supporting scalable enterprise workflows.”

✅ Real modular.  
✅ Real enterprise-grade.  
✅ Real investor-showcase quality.

---

## 📚 Modular Architecture Diagram (Text Version)

```
User Input (Streamlit)
        │
        ▼
FastAPI Server (/route-and-clean)
        │
        ▼
Intent Detector (Ollama LLM - classify intent)
        │
        ▼
Toggle-Based Agent Selector (Streamlit toggles: SurveyCleanMOD, CRM CleanMOD)
        │
        ├── SurveyCleanMOD Agent
        │        └── Clean survey feedback texts and update memory
        │
        ├── CRM Clean Agent (future expansion)
        │        └── Clean CRM log entries
        │
        └── Future Modular Agents
                 └── Specialized domain-specific cleaners (e.g., HR Feedback Cleaner, Bug Report Cleaner)
        
        ▼
Cleaned Output Returned
        │
        ▼
User Downloads Cleaned TXT or CSV File (Streamlit)
```

---

## 🔍 Code Overview

- **FastAPI server:** Handles text routing and calling the right modular agent.
- **Streamlit frontend:** User can upload text or CSV, choose agent toggles, and download cleaned outputs.
- **Ollama LLM:** Used to classify text intent (CRM cleaning, survey feedback, model input, etc.).
- **agents/survey_clean_mod.py:** Cleans survey feedback, deduplicates based on internal memory.
- **agents/crm_clean_mod.py:** (Ready for future expansion to clean CRM logs.)
- **utils/cleaner.py:** Text normalization, lemmatization, stopword removal — shared across agents.
- **logs/cleaned_survey_state.json:** Smart memory file to avoid re-processing same inputs.
- **Live Progress Bar:** Users see % cleaning completion during large batch runs.

---

# 📸 Screenshot Placeholder
_(Will add UI screenshots showing multi-agent toggling, cleaning outputs, and download buttons after expanding agents.)_

---

# 📚 License

⚠️ This project is **NOT open-source**.  
You may **NOT copy, use, distribute, or modify** this code for any purpose without express written permission from the creator.

**© All rights reserved by the author.**

