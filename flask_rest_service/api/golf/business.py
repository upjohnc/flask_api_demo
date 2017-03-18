from flask_rest_service.database import db
from flask_rest_service.database.models import GolfCourse


def create_course(data):
    course_name = data.get('course_name')
    city = data.get('city')
    state = data.get('state')

    print(course_name)
    course = GolfCourse(course_name=course_name, city=city, state=state)

    db.session.add(course)
    db.session.commit()


def update_course(id, data):
    course = GolfCourse.query.filter(GolfCourse.id == id).one()
    course_name = data.get('course_name', None)
    if course_name:
        course.course_name = course_name
    db.session.add(course)
    db.session.commit()
