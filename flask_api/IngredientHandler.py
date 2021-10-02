from flask_restful import Api, Resource, reqparse


class IngredientApiHandler(Resource):
    def get(self, id):
        return {'resultStatus': 'SUCCESS',
                'foo': id,
                'message': 'Hello World',
                'ingredient-1': 'lettuce',
                'ingredient-2': 'poop',
                }, 200

class IngredientListHandler(Resource):
    def get(self):
        return { 
            'foo': 'bar',
        }, 200
