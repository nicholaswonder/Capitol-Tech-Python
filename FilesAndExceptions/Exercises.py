import random
# Wait function so I dont have to write it out every time
def wait():
    input("Press Enter To Continue")

# Ex 1
file = open("numbers.txt", "r")
print(file.readline())
file.close()
wait()

#Ex 2
file = open(input("Enter name of file: "), "r")
for x in range(5):
    print(file.readline())
file.close()
wait()

#Ex 3
i = 0
with open(input("Enter name of file: "), "r") as file:
    for line in file:
        i += 1
        print(line + ": Line", i)
wait()

#Ex 4
# Just reusing the code from Ex 3
with open(input("Enter name of file: "), "r") as file:
    for line in file:
        print(line)
file.close()
wait()

#Ex 5
file = open("numbers.txt", "r")
line = file.readline()
numbers = line.split(" ")
ans = 0
for num in numbers:
    ans += int(num)
print(ans)
wait()

#Ex 6
file = open("numbers.txt", "r")
line = file.readline()
numbers = line.split(" ")
ans = 0
size = 0
for num in numbers:
    ans += int(num)
    size += 1
ans = ans/size
print(ans)

#Ex 7
amount = int(input("Enter the amount of numbers to generate: "))
file = open("randomNumbers.txt", "w")
for x in range(amount):
    file.write(str(random.randint(0, 501)))
    file.write(" ")
file.close()

#Ex 8
file = open("randomNumbers.txt", "r")
line = file.readline()
numbers = line.split(" ")
ans = 0
size = 0
for num in numbers:
    if num != "":
        ans += int(num)
        size += 1
print("Total:", ans)
print("Amount:", size)
wait()

#Ex 9
try:
    file = open("numbers.txt", "r")
    line = file.readline()
    numbers = line.split(" ")
    ans = 0
    size = 0
    for num in numbers:
        ans += int(num)
        size += 1
    ans = ans/size
    print(ans)
except IOError:
    print("An IOError Occurred")
except ValueError:
    print("A ValueException Occurred")