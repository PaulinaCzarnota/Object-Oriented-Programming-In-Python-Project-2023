"""
Completed By: Paulina Czarnota C21365726

Due Date: 04/08/2023

Program Description:

This Python application is a School Management System designed to facilitate efficient student administration across three distinct subjects: Math, History, and English. Leveraging the power of object-oriented programming, the system provides well-defined classes to represent students and the school.

The program boasts versatility and ease of use by enabling administrators to store, read, and write student information to and from external files in a convenient text format (.txt). Administrators can add, view, update, and remove students, with data validation mechanisms in place.

Key features of the program include:

1. Object-Oriented Design: The program defines a base class "Student" and three subclasses, each representing a specific subject: MathStudent, HistoryStudent, and EnglishStudent. The class hierarchy allows the system to handle subject-specific grading criteria effectively.

2. Compute Final Grades: Each student subclass implements a method to compute the final grade based on the subject-specific assessment components, such as quizzes, tests, attendance, projects, and final exams. The system accurately calculates the final grade for each student.

3. CRUD Operations: Administrators can easily Create, Read, Update, and Delete (CRUD) student data through intuitive console-based user interactions. The program ensures that student IDs are unique to prevent duplication.

4. Data Persistence: The system efficiently stores student data by reading from and writing to external files specific to each subject. This enables administrators to access and modify student information persistently.

5. Summary Reports: The program generates comprehensive summary reports for all students, displaying essential information such as subject, name, student ID, quiz average, test scores, attendance, and final grade. The reports provide a clear overview of students' academic performance.

The main function handles user authentication to ensure secure access to the system. Once authenticated, administrators can use the program's menu-based interface to perform various tasks, such as adding new students, updating existing student data, generating reports, and managing students effectively.

"""




# Define a base class for students
class Student:
    def __init__(self, name, student_id, subject):
        # Initialize student attributes
        self._name = name
        self._student_id = student_id
        self._subject = subject

    def __str__(self):
        # Return a string representation of the student
        return f"{self.__class__.__name__}: {self._name} (ID: {self._student_id})"

    # Abstract method to compute final grade (to be implemented by subclasses)
    def compute_final_grade(self):
        raise NotImplementedError("Subclasses should implement compute_final_grade method.")

    # Abstract method to print student information (to be implemented by subclasses)
    def print_info(self):
        raise NotImplementedError("Subclasses should implement print_info method.")

    # Getters for student attributes
    @property
    def name(self):
        # Return the student's name
        return self._name

    @property
    def student_id(self):
        # Return the student's ID
        return self._student_id

    @property
    def subject(self):
        # Return the subject of the student
        return self._subject


# Subclass for Math students
class MathStudent(Student):
    def __init__(self, name, student_id):
        # Call the superclass constructor and set additional attributes for Math students
        super().__init__(name, student_id, "Math")
        self._quizzes = []  # List to store quiz scores
        self._test1_score = 0   # Score for Test 1
        self._test2_score = 0   # Score for Test 2
        self._final_exam_score = 0  # Score for the final exam

    # Method to add quiz score to the list of quizzes
    def add_quiz_score(self, score):
        """
        Adds a quiz score to the list of quizzes for the Math student.

        Parameters:
            score (float): The score of the quiz to be added.

        Returns:
            None
        """
        if len(self._quizzes) < 5:
            self._quizzes.append(score)
        else:
            print("Maximum number of quizzes reached.")

    # Method to compute quiz average
    def compute_quiz_average(self):
        """
        Computes the quiz average for the Math student.

        Returns:
            float: The quiz average.
        """
        valid_quizzes = [quiz for quiz in self._quizzes if quiz is not None]
        if not valid_quizzes:
            return 0
        return sum(valid_quizzes) / len(valid_quizzes)

    # Method to compute the final grade for Math students
    def compute_final_grade(self):
        """
        Computes the final grade for the Math student based on assessment components.

        Returns:
            float: The final grade.
        """
        quiz_average = self.compute_quiz_average()
        final_grade = quiz_average * 0.15 + self._test1_score * 0.15 + self._test2_score * 0.15 + self._final_exam_score * 0.55
        return final_grade

    # Method to print Math student information
    def print_info(self):
        """
        Generates a detailed report of Math student information.

        Returns:
            str: The formatted report with student information.
        """
        quiz_average = self.compute_quiz_average()
        final_grade = self.compute_final_grade()

        report = f"{self}\n"
        report += f"Quiz Average: {quiz_average}\n"
        report += f"Final Grade: {final_grade}\n"
        return report


# Subclass for History students
class HistoryStudent(Student):
    def __init__(self, name, student_id):
        # Call the superclass constructor and set additional attributes for History students
        super().__init__(name, student_id, "History")
        self._attendance_score = 0  # Score for attendance
        self._project_score = 0 # Score for the project
        self._exam1_score = 0   # Score for Exam 1
        self._exam2_score = 0   # Score for Exam 2

    # Method to compute the final grade for History students
    def compute_final_grade(self):
        """
        Computes the final grade for the History student based on assessment components.

        Returns:
            float: The final grade.
        """
        final_grade = self._attendance_score * 0.1 + self._project_score * 0.3 + self._exam1_score * 0.3 + self._exam2_score * 0.3
        return final_grade

    # Method to print History student information
    def print_info(self):
        """
        Generates a detailed report of History student information.

        Returns:
            str: The formatted report with student information.
        """
        final_grade = self.compute_final_grade()

        report = f"{self}\n"
        report += f"Final Grade: {final_grade}\n"
        return report


# Subclass for English students
class EnglishStudent(Student):
    def __init__(self, name, student_id):
        # Call the superclass constructor and set additional attributes for English students
        super().__init__(name, student_id, "English")
        self._attendance_score = 0  # Score for attendance
        self._final_exam_score = 0  # Score for the final exam
        self._quiz1_score = 0   # Score for Quiz 1
        self._quiz2_score = 0   # Score for Quiz 2

    # Method to compute the final grade for English students
    def compute_final_grade(self):
        """
        Computes the final grade for the English student based on assessment components.

        Returns:
            float: The final grade.
        """
        final_grade = self._attendance_score * 0.1 + self._final_exam_score * 0.6 + self._quiz1_score * 0.15 + self._quiz2_score * 0.15
        return final_grade

    # Method to print English student information
    def print_info(self):
        """
        Generates a detailed report of English student information.

        Returns:
            str: The formatted report with student information.
        """
        final_grade = self.compute_final_grade()

        report = f"{self}\n"
        report += f"Final Grade: {final_grade}\n"
        return report


class School:
    # File paths for storing student data for different subjects
    FILE_PATHS = {
        "Math": "mathstudent.txt",
        "History": "historystudent.txt",
        "English": "englishstudent.txt",
    }

    def __init__(self):
        # Initialize an empty list to store students
        self.students = []

    # Method to add a student to the school
    def add_student(self, student):
        """
        Adds a student to the school.

        Parameters:
            student (Student): The student object to be added.

        Returns:
            None
        """
        # Check if a student with the same ID already exists
        if any(stud.student_id == student.student_id for stud in self.students):
            print(f"Error: Student with ID {student.student_id} already exists.")
            return
        self.students.append(student)

    # Method to remove a student from the school by student ID
    def remove_student(self, student_id):
        """
        Removes a student from the school based on student ID.

        Parameters:
            student_id (int): The ID of the student to be removed.

        Returns:
            None
        """
        found = False
        updated_students = []
        for student in self.students:
            if student.student_id == student_id:
                found = True
            else:
                updated_students.append(student)

        if not found:
            print(f"Error: Student with ID {student_id} not found.")
            return

        self.students = updated_students

    # Method to find a student by student ID
    def find_student_by_id(self, student_id):
        """
        Finds a student by student ID.

        Parameters:
            student_id (int): The ID of the student to be found.

        Returns:
            Student or None: The found student object or None if not found.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # Method to print information of all students in the school
    def print_all_students_info(self):
        """
        Prints information of all students in the school.

        Returns:
            None
        """
        if not self.students:
            print("No students found.")
        else:
            print("\n===== ALL STUDENTS =====")
            for student in self.students:
                print(f"{student.subject}: {student.name} (ID: {student.student_id})")
            print("=========================")

    # Method to read student data from a file for a given subject
    def read_student_data(self, subject):
        """
        Reads student data from a file for a given subject.

        Parameters:
            subject (str): The subject for which student data is to be read.

        Returns:
            list: A list of student objects read from the file.
        """
        students = []
        file_path = self.FILE_PATHS.get(subject, "")
        if not file_path:
            return students

        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                student_data = line.strip().split(",")
                if len(student_data) < 3:
                    # Skip incomplete data
                    continue

                name = student_data[1]
                student_id = int(student_data[2])

                if subject == "Math":
                    # Create a MathStudent object and set its attributes
                    student = MathStudent(name, student_id)
                    if len(student_data) >= 8:
                        student._quizzes = [float(score) if score else None for score in student_data[3:8]]
                        student._test1_score = float(student_data[8]) if len(student_data) > 8 and student_data[8] else 0
                        student._test2_score = float(student_data[9]) if len(student_data) > 9 and student_data[9] else 0
                        student._final_exam_score = float(student_data[10]) if len(student_data) > 10 and student_data[10] else 0
                elif subject == "History":
                    # Create a HistoryStudent object and set its attributes
                    student = HistoryStudent(name, student_id)
                    if len(student_data) >= 7:
                        student._attendance_score = float(student_data[3])
                        student._project_score = float(student_data[4])
                        student._exam1_score = float(student_data[5])
                        student._exam2_score = float(student_data[6])
                elif subject == "English":
                    # Create an EnglishStudent object and set its attributes
                    student = EnglishStudent(name, student_id)
                    if len(student_data) >= 7:
                        student._attendance_score = float(student_data[3])
                        student._final_exam_score = float(student_data[4])
                        student._quiz1_score = float(student_data[5])
                        student._quiz2_score = float(student_data[6])
                else:
                    # Invalid subject, skip this data
                    continue

                # Add the student object to the list
                students.append(student)

        return students


    # Method to write student data to a file for a given subject
    def write_student_data(self, subject):
        """
        Writes student data to a file for a given subject.

        Parameters:
            subject (str): The subject for which student data is to be written.

        Returns:
            None
        """
        file_path = self.FILE_PATHS.get(subject, "")
        if not file_path:
            return

        with open(file_path, "w") as file:
            for student in self.students:
                if student.subject == subject:
                    if isinstance(student, MathStudent):
                        # Write Math student data to the file
                        quiz_scores = ",".join(str(score) if score is not None else "" for score in student._quizzes)
                        file.write(f"Math,{student.name},{student.student_id},{quiz_scores},{student._test1_score},{student._test2_score},{student._final_exam_score}\n")
                    elif isinstance(student, HistoryStudent):
                        # Write History student data to the file
                        file.write(f"History,{student.name},{student.student_id},{student._attendance_score},{student._project_score},{student._exam1_score},{student._exam2_score}\n")
                    elif isinstance(student, EnglishStudent):
                        # Write English student data to the file
                        file.write(f"English,{student.name},{student.student_id},{student._attendance_score},{student._final_exam_score},{student._quiz1_score},{student._quiz2_score}\n")

    # Method to generate and print student reports for all students in the school
    def generate_student_reports(self):
        """
        Generates and prints student reports for all students in the school.

        Returns:
            None
        """
        if not self.students:
            print("No students found.")
        else:
            print("\n===== STUDENT REPORTS =====")
            for student in self.students:
                print(student.print_info())
                print("-" * 30)
            print("===========================")


# Function to simulate login (always returns True for this example)
def login():
    """
    Simulates the login process for user authentication.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username == "admin" and password == "password"


# Function to update student data based on student type
def update_student_data(student):
    """
    Updates student data based on the student type.

    Parameters:
        student (Student): The student object to be updated.

    Returns:
        None
    """
    if isinstance(student, MathStudent):
        # Update Math student data
        print("\n===== UPDATE MATH STUDENT DATA =====")
        # Loop to get quiz scores from the user
        for i in range(5):
            while True:
                try:
                    quiz_score = float(input(f"Enter Quiz {i + 1} score: "))
                    if 0 <= quiz_score <= 100:
                        student.add_quiz_score(quiz_score)
                        break
                    else:
                        print("Error: Quiz score should be between 0 and 100.")
                except ValueError:
                    print("Error: Invalid input. Please enter a valid quiz score.")

        # Get and validate Test 1 score
        while True:
            try:
                student._test1_score = float(input("Enter Test 1 score: "))
                if 0 <= student._test1_score <= 100:
                    break
                else:
                    print("Error: Test 1 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid test score.")

        # Get and validate Test 2 score
        while True:
            try:
                student._test2_score = float(input("Enter Test 2 score: "))
                if 0 <= student._test2_score <= 100:
                    break
                else:
                    print("Error: Test 2 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid test score.")

        # Get and validate Final Exam score
        while True:
            try:
                student._final_exam_score = float(input("Enter Final Exam score: "))
                if 0 <= student._final_exam_score <= 100:
                    break
                else:
                    print("Error: Final Exam score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid final exam score.")

    elif isinstance(student, HistoryStudent):
        # Update History student data
        print("\n===== UPDATE HISTORY STUDENT DATA =====")
        # Get and validate Attendance score
        while True:
            try:
                student._attendance_score = float(input("Enter Attendance score: "))
                if 0 <= student._attendance_score <= 100:
                    break
                else:
                    print("Error: Attendance score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid attendance score.")

        # Get and validate Project score
        while True:
            try:
                student._project_score = float(input("Enter Project score: "))
                if 0 <= student._project_score <= 100:
                    break
                else:
                    print("Error: Project score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid project score.")

        # Get and validate Exam 1 score
        while True:
            try:
                student._exam1_score = float(input("Enter Exam 1 score: "))
                if 0 <= student._exam1_score <= 100:
                    break
                else:
                    print("Error: Exam 1 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid exam score.")

        # Get and validate Exam 2 score
        while True:
            try:
                student._exam2_score = float(input("Enter Exam 2 score: "))
                if 0 <= student._exam2_score <= 100:
                    break
                else:
                    print("Error: Exam 2 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid exam score.")

    elif isinstance(student, EnglishStudent):
        # Update English student data
        print("\n===== UPDATE ENGLISH STUDENT DATA =====")
        # Get and validate Attendance score
        while True:
            try:
                student._attendance_score = float(input("Enter Attendance score: "))
                if 0 <= student._attendance_score <= 100:
                    break
                else:
                    print("Error: Attendance score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid attendance score.")

        # Get and validate Final Exam score
        while True:
            try:
                student._final_exam_score = float(input("Enter Final Exam score: "))
                if 0 <= student._final_exam_score <= 100:
                    break
                else:
                    print("Error: Final Exam score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid final exam score.")

        # Get and validate Quiz 1 score
        while True:
            try:
                student._quiz1_score = float(input("Enter Quiz 1 score: "))
                if 0 <= student._quiz1_score <= 100:
                    break
                else:
                    print("Error: Quiz 1 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid quiz score.")

        # Get and validate Quiz 2 score
        while True:
            try:
                student._quiz2_score = float(input("Enter Quiz 2 score: "))
                if 0 <= student._quiz2_score <= 100:
                    break
                else:
                    print("Error: Quiz 2 score should be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid quiz score.")

    else:
        # Invalid student type
        print("Invalid student type.")


# Main function to run the school management system
def main():
    # Check if the login is successful before proceeding
    if not login():
        print("Invalid login credentials. Exiting...")
        return

    # Create the school object to manage students
    school = School()

    # Read existing student data from files and add to the school
    school.students.extend(school.read_student_data("Math"))
    school.students.extend(school.read_student_data("History"))
    school.students.extend(school.read_student_data("English"))

    # Main loop for the school management system
    while True:
        print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Remove a student")
        print("4. Update student data")
        print("5. Generate student reports")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # View all students' information
            school.print_all_students_info()
        elif choice == "2":
            print("\n===== ADD A NEW STUDENT =====")
            print("Student Types:")
            print("1. Math")
            print("2. History")
            print("3. English")
            student_type_choice = input("Enter student type (1/2/3): ")
            if student_type_choice not in ("1", "2", "3"):
                print("Error: Invalid student type choice.")
                continue

            # Get student name and ID
            name = input("Enter student name: ")
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Error: Invalid student ID. Please enter a valid number.")
                continue

            if student_type_choice == "1":
                # Create a Math student object and add it to the school
                student = MathStudent(name, student_id)
            elif student_type_choice == "2":
                # Create a History student object and add it to the school
                student = HistoryStudent(name, student_id)
            else:
                # Create an English student object and add it to the school
                student = EnglishStudent(name, student_id)

            # Add the new student to the school and write data to file
            school.add_student(student)
            school.write_student_data(student.subject)

        elif choice == "3":
            # Remove a student from the school
            print("\n===== REMOVE A STUDENT =====")
            try:
                student_id = int(input("Enter the ID of the student to remove: "))
            except ValueError:
                print("Error: Invalid student ID. Please enter a valid number.")
                continue

            school.remove_student(student_id)
            # Update student data in files after removing the student
            school.write_student_data("Math")
            school.write_student_data("History")
            school.write_student_data("English")

        elif choice == "4":
            # Update student data in the school
            print("\n===== UPDATE STUDENT DATA =====")
            try:
                student_id = int(input("Enter the ID of the student to update: "))
            except ValueError:
                print("Error: Invalid student ID. Please enter a valid number.")
                continue

            # Find the student by ID and update the data
            student = school.find_student_by_id(student_id)

            if student is None:
                print("Student not found.")
            else:
                print("\nStudent Information:")
                print(student.print_info())
                update_choice = input("Do you want to update this student's data? (yes/no): ").lower()
                if update_choice == "yes":
                    update_student_data(student)
                    # Update student data in files after updating the data
                    school.write_student_data(student.subject)

        elif choice == "5":
            # Generate and print student reports
            school.generate_student_reports()

        elif choice == "6":
            # Exit the program
            # Before exiting, write all student data back to files
            school.write_student_data("Math")
            school.write_student_data("History")
            school.write_student_data("English")
            print("Exiting the school management system. Goodbye!")
            break

        else:
            # Invalid choice, prompt user to try again
            print("Invalid choice. Please select a valid option (1-6).")


# Driver Code 
if __name__ == "__main__":
    main()