import tkinter as tk
from tkinter import simpledialog, messagebox

class QuestionInput:
    def __init__(self, window, difficulty, category, on_done):
        self.window = window
        self.difficulty = difficulty
        self.category = category
        self.on_done = on_done
        self.get_question()
        