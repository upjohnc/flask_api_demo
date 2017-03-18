import datetime as dt

from flask_rest_service.database import db
from flask_rest_service.database.models import GolfCourse, GolfScore


def create_course(data):
    course_name = data.get('course_name')
    city = data.get('city')
    state = data.get('state')

    course = GolfCourse(course_name=course_name, city=city, state=state)

    db.session.add(course)
    db.session.commit()


def update_course(id, data):
    course = GolfCourse.query.filter(GolfCourse.id == id).one()
    course_name = data.get('course_name', None)
    if course_name:
        course.course_name = course_name
    city = data.get('city', None)
    if city:
        course.city = city
    state = data.get('state', None)
    if state:
        course.state = state

    db.session.add(course)
    db.session.commit()


def create_score(data):
    score = data.get('score')
    timestamp = data.get('timestamp', None)
    if timestamp:
        timestamp = dt.datetime.strptime(timestamp, '%Y-%m-%d')
    else:
        timestamp = dt.datetime.now()
    course_id = data.get('course_id')

    course = GolfCourse.query.filter(GolfCourse.id == course_id).one()
    print(course)

    # new_score = GolfScore(score=score, timestamp=timestamp, course_id=course)
    new_score = GolfScore(score, course)
    db.session.add(new_score)
    db.session.commit()
