from flask import Flask, request, Response
from flask_restful import Resource, Api
from sqlalchemy import select, func
from dicttoxml import dicttoxml
import json
try:
    from queries import add_students, delete_student, find_students_by_course, add_students_to_course, \
        remove_student_from_course, session
    from models import GroupModel, StudentModel, CourseModel
    from create_dict import create_groups_dict, create_group_dict, create_students_dict, create_courses_dict
except ModuleNotFoundError:
    from pathlib import Path
    import sys
    ROOT = Path().resolve().parent
    sys.path.append(str(ROOT / 'app'))
    from queries import add_students, delete_student, find_students_by_course, add_students_to_course, \
        remove_student_from_course, session
    from models import GroupModel, StudentModel, CourseModel
    from create_dict import create_groups_dict, create_group_dict, create_students_dict, create_courses_dict

app = Flask(__name__)
api = Api(app)


class AllGroups(Resource):
    def get(self):
        format = request.args.get('format')
        query = session.execute(select(GroupModel.id, GroupModel.name)).all()
        if format == 'json':
            return Response(json.dumps(create_groups_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_groups_dict(query)), mimetype='text/xml')


class Group(Resource):
    def get(self, group_name):
        format = request.args.get('format')
        query = session\
            .execute(select(GroupModel.id, GroupModel.name, func.count(StudentModel.id))
                     .where(GroupModel.name == group_name)
                     .where(GroupModel.id == StudentModel.group_id)
                     .group_by(GroupModel.name, GroupModel.id)).one()

        if format == 'json':
            return Response(json.dumps(create_group_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_group_dict(query)), mimetype='text/xml')


class AllStudents(Resource):
    def get(self):
        format = request.args.get('format')
        query = session.execute(select(StudentModel.id, StudentModel.last_name, StudentModel.first_name)).all()
        if format == 'json':
            return Response(json.dumps(create_students_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_students_dict(query)), mimetype='text/xml')

    def put(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        group_id = request.form['group_id']
        return add_students(first_name, last_name, group_id), 201


class Student(Resource):
    def get(self, id):
        format = request.args.get('format')
        query = session.execute(select(StudentModel.id, StudentModel.last_name, StudentModel.first_name)
                                .where(StudentModel.id == id)).all()
        if format=='json':
            return Response(json.dumps(create_students_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_students_dict(query)), mimetype='text/xml')

    def delete(self, id):
        return delete_student(id), 204


class AllCourses(Resource):
    def get(self):
        format = request.args.get('format')
        query = session.execute(select(CourseModel.id, CourseModel.name, CourseModel.description)).all()
        if format == 'json':
            return Response(json.dumps(create_courses_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_courses_dict(query)), mimetype='text/xml')


class Course(Resource):
    def get(self, course_name):
        format = request.args.get('format')
        query = session.execute(select(CourseModel.id, CourseModel.name, CourseModel.description)
                                .where(CourseModel.name == course_name)).all()
        if format == 'json':
            return Response(json.dumps(create_courses_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_courses_dict(query)), mimetype='text/xml')


class CourseStudents(Resource):
    def get(self, course_name):
        format = request.args.get('format')
        query = find_students_by_course(course_name)
        if format == 'json':
            return Response(json.dumps(create_students_dict(query)), mimetype='application/json')
        elif format == 'xml':
            return Response(dicttoxml(create_students_dict(query)), mimetype='text/xml')

    def put(self, course_name):
        id = request.form['id']
        return add_students_to_course(id, [course_name]), 201

    def delete(self, course_name):
        id = request.form['id']
        return remove_student_from_course(id, course_name), 204


api.add_resource(AllGroups, '/api/v1/school/groups')
api.add_resource(Group, '/api/v1/school/groups/<string:group_name>')
api.add_resource(AllStudents, '/api/v1/school/students')
api.add_resource(Student, '/api/v1/school/students/<int:id>')
api.add_resource(AllCourses, '/api/v1/school/courses')
api.add_resource(Course, '/api/v1/school/courses/<string:course_name>')
api.add_resource(CourseStudents, '/api/v1/school/courses/<string:course_name>/students')


if __name__ == '__main__':
    app.run(debug=True)

