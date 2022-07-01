from sqlalchemy import select, func, insert
from sqlalchemy.orm import Session
from db import engine
from models import GroupModel, StudentModel, CourseModel, association_table


session = Session(engine)


def find_groups(group_name):
    group_students = session.execute(
        select(GroupModel.name, func.count(StudentModel.id))
        .where(GroupModel.id == StudentModel.group_id)
        .where(GroupModel.name == group_name)
        .group_by(GroupModel.name)
        ).one()[1]

    groups = select(GroupModel.name, func.count(StudentModel.id))\
        .where(GroupModel.id == StudentModel.group_id)\
        .group_by(GroupModel.name)\
        .having(func.count(StudentModel.id) <= group_students)
    return session.execute(groups).all()


def find_students_by_course(course_name):
    students = session.query(StudentModel.last_name, StudentModel.first_name).select_from(CourseModel)\
        .join(association_table, association_table.c.courses_id == CourseModel.id)\
        .join(StudentModel, association_table.c.students_id == StudentModel.id)\
        .where(CourseModel.name == course_name)

    return students.all()


def add_students(student_first_name, student_last_name, student_group, course_name):
    course = session.execute(select(CourseModel).where(CourseModel.name == course_name)).one()[0]
    student = StudentModel(first_name=student_first_name, last_name=student_last_name, group_id=student_group)
    student.course_id.append(course)
    session.add(student)
    session.commit()


# def delete_student(student_id):
#     session.query(association_table).filter_by(students_id=student_id).delete()
#     session.query(StudentModel).filter_by(id=student_id).delete()
#
# delete_student(1)


