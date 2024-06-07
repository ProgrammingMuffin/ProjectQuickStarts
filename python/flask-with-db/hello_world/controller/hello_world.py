from flask import Blueprint
from hello_world.db import hello_world_repo

hello_world = Blueprint("hello_world", __name__)

@hello_world.route("/hello_world", methods=["GET"])
def hello():
    return "<h1>hello world!</h1>"

@hello_world.route("/hello_world_db", methods=["GET"])
def hello_world_db():
    helloWorld = hello_world_repo.HelloWorld()
    helloWorld.storeWelcomeMessageForUser("hello world!", "world")
    return "<h1>stored hello world in DB</h1>"
