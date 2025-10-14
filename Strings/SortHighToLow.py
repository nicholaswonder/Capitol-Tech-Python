# Declare tuples
prices = []

# Get data from file
with open("GasPrices-1.txt") as file:
    for line in file:
        if line != '}':
            price = line
            # Get rid of extra slash and newline characters from strings
            price = price.replace('\\','')
            price = price.replace('\n', '')
            data = price.split(':')
            data[1] = float(data[1])
            unsorted_data = [data[1], data[0]]  # Reverse the data so the sort function sorts by price and not date
            prices.append(unsorted_data)
    file.close()

prices.sort(reverse=True)

with open("GasPricesHighToLow.txt", 'w') as file:
    for item in prices:
        line = str(item[0]) + " : " + item[1] + '\n'
        file.write(line)