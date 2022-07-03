from sqlalchemy import create_engine
from config import db_config
from sqlalchemy.orm import Session
from models import Base
from create_tables_date import create_groups_data, create_courses_data, create_students_date, create_association_data
from data_for_tables import *


engine = create_engine(f"postgresql://{db_config['postgresql']['user']}:{db_config['postgresql']['pass']}@"
                       f"{db_config['postgresql']['host']}/test_3")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        table_groups = create_groups_data(groups)
        table_courses = create_courses_data(courses, course_description)
        table_students = create_students_date(first_names, last_names, 200, 10)
        create_association_data(table_students, table_courses)
        session.add_all(table_groups+table_courses+table_students)
        session.commit()

