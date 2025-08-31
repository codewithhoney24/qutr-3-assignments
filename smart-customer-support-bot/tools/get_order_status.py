# Google Gemini ka SDK import kiya jata hai
import google.generativeai as genai

# Operating system library import karte hain taki .env file se API key load ho sake
import os

# Yahan hum Gemini API key ko environment variable se load karke configure karte hain
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ---- Custom Function Definition ----
# Ye function ek fake order management system ka part hai
# Order ID input leta hai aur uska status return karta hai
def get_order_status(order_id: str):
    # Fake orders ka dictionary banaya gaya hai jisme kuch sample order IDs aur unke statuses diye gaye hain
    fake_orders = {
        "1001": "Shipped",
        "1002": "Processing",
        "1003": "Delivered"
    }
    # Agar order ID match ho jaye to uska status return hoga warna "Order ID not found." return hoga
    return fake_orders.get(order_id, "Order ID not found.")

# ---- Gemini Model Initialization ----
# Yahan hum Gemini ka ek specific model (gemini-1.5-flash) initialize karte hain
# Ye model text generation aur AI tasks perform karne ke liye use hota hai
model = genai.GenerativeModel("gemini-1.5-flash")

# ---- Example User Query ----
# User se ek order ID li jati hai (yahan hum manually "1002" set kar rahe hain demo ke liye)
user_order = "1002"

# Apne banaye gaye function ko call kar ke order ka status check karte hain
response = get_order_status(user_order)

# Final result console per print hota hai
print(f"Order {user_order} status: {response}")
