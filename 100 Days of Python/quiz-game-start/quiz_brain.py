class QuizBrain:
    def __init__(self, list, score) -> None:
        self.number = 0
        self.list = list
        self.score = 0
    
    def nextQuestion(self):
        currentQuestion = self.list[self.number]
        self.number += 1
        userAnswer = input(f"Q{self.number}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(userAnswer, currentQuestion.answer)


    def stillHasQuestions(self):
        if self.number < len(self.list):
            return True
        else:
            return False
        
    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            self.number += 1
            print(f"You got it right! {self.score}/{self.number}")
        else:
            print("low T")
            self.number += 1
        print(f"correct answer: {correctAnswer}")