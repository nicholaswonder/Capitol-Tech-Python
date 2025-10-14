import random

def guessNumber(num1, num2, answer):
    if answer == (num1 + num2):
        print("Correct!")
    else:
        print("Incorrect! The answer was", (num1 + num2))

num1 = random.randint(1,999)
num2 = random.randint(1,999)
print("Math Quiz!")
print(num1, " + ", num2)
answer = int(input("Answer: "))

guessNumber(num1, num2, answer)