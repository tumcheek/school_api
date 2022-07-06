from app import app


client = app.test_client()

def test_non_existent_index():
    response = client.get('/')
    assert response.status_code == 404


def test_all_groups_api():
    response_json = client.get('/api/v1/school/groups?format=json')
    response_xml = client.get('/api/v1/school/groups?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_all_students_get_api():
    response_json = client.get('/api/v1/school/students?format=json')
    response_xml = client.get('/api/v1/school/students?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_all_students_put_api():
    response = client.put('/api/v1/school/students', data=dict(first_name='Dan', last_name='Fox', group_id=2))
    assert response.status_code == 201


def test_student_get_api():
    response_json = client.get('/api/v1/school/students/1?format=json')
    response_xml = client.get('/api/v1/school/students/1?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_student_delete_api():
    response = client.delete('/api/v1/school/students/1')
    assert response.status_code == 204


def test_all_courses_api():
    response_json = client.get('/api/v1/school/courses?format=json')
    response_xml = client.get('/api/v1/school/courses?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_course_api():
    response_json = client.get('/api/v1/school/courses/math?format=json')
    response_xml = client.get('/api/v1/school/courses/math?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_course_students_get_api():
    response_json = client.get('/api/v1/school/courses/math/students?format=json')
    response_xml = client.get('/api/v1/school/courses/math/students?format=xml')
    assert response_json.status_code == 200
    assert response_xml.status_code == 200


def test_course_students_put_api():
    response = client.put('/api/v1/school/courses/math/students', data=dict(id=2))
    assert response.status_code == 201


def test_course_students_delete_api():
    response = client.delete('/api/v1/school/courses/math/students', data=dict(id=2))
    assert response.status_code == 204
