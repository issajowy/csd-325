import json

def print_student_list(students):
    """Loops through the list and prints values in the required format."""
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")

def main():
    # 1. Load the JSON file into a list
    try:
        with open("module-8/Student.json", "r") as file:
            student_list = json.load(file)
    except FileNotFoundError:
        print("Error: student.json not found.")
        return

    # 2. Output notification and call print function for original list
    print("-- Original Student List --")
    print_student_list(student_list)
    print()

    # 3. Append your information
    # Using 'Joey' and 'Barberich' as per your profile
    new_student = {
        "F_Name": "Joey",
        "L_Name": "Barberich",
        "Student_ID": 99999, # Fictional ID
        "Email": "jbarberich@bellevue.edu"
    }
    student_list.append(new_student)

    # 4. Output notification and call print function for updated list
    print("-- Updated Student List --")
    print_student_list(student_list)
    print()

    # 5. Use JSON dump() to update the file
    with open("module-8/Student.json", "w") as file:
        json.dump(student_list, file, indent=4)

    # 6. Output final notification
    print("The student.json file was updated successfully.")

if __name__ == "__main__":
    main()
    