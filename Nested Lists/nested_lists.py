class StudentsClass:
    """
    input array of students with grades
    [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    """
    def __init__(self, students_with_grades):
        self.students_with_grades = students_with_grades
        self.lowest_grade_student = 0.00
    
    def student_with_lowest_grade(self):
        for student_grade in self.students_with_grades:
            if student_grade[1] < self.lowest_grade_student:
                self.lowest_grade_student = student_grade[1]


if __name__ == "__main__":
    students_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grades.append([name, score])

    students = StudentsClass(students_grades)
    students.student_with_lowest_grade()
    print(students.lowest_grade_student)
