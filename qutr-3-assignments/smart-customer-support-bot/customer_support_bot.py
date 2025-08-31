# ===============================
# Smart Customer Support Bot
# Assignment: Using Gemini API + Human fallback system
# ===============================

import os
import google.generativeai as genai
from dotenv import load_dotenv

# --------------------------------
# 1. Load Environment Variables
# Requirement: Use .env file for storing API key securely
# --------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --------------------------------
# 2. Bot Response Function
# Requirement: Use Gemini API for generating AI-based answers
# --------------------------------
def bot_response(query):
    # Using Gemini 1.5 Flash (fast & efficient model)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    return response.text  # Returns AI-generated answer

# --------------------------------
# 3. Human Agent Fallback
# Requirement: If AI fails to generate an answer → forward to human
# --------------------------------
def human_response(query):
    return f"[Human Agent] Please handle: {query}"

# --------------------------------
# 4. Query Handler
# Requirement: Decide whether to give AI answer or human fallback
# --------------------------------
def handle_query(user_query):
    response = bot_response(user_query)
    if not response:  # If Gemini fails or gives empty output
        return human_response(user_query)
    return response

# --------------------------------
# 5. Main Program Loop
# Requirement: CLI program → user can ask multiple questions until exit
# --------------------------------
if __name__ == "__main__":
    while True:
        query = input("Enter your question: ")
        
        # Exit condition (requirement: quit option)
        if query.lower() in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break
        
        # Print bot/human response
        print("\nBot Response:\n", handle_query(query))
