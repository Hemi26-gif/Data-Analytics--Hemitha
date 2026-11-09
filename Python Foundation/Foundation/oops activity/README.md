<img width="479" height="365" alt="Output 9" src="https://github.com/user-attachments/assets/bce3a6ef-424d-4f28-96e7-248e40fc0ee1" />

# Nova University – Student Management Module

## Purpose
A Python console application to maintain multiple student and faculty records, check attendance eligibility, and calculate academic results.

## Design
- `Person`: common name, email, and phone.
- `Student(Person)`: student details, validated attendance, marks, result and grade.
- `Faculty(Person)`: faculty-specific details.
- `University`: stores multiple objects and manages the console menu.

## OOP concepts
- Classes and objects
- Inheritance (`Student` and `Faculty` inherit from `Person`)
- Encapsulation (attendance is validated using a property)
- Reusable methods for total, average, pass/fail, grade and attendance eligibility

## Rules
- Attendance: 0–100; exam eligible at 75% or above.
- Each subject mark: 0–100.
- Average >= 50 means PASS.
- Grade bands in this implementation: A >= 90, B >= 80, C >= 70, D >= 60, E >= 50, F < 50. The BRD asks for grades but does not specify the bands, so these are implementation choices.

## Run
Open a terminal in this folder and run `python main.py` (or `py main.py` on Windows).

## Manual testing
1. Attendance 75: eligible.
2. Attendance 0 and 100: accepted.
3. Attendance -5 or 105: rejected.
4. Enter letters instead of a number: error message and retry.
5. Add two students with different IDs: both should display.
6. Average exactly 50: PASS.
7. Average below 50: FAIL.
8. Add a faculty member and view faculty.


