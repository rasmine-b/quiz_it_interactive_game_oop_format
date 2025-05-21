class QuizLogic:
    def __init__(self, questions_data):
        self.questions_data = questions_data
        self.score_correct = 0
        self.score_total = 0

    def get_difficulties(self):
        return list(self.questions_data.keys())
    
    def get_categories(self, difficulty):
        return list(self.questions.get(difficulty, {}).keys())
    