students=[]
#Creating A Menu that goes for a loop 
while True:
    print("\n----STUDENT MANAGEMENT SYSTEM----")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Delete Student")
    print("5. Exit")
#Ask for choice from user
    choice=input("Enter your choice: ")
    if choice == "1":
        name=input("Enter Students Name: ")
        roll=int(input("Enter roll number: "))
        student = {
            "name":name,
            "roll":roll
        }
        students.append(student)
        print("Student addedd Successfully!")
#First choice asked from user and addedd
    elif choice == "2":
        if len(students) == 0:
            print("No Student Found!")
        else:
            print("\nStudent List:")
            for student in students:
                print("Name: ",student["name"])
                print("Roll:",student["roll"])
#Second choice asked from user
    elif choice == "3":
        search_name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student Found!")
                print("Name: ",student["name"])
                print("Roll_number: ",student["roll"])
                found = True
            if not found:
                print("Student Not Found!")
#Third choice asked from user
    elif choice == "4":
        delete_name = input("Enter the name to delete: ")
        found = False
        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted Successfully")
                found = True
                break
            if not found:
                print("Student not found!")
#Fourth choice asked from user
    elif choice == "5":
        print("Program exited.")
        break
    else:
        print("Invalid Choice")
