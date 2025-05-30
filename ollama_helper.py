import requests
import json

def create_symptom_prompt(symptoms):
    """
    Create a detailed prompt for symptom analysis
    """
    prompt = f"""
You are a medical AI assistant designed to provide educational information about symptoms. 
Analyze the following symptoms and provide a structured response.

IMPORTANT: This is for educational purposes only and should never replace professional medical advice.

Symptoms described: {symptoms}

Please provide a comprehensive analysis in the following format:

**Possible Medical Causes:**
- List potential conditions that could cause these symptoms
- Include both common and less common possibilities
- Mention if symptoms could be related to lifestyle factors

**Affected Body Systems:**
- Identify which body systems might be involved
- Explain how these systems could be affected

**Recommended Medical Specialist:**
- Suggest which type of healthcare provider would be most appropriate
- Explain why this specialist would be suitable

**Warning Signs to Monitor:**
- List symptoms that would indicate worsening condition
- Mention any red flags that require immediate attention

**Seek Emergency Care If:**
- Clearly list emergency symptoms
- Emphasize when immediate medical attention is needed

**Next Steps:**
- Provide practical advice for symptom management
- Suggest when to schedule medical appointments
- Recommend keeping symptom diary if appropriate

Remember to:
- Be thorough but not alarmist
- Emphasize the importance of professional medical evaluation
- Provide educational information while being clear about limitations
- Use clear, understandable language
- Always recommend consulting healthcare professionals

End your response with a clear disclaimer about seeking professional medical advice.
"""
    return prompt

def call_ollama_api(prompt, model="llama3.1"):
    """
    Call the Ollama API with the given prompt
    """
    try:
        url = "http://localhost:11434/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": 2000
            }
        }
        
        response = requests.post(url, json=payload, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', '')
        else:
            print(f"Error: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure Ollama is running on localhost:11434")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out. The model might be taking too long to respond.")
        return None
    except Exception as e:
        print(f"Error calling Ollama API: {str(e)}")
        return None

def validate_symptoms(symptoms):
    """
    Basic validation of symptom input
    """
    if not symptoms or len(symptoms.strip()) < 10:
        return False, "Please provide a more detailed description of your symptoms."
    
    if len(symptoms) > 2000:
        return False, "Please keep your symptom description under 2000 characters."
    
    return True, "Valid input"

def analyze_symptoms(symptoms):
    """
    Main function to analyze symptoms using Ollama
    """
    # Validate input
    is_valid, message = validate_symptoms(symptoms)
    if not is_valid:
        return f"Input validation error: {message}"
    
    # Create prompt
    prompt = create_symptom_prompt(symptoms)
    
    # Call Ollama API
    analysis = call_ollama_api(prompt)
    
    if analysis:
        return analysis
    else:
        return "Unable to analyze symptoms. Please check your Ollama setup and try again."

def test_ollama_connection():
    """
    Test if Ollama is running and accessible
    """
    try:
        url = "http://localhost:11434/api/tags"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            models = response.json().get('models', [])
            return True, f"Ollama is running. Available models: {[model['name'] for model in models]}"
        else:
            return False, f"Ollama responded with status code: {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to Ollama. Make sure Ollama is running on localhost:11434"
    except Exception as e:
        return False, f"Error testing Ollama connection: {str(e)}"

if __name__ == "__main__":
    # Test the connection
    is_connected, message = test_ollama_connection()
    print(f"Ollama connection test: {message}")
    
    if is_connected:
        # Test symptom analysis
        test_symptoms = "I have been experiencing headaches and fatigue for the past 3 days."
        print(f"\nTesting with symptoms: {test_symptoms}")
        
        result = analyze_symptoms(test_symptoms)
        print(f"\nAnalysis result:\n{result}")
