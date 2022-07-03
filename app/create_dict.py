def create_groups_dict(groups):
    groups_dict = {}
    for group in groups:
        groups_dict[f'id_{group[0]}'] = {
            'name': group[1]
        }
    return groups_dict


def create_group_dict(group):
    group_dict = {
        f'id_{group[0]}': {
            'name': group[1],
            'students_number': group[2]
                        }
                }
    return group_dict


def create_students_dict(students):
    students_dict = {}
    for student in students:
        students_dict[f'student_id_{student[0]}'] = {
            'last_name': student[1],
            'first_name': student[2]

        }
    return students_dict


def create_courses_dict(courses):
    courses_dict = {}
    for course in courses:
        courses_dict[f'course_id_{course[0]}'] = {
            'course_name': course[1],
            'description': course[2]

        }
    return courses_dict
