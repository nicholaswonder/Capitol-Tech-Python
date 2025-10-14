import matplotlib.pyplot as plt

def wait():
    input("Press Enter to Continue")

# Line graph
x_coords = [0, 1, 2, 3, 4]
y_coords = [0, 3, 1, 5, 2]

plt.plot(x_coords,y_coords)
plt.show()

# Line Graph 2
plt.plot(x_coords,y_coords)
plt.title('Sample Data')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# Line Graph 3
plt.plot(x_coords,y_coords)
plt.title('Sample Data')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-1, 10)
plt.ylim(-1, 6)
plt.grid(True)
plt.show()

# Line Graph 4
plt.plot(x_coords,y_coords)
plt.title('Sales by Year')
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks([0,1,2,3,4], ['2016','2017','2018','2019','2020'])
plt.yticks([0,1,2,3,4,5], ['$0m','$1m','$2m','$3m','$4m','$5m'])
plt.grid(True)
plt.show()

# Line Graph 5
plt.plot(x_coords,y_coords, marker='o')
plt.title('Sales by Year')
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks([0,1,2,3,4], ['2016','2017','2018','2019','2020'])
plt.yticks([0,1,2,3,4,5], ['$0m','$1m','$2m','$3m','$4m','$5m'])
plt.grid(True)
plt.show()

# Bar Chart 1
left_edges = [0,10,20,30,40]
heights = [100,200,300,400,500]
plt.bar(left_edges,heights)
plt.show()

# Bar Chart 2
bar_width = 5
plt.bar(left_edges,heights, bar_width)
plt.show()

# Bar Chart 3
bar_width = 10
plt.bar(left_edges,heights, bar_width, color=('r','g','b','w','k'))
plt.title('Sales by Year')
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks([5,15,25,35,45], ['2016','2017','2018','2019','2020'])
plt.yticks([0,100,200,300,400,500], ['$0m','$1m','$2m','$3m','$4m','$5m'])
plt.show()

# Pie Chart
values = [20,60,80,40]
plt.pie(values)
plt.show()

# Pie Chart 2
sales = [100,400,300,600]
slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
plt.pie(values, labels=slice_labels)
plt.show()

# Expense Pie Chart
f = open("Expenses.txt")
line = f.readline().split(",")
expenses = []
for category in line:
    expenses.append(int(category))
slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
plt.pie(expenses, labels=slice_labels)
plt.show()