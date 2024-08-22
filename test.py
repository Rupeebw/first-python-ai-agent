import unittest
from generate_text import generate_text  # Make sure the import path matches your project structure

class TestChatGPTFunction(unittest.TestCase):

    def test_generate_text_weather(self):
        # Define a sample prompt about weather
        prompt = "Shall I take an umbrella today in California when I go out?"
        
        # Call the generate_text function using the GPT-4 model
        response = generate_text(prompt, model="gpt-3.5-turbo")
        
        # Print the response for visibility
        print("\nGenerated Response for Weather Prompt:", response)
        
        # Check if the response is not None
        self.assertIsNotNone(response, "The response should not be None.")
        
        # Check if the response contains expected text (e.g., mentions of rain or weather conditions)
        # Adjust the expected text based on the likely response structure from GPT-4
        expected_keywords = ["rain", "umbrella", "wet", "showers", "weather"]
        contains_expected_keyword = any(keyword in response.lower() for keyword in expected_keywords)
        
        self.assertTrue(contains_expected_keyword, f"The response should mention weather conditions such as 'rain'.")

if __name__ == "__main__":
    unittest.main()
