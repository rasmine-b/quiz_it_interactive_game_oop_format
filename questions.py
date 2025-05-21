import tkinter as tk
from tkinter import simpledialog, messagebox

class QuestionInput:
    def __init__(self, window, difficulty, category, on_done, on_finish):
        self.window = window
        self.difficulty = difficulty
        self.category = category
        self.on_done = on_done
        self.on_finish = on_finish
        self.get_question()
    
    def get_question(self):
        while True:
            question = simpledialog.askstring("Input", "Enter your question:", parent=self.window)
            if not question:
                # User cancelled or left blank
                if messagebox.askyesno("Finish?", "No question entered. Do you want to finish adding questions?"):
                    self.on_finish()
                    return
                else:
                    continue
            choices = []
            labels = ['a', 'b', 'c', 'd']
            for label in labels:
                choice = simpledialog.askstring("Input", f"Enter choice {label} =", parent=self.window)
                if choice is None:
                    messagebox.showinfo("Cancelled", "Question input cancelled.")
                    if messagebox.askyesno("Finish?", "Do you want to finish adding questions?"):
                        self.on_finish()
                    else:
                        continue  # Restart question input
                    return
                choices.append(choice)
            correct = simpledialog.askstring("Input", "Enter the correct answer label (a/b/c/d):", parent=self.window)
            if not correct or correct.lower() not in labels:
                messagebox.showerror("Invalid Input", "Correct answer must be one of a, b, c, or d.")
                continue

            self.on_done(question, choices, correct.lower(), self.difficulty, self.category)

            if not messagebox.askyesno("Add Another?", "Do you want to add another question?"):
                self.on_finish()
