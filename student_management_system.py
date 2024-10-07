# student_management_system.py

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = {}

    def add_course(self, course, grade):
        self.courses[course] = grade

    def update_course(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade
        else:
            print(f"Course {course} not found for student {self.name}")

    def view_courses(self):
        if self.courses:
            print(f"Courses for {self.name}:")
            for course, grade in self.courses.items():
                print(f"{course}: {grade}")
        else:
            print(f"No courses assigned to {self.name}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student = Student(student_id, name, age)
        self.students[student_id] = student
        print(f"Student {name} added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student_id, student in self.students.items():
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}")

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        if student_id in self.students:
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            self.students[student_id].name = name
            self.students[student_id].age = age
            print(f"Student {student_id} updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def add_course_to_student(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            course = input("Enter course name: ")
            grade = input("Enter grade: ")
            self.students[student_id].add_course(course, grade)
            print(f"Course {course} added to student {student_id}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_student_courses(self):
        student_id = input("Enter student ID to view courses: ")
        if student_id in self.students:
            self.students[student_id].view_courses()
        else:
            print(f"Student with ID {student_id} not found.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Course to Student")
        print("6. View Student Courses")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.update_student()
        elif choice == "4":
            system.delete_student()
        elif choice == "5":
            system.add_course_to_student()
        elif choice == "6":
            system.view_student_courses()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
