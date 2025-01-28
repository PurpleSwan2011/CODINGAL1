import random
playing=True
number=str(random.randint(10,20))
print("i will generate a number from 10 to 20  and u have to guess the number one digit at a time ")
print(" the game ends when u get 1 hero!")
while playing:
    guess=input("give me the best!")
    if number == guess:
        print("u win ")
        print("the no was,",number)
        break
    else:
        print("ur guess isn't right,try again")