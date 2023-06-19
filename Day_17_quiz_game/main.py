from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)
# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()

current_score = quiz.score

print("You have completed the QUIZ !!!")
print(f"Your final score is {current_score}/{len(question_bank)}")