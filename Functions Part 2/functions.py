import random

# Paint Job Estimator
def EstimateJob(area, cost):
    Gallons = area / 112.0   # 112 square feet takes one gallon of paint
    TotalPaintCost = Gallons * cost
    Hours = Gallons * 8         # Each gallon of paint takes 8 hours
    Charge = 35 * Hours
    print("Square footage of job:", area)
    print("Gallons of paint required:", Gallons)
    print("Total cost of paint:", TotalPaintCost)
    print("Work hours required:", Hours)
    print("Cost of labor:", Charge)

JobArea = float(input("Enter the square footage of the wall to be painted: "))
PaintCost = float(input("Enter the price per gallon of paint: $"))
EstimateJob(JobArea, PaintCost)
print() # WhiteSpace

# Rock Paper Scissors
