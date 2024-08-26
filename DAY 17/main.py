# class User:
    
#    def __init__(self, user_id, user_name):
#        self.user_id = user_id
#        self.user_name = user_name
    
# user_1 = User('001', 'N0B0DY')

# print(user_1.user_name)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))
    
qb = QuizBrain(question_bank)

while qb.still_has_question():
    qb.next_question()

print(f"You've completed the Quiz!")
print(f"Your final score is: {qb.score}/{len(qb.questions_list)}.")