import streamlit as st
from streamlit import session_state as ss
from common.model import Quiz, Question, Views, Choice
import time


class Controller:
    """
    Handles the logic of the quiz and completes 3 main methods: 
    1. Generate request input
    2. Process response
    3. Handle user interactions with quiz
    
    Has utility functions to help accomplish logic by calling the view with parameters
    """
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        if 'current_question_index' not in ss:
            ss.current_question_index = 0
    
    def set_view(self, view):
        # Create a reference to the view
        self.view = view
    
    def run(self):
        if self.view:
            self.view.render()
        else:
            raise ValueError("View has not been set")
    
    def generate_quiz(self, topic):
        self.quiz: Quiz = self.generate_quiz_from_topic(topic)
        ss.quiz = self.quiz
        ss.current_question_index = 0
        # Synchronize view
        ss.current_view = Views.QUIZ
        self.view.current_view = ss.current_view
        self.view.render(self)
    
    
    def answer_question(self, choice_key, curr_question: Question) -> bool:
        return curr_question.answer == choice_key
    
    
    def handle_quiz_progression(self):
        if ss.current_question_index < len(self.quiz.questions) - 1:
            ss.current_question_index += 1
            self.view.show_next_question()
        else:
            self.view.show_results()
    
    
    def generate_quiz_from_topic(self, topic: str):
        # Placeholder method to generate a quiz
        return Quiz(
            questions=[
                Question(
                    question=f"Sample Question about {topic}",
                    choices=[
                        Choice(key="A", value="Choice A"),
                        Choice(key="B", value="Choice B"),
                        Choice(key="C", value="Choice C"),
                        Choice(key="D", value="Choice D"),
                    ],
                    answer="A"
                )
            ]
        )