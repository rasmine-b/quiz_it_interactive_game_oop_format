import tkinter as tk
from data import DataManager
from quiz import QuizLogic

class QuizApp:
    def __init__(self, window):
        self.window = window
        self.data_manager = DataManager()
        self.questions_data, self.original_total_questions = self.data_manager.load_questions()
        self.quiz_logic = QuizLogic(self.questions_data)

        self.show_main_window()
