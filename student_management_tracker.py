# 🎓 STUDENT MANAGEMENT TRACKER
# This project shows how to use variables, loops, conditionals, lists, dictionaries, tuples, and sets.

# List to hold all student records
students = []

# Function to add a student
def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    
    # Tuple for fixed info (name, age)
    info = (name, age)
    
    # Dictionary to store subject marks
    marks = {}
    subjects = int(input("Enter number of subjects: "))
    
    # Loop to collect marks
    for i in range(subjects):
        subject = input(f"Enter subject {i+1} name: ")
        score = int(input(f"Enter {subject} marks: "))
        marks[subject] = score
    
    # Combine into one dictionary
    student = {"info": info, "course": course, "marks": marks}
    students.append(student)
    print(f"✅ {name} added successfully!")

# Function to display all students
def display_students():
    print("\n--- All Students ---")
    if not students:
        print("No students available yet.")
    else:
        for i, student in enumerate(students, 1):
            name, age = student["info"]
            print(f"{i}. {name} ({age} yrs) - {student['course']}")
            for sub, mark in student["marks"].items():
                print(f"   {sub}: {mark}")

# Function to show top performer
def top_performer():
    print("\n--- Top Performer ---")
    if not students:
        print("No student records yet.")
        return
    
    top_student = None
    top_avg = 0
    
    for student in students:
        marks = student["marks"].values()
        avg = sum(marks) / len(marks)
        if avg > top_avg:
            top_avg = avg
            top_student = student
    
    name, _ = top_student["info"]
    print(f"🏆 Top Performer: {name} with average {top_avg:.2f}")

# Set to track unique courses
courses = set()

# Main menu loop
while True:
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Top Performer")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
        courses.add(students[-1]["course"])  # store unique course
    elif choice == "2":
        display_students()
    elif choice == "3":
        top_performer()
    elif choice == "4":
        print(f"\nUnique Courses: {courses}")
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")