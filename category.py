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
    
    def display_randomizing_ui(self):
        self.clear_window()
        self.window.config(bg="#FFD8B1")

        self.category_box = tk.Label(self.window, text="...", font=("Comic Sans MS", 50, "bold"), fg="#F88379", bg="#FCE0D6",
                                 width=20, height=2, relief="solid")
        self.category_box.pack(pady=50)

        self.update_category()
        self.window.after(2000, self.finish_randomizing)

    
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()