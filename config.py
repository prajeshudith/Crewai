import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/Isotonic/distilbert_finetuned_ai4privacy_v2"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}