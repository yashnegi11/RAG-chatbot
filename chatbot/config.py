import os
from dotenv import load_dotenv
load_dotenv()  

api_key = os.getenv("LLM_API_KEY")
LLM_BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-r1:free"