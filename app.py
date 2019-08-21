# imports here:

from api.user import user
from flask import Flask, g, session
from flask_login import LoginManager
from flask_cors import CORS
import models
from api.task import task


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


CORS(task, origins=['http://localhost:3000'], supports_credentials=True)
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)

# register blueprints here
app.register_blueprint(task)
app.register_blueprint(user)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


app.register_blueprint(task)

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    session['user'] = 'Tina'
    return 'hi'

# this will be login route
@app.route('/login')
def getsession():
    if 'user' in session:
        return session['user']
    return 'not logged in!'

# this will be logout route
@app.route('/logout')
def dropsession():
    # session.pop('user', None)
    session.clear()
    return 'Dropped!'


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
