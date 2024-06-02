from flask import Flask
from hello_world.hello_world import hello_world

application = Flask(__name__)

application.register_blueprint(hello_world)
application.run("0.0.0.0", 5000)