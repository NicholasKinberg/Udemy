from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# class Quiz:
#     pass

questionList = []
for question in question_data:
    newQuestion = Question(question["text"], question["answer"])
    questionList.append(newQuestion)

quiz = QuizBrain(questionList)
quiz.nextQuestion()

while quiz.stillHasQuestions():
    quiz.nextQuestion