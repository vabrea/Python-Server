
from ast import keyword
from operator import is_not
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

#find a prodct based on the unique id
@app.route("/api/products/<id>")
def find_product(id):
   for prod in mock_catalog:
        if id == prod["_id"]:
            
            return json.dumps(prod)

#get the list of categories from the catalog
@app.route("/api/products/categories")
def find_categories():
    categories = []
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

            
    return json.dumps(categories)

@app.route("/api/products/categories/<cat_name>")
def nike_category(cat_name):
    results = []
    for prod in mock_catalog:
        if prod["category"].lower() == cat_name.lower():
            results.append(prod)

    
    return json.dumps(results)

#search by text inside the title

@app.route("/api/products/search/<text>")
def search_category(text):
    results = []
    text = text.lower()

    for prod in mock_catalog:
        title = prod["title"].lower()
        if text in title:
            results.append(prod)
    
    return json.dumps(results)

#start the server
app.run(debug=True)