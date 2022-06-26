from sqlalchemy.orm import Session
from models import *
from random import choice, randint


def fill_groups_table(groups, engine):
    for group in groups:
        with Session(engine) as session:
            session.add_all([GroupModel(name=group)])
            session.commit()


def fill_courses_table(courses, description, engine):
    for course in courses:
        with Session(engine) as session:
            session.add_all([CourseModel(name=course, description=choice(description))])
            session.commit()


def fill_students_table(first_names, last_names, student_number, group_number, engine):
    for i in range(student_number):
        with Session(engine) as session:
            session.add_all([StudentModel(first_name=choice(first_names),
                                          last_name=choice(last_names), group_id=randint(1, group_number))])
            session.commit()


# ******************************************************************************
def fill_association_table(students, courses, engine):
    for student in students:
        with Session(engine) as session:
            user=session.scalars(student).one()
            user.group_id.append(choice(courses))

            session.commit()
# ******************************************************************************
