def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    return {"id": student_id, "name": name, "dob": dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_student_marks(students, course):
    marks = {}
    course_id = course["id"]

    print(f"Enter marks for students in course {course['name']}")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[student['id']] = mark

    return {"course_id": course_id, "marks": marks}

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}\t Course Name: {course['name']}")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"Student ID: {student['id']}\t Name: {student['name']}\t DoB: {student['dob']}")

def show_student_marks(marks, course, students):
    if len(students) == 0:
        print("You haven't had any student in class.")
        return
    
    course_id = course["id"]
    print(f"Student marks for course {course['name']}:")
    for student_id, mark in marks.items():
        student_name = next((student["name"] for student in students if student["id"] == student_id), "Unknown")
        print(f"Student ID: {student_id}\t Name: {student_name}\t Mark: {mark}")


if __name__ == "__main__":
    students = []
    courses = []
    marks = []

    while True:
        print("\nOptions:")
        print("1. Input student's information")
        print("2. Input course information")
        print("3. Input student marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            num_students = input_number_of_students()
            print(f"Number of students in class: {num_students}")
            for _ in range(num_students):
                students.append(input_student_information())

        elif choice == 2:
            num_courses = input_number_of_courses()
            print(f"Number of courses: {num_courses}")
            for _ in range(num_courses):
                courses.append(input_course_information())

        elif choice == 3:
            list_courses(courses)
            selected_course_id = input("Select a course id: ")
            selected_course = next((course for course in courses if course["id"] == selected_course_id), None)

            if selected_course:
                marks.append(input_student_marks(students, selected_course))
            else:
                print("Invalid course ID. Try again.")

        elif choice == 4:
            list_courses(courses)

        elif choice == 5:
            list_students(students)

        elif choice == 6:
            list_courses(courses)
            selected_course_id = input("Select a course_id : ")
            selected_course = next((course for course in courses if course["id"] == selected_course_id), None)

            if selected_course:
                show_student_marks(marks, selected_course, students)
            else:
                print("Invalid course ID. Try again.")

        elif choice == 0:
            break

        else:
            print("Invalid choice. Try again.")
