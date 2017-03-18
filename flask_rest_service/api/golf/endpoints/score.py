from flask import request
from flask_restplus import Resource
from flask_rest_service.api.golf.business import create_score
from flask_rest_service.api.golf.serializers import scores
from flask_rest_service.api.golf.restplus import api
from flask_rest_service.database.models import GolfScore

ns = api.namespace('golf/scores', description='Operations related to golf scores.')


@ns.route('/')
class ScoreCollection(Resource):
    @api.marshal_list_with(scores)
    def get(self):
        """Returns a list of scores"""
        golf_scores = GolfScore.query.all()
        return golf_scores

    @api.response(201, 'Score successfully added.')
    @api.expect(scores)
    def post(self):
        """Creates a new score entry."""
        data = request.json
        create_score(data)
        return None, 201
