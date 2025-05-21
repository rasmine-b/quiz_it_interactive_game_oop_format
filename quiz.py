import tkinter as tk
from tkinter import messagebox

class QuizLogic:
    def __init__(self, window, questions_data):
        self.window = window
        self.questions_data = questions_data
        
        # Flatten questions to a list for easy traversal
        self.questions = []
        for difficulty, cats in questions_data.items():
            for cat, qs in cats.items():
                self.questions.extend(qs)
        
        self.index = 0
        self.score = 0
        self.total = len(self.questions)

        if self.total == 0:
            messagebox.showinfo("No Questions", "No saved questions available.")
            self.window.after(100, self.window.quit)  # optional: close app or return to main menu
            return

        
        self.frame = tk.Frame(window)
        self.frame.pack(fill="both", expand=True)
        self.show_question()

    def show_question(self):
        if self.index >= self.total:
            self.show_result()
            return

        q = self.questions[self.index]

        # Clear previous widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        question_label = tk.Label(self.frame, text=q["question"], wraplength=600)
        question_label.pack(pady=10)

        self.var = tk.StringVar()

        for choice in q["choices"]:
            # Each choice is something like 'a = Choice text'
            label, text = choice.split("=", 1)
            label = label.strip()
            text = text.strip()
            rb = tk.Radiobutton(self.frame, text=text, variable=self.var, value=label)
            rb.pack(anchor="w")

        submit_btn = tk.Button(self.frame, text="Submit", command=self.check_answer)
        submit_btn.pack(pady=10)

    def check_answer(self):
        selected = self.var.get()
        correct = self.questions[self.index]["correct_answer"]
        if selected == correct:
            self.score += 1
        self.index += 1
        self.show_question()

    def show_result(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        result_label = tk.Label(self.frame, text=f"Quiz complete! Your score: {self.score} / {self.total}")
        result_label.pack(pady=20)

        close_btn = tk.Button(self.frame, text="Close", command=self.frame.destroy)
        close_btn.pack(pady=10)