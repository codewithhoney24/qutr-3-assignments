# -------------------------------
# Assignment Task: Bot Agent Initialization
# Purpose: AI Bot Agent create karna jo user queries handle kare aur guardrails apply kare
# -------------------------------

from openai import OpenAI
from openai.agent import Agent, OutputGuard

# Step 1: Import custom OutputGuard (negative input guard)
from guardrails.negative_input_guard import negative_guard

# Step 2: Import example function tool (order status lookup)
from tools.get_order_status import get_order_status

# Step 3: OpenAI client configure karo (API key ya .env ke zariye)
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # Replace with actual key or .env variable

# Step 4: Bot Agent create karo
bot_agent = Agent(
    client=client,                 # OpenAI client
    model="gpt-4.1-mini",          # AI model
    output_guards=[negative_guard],# Output guard apply karo
    name="BotAgent",               # Agent ka name
    # Function tools ya extra configurations yahan add ki ja sakti hain
)

# -------------------------------
# Notes (Assignment Style):
# - bot_agent ab user ke queries handle karega
# - Agar response me negative/offensive language hogi, guardrail trigger hoga
# - Future me function_tool decorators ya aur tools bhi add kiye ja sakte hain
# -------------------------------
