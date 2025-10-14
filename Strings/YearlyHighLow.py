# Declare tuples
prices = []
price_extremes = []

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
# Set high and low
high = float(data[1])
low = float(data[1])

for line in prices:
    if line != '}': # EOF is delimited with '}'
        data = line.split(':')
        date = data[0].split('-')
        year = date[2]
        if year == working_year: # If the next point of data is within the same year as the last
            if float(data[1]) > high:
                high = float(data[1])
            elif float(data[1]) < low:
                low = float(data[1])
        else: # If data is from the next year, reset high and low and begin again
            price_extremes.append(working_year + " : " + str(high) + " | " + str(low))
            working_year = year
            high = float(data[1])
            low = float(data[1])
    else: # Save final data
        price_extremes.append(working_year + " : " + str(high) + " | " + str(low))

for line in price_extremes:
    print(line)