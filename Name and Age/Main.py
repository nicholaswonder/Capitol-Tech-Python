from datetime import datetime

name = input("What's your name? : ")
birthYear = int(input("What year were you born? : "))
age = int(datetime.today().year) - birthYear
print("Alright, {0}, I'm pretty sure you are {1} year(s) old".format(name, age))