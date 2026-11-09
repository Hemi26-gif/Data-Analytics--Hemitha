class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def display_basic_info(self):
        print(f"Name: {self.name} | Email: {self.email} | Phone: {self.phone}")


class Student(Person):
    def __init__(self, student_id, name, email, phone, department,
                 attendance, python_marks, sql_marks, excel_marks):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.department = department
        self.attendance = attendance
        self.python_marks = self._validate_mark(python_marks, "Python")
        self.sql_marks = self._validate_mark(sql_marks, "SQL")
        self.excel_marks = self._validate_mark(excel_marks, "Excel")

    @staticmethod
    def _validate_mark(value, subject):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"{subject} marks must be numeric.")
        if not 0 <= value <= 100:
            raise ValueError(f"{subject} marks must be between 0 and 100.")
        return value

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Attendance must be numeric.")
        if not 0 <= value <= 100:
            raise ValueError("Attendance must be between 0 and 100.")
        self._attendance = value

    def is_exam_eligible(self):
        return self.attendance >= 75

    def total_marks(self):
        return self.python_marks + self.sql_marks + self.excel_marks

    def average_marks(self):
        return self.total_marks() / 3

    def result_status(self):
        return "PASS" if self.average_marks() >= 50 else "FAIL"

    def grade(self):
        # Grade bands are a design choice; the BRD does not specify them.
        avg = self.average_marks()
        if avg >= 90: return "A"
        if avg >= 80: return "B"
        if avg >= 70: return "C"
        if avg >= 60: return "D"
        if avg >= 50: return "E"
        return "F"

    def display_academic_info(self):
        print(f"\nStudent ID: {self.student_id}")
        self.display_basic_info()
        print(f"Department: {self.department}")
        print(f"Attendance: {self.attendance:.1f}%")
        print(f"Python: {self.python_marks:.1f} | SQL: {self.sql_marks:.1f} | Excel: {self.excel_marks:.1f}")
        print(f"Total: {self.total_marks():.1f}/300")
        print(f"Average: {self.average_marks():.2f}%")
        print(f"Result: {self.result_status()} | Grade: {self.grade()}")
        print("Exam eligibility:", "Eligible" if self.is_exam_eligible() else "Not eligible")


class Faculty(Person):
    def __init__(self, faculty_id, name, email, phone, department, subject):
        super().__init__(name, email, phone)
        self.faculty_id = faculty_id
        self.department = department
        self.subject = subject

    def display_info(self):
        print(f"\nFaculty ID: {self.faculty_id}")
        self.display_basic_info()
        print(f"Department: {self.department} | Subject: {self.subject}")


class University:
    DEPARTMENTS = ["CSE", "IT", "AI&DS", "ECE", "BBA"]

    def __init__(self):
        self.students = {}
        self.faculty_members = {}

    @staticmethod
    def read_text(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This field cannot be empty.")

    @staticmethod
    def read_number(prompt, minimum=0, maximum=100):
        while True:
            try:
                value = float(input(prompt).strip())
                if minimum <= value <= maximum:
                    return value
                print(f"Enter a value from {minimum} to {maximum}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_department(self):
        print("Departments:", ", ".join(self.DEPARTMENTS))
        while True:
            value = self.read_text("Department: ").upper()
            if value in self.DEPARTMENTS:
                return value
            print("Choose a department shown above.")

    def add_student(self):
        print("\n--- Add Student ---")
        sid = self.read_text("Student ID: ")
        if sid in self.students:
            print("Student ID already exists.")
            return
        name = self.read_text("Name: ")
        email = self.read_text("Email: ")
        phone = self.read_text("Phone: ")
        department = self.choose_department()
        attendance = self.read_number("Attendance (0-100): ")
        py = self.read_number("Python marks (0-100): ")
        sql = self.read_number("SQL marks (0-100): ")
        excel = self.read_number("Excel marks (0-100): ")
        student = Student(sid, name, email, phone, department, attendance, py, sql, excel)
        self.students[sid] = student
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students added yet.")
            return
        for s in self.students.values():
            print(f"{s.student_id} | {s.name} | {s.department} | Attendance {s.attendance:.1f}%")

    def find_student(self):
        sid = self.read_text("Student ID: ")
        student = self.students.get(sid)
        if student is None:
            print("Student not found.")
        return student

    def check_attendance(self):
        student = self.find_student()
        if student:
            print(f"{student.name}: {student.attendance:.1f}%")
            print("Eligible for exam." if student.is_exam_eligible()
                  else "Not eligible: attendance must be at least 75%.")

    def view_result(self):
        student = self.find_student()
        if student:
            student.display_academic_info()

    def add_faculty(self):
        print("\n--- Add Faculty ---")
        fid = self.read_text("Faculty ID: ")
        if fid in self.faculty_members:
            print("Faculty ID already exists.")
            return
        name = self.read_text("Name: ")
        email = self.read_text("Email: ")
        phone = self.read_text("Phone: ")
        department = self.choose_department()
        subject = self.read_text("Subject handled: ")
        self.faculty_members[fid] = Faculty(fid, name, email, phone, department, subject)
        print("Faculty added successfully.")

    def view_faculty(self):
        if not self.faculty_members:
            print("No faculty members added yet.")
            return
        for faculty in self.faculty_members.values():
            faculty.display_info()

    def run(self):
        while True:
            print("\n===== NOVA UNIVERSITY =====")
            print("1. Add Student\n2. View Students\n3. Check Attendance Eligibility")
            print("4. View Academic Result\n5. Add Faculty\n6. View Faculty\n7. Exit")
            choice = input("Choose an option (1-7): ").strip()
            if choice == "1": self.add_student()
            elif choice == "2": self.view_students()
            elif choice == "3": self.check_attendance()
            elif choice == "4": self.view_result()
            elif choice == "5": self.add_faculty()
            elif choice == "6": self.view_faculty()
            elif choice == "7":
                print("Thank you for using Nova University Student Management.")
                break
            else:
                print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    University().run()
