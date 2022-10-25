from re import T


class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list
        self.score = 0
      
      
    def next_question(self):
        current_question = self.quiz_list[self.quiz_number]
        self.quiz_number += 1
        user_answer = input(f'Q.{self.quiz_number}: {current_question.text}. (True / False)\n')
        self.check_answer(user_answer, current_question.answer)
        if self.quiz_number == len(self.quiz_list):
            self.final_score()
        
    def still_has_questions(self):
        return self.quiz_number < len(self.quiz_list)
    
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('You got it wrong!')
        print(f'The correct answer is {correct_answer}')
        print(f'Current score is {self.score}/{self.quiz_number}\n')
        
    def final_score(self):
        total_questions = len(self.quiz_list)
        total_score = self.score
        print("You've completed te quiz!!!")
        print(f"Your final score is {total_score}/{total_questions}!!!")