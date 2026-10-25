#Student_Marks_Manager

students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}
topper=""
highest_average=-1

for name in students:
    total = 0
    for mark in students[name]:
        total += mark
    average = total / len(students[name])

    if average>=85:
        grade="A"
    elif average>=70:
        grade="B"
    elif average>=50:
        grade="C"
    else:
        grade="F"
    print(name, round(average, 2),grade)

    if average>highest_average:
        highest_average=average
        topper=name
print("Topper:",topper)
while True:
    print("=====Student Management Menu=====\n" 
    "1.Add student\n" 
    "2.View all\n" 
    "3.Show topper\n" 
    "4.Exit")
    choice=int(input("Choose the option:"))
    if choice==1:
        name=input("Enter student name: ")
        if name in students:
            print("Student already exists.")
        else:
            marks=[]
            for i in range(3):
                mark=int(input("Enter mark: "))
                marks.append(mark)
                break
            students[name]=marks
            print("Student added successfully.")
            
    elif choice==2:
        for name in students:
            total=0
            for mark in students[name]:
                total+=mark
            average = total / len(students[name])

            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"
            print(name, round(average, 2), grade)
    elif choice==3:
        topper = ""
        highest_average = -1

        for name in students:
            total = 0

            for mark in students[name]:
                total += mark

            average = total / len(students[name])

            if average > highest_average:
                highest_average = average
                topper = name

        print("Topper:", topper)
        print("Highest Average:", round(highest_average, 2))

    elif choice==4:
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Try again.")
