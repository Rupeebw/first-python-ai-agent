# Hardcoded Agent
from generate_text import generate_text
from sample_functions import get_weather

# Get the current weather for California
current_weather = get_weather("California")

# Define the prompt, including the current weather in the prompt
prompt = f"""
Should I take an umbrella when going out today in California based on the following weather conditions: {current_weather}?
"""

# Generate the text response using the GPT-4 model
response = generate_text(prompt, model="gpt-3.5-turbo")

# Print the generated response
print(response)
