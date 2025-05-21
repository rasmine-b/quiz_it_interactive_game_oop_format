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
                if line.startswith("Question: "):
                    question = line.split(": ", 1)[1]
                    index += 1
                    choices = []
                    while index < len(lines) and lines[index].strip().startswith(('a =', 'b =', 'c =', 'd =')):
                        choices.append(lines[index].strip())
                        index += 1
                    correct_answer = ""
                    if index < len(lines) and lines[index].strip().startswith("Correct Answer:"):
                        parts = lines[index].strip().split(": ", 1)
                        if len(parts) == 2:
                            correct_answer = parts[1]
                        else:
                            print(f"[Warning] Malformed correct answer line: {lines[index]}")

                    questions_data[current_difficulty][current_category].append({
                        "question": question,
                        "choices": choices,
                        "correct_answer": correct_answer
                    })
                    original_total_questions += 1
                index += 1
        except FileNotFoundError:
            pass
        return questions_data, original_total_questions
    def save_questions(self, questions_data):
        with open(self.filename, "w") as file:
            for difficulty, categories in questions_data.items():
                file.write(f"Difficulty Level: {difficulty}\n")
                for category, questions in categories.items():
                    if questions:
                        file.write(f"Category: {category}\n")
                        for q in questions:
                            file.write(f"Question: {q['question']}\n")
                            for choice in q['choices']:
                                file.write(f"{choice}\n")
                            file.write(f"Correct Answer: {q['correct_answer']}\n\n")
