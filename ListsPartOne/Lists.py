import random

def wait():
    input("Press Enter To Continue")
    print()

# Total Sales
sales = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for x in range(7):
    sales[x] = float(input("Enter revenue from day: $"))
total = 0
for x in range(7):
    total += sales[x]
print("Revenue from week:", sales)
print("Total revenue:", total)
wait()

#Lottery Numbers
lottery = [0,0,0,0,0,0,0]
for x in range(7):
    lottery[x] = random.randint(0,9)
print("Winning Lottery Numbers")
for num in lottery:
    print(num)
wait()

# Rainfall stats
rain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
lowest = 0
highest = 0
total = 0
for x in range(12):
    rain[x] = float(input("Enter amount of rain for month: "))
    total += rain[x]
    if rain[x] > highest:
        highest = rain[x]
    if x == 0:
        lowest = rain[x]
    elif rain[x] < lowest:
        lowest = rain[x]
print("Total rainfall:", total)
print("Average rain:", (total/12))
print("Lowest amount:", lowest)
print("Highest amount:", highest)
wait()

#Number Analysis
highest = 0
lowest = 0
total = 0
numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(20):
    numbers[x] = int(input("Insert a number:"))
    total += numbers[x]
    if x == 0:
        lowest = numbers[x]
    elif numbers[x] < lowest:
        lowest = numbers[x]
    if numbers[x] > highest:
        highest = numbers[x]
print("Lowest amount:", lowest)
print("Highest amount:", highest)
print("Total:", total)
print("Average:", (total/20))