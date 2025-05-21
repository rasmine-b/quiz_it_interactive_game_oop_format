class QuizLogic:
    def __init__(self, questions_data):
        self.questions_data = questions_data
        self.score_correct = 0
        self.score_total = 0

    def get_difficulties(self):
        return list(self.questions_data.keys())
    
    def get_categories(self, difficulty):
        return list(self.questions.get(difficulty, {}).keys())
    
    def get_available_categories(self, difficulty):
        return [cat for cat, qs in self.questions_data.get(difficulty, {}).items() if qs]

    def add_question(self, difficulty, category, question, choices, correct_answer):
        self.questions_data[difficulty][category].append({
            "question": question,
            "choices": choices,
            "correct_answer": correct_answer
        })

    def check_answer(self, selected, correct):
        return selected == correct
    
    def reset_score(self):
        self.score_correct = 0
        self.score_total = 0
