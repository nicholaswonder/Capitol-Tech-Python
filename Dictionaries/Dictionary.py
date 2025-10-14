def wait():
    input("Press Enter to Continue...")

# Course Info
course_rooms = {
    "CS101" : 3004,
    "CS102" : 4501,
    "CS103" : 6755,
    "NT110" : 1244,
    "CM241" : 1411
}

course_instructors = {
    "CS101" : "Haynes",
    "CS102" : "Alvarado",
    "CS103" : "Rich",
    "NT110" : "Burke",
    "CM241" : "Lee"
}

course_times = {
    "CS101" : "8:00 am",
    "CS102" : "9:00 am",
    "CS103" : "10:00 am",
    "NT110" : "11:00 am",
    "CM241" : "1:00 pm"
}
print("Choose a course from the following selection to see its information")
print("CS101, CS102, CS103, NT110, CM241")
course = input("Type in the course number: ")
print(course_rooms[course], course_times[course], course_instructors[course])
wait()

# Unique Words
unique_words = []
with open("Words.txt") as file:
    for line in file:
        word = line.rstrip()
        if not unique_words.__contains__(word):
            unique_words.append(word)

print(unique_words)
wait()