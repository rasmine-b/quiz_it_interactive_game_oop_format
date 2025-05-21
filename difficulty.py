import tkinter as tk

class DifficultySelector:
    def __init__(self, window, on_difficulty_selected, on_exit):
        self.window = window
        self.on_difficulty_selected = on_difficulty_selected
        self.on_exit = on_exit
        self.display()
