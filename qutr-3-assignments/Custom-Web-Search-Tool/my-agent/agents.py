from  my_guardrails import Agent, ModelSettings
from tools import get_order_status
from my_guardrails import check_offensive
# guardrails_setup.py
from  my_guardrails import Guard

def create_guard():
    return Guard().use(
        validators=["json", "length"]
    )



from tavily_tool import tavily_search

# 🤖 BotAgent: Handles FAQs, orders, search
BotAgent = Agent(
    name="BotAgent",
    model="gemini-1.5-flash",   # Gemini use ho raha hai
    api_key="GEMINI_API_KEY",   # env se load hoga
    tools=[get_order_status, tavily_search],  # Function tools
    guardrails=[check_offensive],
    model_settings=ModelSettings(
        tool_choice="auto",  # Bot automatically tool use kare
        metadata={"customer_id": "CUST-001"}
    )
)

# 👨 HumanAgent: Escalation ke liye
HumanAgent = Agent(
    name="HumanAgent",
    model="gemini-1.5-flash",
    api_key="GEMINI_API_KEY"
)
