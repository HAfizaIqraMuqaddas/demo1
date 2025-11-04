# flask app routing
from flask import Flask

# create flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome"

@app.route("/index", methods=["GET"])
def index():
    return "Welcome to the index function"

if __name__ == "__main__":
    app.run(debug=True)
