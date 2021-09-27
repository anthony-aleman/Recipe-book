from flask_restful import Api, Resource, reqparse


class RecipeApiHandler(Resource):
    def get(self):
        return {'resultStatus': 'SUCCESS',
                'message': 'Hello World'
                }, 200

    
