from sqlalchemy.orm import Session
from models import *
from random import choice, randint


def fill_groups_table(groups, engine):
    with Session(engine) as session:
        for group in groups:
            session.add_all([GroupModel(name=group)])
            session.commit()


def fill_courses_table(courses, description, engine):
    with Session(engine) as session:
        for course in courses:
            session.add_all([CourseModel(name=course, description=choice(description))])
            session.commit()


def fill_students_table(first_names, last_names, student_number, group_number, engine):
    with Session(engine) as session:
        for i in range(student_number):
            session.add_all([StudentModel(first_name=choice(first_names),
                                          last_name=choice(last_names), group_id=randint(1, group_number))])
            session.commit()


def fill_association_table(students, courses, engine):
    with Session(engine) as session:
        for student in students:
            student.course_id.append(choice(courses))
            session.commit()

