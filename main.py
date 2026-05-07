import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from dotenv import load_dotenv
import os

load_dotenv() # এটি ফাইলটি খুঁজে বের করে এবং কি-টি লোড করে
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="তুমি একজন দক্ষ সফটওয়্যার ইঞ্জিনিয়ার। সবসময় ক্লিন কোড এবং ব্যাখ্যাসহ উত্তর দেবে।")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_gemini(query: Query):
    try:
        response = model.generate_content(query.question)
        return {"answer": response.text}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
