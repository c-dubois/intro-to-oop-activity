# add your get_student_with_more_classes function here!
def get_student_with_more_classes(student1, student2):

    if len(student1.courses) > len(student2.courses):
        return student1.name
    return student2.name
