from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Divider for clean output
def divider(title):
    print("\n" + "=" * 60)
    print(f"🔷 {title}")
    print("=" * 60)

# 1. Simple Chat Completion
def experiment_simple_chat():
    divider("1. Simple Chat Completion")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "What is the capital of India?"}],
        temperature=0.5,
        max_tokens=50
    )
    print(response.choices[0].message.content)

# 2. Prompt Engineering Basics
def experiment_prompt_engineering():
    divider("2. Prompt Engineering Basics")

    # System Prompt
    print("\n🔹 System Prompt:")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Python programming tutor."},
            {"role": "user", "content": "What is a tuple in Python?"}
        ]
    )
    print(response.choices[0].message.content)

    # Role-play Prompt
    print("\n🔹 Role-play Prompt (Explain like a pirate):")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a pirate who teaches Python."},
            {"role": "user", "content": "What is a loop?"}
        ]
    )
    print(response.choices[0].message.content)

# 3. Text Processing Tasks
def experiment_text_processing():
    divider("3. Text Processing Tasks")

    # Summarization
    print("\n🔹 Summarization:")
    text = "OpenAI is an AI research company that creates powerful tools like ChatGPT. It helps people write, code, and learn more effectively using natural language."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    print(response.choices[0].message.content)

    # Translation
    print("\n🔹 Translation (EN ➝ Hindi):")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Translate 'I love artificial intelligence' into Hindi."}]
    )
    print(response.choices[0].message.content)

    # Sentiment Analysis
    print("\n🔹 Sentiment Analysis:")
    sentiment_text = "The new phone is terrible. I'm very disappointed."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Analyze the sentiment of this sentence: '{sentiment_text}'"}]
    )
    print(response.choices[0].message.content)

# 4. Structured Output
def experiment_structured_output():
    divider("4. Structured Output Generation")

    # JSON Output
    print("\n🔹 JSON Output:")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "List 3 programming languages with their creator in JSON format."}
        ]
    )
    print(response.choices[0].message.content)

    # CSV Output
    print("\n🔹 CSV Output:")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Create a CSV table of 5 Indian states with their capitals."}
        ]
    )
    print(response.choices[0].message.content)

# 5. Optional: Consistency vs Creativity (Temperature Tuning)
def experiment_temperature():
    divider("5. Temperature Variation (Consistency vs Creativity)")

    for temp in [0.2, 0.7, 1.0]:
        print(f"\n🔸 Temperature = {temp}")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Suggest a creative name for a space travel startup."}],
            temperature=temp
        )
        print(response.choices[0].message.content)

# Run all experiments
if __name__ == "__main__":
    experiment_simple_chat()
    experiment_prompt_engineering()
    experiment_text_processing()
    experiment_structured_output()
    experiment_temperature()