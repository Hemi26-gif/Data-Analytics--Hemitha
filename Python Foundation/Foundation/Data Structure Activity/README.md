# Nova University — Student Management & Academic Service System

## Business purpose
A console-based Python application for university administration to register and search students, maintain courses, marks and attendance, calculate results, view statistics, and process student withdrawals.

## Problem statement
Nova University needs one simple console program to replace several manual student-service activities. The application keeps student details together, validates input, prevents duplicate student IDs and course registrations, and provides basic academic summaries.

## Requirements and scope
- Python terminal/console application only.
- No GUI, website, mobile application, or database is required.
- Records are stored in memory; data resets when the program exits.
- One complete program supports repeated operations through a menu.

## Features
- Register, search, update, list, and withdraw students.
- Validate unique Student IDs and department codes.
- Add and remove courses without duplicate course registration.
- Add/update marks and calculate total, average, pass/fail, and grade.
- Update attendance and check examination eligibility at 75% or above.
- Show department information, course overlap, statistics, and batch academic summaries.
- Validate numeric ranges and handle unknown menu choices.

## Business rules
1. Student IDs are unique.
2. Department code must be one of CSE, IT, AI&DS, ECE, or BBA.
3. Attendance and marks must be from 0 to 100.
4. Attendance >= 75% means eligible for semester examination.
5. A subject mark >= 50 is considered a pass; the student passes only if all entered subject marks are >= 50.
6. Grade is based on average: 90–100 A, 80–89 B, 70–79 C, 60–69 D, 50–59 E, below 50 F.
7. A student cannot register for the same course twice.
8. Withdrawal marks a student inactive; their record is retained but excluded from active processing.
9. The application has no permanent storage; records last only for the current run.

## Data structures
See `design/data_structure_design.md`.

## Run the application
1. Install Python 3 if it is not already installed.
2. Open a terminal in this project folder.
3. Run `python student_service_portal.py` (on some systems use `python3 student_service_portal.py`).
4. Select a menu number and follow the prompts.
5. Choose `0` to exit.

## Suggested demo
Register two students, add course registrations, enter marks and attendance, view results, run statistics, and withdraw one student. Search and try duplicate IDs to demonstrate validation.

## Testing
Test scenarios are listed in `testing/test_cases.md`. Record actual outcomes after running each test.

## Assumptions
- The BRD does not define a required email or phone format, so the program only checks that these fields are not empty.
- Marks are entered per subject, and the student passes only if every entered subject mark is at least 50.
- Grade is based on average marks.
- The sample course overlap analysis accepts two comma-separated groups of Student IDs.
- Data persistence and authentication are outside the BRD scope.
