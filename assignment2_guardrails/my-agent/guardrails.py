"""
guardrails_gemini.py
Assignment 2: Implement Output Guardrail Functionality (using Gemini API)
"""

import google.generativeai as genai
import logging
import os

# ------------------ Setup ------------------
from dotenv import load_dotenv
load_dotenv()  # load API key from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

logging.basicConfig(
    filename="agent_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------ Function Tools ------------------

def get_order_status(order_id: str) -> str:
    """Simulated tool call: fetch order status"""
    fake_orders = {
        "123": "Shipped",
        "456": "Processing",
        "789": "Delivered"
    }
    if order_id not in fake_orders:
        # Tool error handling: friendly error message
        return f"❌ Sorry, no order found for ID {order_id}."
    # Logging tool call
    logging.info(f"Tool call → get_order_status({order_id}) → {fake_orders[order_id]}")
    return f"📦 Order {order_id} status: {fake_orders[order_id]}"


# ------------------ Guardrails ------------------

def block_non_math(query: str):
    """Input guardrail: only allow math or order-related queries"""
    if "order" not in query.lower() and not any(c.isdigit() for c in query):
        logging.warning(f"Guardrail triggered: non-math/non-order input → {query}")
        return "⚠️ Please ask me only math-related or order-related queries."
    return None


def avoid_politics(response: str):
    """Output guardrail: block political responses"""
    political_keywords = ["politics", "election", "government", "president", "prime minister", "minister"]
    for keyword in political_keywords:
        if keyword.lower() in response.lower():
            logging.warning(f"Output guardrail triggered: political content → {response}")
            return "⚠️ Sorry, I cannot provide responses about political topics or figures."
    return response


def block_negative_language(query: str):
    """Input guardrail: detect offensive input and escalate"""
    bad_words = ["stupid", "idiot", "hate", "nonsense"]
    for word in bad_words:
        if word in query.lower():
            logging.warning(f"Escalation triggered due to negative language → {query}")
            return "⚠️ Your message seems negative. Escalating to human agent."
    return None


# ------------------ Agents ------------------

def human_agent(query: str) -> str:
    """Handoff: human agent handles complex or negative queries"""
    logging.info(f"Handoff → human_agent received query: {query}")
    return f"[HumanAgent] I will handle your request personally: '{query}'"


def bot_agent(query: str) -> str:
    """Main bot with guardrails and tool calls"""
    logging.info(f"User Query → {query}")

    # Guardrail 1: Negative language → escalate to human agent
    if block_negative_language(query):
        return human_agent(query)

    # Guardrail 2: Input filter (math/order only)
    input_guardrail = block_non_math(query)
    if input_guardrail:
        return input_guardrail

    # Tool: Order status lookup (function_tool call)
    if "order" in query.lower():
        for word in query.split():
            if word.isdigit():
                return get_order_status(word)  # Tool call + logging

    # Otherwise → send to Gemini model
    response = model.generate_content(query)
    output = response.text.strip()

    # Guardrail 3: Output filter (avoid politics)
    output_guardrail = avoid_politics(output)
    return output_guardrail


# ------------------ Example Run ------------------

if __name__ == "__main__":
    print(bot_agent("2 + 2"))                           # Math query → allowed by input guardrail
    print(bot_agent("Check order 123"))              # Tool call: get_order_status
    print(bot_agent("Tell me about politics"))         # Output guardrail triggered
    print(bot_agent("You are stupid"))                 # Escalation (handoff) to human agent
    print(bot_agent("What is the capital of France"))   # Input guardrail blocks non-math/non-order



#----------------------------------------------------------#
# Dekhiye kya hua run karte waqt:

# "2 + 2 = 4" → Math wali query correct handle hui.

# "📦 Order 123 status: Shipped" → Order wali query sahi se response mila.

# "You are stupid" → Guardrails ne detect kiya ke ye irrelevant / offensive query hai, aur usko human-agent (fallback) ke zariye handle kar diya. Fir guardrail ne warning bhi dikhayi:

# ⚠️ Please ask me only math-related or order-related queries.


# Matlab guardrails system kaam kar raha hai aur aapke restrictions enforce ho rahe hain 🎯

# 👉 Ab aap chaho to aur guardrails bana sakte ho:

# Only financial queries allowed

# Only weather + news queries

# Only polite queries (bad words block ho jayein)

