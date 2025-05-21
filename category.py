import tkinter as tk
import random

class CategoryRandomizer:
    def __init__(self, window, categories, difficulty, on_category_choosen):
        self.window = window
        self.categories = categories
        self.difficulty = difficulty
        self.on_category_chosen = on_category_choosen
        self.randomizing_active = True

        self.display_randomizing_ui()
        