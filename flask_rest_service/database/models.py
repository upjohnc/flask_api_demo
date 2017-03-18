from flask_rest_service.database import db
from datetime import datetime


class GolfCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64), index=True, unique=True)
    city = db.Column(db.String(120), index=True)
    state = db.Column(db.String(120), index=True)
    # scores = db.relationship('GolfScore', backref='golf_course', lazy='dynamic')

    def __init__(self, course_name, city, state):
        self.course_name = course_name
        self.city = city
        self.state = state

    def __repr__(self):
        return '<Course {}>'.format(self.course_name)


class GolfScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    course_id = db.Column(db.Integer, db.ForeignKey('golf_course.id'))
    course = db.relationship('GolfCourse', backref=db.backref('scores', lazy='dynamic'))

    def __init__(self, score, course, timestamp=None):
        self.score = score
        self.course = course
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
        return '<Score {}>'.format(self.score)
