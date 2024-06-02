from flask import Blueprint

hello_world = Blueprint("hello_world", __name__)

@hello_world.route("/hello_world", methods=["GET"])
def hello():
    return "<h1>hello world!</h1>"

@hello_world.route("/hello_world_db", methods=["GET"])
def hello_world_db():
    return "<h1>stored hello world in DB</h1>"
