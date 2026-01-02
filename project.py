import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("✅ Student added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        print("\n--- Student Records ---")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
    print()


def search_student():
    roll_no = input("Enter roll number to search: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_no:
                print(f"\n🎯 Found: {name} | Marks: {marks}\n")
                return

    print("❌ Student not found.\n")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            roll, name, marks = line.strip().split(",")
            if roll != roll_no:
                file.write(line)
            else:
                found = True

    if found:
        print("🗑️ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program. Bye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


main()
