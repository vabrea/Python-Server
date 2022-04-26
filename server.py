
from unittest import mock
from flask import Flask
import json
from mockdata import mock_catalog


app = Flask('server')

@app.route("/home")
def home():
    return "Hello buddy..."

@app.route("/")
def root():
    return "Welcome to the onine store server."

# @app.route("/about")
# def about():
#     return "Hello my name is Von"

###########################################
########### API CATALOG ###################
###########################################

@app.route("/api/about", methods=["POST"])
def about():
    me = {
        "first": "Von",
        "last": "Abrea"
    }
    return json.dumps(me) #parse to json and return


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)

@app.route("/api/catalog/cheapest")
def cheapest_catalog():
    solution = mock_catalog[0]
    for prod in mock_catalog:
        # print(prod["title"])

        if prod["price"]< solution["price"]:
          solution = prod

    return json.dumps(solution)

#sum of all prices in catalog
@app.route("/api/catalog/total")
def total_catalog():
    total = 0
    for x in mock_catalog:
        total += x["price"]
    
    return json.dumps(total)
        

#start the server
app.run(debug=True)