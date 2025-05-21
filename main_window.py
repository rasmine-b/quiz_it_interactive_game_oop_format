import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, window, on_start, on_exit, on_saved_quiz):
        self.window = window
        self.on_start = on_start
        self.on_exit = on_exit
        self.on_saved_quiz = on_saved_quiz
        self.setup_main_screen()

    def setup_main_screen(self):
        self.clear_window()
        self.window.config(bg="#FCE0D6")

        title_label = tk.Label(self.window, text="Welcome to QuizIt!", font=("Comic Sans MS", 50, "bold"), fg="#F88379", bg="#FCE0D6")
        title_label.pack(pady=50)

        start_button = tk.Button(self.window, text="Start Making a Quiz", font=("Comic Sans MS", 20, "bold"), bg="#FFFB8F",
                             fg="#FF6347", relief="raised", bd=5, command=self.on_start)
        start_button.pack(pady=20)

        exit_button = tk.Button(self.window, text="Exit", font=("Comic Sans MS", 20, "bold"), bg="#90EE90", fg="#FF6347",
                            relief="raised", bd=5, command=self.on_exit)
        exit_button.pack(pady=20)

        self.saved_quiz_button = tk.Button(self.window, text="Take Saved Quiz", font=("Comic Sans MS", 20, "bold"),
                                       bg="#F88379", fg="white", relief="raised", bd=5, command=self.on_saved_quiz)
        self.saved_quiz_button.pack(pady=10)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
