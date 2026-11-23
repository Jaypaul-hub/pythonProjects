def add_student(students: dict[str, list[float]]) -> None:
    """Add a new student with an empty list of marks."""
    name = input("Andika jina la mwanafunzi: ").strip()
    if not name:
        print("Jina haliwezi kuwa tupu.")
        return
    if name in students:
        print(f"Mwanafunzi '{name}' tayari yupo.")
        return
    students[name] = []
    print(f"Mwanafunzi '{name}' ameongezwa.")


def add_marks(students: dict[str, list[float]]) -> None:
    """Add a validated mark (0-100) to an existing student."""
    name = input("Andika jina la mwanafunzi wa kumuongezea alama: ").strip()
    if name not in students:
        print("Mwanafunzi hajapatikana.")
        return
    mark = get_float("Andika alama (0 - 100): ", 0.0, 100.0)
    students[name].append(mark)
    print(f"Alama {mark} imeongezwa kwa {name}.")


def calculate_average(marks: list[float]) -> float | None:
    """Return average of marks, or None if the student has no marks yet."""
    if not marks:
        return None
    return sum(marks) / len(marks)


def view_all(students: dict[str, list[float]]) -> None:
    """Display all students, their marks, and individual averages."""
    if not students:
        print("Hakuna wanafunzi waliorekodiwa bado.")
        return
    for name, marks in students.items():
        avg = calculate_average(marks)
        avg_text = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"- {name}: alama={marks} | wastani={avg_text}")


def search_student(students: dict[str, list[float]]) -> None:
    """Search for a student by name and show their marks and average."""
    name = input("Andika jina la mwanafunzi unayemtafuta: ").strip()
    if name not in students:
        print(f"Hakuna mwanafunzi mwenye jina '{name}'.")
        return
    marks = students[name]
    avg = calculate_average(marks)
    avg_text = f"{avg:.2f}" if avg is not None else "N/A"
    print(f"Jina: {name} | Alama: {marks} | Wastani: {avg_text}")


def class_average(students: dict[str, list[float]]) -> None:
    """Calculate and display the overall average across all recorded marks."""
    all_marks = [mark for marks in students.values() for mark in marks]
    if not all_marks:
        print("Hakuna alama zilizorekodiwa darasani bado.")
        return
    print(f"Wastani wa darasa: {sum(all_marks) / len(all_marks):.2f}")


def top_three_students(students: dict[str, list[float]]) -> None:
    """Display up to the top 3 students ranked by their average score."""
    ranked = []
    for name, marks in students.items():
        avg = calculate_average(marks)
        if avg is not None:
            ranked.append((avg, name))

    if not ranked:
        print("Hakuna wanafunzi wenye alama za kulinganisha.")
        return

    ranked.sort(reverse=True)
    print("\n--- Top 3 Students ---")
    for rank, (avg, name) in enumerate(ranked[:3], start=1):
        print(f"{rank}. {name} — Wastani: {avg:.2f}")


def get_float(prompt: str, min_val: float | None = None, max_val: float | None = None) -> float:
    """Prompt the user for a float and validate optional min/max limits."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Tafadhali weka namba sahihi.")
            continue
        if min_val is not None and value < min_val:
            print(f"Namba isipungue {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"Namba isizidi {max_val}.")
            continue
        return value


def main() -> None:
    """Run the main menu loop for the student grade manager."""
    students: dict[str, list[float]] = {}

    while True:
        print("\n=== STUDENT GRADE MANAGER ===")
        print("1. Add student")
        print("2. Add marks")
        print("3. View all")
        print("4. Search")
        print("5. Class average")
        print("6. Top 3 students")
        print("7. Quit")

        choice = input("Chagua namba (1-7): ").strip()
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
            print("Kwaheri!")
            break
        else:
            print("Chaguo batili. Chagua kati ya 1 na 7.")


if __name__ == "__main__":
    main()