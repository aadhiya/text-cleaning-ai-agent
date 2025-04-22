from fastapi import FastAPI
from pydantic import BaseModel
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

app = FastAPI()

class TextData(BaseModel):
    text: str

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')  # No need for punkt

def clean_text(text: str) -> str:
    try:
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        words = tokenizer.tokenize(text)
        cleaned_words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
        return ' '.join(cleaned_words)
    except Exception as e:
        return f"Error during cleaning: {str(e)}"

@app.post("/clean")
async def clean_endpoint(data: TextData):
    try:
        cleaned = clean_text(data.text)
        return {"original": data.text, "cleaned": cleaned}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "Text Cleaning Agent is ready. POST text to /clean"}
