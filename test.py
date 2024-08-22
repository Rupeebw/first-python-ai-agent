import unittest
from generate_text import generate_text

class TestChatGPTFunction(unittest.TestCase):

    def test_generate_text(self):
        # Define a sample prompt
        prompt = "What is the capital of France?"
        
        # Call the generate_text function
        response = generate_text(prompt)
        
        # Print the response for visibility
        print("\nGenerated Response:", response)
        
        # Check if the response is not None and contains expected text
        self.assertIsNotNone(response, "The response should not be None.")
        self.assertIn("Paris", response, "The response should contain 'Paris'.")

if __name__ == "__main__":
    unittest.main()
