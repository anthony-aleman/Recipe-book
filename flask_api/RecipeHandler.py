from flask_restful import Api, Resource, reqparse


class RecipeApiHandler(Resource):
    def get(self, id):
        return {'resultStatus': 'SUCCESS',
                'foo': id,
                'message': 'Hello World'
                }, 200


class RecipeListHandler(Resource):
    def get(self):
        return { 'list': 'lit',
                'foo': 'bar',
        }, 200

