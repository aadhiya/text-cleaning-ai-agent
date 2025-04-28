# 📜 CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

---

## [Unreleased]
- Planning for additional specialized agents (e.g., HR Feedback Cleaner, Bug Report Cleaner)
- Adding UI screenshots after agent expansion
- Potential integration with more LLMs beyond Ollama

---

## [2025-04-29] - Major Modular Architecture Update
### Added
- Full Modular Agent-Based Architecture.
- Async backend processing using `asyncio` with Ollama LLM for intent detection.
- Streamlit UI improvements:
  - Toggle agents ON/OFF.
  - Upload TXT and CSV files.
  - Live progress bar during cleaning.
- SurveyCleanMOD agent and state memory management.
- Separate cleaning outputs for text and CSV downloads.

### Changed
- Updated `README.md`:
  - Added badges (FastAPI, Streamlit, Modular Architecture, Ollama, Async Backend).
  - Explained Modular Architecture in table format.
  - Inserted Modular System Diagram.
  - Detailed Code Overview.
  - Clear License section.
- Upgraded `survey_clean_mod.py` to reload memory state fresh every run.
- Improved error handling in FastAPI endpoints.

### Fixed
- "Nothing new was cleaned" bug due to cached memory state.
- Encoding issues with CSV files containing special characters.

---

## [2025-04-27] - Initial Commit
### Added
- FastAPI backend server with `/route-and-clean` and `/toggle-agent` endpoints.
- Initial Streamlit UI for single text input and simple agent run.
- Base utilities for text cleaning (contractions expansion, lemmatization, normalization).

