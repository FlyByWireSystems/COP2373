import csv


def read_grades():
    # Opens and reads the CSV file using the 'with' keyword
    # Opening the file in read mode ('r') ensures we only read from the file.
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)

        # Converts the data to a list to turn it into readable rows
        data = list(reader)

        # Print a formatted header row with aligned columns.
        # The <15 or <10 means left-align text within a fixed width.
        print("\n ALL STUDENT GRADES\n")
        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
        print("--------------------------------------------------------------------")

        # Loops through each row in the data, skipping the first row (the header).
        for row in data[1:]:
            # row[0] = First Name, row[1] = Last Name, etc.
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


read_grades()