from flask import Flask
from api.task import task
import models


DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.register_blueprint(task)

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)