import os
from langchain_google_genai import GoogleGenerativeAI
from crewai import Agent
from tool import FileTools

GOOGLE_API_KEY = os.getenv("GEMINI_AIPI_KEY")
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

print(llm.invoke("Who is the PM of India?"))