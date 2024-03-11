def input_number_student():
    return int(input("Enter number of students: "))

def input_student_info():
    student_id = input("Enter student's id:")
    student_name = input("Enter student's name:")
    student_dob = input("Enter student's date of birth:")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def input_number_courses():
    return int(input("Enter number of courses:"))

def input_course_info():
    course_id = input("Enter course's id:")
    course_name = input("Enter course's name:")
    return {"id": course_id, "name": course_name}

def input_marks(courses, students):
    marks = {}
    course_id = input("Enter the course id:")
    if course_id not in courses:
        print("Invalid id.")
    else:
        marks = {}
        for student_id, student_info in students.items():
            try:
                mark = float(input(f"Enter mark for student {student_info['name']}: "))
                marks[student_id] = mark
            except ValueError:
                print("Invalid marks! Please re-enter a valid mark.")
    return marks

def list_courses(courses):
    print("List of available courses: ")
    for course_id, course_info in courses.items():
        print(f"Course ID: {course_id}\t Course name: {course_info['name']}")

def list_students(students):
    print("List of students: ")
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}\t Student name: {student_info['name']}\t Student DoB: {student_info['dob']}")

def show_marks(marks, courses, students):
    course_id = input("Enter the ID of the course you want to choose: ")
    
    if course_id not in courses:
        print("Invalid course ID.")
        return
    if course_id not in marks:
        print("No marks for this course yet.")
        return
    print(f"Student marks for course {courses[course_id]['name']}: ")
    for student_id, mark in marks[course_id].items():
        student_name = students[student_id]["name"]
        print(f"{student_name}: {mark}")

def main():
    students = {}
    courses = {}
    marks = {}

    while True: 
        title = "STUDENT MANAGEMENT SYSTEM"
        width = 50
        print(f"{title:^{width}}")
        print("--------------------------------------------")
        print("\nChoose an option: ")
        print("1. Add students")
        print("2. Add courses")
        print("3. Add marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_student = input_number_student()
            for _ in range(num_student):
                student_info = input_student_info()
                students[student_info["id"]] = student_info

        elif choice == "2":
            num_course = input_number_courses()
            for _ in range(num_course):
                course_info = input_course_info()
                courses[course_info["id"]] = course_info

        elif choice == "3":
            marks = input_marks(courses,students)
        
        elif choice == "4":
            list_courses(courses)

        elif choice == "5":
            list_students(students)

        elif choice == "6":
            show_marks(marks,courses, students)
        
        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please re-enter a valid option.")

if __name__ == "__main__":
    main()
