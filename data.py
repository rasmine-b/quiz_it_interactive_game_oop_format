class DataManager:
    def __init__(self, filename="quiz_data.txt"):
        self.filename = filename
    def load_questions(self):
        questions_data = {
            "Easy": {"Food and Drinks": [], "Science": [], "Geography": [], "Movies": [], "Pop Culture": [], "Literature": [], "History": []},
            "Medium": {"Food and Drinks": [], "Science": [], "Geography": [], "Movies": [], "Pop Culture": [], "Literature": [], "History": []},
            "Hard": {"Food and Drinks": [], "Science": [], "Geography": [], "Movies": [], "Pop Culture": [], "Literature": [], "History": []}
        }
        original_total_questions = 0
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []
