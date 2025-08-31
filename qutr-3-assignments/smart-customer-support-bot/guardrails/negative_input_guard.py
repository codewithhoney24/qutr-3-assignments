# -------------------------------
# Assignment Task: Guardrail / Output Filter
# Purpose: User input me negative ya offensive words block karna
# -------------------------------

from openai.agent import OutputGuard

# Step 1: Guard function define karo
def block_negative_input(text: str) -> str:
    """
    Ye function user ke input ya AI ke response me forbidden words check karta hai.
    Agar koi negative word milta hai to guardrail trigger hota hai.
    """
    forbidden = ["stupid", "hate", "dumb", "bad", "idiot"]  # Negative words ki list
    for word in forbidden:
        if word.lower() in text.lower():  # Case-insensitive check
            return "[Guardrail Triggered] Please use polite language."  # Guardrail message
    return text  # Agar koi forbidden word nahi mila, normal text return karo

# Step 2: OutputGuard object create karo
# Ye guard AI agent ke responses me apply kiya ja sakta hai
negative_guard = OutputGuard(func=block_negative_input)

# -------------------------------
# Usage Example (Assignment style)
# response_text = "You are stupid!"
# safe_response = negative_guard.apply(response_text)
# print(safe_response)  # Output: [Guardrail Triggered] Please use polite language.
# -------------------------------
