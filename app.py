# import blueprints here:

from api.user import user
from flask import Flask, g
from flask_login import LoginManager
import models

DEBUG = True
PORT = 8000

login_manager = LoginManager()

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
app.secret_key = 'supercalifragilisticexpialidocius'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.user.id == userid)
    except models.DoesNotExist:
        return None


# register blueprints here
app.register_blueprint(user)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
