# import ssl
# import os
# import urllib.request
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Disable SSL verification globally
# ssl._create_default_https_context = ssl._create_unverified_context

# # Disable SSL verification for requests
# os.environ["REQUESTS_CA_BUNDLE"] = ""

# # Load API Key from .env
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Configure Gemini API
# genai.configure(api_key=API_KEY)

# # Function to generate AI response
# def generate_summary(topic):
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content(f"Explain {topic} in simple terms for a beginner.")
#     print(response.text)  # Print the response to the console (instead of streamlit)
#     return response.text

# # Example usage
# topic = "Artificial Intelligence"
# if topic:
#     summary = generate_summary(topic)  # This will print to the console
