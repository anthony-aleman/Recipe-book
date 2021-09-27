from flask_restful import Api, Resource, reqparse

parser = reqparse.RequestParser()

class RecipeApiHandler(Resource):
    def get(self):
        return {'resultStatus': 'SUCCESS',
                'message': 'Hello World'}
