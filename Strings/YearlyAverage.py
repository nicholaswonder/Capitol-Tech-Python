# Declare tuples
prices = []
averages = []

# Get data from file
with open("GasPrices-1.txt") as file:
    for line in file:
        price = line
        # Get rid of extra slash and newline characters from strings
        price = price.replace('\\','')
        price = price.replace('\n', '')
        prices.append(price)
    file.close()

# Find first year in data
data = prices[0].split(':')
date = data[0].split('-')
working_year = date[2]
total = 0.0
counter = 0

for line in prices:
    if line != '}': # EOF is delimited with '}'
        data = line.split(':')
        date = data[0].split('-')
        year = date[2]
        if year == working_year: # If the next point of data is within the same year as the last
            total += float(data[1])
            counter += 1
        else: # If data is from the next year, store the average of previous year and restart calculation
            averages.append(working_year + " : " + str((total/counter)))
            total = float(data[1])
            counter = 1
            working_year = year
    else: # If EOF, save final average
        averages.append(working_year + " : " + str((total / counter)))

# Print results
for line in averages:
    print(line)