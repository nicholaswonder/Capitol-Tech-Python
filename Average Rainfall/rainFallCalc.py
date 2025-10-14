years = int(input("How many years to collect data: "))
months = 0
total = 0

for x in range(years):
    for y in range(12):
        months += 1
        total += float(input("Enter the amount of rain for month {0}: ".format(months)))

print("Rainfall recorded for {0} months".format(months))
print("Total amount of rain: {0} inches".format(total))
print("Average rain per month: {0} inches".format(total/float(months)))