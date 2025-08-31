import logging
# my_guardrails.py

# Custom decorator to act as a "guardrail"
def guardrail(func):
    def wrapper(query, *args, **kwargs):  # self nahi, sirf query
        bad_words = ["badword", "stupid", "idiot"]
        for word in bad_words:
            if word in query.lower():
                warning = {"warning": "⚠️ Offensive language detected. Please rephrase."}
                logging.info(f"Guardrail triggered: {query}")
                return warning
        return func(query, *args, **kwargs)
    return wrapper



# Function to check offensive queries
@guardrail
def check_offensive(query: str):
    """
    Agar query offensive hai to usko block karega.
    """
    bad_words = ["badword", "stupid", "idiot"]  # Sample offensive words
    for word in bad_words:
        if word in query.lower():
            return {"warning": "⚠️ Offensive language detected. Please rephrase."}
    return {"ok": True}

# Test code
if __name__ == "__main__":
    # Sample tests
    queries = [
        "You are stupid",
        "Hello world",
        "This is badword example"
    ]

    for q in queries:
        result = check_offensive(q)
        print(f"Query: '{q}' → Result: {result}")
