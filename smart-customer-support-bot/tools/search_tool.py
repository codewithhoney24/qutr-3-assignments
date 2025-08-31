# -------------------------------
# Assignment Task: Function Calling / Tool Use
# Example Tool: Web Search (Tavily Integration)
# -------------------------------

import google.generativeai as genai
import os
from tavily import TavilyClient   # Tavily ka Python client import kiya
from dotenv import load_dotenv

# Step 1: .env file load karna
load_dotenv()

# Step 2: Gemini API key configure karna
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 3: Tavily client initialize karna
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Step 4: Web search tool define karna (Tavily ke sath)
def search_web(query: str):
    """
    Ye function Tavily API ko call karta hai aur
    query ke liye top results return karta hai.
    """
    results = tavily.search(query=query, search_depth="basic")  
    return results  # Pure Tavily response return karega (list of results)

# Step 5: Gemini model load karna
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 6: Example user query
user_query = "Latest AI trends"

# Step 7: Tavily se search results lana
response = search_web(user_query)

# Step 8: Output display karna
print(f"User query: {user_query}")
print("Search Tool Response (Tavily):")
print(response)
