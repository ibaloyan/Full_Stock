# import dependencies
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

# init the Flask
app = Flask(__name__)

# app.config["MONGO_URI"] = 'mongodb://localhost:27017/bitcoin_y_o_y'
# mongo = PyMongo(app)
#
# # Pass connection to the pymongo instance.
#
#
# # Connect to a database. Will create one if not already available.
# db = mongo.db

# create a route for scraping
@app.route("/bit_y_o_y")
##### Give new name
def BTC_vs_BTC():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/bitcoin_y_o_y'
    mongo = PyMongo(app)
    db = mongo.db

    btcY = db.bit_y_o_y.find_one()
    print(btcY)
    btcY_title = btcY["labels"]
    btcY_numbers = btcY["numbers"]
    btcY_dict = {"title":btcY_title, "numbers": btcY_numbers}
    print(btcY_title)
    # return appl_title
    return jsonify(btcY_dict)


@app.route("/btc_v_all")
##### Give new name
def btc_v_all1():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/bitcoin_v_All'
    mongo = PyMongo(app)
    db = mongo.db

    btcA = db.bitcoin_v_All1.find_one()
    print(btcA)
    btcA_title = btcA["labels"]
    btcA_numbers = btcA["numbers"]
    btcA_dict  = {"title":btcA_title, "numbers":btcA_numbers}
    return jsonify(btcA_dict)


@app.route("/btc_Q")
##### Give new name
def btc_Q():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/bitcoin_Q'
    mongo = PyMongo(app)
    db = mongo.db

    btcQ = db.bitcoin_q.find_one()
    print(btcQ)
    btcQ_title = btcQ["labels"]
    btcQ_numbers = btcQ["numbers"]
    btcQ_dict  = {"title":btcQ_title, "numbers":btcQ_numbers}
    return jsonify(btcQ_dict)
# @app.route("/microsoft")
# ##### Give new name
# def micro():
#     msft = list(db.collection_name.find())
#     return jsonify(msft)

# @app.route("/google")
# ##### Give new name
# def Goog():
#     goog = list(db.collection_name.find())
#     return jsonify(goog)

# @app.route("/bitcoin")
# ##### Give new name
# def BTC():
#     btc = list(db.collection_name.find())
#     return jsonify(btc)

# create a index route
@app.route('/')
def index():
    # Return the template with the teams list passed in
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
