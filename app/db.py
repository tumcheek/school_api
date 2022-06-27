from sqlalchemy import create_engine
from config import db_config
from sqlalchemy.orm import Session
from models import GroupModel, StudentModel, CourseModel, Base
from fill_tables import fill_groups_table, fill_courses_table, fill_students_table, fill_association_table
from data_for_tables import *
from sqlalchemy import select


engine = create_engine(f"postgresql://{db_config['postgresql']['user']}:{db_config['postgresql']['pass']}@"
                       f"{db_config['postgresql']['host']}/test_1")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        query_students = select(StudentModel)
        query_courses = select(CourseModel)
        fill_groups_table(groups, engine)
        fill_courses_table(courses, course_description, engine)
        fill_students_table(first_names, last_names, 200, 10, engine)
        fill_association_table(session.scalars(query_students).all(), session.scalars(query_courses).all(), engine)
        session.commit()

