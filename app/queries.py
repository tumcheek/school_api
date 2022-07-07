from sqlalchemy import select, func
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
    students = session.query(StudentModel.id, StudentModel.last_name, StudentModel.first_name).select_from(CourseModel)\
        .join(association_table, association_table.c.courses_id == CourseModel.id)\
        .join(StudentModel, association_table.c.students_id == StudentModel.id)\
        .where(CourseModel.name == course_name)

    return students.all()


def add_students(student_first_name, student_last_name, student_group):
    student = StudentModel(first_name=student_first_name, last_name=student_last_name, group_id=student_group)
    session.add(student)
    session.commit()


def delete_student(student_id):
    student = session.query(StudentModel).filter(StudentModel.id == student_id).first()
    all_student_courses = session.query(association_table).filter(association_table.c.students_id == student_id).all()
    for student_id, courses_id in all_student_courses:
        course = session.query(CourseModel).filter(CourseModel.id == courses_id).first()
        student.course_id.remove(course)
    session.query(StudentModel).filter(StudentModel.id == student_id).delete()
    session.commit()


def add_students_to_course(student_id, courses_names):
    student = session.scalars(select(StudentModel).where(StudentModel.id == student_id)).one()
    for course_name in courses_names:
        course = session.execute(select(CourseModel).where(CourseModel.name == course_name)).all()[0][0]
        student.course_id.append(course)
        session.add(student)
        session.commit()


def remove_student_from_course(student_id, course_name):
    student = session.scalars(select(StudentModel).where(StudentModel.id == student_id)).one()
    course = session.execute(select(CourseModel).where(CourseModel.name == course_name)).all()[0][0]
    student.course_id.remove(course)
    session.add(student)
    session.commit()
