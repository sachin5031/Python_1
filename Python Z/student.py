# Student Management System
students = {}

while True:
    print("\nStudent Management System:")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. View All Students")
    print("4. Check Student Details")
    print("5. Exit")
    
    choice = input("Select your choice: ")
    
    if choice == '1':
        while True:
            std_name = input("Enter the student's name: ")
            if std_name == "":
                print("Student name cannot be empty.")
                continue

            age_input = input("Enter the age: ")
            if not age_input.isdigit() or int(age_input) <= 0:
                print("Age must be a positive number.")
                continue

            age = int(age_input)

            marks_input = input("Enter the marks: ")
            if not marks_input.isdigit() or int(marks_input) < 0:
                print("Marks must be a non-negative number.")
                continue

            marks = int(marks_input)

            students[std_name] = {"Age": age, "Marks": marks}
            print(f"Student '{std_name}' was added successfully.")
            
            add_more = input("Do you want to add another student? (yes/no): ")
            if add_more.lower() != 'yes':
                break
    
    elif choice == '2':
        std_name = input("Enter the student's name to remove: ")
        if std_name in students:
            del students[std_name]
            print(f"Student '{std_name}' was removed successfully.")
        else:
            print(f"Student '{std_name}' not found.")
    
    elif choice == '3':
        if len(students) > 0:
            print("\nList of all students:")
            student_names = list(students.keys())
            i = 0
            while i < len(student_names):
                name = student_names[i]
                print("Name: " + name + ", Age: " + str(students[name]["Age"]) + ", Marks: " + str(students[name]["Marks"]))
                i += 1
        else:
            print("No students found.")
    
    elif choice == '4':
        std_name = input("Enter the name of the student to check: ")
        if std_name in students:
            print("Details of " + std_name + ": Age: " + str(students[std_name]["Age"]) + ", Marks: " + str(students[std_name]["Marks"]))
        else:
            print(f"Student '{std_name}' not found.")
    
    elif choice == '5':
        print("Exiting the program...")
        break
    
    else:
        print("Invalid choice. Please try again.")
