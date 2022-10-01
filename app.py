from distutils.log import debug
from email.policy import default
from flask import Flask
from dbhelpers import run_statement
import json
app = Flask(__name__)

@app.get('/cars')
def get_car():
    results = run_statement('CALL get_all_cars()')
    if(type(results) == list):
        cars_json = json.dumps(results, default=str)
        return cars_json
    else:
        return "Sorry, something has gone wrong."

app.run(debug=True)