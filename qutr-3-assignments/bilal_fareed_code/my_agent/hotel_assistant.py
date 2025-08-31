"""
hotel_assistant.py
Assignment 3: Convert Static Instructions into Dynamic Instructions (Gemini Version)

Objective:
-----------
- Use Google Gemini API (instead of OpenAI Agent SDK).
- Allow storing multiple hotels dynamically (in-memory DB).
- Retrieve info about a specific hotel.
- List all stored hotels.
- Handle empty queries gracefully.
"""

import google.generativeai as genai
from typing import Dict

# ------------------ Configure Gemini ------------------
# Replace with your Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Use the latest Gemini model
model = genai.GenerativeModel("gemini-pro")


# ------------------ In-Memory "Database" ------------------

hotels: Dict[str, Dict[str, str]] = {}


# ------------------ Helper Functions (Tools) ------------------

def add_hotel(name: str, location: str, rooms: str, price: str, amenities: str):
    """
    Add a new hotel dynamically.
    """
    hotels[name.lower()] = {
        "name": name,
        "location": location,
        "rooms": rooms,
        "price": price,
        "amenities": amenities,
    }
    return f"✅ Hotel '{name}' has been added successfully."


def get_hotel_info(name: str) -> str:
    """
    Retrieve hotel information.
    """
    hotel = hotels.get(name.lower())
    if not hotel:
        return f"❌ Sorry, I don’t have any details for '{name}'."
    return (
        f"🏨 Hotel Name: {hotel['name']}\n"
        f"📍 Location: {hotel['location']}\n"
        f"🛏 Rooms: {hotel['rooms']}\n"
        f"💲 Price: {hotel['price']}\n"
        f"✨ Amenities: {hotel['amenities']}"
    )


def list_hotels() -> str:
    """
    List all hotels.
    """
    if not hotels:
        return "❌ No hotels available right now. Please add some first."
    return "Here are the hotels I know about:\n- " + "\n- ".join(
        [hotel['name'] for hotel in hotels.values()]
    )


# ------------------ Agent Simulation (Gemini Prompting) ------------------

def hotel_assistant(query: str) -> str:
    """
    Hotel assistant logic using Gemini.
    This simulates "Agent" behavior via prompt-engineering + function calls.
    """

    # Guardrail: empty query
    if not query.strip():
        return "⚠️ Please provide a valid question about hotels."

    # Simple tool routing (instead of OpenAI Agent SDK decorators)
    query_lower = query.lower()

    # Routing logic (simulate function_tool usage)
    if "add hotel" in query_lower:
        return "ℹ️ To add a hotel, please use the `add_hotel(name, location, rooms, price, amenities)` function."
    elif "list hotels" in query_lower:
        return list_hotels()
    else:
        # Try to detect hotel name from query
        for hotel_name in hotels.keys():
            if hotel_name in query_lower:
                return get_hotel_info(hotel_name)

    # Fallback → let Gemini model generate a natural response
    response = model.generate_content(
        f"You are a hotel assistant. The user asked: {query}. "
        f"Known hotels: {', '.join(hotels.keys()) if hotels else 'none'}.\n"
        f"If relevant, answer politely. If not, explain you only handle hotel info."
    )
    return response.text


# ------------------ Example Run ------------------

if __name__ == "__main__":
    # Step 1: Add some hotels
    print(add_hotel("Hotel Paradise", "Dubai", "120 rooms", "$200/night", "Pool, Gym, Spa"))
    print(add_hotel("Sea View Resort", "Karachi", "80 rooms", "$150/night", "Sea View, Free WiFi"))

    # Step 2: Run example queries
    print("\n--- Example Queries ---")
    print(hotel_assistant("Tell me about Hotel Paradise"))
    print(hotel_assistant("List hotels"))
    print(hotel_assistant("What amenities does Sea View Resort have?"))
    print(hotel_assistant(""))  # Guardrail test
