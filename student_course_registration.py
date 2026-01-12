class Student:
    def __init__(self, name, matric_no):
        self.name = name
        self.matric_no = matric_no
        self.registered_courses = []


class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title


class RegistrationSystem:
    def __init__(self):
        self.courses = [
            Course("SEN201", "Software Engineering"),
            Course("COS201", "COMPUTER PROGRAMMING I"),
            Course("CUL-CSC279", "COMPUTING TECHNIQUES AGAINST CULTISM"),
            Course("CUL-CSC283", "MANAGEMENT INFORMATION SYSTEM"),
            Course("CYB201", "INTRODUCTION TO CYBERSECURITY AND STRATEGY")
        ]

    def display_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses:
            print(f"{course.code} - {course.title}")

    def register_course(self, student, course_code):
        for course in self.courses:
            if course.code == course_code:
                student.registered_courses.append(course)
                print(f"{course.code} registered successfully.")
                return
        print("Course not found.")

    def show_registered_courses(self, student):
        print("\nRegistered Courses:")
        for course in student.registered_courses:
            print(f"{course.code} - {course.title}")


# Main Program
name = input("Enter student name: ")
matric = input("Enter matric number: ")

student = Student(name, matric)
system = RegistrationSystem()

while True:
    system.display_courses()
    code = input("\nEnter course code to register (or type 'exit' to finish): ").upper()

    if code == "EXIT":
        break

    system.register_course(student, code)

system.show_registered_courses(student)
