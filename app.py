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
st.set_page_config(page_title="AI Study Genie", page_icon="📚", layout="wide")
st.title("📚 AI Study Genie - Your Personalized Learning Assistant")
st.subheader("Learn any topic interactively with AI!")

# User Settings
st.sidebar.header("⚙️ Customize Your Learning Experience")
learning_style = st.sidebar.selectbox("Choose your learning style:", ["Text Explanation", "Diagrams", "Bullet Points", "Storytelling"])
difficulty = st.sidebar.selectbox("Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])
study_pace = st.sidebar.selectbox("Set your study pace:", ["Quick 5-minute review", "30-minute deep dive", "Full syllabus"])

# User Input
topic = st.text_input("Enter a topic to learn:")

# Function to generate AI response
def generate_summary(topic, learning_style, difficulty, study_pace):
    model = genai.GenerativeModel("gemini-pro")
    prompt = (
        f"Explain {topic} in a {learning_style} format for a {difficulty} level learner. "
        f"Keep the response concise and suitable for a {study_pace} session."
    )
    response = model.generate_content(prompt)
    return response.text

# Generate Summary Button
if st.button("Generate Study Material"):
    if topic:
        with st.spinner("Generating response..."):
            summary = generate_summary(topic, learning_style, difficulty, study_pace)
        st.subheader("📖 Study Material:")
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
        st.subheader("📌 Quiz:")
        st.write(quiz)
    else:
        st.warning("Enter a topic first!")
