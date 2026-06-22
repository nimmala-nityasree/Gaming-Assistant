from google import genai

API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash-lite"

SYSTEM_PROMPT = """
You are GamerGPT.

You help users with:
- Game recommendations
- PC requirement checks
- Game comparisons
- Gaming tips and tricks
- Setup suggestions

Always answer in a gamer-friendly style.
"""

def chat():
    print("🎮 Gamer Assistant Started!")
    print("Type 'exit' to quit.\n")

    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 GG! Goodbye.")
            break

        history.append(f"User: {user_input}")

        prompt = SYSTEM_PROMPT + "\n\n" + "\n".join(history)

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        answer = response.text

        history.append(f"Assistant: {answer}")

        print("\n🎮 GamerGPT:", answer)
        print()

if __name__ == "__main__":
    chat()