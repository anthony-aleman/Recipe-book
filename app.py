from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from flask_api.RecipeHandler import RecipeApiHandler, RecipeListHandler
from flask_api.IngredientHandler import IngredientApiHandler, IngredientListHandler


app = Flask(__name__, static_url_path='', static_folder='/client/public')
CORS(app) # comment out when deploying
api = Api(app)


@app.route('/')
def serve_client():
    return send_from_directory(directory='/client/public', filename='index.html')

api.add_resource(RecipeApiHandler, '/api/v1.0/recipes/<int:id>')
api.add_resource(RecipeListHandler, '/recipes')
api.add_resource(IngredientListHandler, '/ingredients')
api.add_resource(IngredientApiHandler, '/api/v1.0/ingredients/<int:id>')

