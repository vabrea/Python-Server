
from ast import keyword
from itertools import product
from operator import is_not
from unittest import mock
from flask import Flask, request, abort
import json
from mockdata import mock_catalog
from config import db
from bson import ObjectId
from flask_cors import CORS


app = Flask('server')
CORS(app) #disable CORS policy

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
    cursor = db.products.find({})
    all_products = []

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        all_products.append(prod)

    return json.dumps(all_products)

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

   
    if not "title" in product or len(product["title"]) < 6:
        return abort (400, "Title must be at least 5 characters")

    if type(product["title"]) != str:
        return abort (400, "Please enter a valid title")

    if product["price"] <= 0:
       return abort (400, "a price is required")

    if type(product["price"]) != float and type(product["price"]) != int:
        return abort (400, "price must be greater than zero")

    if not "image" in product or len(product["image"]) < 1:
        return abort (400, "Please provide an image file")

    if not "category" in product or len(product["category"]) < 1:
        return abort (400, "Please provide a category")

    


    print("product saved")
    print(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)

@app.route("/api/catalog/cheapest")
def cheapest_catalog():
    cursor = db.products.find({})

    solution = cursor[0]
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        # print(prod["title"])

        if prod["price"]< solution["price"]:
          solution = prod

    return json.dumps(solution)

#sum of all prices in catalog
@app.route("/api/catalog/total")
def total_catalog():
    cursor = db.products.find({})

    total = 0
    for x in cursor:
        total += x["price"]
    
    return json.dumps(total)

#find a prodct based on the unique id
@app.route("/api/products/<id>")
def find_product(id):

    if not ObjectId.is_valid(id):
        return abort (400, "Not a valid ID")

    prod = db.products.find_one({"_id": ObjectId(id)})
    prod["_id"] = str(prod["_id"])

    return json.dumps(prod)



#get the list of categories from the catalog
@app.route("/api/products/categories")
def find_categories():
    cursor = db.products.find({})
    categories = []

    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

            
    return json.dumps(categories)

@app.route("/api/products/categories/<cat_name>")
def nike_category(cat_name):
    results = []
    cursor = db.products.find({"category": cat_name})

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
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


#######################################
############ Coupon Codes #############
#######################################

@app.route("/api/couponCodes", methods=["post"])
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    if not "couponCode" in coupon or len(coupon["couponCode"]) < 5 or type(coupon["couponCode"]) != type(str):
        return abort(400, "Code is required and must contain at least 5 characters.")


    if not "discount" in coupon:
        return abort(400, "Discount is required")

    if type(coupon["discount"]) != int and type(coupon["discount"]) != float:
        return abort(400, "Please enter a valid number")

    if coupon["discount"] > 35 or coupon["discount"] < 0:
        return abort(400, "Discount must be between 1-35%")


    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)

@app.route("/api/couponCodes")
def get_coupon():
    cursor = db.coupons.find({})
    all_coupons = []

    for coupon in cursor:
        coupon["_id"] = str(coupon["_id"])
        all_coupons.append(coupon)

    return json.dumps(all_coupons)

@app.route("/api/couponCodes/<id>")
def find_coupon(id):

    if not ObjectId.is_valid(id):
        return abort (400, "Not a valid ID")
    coupon = db.coupons.find_one({"_id": ObjectId(id)})
    if not coupon:
        return abort(400, "Invalid Coupon ID")

    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)

#start the server
app.run(debug=True)