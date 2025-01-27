import os


def display_menu():
    print("\nStudent Record Management System")
    print("1. Add Student Record")
    print("2. Update Student Record")
    print("3. Delete Student Record")
    print("4. Search Student Record")
    print("5. View All Students")
    print("6. Save Records to File")
    print("7. Load Records from File")
    print("8. Exit")

def add_student(students):
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    grades = input("Enter student's grades: ")
    students[roll_number] = {"name": name, "grades": grades}
    print(f"Student {name} added successfully!")


def update_student(students):
    roll_number = input("Enter student's roll number to update: ")
    if roll_number in students:
        name = input("Enter new name: ")
        grades = input("Enter new grades: ")
        students[roll_number] = {"name": name, "grades": grades}
        print("Student record updated!")
    else:
        print("Student not found!")


def delete_student(students):
    roll_number = input("Enter student's roll number to delete: ")
    if roll_number in students:
        del students[roll_number]
        print("Student record deleted!")
    else:
        print("Student not found!")


def search_student(students):
    search_choice = input("Search by (1) Name or (2) Roll Number: ")
    if search_choice == "1":
        name = input("Enter student's name: ")
        found = False
        for roll_number, details in students.items():
            if details["name"].lower() == name.lower():
                print(f"Found: Roll Number: {roll_number}, Name: {details['name']}, Grades: {details['grades']}")
                found = True
        if not found:
            print("No student found with that name.")
    elif search_choice == "2":
        roll_number = input("Enter student's roll number: ")
        if roll_number in students:
            details = students[roll_number]
            print(f"Found: Roll Number: {roll_number}, Name: {details['name']}, Grades: {details['grades']}")
        else:
            print("No student found with that roll number.")


def view_all_students(students):
    if students:
        print("\nAll Student Records:")
        for roll_number, details in students.items():
            print(f"Roll Number: {roll_number}, Name: {details['name']}, Grades: {details['grades']}")
    else:
        print("No student records available.")


def save_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for roll_number, details in students.items():
            file.write(f"{roll_number},{details['name']},{details['grades']}\n")
    print("Records saved to file.")


def load_from_file(students, filename="students.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                roll_number, name, grades = line.strip().split(",")
                students[roll_number] = {"name": name, "grades": grades}
        print("Records loaded from file.")
    else:
        print("No previous records found.")


def main():
    students = {}
    load_from_file(students)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            view_all_students(students)
        elif choice == "6":
            save_to_file(students)
        elif choice == "7":
            load_from_file(students)
        elif choice == "8":
            print("Exiting program...")
            save_to_file(students)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
