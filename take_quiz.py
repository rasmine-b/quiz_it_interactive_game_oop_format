import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, window, questions_data):
        self.window = window
        self.questions_data = questions_data

        # Track total score across all quizzes
        self.total_score = {"correct": 0, "total": 0}
        self.original_total_questions = sum(len(qs) for diff in questions_data.values() for qs in diff.values())

        self.current_difficulty = None
        self.current_category = None
        self.quiz_data = []
        self.score = {"correct": 0, "total": 0}
        self.idx = 0

        self.window.config(bg="#FFDAB9")
        self.show_quiz_menu()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_quiz_menu(self):
        self.clear_window()
        self.window.config(bg="#FFDAB9")
        tk.Label(self.window, text="Take the Quiz", font=("Comic Sans MS", 40, "bold"),
                 fg="#F88379", bg="#FCE0D6").pack(pady=40)

        for level in ["Easy", "Medium", "Hard"]:
            tk.Button(self.window, text=level, font=("Comic Sans MS", 20, "bold"),
                      bg="#FFFB8F", fg="#FF6347",
                      command=lambda diff=level: self.choose_category_for_quiz(diff)).pack(pady=10)

        tk.Button(self.window, text="End Quiz & Show Score", font=("Comic Sans MS", 16, "bold"),
                  bg="#FF6347", fg="white", command=self.show_overall_score).pack(pady=30)

    def choose_category_for_quiz(self, difficulty):
        self.clear_window()
        self.window.config(bg="#FFDAB9")
        available = [cat for cat in self.questions_data.get(difficulty, {}) if self.questions_data[difficulty][cat]]
        if not available:
            messagebox.showinfo("No questions", "No questions available for this difficulty.")
            self.show_quiz_menu()
            return

        tk.Label(self.window, text=f"{difficulty} - Choose Category", font=("Comic Sans MS", 30, "bold"),
                 fg="#F88379", bg="#FCE0D6").pack(pady=40)

        for cat in available:
            tk.Button(self.window, text=cat, font=("Comic Sans MS", 18, "bold"),
                      bg="#FFFB8F", fg="#FF6347",
                      command=lambda ct=cat, diff=difficulty: self.start_quiz(diff, ct)).pack(pady=5)

    def start_quiz(self, difficulty, category):
        self.clear_window()
        self.current_difficulty = difficulty
        self.current_category = category
        self.quiz_data = self.questions_data[difficulty][category]

        if not self.quiz_data:
            messagebox.showinfo("No Questions", "No more questions available in this category.")
            self.show_quiz_menu()
            return

        self.score = {"correct": 0, "total": len(self.quiz_data)}
        self.idx = 0

        self.show_question()

    def show_question(self):
        self.clear_window()
        self.window.config(bg="#FFDAB9")

        if self.idx >= len(self.quiz_data):
            # Update overall score
            self.total_score["correct"] += self.score["correct"]
            self.total_score["total"] += self.score["total"]

            messagebox.showinfo("Quiz Completed",
                                f"Finished category: {self.current_category} ({self.current_difficulty})")

            # Remove completed category questions
            self.questions_data[self.current_difficulty][self.current_category] = []

            # Check if all questions are done
            all_done = all(not self.questions_data[diff][ct]
                           for diff in self.questions_data for ct in self.questions_data[diff])

            if all_done:
                self.show_overall_score()
            else:
                self.show_quiz_menu()
            return

        quiz = self.quiz_data[self.idx]
        tk.Label(self.window, text=f"Q{self.idx + 1}: {quiz['question']}", font=("Comic Sans MS", 22),
                 bg="#FCE0D6", wraplength=700).pack(pady=20)

        self.buttons = []
        correct_answer = quiz["correct_answer"]

        def check_answer(selected):
            for btn in self.buttons:
                btn.config(state="disabled")
                if btn["text"].startswith(f"{correct_answer} ="):
                    btn.config(bg="#90EE90", fg="black")  # green correct
                elif btn["text"].startswith(f"{selected} ="):
                    btn.config(bg="#FF6347", fg="white")  # red wrong
                else:
                    btn.config(bg="#FFFB8F", fg="#FF6347")  # yellow others

            if selected == correct_answer:
                self.score["correct"] += 1

            # Remove answered question
            self.quiz_data.pop(self.idx)

            self.window.after(2000, self.show_question)

        for choice in quiz["choices"]:
            key, val = choice.split(" = ")
            btn = tk.Button(self.window, text=choice, font=("Comic Sans MS", 16), width=40,
                            bg="#FFFB8F", fg="#FF6347",
                            command=lambda ky=key: check_answer(ky))
            btn.pack(pady=5)
            self.buttons.append(btn)

    def show_overall_score(self):
        self.clear_window()
        self.window.config(bg="#FCE0D6")
        tk.Label(self.window, text="Overall Score", font=("Comic Sans MS", 35, "bold"),
                 fg="#F88379", bg="#FCE0D6").pack(pady=30)

        tk.Label(self.window,
                 text=f"Score: {self.total_score['correct']} out of {self.original_total_questions}",
                 font=("Comic Sans MS", 25), fg="#FF6347", bg="#FCE0D6").pack(pady=20)

        if messagebox.askyesno("Continue", "Would you like to make another quiz?"):
            self.show_quiz_menu()
        else:
            self.window.destroy()