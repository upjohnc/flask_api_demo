from flask_rest_service.database import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64), index=True, unique=True)
    city = db.Column(db.String(120), index=True)
    state = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Course {}>'.format(self.course_name)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    course = db.relationship('Course', backref=db.backref('course', lazy='dynamic'))

    def __repr__(self):
        return '<Score {}>'.format(self.score)
