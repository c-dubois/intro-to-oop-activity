from student import Student
def get_student_with_more_classes(student1, student2):

    if student1.get_num_classes() > student2.get_num_classes():
        return student1.name
    return student2.name

# example

student1 = Student("Alice", "Sophomore", ["Math", "Science"])
student2 = Student("Bob", "Freshman", ["History"])

print(get_student_with_more_classes(student1, student2))