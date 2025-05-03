import google.generativeai as genai


genai.configure(api_key="AIzaSyA4QfQvdkN4EdxSZW-UjHnlWAvVCVzSKMs")


def generate_response(user_input):
    """Generate a response using the AI model."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(user_input)

        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error generating response: {e}"
