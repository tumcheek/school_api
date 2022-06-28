from models import *
from random import choice, randint


def create_groups_data(groups_list):
    groups = []
    for group in groups_list:
        groups.append(GroupModel(name=group))
    return groups


def create_courses_data(courses_list, description):
    courses = []
    for course in courses_list:
        courses.append(CourseModel(name=course, description=choice(description)))
    return courses


def create_students_date(first_names, last_names, student_number, group_number):
        students = []
        for i in range(student_number):
            students.append(StudentModel(first_name=choice(first_names),
                                         last_name=choice(last_names), group_id=randint(1, group_number)))
        return students


def create_association_data(students, courses):
    for student in students:
        student.course_id.append(choice(courses))

