import tkinter as tk

class DifficultySelector:
    def __init__(self, window, on_difficulty_selected, on_exit):
        self.window = window
        self.on_difficulty_selected = on_difficulty_selected
        self.on_exit = on_exit
        self.display()

    def display(self):
        self.clear_window()
        self.window.config(bg="#FCE0D6")

        game_label = tk.Label(self.window, text="Choose Difficulty", font=("Comic Sans MS", 40, "bold"), fg="#F88379", bg="#FCE0D6")
        game_label.pack(pady=50)

        for level in ["Easy", "Medium", "Hard"]:
            color = {"Easy": "#90EE90", "Medium": "#FFFB8F", "Hard": "#FF6347"}[level]
            text_color = {"Easy": "#FF6347", "Medium": "#FF6347", "Hard": "white"}[level]
            tk.Button(self.window, text=level, font=("Comic Sans MS", 20, "bold"), bg=color, fg=text_color,
                  relief="raised", bd=5, command=lambda d=level: self.on_difficulty_selected(d)).pack(pady=10)

        tk.Button(self.window, text="Exit", font=("Comic Sans MS", 15, "bold"), bg="#FF6347", fg="white",
              bd=5, command=self.on_exit).pack(pady=20)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
