import streamlit as st
from streamlit import session_state as ss
from common import Controller, Quiz, Question, Choice, View
from prompts import ZERO_SHOT_PROMPT


st.set_page_config(page_title="Prompt Engineering Mission - Quiz Generator", layout="wide")

# Init SS
if 'quiz' not in ss:
    ss.quiz = Quiz(questions=[])

if 'current_prompt' not in ss:
    ss.current_prompt = ss.current_prompt = "Zero-shot"

# Init Controller with Current Quiz
controller = Controller(ss.quiz)
view = View()

# Sidebar for selecting prompting technique
technique = st.sidebar.selectbox(
    "Select Prompting Technique",
    ["Zero-Shot"]
)

# Update current prompt based on selected technique
if technique == "Zero-Shot":
    ss.current_prompt = "Zero-shot"


# Run Main app logic
view.render(controller)
