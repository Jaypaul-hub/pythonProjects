def add_student(students):
    name = input("Enter student name: ").strip()

    if name == "":
        print("Please type a name.")
        return

    if name in students:
        print("That student is already in the list.")
        return
    #hapa tunaanza na empty list
    students[name] = []
    print("Added " + name)

def add_marks(students):
    name = input("Whose mark are you adding? ").strip()
    if name not in students:
        print("Student not found.")
        return
    try:
        mark = float(input("Enter mark (0 to 100): "))
    except ValueError:
        print("That is not a valid number.")
        return
    if mark < 0 or mark > 100:
        print("Mark should be between 0 and 100.")
        return
    students[name].append(mark)
    print("Mark added!")


def view_all(students):
    if len(students) == 0:
        print("No students added yet.")
        return

    for name, marks in students.items():
        if len(marks) == 0:
            print(name + " no marks yet")
        else:
            avg = sum(marks) / len(marks)
            print(f"{name} marks: {marks}, avg: {avg:.2f}")


def search_student(students):
    name = input("Enter student name to search: ").strip()

    if name in students:
        marks = students[name]
        print("Student:", name)
        print("Marks:", marks)
        if len(marks) > 0:
            avg = sum(marks) / len(marks)
            print(f"Average: {avg:.2f}")
        else:
            print("Average: no marks yet")
    else:
        print("Could not find that student.")


def class_average(students):
    total = 0
    count = 0

    for marks in students.values():
        for mark in marks:
            total = total + mark
            count = count + 1

    if count == 0:
        print("No marks entered in the class yet.")
        return

    avg = total / count
    print(f"Class average: {avg:.2f}")


def top_three_students(students):
    student_averages = []

    for name, marks in students.items():
        if len(marks) > 0:
            avg = sum(marks) / len(marks)
            student_averages.append((avg, name))

    if len(student_averages) == 0:
        print("No marks yet to rank students.")
        return
    student_averages.sort(reverse=True)

    print("Top students:")
    top_count = 0
    for avg, name in student_averages:
        if top_count == 3:
            break
        top_count = top_count + 1
        print(f"{top_count}. {name} ({avg:.2f})")


def main():
    """Main menu loop."""
    students = {}

    while True:
        print("\n=== Student Grades ===")
        print("1. Add student")
        print("2. Add marks")
        print("3. View all")
        print("4. Search")
        print("5. Class average")
        print("6. Top 3 students")
        print("7. Quit")

        choice = input("Pick an option (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_marks(students)
        elif choice == "3":
            view_all(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            class_average(students)
        elif choice == "6":
            top_three_students(students)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid choice, try 1 to 7.")


main()