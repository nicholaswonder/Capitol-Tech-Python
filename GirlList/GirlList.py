data = open("GirlNames.txt")
girls = []
for line in data:
    girls.append(line.replace("\n", ""))

name = input("Enter a girls name: ")

if girls.__contains__(name):
    print(name, "is in the list")
else:
    print(name, "is not in the list")