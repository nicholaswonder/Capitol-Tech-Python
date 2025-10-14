
grade = float(input("Enter a grade: "))

if 0.0 <= grade <= 100.0:
    if grade >= 90.0:
        print(grade, 'A')
    elif grade >= 80.0:
        print(grade, 'B')
    elif grade >= 70.0:
        print(grade, 'C')
    elif grade >= 60.0:
        print(grade, 'D')
    else:
        print(grade, 'F')
else:
    print("Grade not valid")
