import tkinter as tk
from tkinter import messagebox
from data import DataManager
from quiz import QuizLogic
from main_window import MainWindow
from difficulty import DifficultySelector
from category import CategoryRandomizer
from questions import QuestionInput

class QuizApp:
    def __init__(self, window):
        self.window = window
        self.data_manager = DataManager()
        self.questions_data, self.original_total_questions = self.data_manager.load_questions()
        self.quiz_logic = QuizLogic(self.questions_data)

        self.show_main_window()
    
    def show_main_window(self):
        MainWindow(
            self.window,
            on_start=self.start_game,
            on_exit=self.exit_game,
            on_saved_quiz=self.show_saved_quiz
        )

    def start_game(self):
        self.window.after(2000, self.show_difficulty_selection)

    def show_difficulty_selection(self):
        DifficultySelector(
            self.window,
            on_difficulty_selected=self.show_category_randomizer,
            on_exit=self.exit_game
        )

    def show_category_randomizer(self, difficulty):
        categories = self.quiz_logic.get_categories(difficulty)
        CategoryRandomizer(
            self.window,
            categories,
            difficulty,
            on_category_chosen=self.start_question_input
        )
    
    def start_question_input(self, difficulty, category):
        QuestionInput(
            self.window,
            difficulty,
            category,
            on_done=self.handle_question_input_done
        )

    
    def handle_question_input_done(self, question, choices, correct, difficulty, category):
        if question is None:
            self.show_difficulty_selection()
            return

        # Save the question
        self.quiz_logic.add_question(difficulty, category, question, choices, correct)
        self.data_manager.save_questions(self.quiz_logic.questions_data)

        answer = messagebox.askyesno("Add Another?", "Do you want to add another question?")
        if answer:
            self.show_difficulty_selection()
        else:
            self.show_main_window()

    def show_saved_quiz(self):
        print("Show saved quiz logic here")

    def exit_game(self):
        self.window.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = QuizApp(root)
    root.mainloop()