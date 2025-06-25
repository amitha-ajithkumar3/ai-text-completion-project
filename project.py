from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 

def api_response(prompt, temperature=0.7, max_tokens=100):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception:
        return "There was an API error."

choice = int(input("Welcome to the AI Text Generator! Choose an option: 1. Generate Text 2. Exit: "))

while choice != 2:
    if choice == 1:
        prompt = input("Enter your prompt: ")

        if prompt.strip() == "":
            print("Prompt is empty! \n")
        else:
            try:
                temp = input("Set temperature (0.0 to 1.0, default 0.7): ")
                if temp == "":
                    temperature = 0.7
                else:
                    temperature = float(temp)

                tokens = input("Set max tokens (default 100): ")
                if tokens == "":
                    max_tokens = 100
                else:
                    max_tokens = int(tokens)

            except ValueError:
                print("Invalid input, enter text\n")
                temperature = 0.7
                max_tokens = 100

            print("\nGenerating response...\n")
            response = api_response(prompt, temperature, max_tokens)
            print(f"AI Response: {response}")

    else:
        print("Invalid choice. Try again.\n")

    choice = int(input("Try again: 1. Generate Text 2. Exit: "))

print("Thanks for using the AI Text Generator!")
