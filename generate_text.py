import openai
from dotenv import load_dotenv
import os  # Make sure this line is included to import the 'os' module

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt, model="gpt-4", max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated text from the response
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    generated_text = generate_text(prompt)
    print(f"Generated Text:\n{generated_text}")
