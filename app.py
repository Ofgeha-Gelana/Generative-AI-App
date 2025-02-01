# import ssl
# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# ssl._create_default_https_context = ssl._create_unverified_context


# # Load API Key from .env
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Configure Gemini API
# genai.configure(api_key=API_KEY)

# # Streamlit UI
# st.set_page_config(page_title="AI Study Assistant", page_icon="📚")
# st.title("📚 AI Study Assistant")
# st.subheader("Learn any topic interactively with AI!")

# # User Input
# topic = st.text_input("Enter a topic to learn:")

# # Function to generate AI response
# def generate_summary(topic):
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content(f"Explain {topic} in simple terms for a beginner.")
#     return response.text

# # Generate Summary Button
# if st.button("Generate Summary"):
#     if topic:
#         with st.spinner("Generating response..."):
#             summary = generate_summary(topic)
#         st.write(summary)
#     else:
#         st.warning("Please enter a topic to generate content.")

# # Optional: Add Quizzes
# st.subheader("📝 Want a Quiz on this Topic?")
# if st.button("Generate Quiz"):
#     if topic:
#         with st.spinner("Creating quiz questions..."):
#             quiz = genai.GenerativeModel("gemini-pro").generate_content(
#                 f"Create a 3-question multiple-choice quiz on {topic} with answers."
#             ).text
#         st.write(quiz)
#     else:
#         st.warning("Enter a topic first!")






import ssl
import os
import urllib.request
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Disable SSL verification globally
ssl._create_default_https_context = ssl._create_unverified_context

# Optionally, disable SSL for requests
os.environ["REQUESTS_CA_BUNDLE"] = ""

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="AI Study Assistant", page_icon="📚")
st.title("📚 AI Study Assistant")
st.subheader("Learn any topic interactively with AI!")

# User Input
topic = st.text_input("Enter a topic to learn:")

# Function to generate AI response
def generate_summary(topic):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Explain {topic} in simple terms for a beginner.")
    return response.text

# Generate Summary Button
if st.button("Generate Summary"):
    if topic:
        with st.spinner("Generating response..."):
            summary = generate_summary(topic)
        st.write(summary)
    else:
        st.warning("Please enter a topic to generate content.")

# Optional: Add Quizzes
st.subheader("📝 Want a Quiz on this Topic?")
if st.button("Generate Quiz"):
    if topic:
        with st.spinner("Creating quiz questions..."):
            quiz = genai.GenerativeModel("gemini-pro").generate_content(
                f"Create a 3-question multiple-choice quiz on {topic} with answers."
            ).text
        st.write(quiz)
    else:
        st.warning("Enter a topic first!")
