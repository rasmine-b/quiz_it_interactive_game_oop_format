import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, window, on_start, on_exit, on_saved_quiz):
        self.window = window
        self.on_start = on_start
        self.on_exit = on_exit
        self.on_saved_quiz = on_saved_quiz
        self.setup_main_screen()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
