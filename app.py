from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from api.RecipeHandler import RecipeHandler


app = Flask(__name__, static_url_path='', static_folder='/client/public')
CORS(app)
api = Api(app)


@app.route('/')
def serve_client():
    return send_from_directory(directory=app.static_folder, filename='index.html')

api.add_resource(RecipeHandler, '/hello')

