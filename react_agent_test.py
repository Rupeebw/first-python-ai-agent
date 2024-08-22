from generate_text import generate_text
from prompts import react_system_prompt

# Define the prompt, including the current weather in the prompt
prompt = """
Should I take an umbrella when going out today in Arizona?
"""

# Generate the text response using the GPT-3.5-turbo model with a custom system prompt
response = generate_text(prompt=prompt, model="gpt-3.5-turbo", system_prompt=react_system_prompt)

# Print the generated response
print(response)
