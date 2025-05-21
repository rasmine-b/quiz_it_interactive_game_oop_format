import tkinter as tk
from tkinter import simpledialog, messagebox

class QuestionInput:
    def __init__(self, window, difficulty, category, on_done):
        self.window = window
        self.difficulty = difficulty
        self.category = category
        self.on_done = on_done
        self.get_question()
    
    def get_question(self):
        question = simpledialog.askstring("Input", "Enter your question:", parent=self.window)
        if question:
            choices = []
            labels = ['a', 'b', 'c', 'd']
            for label in labels:
                choice = simpledialog.askstring("Input", f"Enter choice {label} =", parent=self.window)
                if choice is None:
                    messagebox.showinfo("Cancelled", "Question input cancelled.")
                    return
                choices.append(choice)
            correct = simpledialog.askstring("Input", "Enter the correct answer label (a/b/c/d):", parent=self.window)
            self.on_done(question, choices, correct, self.difficulty, self.category)
