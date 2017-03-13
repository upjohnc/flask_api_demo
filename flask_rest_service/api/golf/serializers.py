from flask_restplus import fields
from flask_rest_service.api.golf.restplus import api

scores = api.model('Golf scores', {'id': fields.Integer(readOnly=True, description='Unique identifier of the the score.'),
                                   'score': fields.Integer(required=True, description='Golf score'),
                                   'timestamp': fields.DateTime(reqired=True, description='Date of the score'),
                                   'course_id': fields.Integer(attribute='course.id'),
                                   'course': fields.String(attribute='course.id')
                                   })

course = api.model('Golf course', {'id': fields.Integer(readOnly=True, description='The unique identifier of a golf course.'),
                                   'course_name': fields.String(required=True, description='Course name'),
                                   'city': fields.String(description='City of the golf course'),
                                   'state': fields.String(description='State of the golf course')
                                   })

course_with_scores = api.inherit('Course with scores', course, {'scores': fields.List(fields.Nested(scores))})
