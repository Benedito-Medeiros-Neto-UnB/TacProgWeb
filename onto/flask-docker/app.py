from flask import Flask
from flask_restful import Resource, Api
from owlready2 import *

app = Flask(__name__)

@app.route('/')
def index():
    onto_path.append(".")
    onto = get_ontology("http://127.0.0.1/onto_mental_health.owl").load()
    return onto


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')