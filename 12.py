import json

class MockLLMResponse:
    def __init__(self, content):
        self.content = content

def simulate_llm_response(prompt):
    """Simulate an LLM API call with different responses based on prompt type"""
    return MockLLMResponse(prompt)

def demonstrate_prompting():
    # Basic prompt
    basic_prompt = """
    Write about a coffee maker.
    """
    
    # Specific prompt with parameters
    specific_prompt = """
    Describe a 12-cup programmable coffee maker with the following details:
    - Capacity: 12 cups
    - Temperature settings: 3 levels
    - Programming features: 24-hour
    """
    
    # Structured prompt with JSON format
    structured_prompt = """
    Create a product description in the following JSON format:
    {
        "product": "Coffee Maker",
        "capacity": "12 cups",
        "key_features": ["programmable", "temperature control"],
        "target_audience": "home users"
    }
    """
    
    # Demonstrate different responses
    prompts = {
        "Basic Prompt": basic_prompt,
        "Specific Prompt": specific_prompt,
        "Structured Prompt": structured_prompt
    }
    
    results = {}
    for prompt_type, prompt in prompts.items():
        # Simulate LLM response
        response = simulate_llm_response(prompt)
        results[prompt_type] = response.content
        
        # Print results with clear separation
        print(f"\n{'='*50}")
        print(f"Prompt Type: {prompt_type}")
        print(f"{'='*50}")
        print(f"Prompt:")
        print(prompt.strip())
        print(f"\nExpected Response Pattern:")
        
        if prompt_type == "Basic Prompt":
            print("Generic, unstructured text about a coffee maker")
        elif prompt_type == "Specific Prompt":
            print("Detailed description with specific features")
        else:
            print("Structured JSON output with defined fields")

if __name__ == "__main__":
    demonstrate_prompting()
