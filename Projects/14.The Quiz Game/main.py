import os
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from art import logo
print(logo)

question_bank = []

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your score is: {quiz.score}/{quiz.q_num}")

os.system('cls')
print(logo)
print("Thanks for playing!")