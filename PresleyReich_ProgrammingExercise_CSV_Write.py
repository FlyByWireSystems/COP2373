import csv



def write_grades():
    # Ask the teacher for the number of students
    num_students = int(input("Enter number of students: "))


    # Opens the file with the 'with' keyword to ensure it closes correctly
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Writes the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loops to collect all the data for each student
        for i in range(num_students):
            print(f"\nEntering the data for student {i+1}:")
            first = input("First name: ")
            last = input("Last name: ")

            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            # Writes a row for each student and their data
            writer.writerow([first, last, exam1, exam2, exam3])

    print("\n The file has been created.")

# Runs the program
write_grades()