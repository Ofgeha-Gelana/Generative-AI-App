import streamlit as st
import google.generativeai as genai
import os

# Load Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Missing GEMINI_API_KEY. Please check your .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

def generate_study_content(topic, learning_style, difficulty, study_pace):
    """Generates AI-powered study content based on user preferences."""
    prompt = (
        f"""
        You are an AI study assistant. Explain the topic '{topic}' in a 
        '{learning_style}' style for a '{difficulty}' level learner. 
        Keep the response within a '{study_pace}' timeframe.
        """
    )
    response = genai.chat(prompt)
    return response.text if response else "Error generating content."

# Streamlit UI
st.set_page_config(page_title="AI Study Genie", layout="wide")
st.title("📚 AI Study Genie - Your Personalized Learning Assistant")

# User Input Section
topic = st.text_input("Enter a topic to study:")
learning_style = st.selectbox("Choose your learning style:", ["Text Explanation", "Diagrams", "Bullet Points", "Storytelling"])
difficulty = st.selectbox("Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])
study_pace = st.selectbox("Set your study pace:", ["Quick 5-minute review", "30-minute deep dive", "Full syllabus"])

if st.button("Generate Study Material"):
    if topic:
        with st.spinner("Generating study content..."):
            study_material = generate_study_content(topic, learning_style, difficulty, study_pace)
            st.subheader("📖 Study Material:")
            st.write(study_material)
    else:
        st.warning("Please enter a topic before generating study material.")
