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
            current_difficulty = ""
            current_category = ""
            index = 0
            while index < len(lines):
                line = lines[index].strip()
                if line.startswith("Difficulty Level: "):
                    current_difficulty = line.split(": ")[1]
                elif line.startswith("Category: "):
                    current_category = line.split(": ")[1]
                index += 1
        except FileNotFoundError:
            lines = []
