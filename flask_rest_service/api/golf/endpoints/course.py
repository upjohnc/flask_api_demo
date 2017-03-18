from flask import request
from flask_restplus import Resource
from flask_rest_service.api.golf.business import create_course, update_course
from flask_rest_service.api.golf.serializers import course, course_with_scores
from flask_rest_service.api.golf.restplus import api
from flask_rest_service.database.models import GolfCourse

ns = api.namespace('golf/courses', description='Operations related to golf courses.')


@ns.route('/')
class CourseCollection(Resource):
    @api.marshal_list_with(course)
    def get(self):
        """Returns list of courses"""
        courses = GolfCourse.query.all()
        return courses

    @api.response(201, 'Course successfully created.')
    @api.expect(course)
    def post(self):
        """Creates a new golf course entry."""
        data = request.json
        create_course(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Course not found.')
class CourseItem(Resource):
    @api.marshal_with(course_with_scores)
    def get(self, id):
        """Returns a course with related scores."""
        return GolfCourse.query.filter(GolfCourse.id == id).one()

    @api.expect(course, validate=True)
    @api.response(204, 'Course successfully updated.')
    def put(self, id):
        """
        updates a course

        expected json with optional fields:
        course_name,
        city,
        state
        """
        data = request.json
        update_course(id, data)
        return None, 204
