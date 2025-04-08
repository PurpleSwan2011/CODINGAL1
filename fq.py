import random
class FruitQuiz:
        def __init__(self):
                self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
        def quiz(self):
                while(True):
                       fruit,color=random.choice(list(self.fruits.items()))
                       print("what is the color of {}".format(fruit))
                       user_answer=input()
if(user_answer.lower()==color):
    
    print("c ans")
else:
    print("wr ans")
option=int(input("enter"))
if(option):
    print("welcs")
fq=FruitQuiz()
fq.quiz()