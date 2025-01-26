def add_student(students):
    name = input("enter student's name:")
    roll_no = input("enter student's roll  number(4 digits):")
    grades = input("enter student's grades:")
    students[roll_no] = {"name": name , "grades": grades}

def up_student(students):
    roll_no = input("enter student's roll  number(4 digits) to update:")
    if roll_no in students:
        name = input("enter new student's name:")
        grades = input("enter new student's grades:")
        students[roll_no] = {"name": name, "grades": grades}
    else:
        print("student not found")

def delete_student(students) :
    roll_no = input("enter student's roll  number(4 digits) to delete:")
    if roll_no in students:
        del students[roll_no]
    else:
        print("student not found")


def main():
    students = {}

    while True:
        print("1. Add student")
        print("2. Update student record")
        print("3. Delete student record")
        print("4. search student record")
        print("5. view all student records")
        print("6. exit")
        choice = int(input("choose an option:"))

        if choice == 1:
            add_student(students)
        elif choice == 2:
            up_student(students)
        elif choice == 3:
            delete_student(students)

