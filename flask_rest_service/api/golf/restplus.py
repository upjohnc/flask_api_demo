from flask_restplus import Api
from flask_rest_service import settings
from sqlalchemy.orm.exc import NoResultFound

api = Api(version='1.01', title='Golf Scores', description='A database to store golf scores.')


@api.errorhandler
def default_error(e):
    message = 'An unhandled exception occurred'

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404
