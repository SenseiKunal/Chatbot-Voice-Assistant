import openai
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ✅ Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🕒 Get current time in India
india = pytz.timezone("Asia/Kolkata")
time_now = datetime.now(india)
print("Current time in India:", time_now.strftime("%I:%M %p"))

def chat_with_openai():
    print("🤖 Hello! I am your chatbot. Type 'exit' to end the chat.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # ✅ GPT 3.5
                messages=messages
            )
            reply = response.choices[0].message.content
            print("🤖:", reply)
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    chat_with_openai()
