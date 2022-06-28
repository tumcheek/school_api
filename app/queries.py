from sqlalchemy import select, func
from sqlalchemy.orm import Session
from db import engine
from models import GroupModel, StudentModel

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
    pass


