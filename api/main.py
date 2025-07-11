from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize this text."},
            {"role": "user", "content": request.text}
        ],
        temperature=0.5,
        max_tokens=100
    )
    return {"summary": response.choices[0].message.content.strip()}
