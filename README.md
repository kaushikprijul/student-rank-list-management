# 🎓 Student Rank List Management System

A Python-based Student Rank List Management System developed using **Object-Oriented Programming (OOP)** principles.

The program accepts student details, calculates total and average marks, assigns grades, and generates a rank list based on total marks.

## ✨ Features

- 👤 Student details management
- 📊 Total and average marks calculation
- 🏆 Automatic rank list generation
- 📝 Grade calculation
- 🏅 Sports score management
- 🔢 Sorting students based on total marks
- 🛡️ Marks validation and error handling

## 🧠 OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Constructor | `__init__()` |
| Encapsulation | Private attributes in `Person` |
| Getter Methods | `get_name()`, `get_age()` |
| Inheritance | `Student` inherits from `Person` |
| Abstraction | `Evaluation` abstract class |
| Abstract Method | `calculate_grade()` |
| Polymorphism | Overridden `display_details()` |
| Multiple Inheritance | `Result` inherits from `Student` and `Sports` |
| Operator Overloading | `__lt__()` |
| Static Method | `validate_marks()` |
| Class Method | `get_student_count()` |
| List of Objects | Student objects stored in a list |
| Sorting | Students sorted to generate ranks |

## 📋 Program Workflow

1. Enter the number of students.
2. Enter each student's name, age, and roll number.
3. Enter marks for three subjects.
4. Enter the sports score.
5. Calculate total and average marks.
6. Calculate the student's grade.
7. Display student details.
8. Sort students according to total marks.
9. Generate the rank list.
10. Display the total number of students created.

## ▶️ How to Run

Make sure Python 3.x is installed.

```bash
python student_rank_list.py
