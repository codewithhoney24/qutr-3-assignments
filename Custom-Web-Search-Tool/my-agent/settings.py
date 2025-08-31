import os
from dotenv import load_dotenv

# .env file load karo
load_dotenv()

# ⚙️ Model settings
settings = {
    "model": "gemini-1.5-flash",   # ya "gemini-1.5-pro"
    "api_key": os.getenv("GEMINI_API_KEY"),
    "tool_choice": "auto",
    "metadata": {"customer_id": "CUST001"}
}
