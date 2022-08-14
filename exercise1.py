import statistics

admins = {"Python": "999", "user2": "888"}

listofStudentsandGrades = {"Alex": [92, 76, 88],
                          "Jeff": [78, 88, 93],
                          "Sam": [89, 92, 93]}
def enterGrades():
    studentName = input("Student Name: ")
    grade = float(input("Grade: "))
    if studentName in listofStudentsandGrades:
        print("Adding Grade...")
        listofStudentsandGrades[studentName].append(grade)
    else:
        print("Student does not exist")
    print(listofStudentsandGrades)

def removeStudent():
    studentNameToRemove = input("Student Name to remove: ")
    if studentNameToRemove in listofStudentsandGrades:
        print(f"Removing {studentNameToRemove}...")
        del listofStudentsandGrades[studentNameToRemove]
    else:
        print("Student does not exist")
    print(listofStudentsandGrades)

def studentAVGs():
    for eachStudent in listofStudentsandGrades:
        gradeList = listofStudentsandGrades[eachStudent]
        averageGrade = statistics.mean(gradeList)
        print(eachStudent, "has an average grade of: ", averageGrade)

def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    
    """)

    action = input("What would you like to do today? (Enter a number) ")

    if action == "1":
        enterGrades()
    elif action == "2":
        removeStudent()
    elif action == "3":
        studentAVGs()
    elif action == "4":
        exit()
    else:
        print("Invalid Number")

login = input("Username: ")
passw = input("Password: ")

if login in admins:
    if admins[login] == passw:
        print("Welcome, ", login)
        while True:
            main()
    else:
        print("Invalid Password")
else:
    print("Invalid Username")