from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("students_id", ForeignKey("students.id")),
    Column("courses_id", ForeignKey("courses.id")),
)


class GroupModel(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class StudentModel(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="CASCADE"), nullable=False)
    course_id = relationship("CourseModel", secondary=association_table)
    first_name = Column(String(20))
    last_name = Column(String(20))


class CourseModel(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(String(100))



