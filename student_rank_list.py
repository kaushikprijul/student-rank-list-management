from abc import ABC, abstractmethod


class Evaluation(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(Person, Evaluation):

    student_count = 0

    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age)

        self.roll_number = roll_number
        self.marks = marks

        Student.student_count += 1

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def calculate_grade(self):
        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print(
            f"Name: {self.get_name()} | "
            f"Age: {self.get_age()} | "
            f"Roll No: {self.roll_number} | "
            f"Marks: {self.marks} | "
            f"Total: {self.total_marks()} | "
            f"Average: {self.average_marks():.2f} | "
            f"Grade: {self.calculate_grade()}"
        )


    def __lt__(self, other):
        return self.total_marks() > other.total_marks()


    @staticmethod
    def validate_marks(mark):
        return 0 <= mark <= 100


    @classmethod
    def get_student_count(cls):
        return cls.student_count


class Sports:

    def __init__(self, sports_score):
        self.sports_score = sports_score

    def display_sports_score(self):
        print(f"Sports Score: {self.sports_score}")


class Result(Student, Sports):

    def __init__(self, name, age, roll_number, marks, sports_score):
        Student.__init__(self, name, age, roll_number, marks)
        Sports.__init__(self, sports_score)


    def display_details(self):
        print(
            f"Name: {self.get_name()} | "
            f"Age: {self.get_age()} | "
            f"Roll No: {self.roll_number} | "
            f"Marks: {self.marks} | "
            f"Total: {self.total_marks()} | "
            f"Average: {self.average_marks():.2f} | "
            f"Grade: {self.calculate_grade()} | "
            f"Sports: {self.sports_score}"
        )


print("=" * 75)
print("                 STUDENT RANK LIST MANAGEMENT SYSTEM")
print("=" * 75)


while True:
    try:
        n = int(input("Enter the number of students: "))

        if n <= 0:
            print("Enter a positive number.")
            continue

        break

    except ValueError:
        print("Invalid input! Enter a valid number.")


students = []


for i in range(n):

    print(f"\nStudent {i + 1}")
    print("-" * 30)

    try:
        name = input("Enter name: ").strip()

        age = int(input("Enter age: "))
        roll_number = int(input("Enter roll number: "))

        marks = []

        for j in range(3):

            while True:
                mark = int(input(f"Enter marks for Subject {j + 1}: "))

                if Student.validate_marks(mark):
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

        sports_score = int(input("Enter sports score: "))

        student = Result(
            name,
            age,
            roll_number,
            marks,
            sports_score
        )

        students.append(student)

    except ValueError:
        print("Invalid input! Please enter numeric values where required.")
        print("Please restart the program with valid details.")
        exit()


print("\n" + "=" * 75)
print("                        STUDENT DETAILS")
print("=" * 75)

for student in students:
    student.display_details()


students.sort()

print("\n" + "=" * 75)
print("                         RANK LIST")
print("=" * 75)

for rank, student in enumerate(students, start=1):

    print(
        f"Rank {rank}: "
        f"{student.get_name()} | "
        f"Roll No: {student.roll_number} | "
        f"Total Marks: {student.total_marks()} | "
        f"Average: {student.average_marks():.2f} | "
        f"Grade: {student.calculate_grade()}"
    )


print("\n" + "=" * 75)
print("Total number of students created:", Student.get_student_count())
print("=" * 75)