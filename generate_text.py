import openai
from dotenv import load_dotenv
import os  # Ensure the 'os' module is imported

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt, model="gpt-3.5-turbo", system_prompt=None):
    try:
        if system_prompt:
            # If a system prompt is provided, prepend it to the prompt
            prompt = f"{system_prompt}\n\n{prompt}"
        
        # Call the OpenAI API to generate the response
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt} if system_prompt else {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ]
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    generated_text = generate_text(prompt)
    print(f"Generated Text:\n{generated_text}")
