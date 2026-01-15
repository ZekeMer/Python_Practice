from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for something in question_data:
    q = Question(something["text"], something["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

