from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 

def api_response(prompt, temperature=0.8, max_tokens=100):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"There was an API error: {e}"

choice = int(input("Welcome to the AI Text Generator! Choose an option: 1. Generate Text 2. Exit: "))

while choice != 2:
    if choice == 1:
        prompt = input("Enter your prompt: ")

        if prompt.strip() == "":
            print("Prompt is empty! \n")
        else:
            try:
                temp = input("Set temperature or leave blank for deault: ")
                if temp == "":
                    temperature = 0.7
                else:
                    temperature = float(temp)

                tokens = input("Set max tokens or leave blank for default ")
                if tokens == "":
                    max_tokens = 100
                else:
                    max_tokens = int(tokens)

            except ValueError:
                print("Invalid input, enter text\n")
                temperature = 0.8
                max_tokens = 100

            print("\nGetting your response...\n")
            response = api_response(prompt, temperature, max_tokens)
            print(f"AI Response: {response}")

    else:
        print("Invalid choice\n")

    choice = int(input("Try again: 1. Generate Text 2. Exit: "))

print("Goodbye!")


    choice = int(input("Try again: 1. Generate Text 2. Exit: "))

print("Thanks for using the AI Text Generator!")
