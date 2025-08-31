# main.py

import logging
from typing import Optional

# ------------------ Logging Setup ------------------
logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ------------------ Guardrail ------------------
def guardrail(func):
    """
    Decorator to check offensive language.
    Works for class methods (self + query).
    """
    def wrapper(self, query, *args, **kwargs):  # self explicitly
        bad_words = ["badword", "stupid", "idiot"]
        for word in bad_words:
            if word in query.lower():
                warning = {"warning": "⚠️ Offensive language detected. Please rephrase."}
                logging.info(f"Guardrail triggered: {query}") # Logging the guardrail event

                return warning
        return func(self, query, *args, **kwargs)
    return wrapper

# ------------------ Function Tool ------------------
def function_tool(func):
    """Decorator to mark a function as a tool"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@function_tool
def get_order_status(order_id: str, is_enabled=True):
    """Simulate fetching order status"""
    orders = {
        "1001": "Shipped",
        "1002": "Processing",
        "1003": "Delivered",
    }
    if not is_enabled:
        return {"error": "Tool disabled for this query."}
    status = orders.get(order_id)
    if not status:
        return {"error": f"Order ID {order_id} not found."}
    logging.info(f"Order status checked: {order_id} → {status}")  # Log tool call
    return {"order_id": order_id, "status": status}

# ------------------ Agents ------------------
class BotAgent:
    def __init__(self, name="BotAgent"):
        self.name = name

    @guardrail
    def handle_query(self, query: str):
        """Bot tries to handle query"""
        logging.info(f"{self.name} received query: {query}")
        query_lower = query.lower()
        # Simple logic: handle order status queries
        if "order" in query_lower:
            order_id = query_lower.split()[-1]  # assume last word is order ID
            return get_order_status(order_id)  # Tool call
        # Unknown queries → escalate
        return {"handoff": "HumanAgent needed for this query."}  # Handoff

class HumanAgent:
    def __init__(self, name="HumanAgent"):
        self.name = name

    def handle_query(self, query: str):
        logging.info(f"{self.name} handling query: {query}")
        return {"response": f"{self.name} processed your query: '{query}'"}

# ------------------ AI Agent Simulation ------------------
def run_agent():
    bot = BotAgent()
    human = HumanAgent()

    test_queries = [
        "Check order 1001",   # Bot handles
        "You are stupid",       # Guardrail triggers → Handoff
        "What is the status of order 9999",  # Unknown order → Handoff
        "Hello, how are you?"     # Unknown query → Handoff
    ]

    for q in test_queries:
        result = bot.handle_query(q)

        # If guardrail triggers or bot can't handle → handoff to HumanAgent

        if "handoff" in result or "warning" in result:
            # Handoff to human if bot can't handle or offensive
            human_result = human.handle_query(q)
            print(f"Query: '{q}' → Bot Result: {result} → Human Result: {human_result}")
        else:
            print(f"Query: '{q}' → Bot Result: {result}")

# ------------------ Run ------------------
if __name__ == "__main__":
    run_agent()
