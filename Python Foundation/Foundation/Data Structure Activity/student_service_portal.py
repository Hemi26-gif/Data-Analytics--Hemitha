"""
Nova University - Student Management & Academic Service System
Console-only Python application. Data is stored in memory for the current session.
"""

DEPARTMENTS = {
    "CSE": "Computer Science & Engineering",
    "IT": "Information Technology",
    "AI&DS": "Artificial Intelligence & Data Science",
    "ECE": "Electronics & Communication Engineering",
    "BBA": "Business Administration",
}
PASS_MARK = 50
MIN_ATTENDANCE = 75.0


def get_student(student_id, include_inactive=False):
    """Return a student record if found; otherwise return None."""
    student = students.get(student_id.strip().upper())
    if student and (include_inactive or student["active"]):
        return student
    return None


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def input_number(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def display_departments():
    print("\nAvailable departments:")
    for code, name in DEPARTMENTS.items():
        print(f"  {code} - {name}")


def register_student():
    print("\n--- Student Registration ---")
    student_id = input_non_empty("Student ID: ").upper()
    if student_id in students:
        print("Registration rejected: this Student ID already exists.")
        return
    name = input_non_empty("Student name: ")
    display_departments()
    department = input_non_empty("Department code: ").upper()
    if department not in DEPARTMENTS:
        print("Invalid department. Registration cancelled.")
        return
    year = int(input_number("Year (1-4): ", 1, 4))
    email = input_non_empty("Email: ")
    phone = input_non_empty("Phone number: ")
    attendance = input_number("Attendance percentage (0-100): ", 0, 100)

    students[student_id] = {
        "student_id": student_id,
        "name": name,
        "department": department,
        "year": year,
        "email": email,
        "phone": phone,
        "attendance": attendance,
        "marks": {},
        "courses": set(),
        "active": True,
    }
    print(f"Student {student_id} registered successfully.")


def show_student(student):
    print("\n--- Student Details ---")
    print(f"ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']} - {DEPARTMENTS[student['department']]}")
    print(f"Year: {student['year']}")
    print(f"Email: {student['email']}")
    print(f"Phone: {student['phone']}")
    print(f"Attendance: {student['attendance']:.1f}%")
    print(f"Eligibility: {'Eligible' if student['attendance'] >= MIN_ATTENDANCE else 'Not eligible'}")
    print(f"Courses: {', '.join(sorted(student['courses'])) if student['courses'] else 'None'}")
    print(f"Marks: {student['marks'] if student['marks'] else 'No marks entered'}")
    print(f"Academic status: {'Active' if student['active'] else 'Withdrawn'}")


def search_student():
    student_id = input_non_empty("Enter Student ID: ").upper()
    student = get_student(student_id)
    if student:
        show_student(student)
    else:
        print("No active student found with that ID.")


def update_student():
    student_id = input_non_empty("Enter Student ID to update: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    print("1. Name  2. Email  3. Phone  4. Year  5. Department")
    choice = input("Choose field to update: ").strip()
    if choice == "1":
        student["name"] = input_non_empty("New name: ")
    elif choice == "2":
        student["email"] = input_non_empty("New email: ")
    elif choice == "3":
        student["phone"] = input_non_empty("New phone: ")
    elif choice == "4":
        student["year"] = int(input_number("New year (1-4): ", 1, 4))
    elif choice == "5":
        display_departments()
        department = input_non_empty("New department code: ").upper()
        if department not in DEPARTMENTS:
            print("Invalid department; no changes made.")
            return
        student["department"] = department
    else:
        print("Invalid choice.")
        return
    print("Student information updated.")


def register_course():
    student_id = input_non_empty("Student ID: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    course = input_non_empty("Course name: ").title()
    if course in student["courses"]:
        print("Duplicate course registration rejected.")
        return
    student["courses"].add(course)
    print(f"{course} added for {student_id}.")


def remove_course():
    student_id = input_non_empty("Student ID: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    course = input_non_empty("Course name to remove: ").title()
    if course in student["courses"]:
        student["courses"].remove(course)
        print(f"{course} removed.")
    else:
        print("This student is not registered for that course.")


def manage_attendance():
    student_id = input_non_empty("Student ID: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    print(f"Current attendance: {student['attendance']:.1f}%")
    student["attendance"] = input_number("New attendance (0-100): ", 0, 100)
    eligible = student["attendance"] >= MIN_ATTENDANCE
    print(f"Attendance updated. Exam eligibility: {'Eligible' if eligible else 'Not eligible'}.")


def manage_marks():
    student_id = input_non_empty("Student ID: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    subject = input_non_empty("Subject name (e.g. Python, SQL): ").title()
    mark = input_number("Mark (0-100): ", 0, 100)
    student["marks"][subject] = mark
    print(f"{subject} mark saved as {mark:g}.")


def get_result(student):
    marks = student["marks"]
    if not marks:
        return None
    total = sum(marks.values())
    average = total / len(marks)
    passed = all(mark >= PASS_MARK for mark in marks.values())
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 50:
        grade = "E"
    else:
        grade = "F"
    eligible = student["attendance"] >= MIN_ATTENDANCE
    return {"total": total, "average": average, "passed": passed,
            "grade": grade, "eligible": eligible}


def show_result():
    student_id = input_non_empty("Student ID: ").upper()
    student = get_student(student_id)
    if not student:
        print("No active student found.")
        return
    result = get_result(student)
    if result is None:
        print("No marks available for this student yet.")
        return
    print("\n--- Examination Result ---")
    print(f"Student: {student['name']} ({student_id})")
    for subject, mark in student["marks"].items():
        print(f"{subject}: {mark:g}")
    print(f"Total: {result['total']:g}")
    print(f"Average: {result['average']:.2f}")
    highest_subject = max(student["marks"], key=student["marks"].get)
    failed_subjects = [subject for subject, mark in student["marks"].items() if mark < PASS_MARK]
    print(f"Highest mark: {student['marks'][highest_subject]:g} ({highest_subject})")
    print(f"Failed subjects: {', '.join(failed_subjects) if failed_subjects else 'None'}")
    print(f"Pass/Fail: {'Pass' if result['passed'] else 'Fail'}")
    print(f"Grade: {result['grade']}")
    print(f"Exam eligibility (attendance): {'Eligible' if result['eligible'] else 'Not eligible'}")


def academic_summary():
    active_students = [s for s in students.values() if s["active"]]
    if not active_students:
        print("No active students to process.")
        return
    print("\n--- Academic Summary ---")
    for student in active_students:
        result = get_result(student)
        average = f"{result['average']:.2f}" if result else "Not available"
        pass_fail = ("Pass" if result["passed"] else "Fail") if result else "Not available"
        grade = result["grade"] if result else "Not available"
        eligibility = "Eligible" if student["attendance"] >= MIN_ATTENDANCE else "Not eligible"
        print(f"{student['student_id']} | {student['name']} | Attendance: {student['attendance']:.1f}% "
              f"| {eligibility} | Average: {average} | {pass_fail} | Grade: {grade}")


def department_information():
    display_departments()
    represented = {s["department"] for s in students.values() if s["active"]}
    print("Departments represented by active students:",
          ", ".join(sorted(represented)) if represented else "None")


def course_overlap_analysis():
    print("\nEnter Student IDs registered for each course, separated by commas.")
    python_entries = [item.strip().upper() for item in input("Python Training IDs: ").split(",") if item.strip()]
    sql_entries = [item.strip().upper() for item in input("SQL Training IDs: ").split(",") if item.strip()]
    python_ids = set(python_entries)
    sql_ids = set(sql_entries)
    python_duplicates = sorted({item for item in python_entries if python_entries.count(item) > 1})
    sql_duplicates = sorted({item for item in sql_entries if sql_entries.count(item) > 1})
    print("Duplicate IDs in Python group:", python_duplicates if python_duplicates else "None")
    print("Duplicate IDs in SQL group:", sql_duplicates if sql_duplicates else "None")
    print("Students in both courses:", sorted(python_ids & sql_ids))
    print("Python but not SQL:", sorted(python_ids - sql_ids))
    print("At least one course:", sorted(python_ids | sql_ids))
    print("Exactly one course:", sorted(python_ids ^ sql_ids))
    print("Duplicate IDs within each entered group are automatically removed by sets.")
    print("Groups completely different:", "Yes" if python_ids.isdisjoint(sql_ids) else "No")


def student_statistics():
    active_students = [s for s in students.values() if s["active"]]
    print("\n--- Student Statistics ---")
    print("Total active students:", len(active_students))
    department_counts = {}
    eligible_count = 0
    failed_count = 0
    averages = []
    for student in active_students:
        department_counts[student["department"]] = department_counts.get(student["department"], 0) + 1
        if student["attendance"] >= MIN_ATTENDANCE:
            eligible_count += 1
        result = get_result(student)
        if result:
            averages.append(result["average"])
            if not result["passed"]:
                failed_count += 1
    print("Students by department:", department_counts if department_counts else "None")
    print("Eligible students:", eligible_count)
    print("Students who failed:", failed_count)
    if averages:
        print(f"Highest average: {max(averages):.2f}")
        print(f"Lowest average: {min(averages):.2f}")
        print(f"Batch average performance: {sum(averages) / len(averages):.2f}")
    else:
        print("Average statistics unavailable because no active student has marks.")
    print("Unique departments represented:",
          sorted({s["department"] for s in active_students}))
    course = input("Optional: enter a course to count registered students (or press Enter to skip): ").strip().title()
    if course:
        count = sum(course in s["courses"] for s in active_students)
        print(f"Students registered for {course}: {count}")


def withdraw_student():
    student_id = input_non_empty("Student ID to withdraw: ").upper()
    student = get_student(student_id, include_inactive=True)
    if not student:
        print("Student ID not found.")
        return
    if not student["active"]:
        print("This student is already withdrawn.")
        return
    show_student(student)
    confirm = input("Confirm withdrawal? (y/n): ").strip().lower()
    if confirm == "y":
        student["active"] = False
        print("Student marked as withdrawn and excluded from active processing.")
    else:
        print("Withdrawal cancelled.")


def list_active_students():
    active_students = [s for s in students.values() if s["active"]]
    if not active_students:
        print("No active students.")
        return
    for student in active_students:
        print(f"{student['student_id']} - {student['name']} ({student['department']})")


def main():
    while True:
        print("""
========== NOVA UNIVERSITY ==========
1. Register student
2. Search student
3. Update student information
4. List active students
5. Register course
6. Remove course
7. Update attendance
8. Add/update marks
9. View examination result
10. Department information
11. Course overlap analysis
12. Student statistics
13. Student withdrawal
14. Academic summary for all students
0. Exit
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            register_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            list_active_students()
        elif choice == "5":
            register_course()
        elif choice == "6":
            remove_course()
        elif choice == "7":
            manage_attendance()
        elif choice == "8":
            manage_marks()
        elif choice == "9":
            show_result()
        elif choice == "10":
            department_information()
        elif choice == "11":
            course_overlap_analysis()
        elif choice == "12":
            student_statistics()
        elif choice == "13":
            withdraw_student()
        elif choice == "14":
            academic_summary()
        elif choice == "0":
            print("Thank you for using Nova University Student Services.")
            break
        else:
            print("Invalid menu selection. Choose an available option.")


students = {}

if __name__ == "__main__":
    main()
