# text-cleaning-ai-agent
A FastAPI agent that automatically cleans and normalizes raw text data.
# 🧠 Text Cleaning AI Agent

This is a FastAPI-based AI micro-agent that automatically cleans raw text input for NLP or data preprocessing purposes. It supports both single and batch processing, including:

- ✅ Contraction expansion (e.g. "can't" → "cannot")
- ✅ Lowercasing and punctuation removal
- ✅ Stopword filtering
- ✅ Lemmatization
- ✅ Duplicate removal for batch inputs

---

## 🚀 Features

| Feature                    | Supported |
|---------------------------|-----------|
| Contraction Expansion      | ✅         |
| Lowercasing                | ✅         |
| Special Character Removal  | ✅         |
| Stopword Removal           | ✅         |
| Lemmatization              | ✅         |
| Duplicate Detection (Batch)| ✅         |

---

## 🔧 How It Works

The agent exposes two endpoints:

- `POST /clean`: Accepts a single string and returns its cleaned form.
- `POST /clean_batch`: Accepts a list of strings, cleans each one, and removes duplicate results.

---

## 🧱 Libraries Used

| Library         | Purpose                                      |
|----------------|----------------------------------------------|
| `fastapi`       | API framework                                |
| `uvicorn`       | ASGI server to run the app                   |
| `nltk`          | Tokenization, lemmatization, stopword removal |
| `contractions`  | Expands contractions in English              |
| `pandas`        | Used to drop duplicate rows in batch cleanup |

Install dependencies via:

```bash
pip install fastapi uvicorn nltk contractions pandas

Don’t forget to download the necessary NLTK data once:

import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

🧪 How We Tested

Run the server locally:

uvicorn main:app --reload

Then test in Swagger UI:
📍 http://127.0.0.1:8000/docs
Example for /clean:

{
  "text": "I can't believe it's working!"
}

Example for /clean_batch:

{
  "texts": [
    "I can't believe it's working!",
    "It's working!",
    "This is another test.",
    "This is another test."
  ]
}

Expected Output:

{
  "original_count": 4,
  "unique_cleaned_texts": [
    "cannot believe working",
    "working",
    "another test"
  ]
}

🌍 Real-World Use Cases
1. Customer Feedback & Review Analysis

Clean messy product reviews before sentiment or keyword analysis.
2. Survey Data Preprocessing

Standardize open-ended answers for aggregation and clustering.
3. NLP Model Training

Normalize raw text data before feeding it into models for better generalization.
4. CRM Ticket Deduplication

Detect repeated support queries more reliably after cleaning.
5. Web-Scraped Text or Transcription Cleanup

Process noisy scraped/transcribed input for cleaner datasets.
6. Social Media Text Normalization

Filter hashtags, slang, and contractions for trend analysis or moderation.


⚠️ License

This project is NOT open-source.
You may NOT copy, use, distribute, or modify this code for any purpose — personal or commercial — without express written permission from the creator.

    © All rights reserved by the author.