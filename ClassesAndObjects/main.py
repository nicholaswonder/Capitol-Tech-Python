from Employee import Employee

def Display(emp: Employee):
    print(emp.GetName(), emp.GetId(), emp.GetDep(), emp.GetTitle())

one = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
two = Employee("Mark Jones", 39119, "IT", "Programmer")
three = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

Display(one)
Display(two)
Display(three)