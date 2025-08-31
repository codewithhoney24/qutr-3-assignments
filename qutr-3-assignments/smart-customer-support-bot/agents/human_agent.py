# -------------------------------
# Assignment Task: Human Agent Initialization
# Purpose: Human Agent create karna jo complex ya guardrail-triggered queries handle kare
# -------------------------------

from openai import OpenAI
from openai.agent import Agent

# Step 1: OpenAI client configure karo (API key ya .env se)
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # Replace with actual key or .env variable

# Step 2: Human Agent create karo
human_agent = Agent(
    client=client,            # OpenAI client
    model="gpt-4.1-mini",     # AI model
    name="HumanAgent",         # Agent ka name
    # Note: Human Agent me output guards zaroori nahi, kyunki ye manual/complex queries handle karega
)

# -------------------------------
# Notes (Assignment Style):
# - human_agent ab bot ke handoff ke liye ready hai
# - Jab bot ka response guardrail trigger kare ya complex ho, human_agent call kiya jayega
# -------------------------------
