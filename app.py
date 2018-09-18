# import dependencies
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import Create_mongo

Create_mongo.populate()

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
def btc_v_all1():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/bitcoin_v_All'
    mongo = PyMongo(app)
    db = mongo.db

    btcA = db.bitcoin_v_All1.find_one()
    print(btcA)
    btcA_title = btcA["labels"]
    btcA_numbers = btcA["numbers"]
    btcA_Dates = btcA["Dates"]
    btcA_dict  = {"title":btcA_title, "numbers":btcA_numbers, "Dates": btcA_Dates}
    return jsonify(btcA_dict)


@app.route("/btc_Q")
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
#
@app.route("/applY")
def applY():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/Apple_y_y'
    mongo = PyMongo(app)
    db = mongo.db

    applY = db.apple_y_o_y.find_one()
    print(applY)
    applY_title = applY["labels"]
    applY_numbers = applY["numbers"]
    applY_Dates = applY["Dates"]
    applY_nDates = applY["Dates_Normal"]
    applY_Vol = applY["Volume"]
    applY_Close = applY["Close"]
    applY_Q = applY["Qs"]
    applY_Ql = applY["Qmarks"]
    applY_dict  = {"title":applY_title, "Change":applY_numbers, "Dates": applY_Dates, "DatesN": applY_nDates, "Volume": applY_Vol, "Close": applY_Close,
    "Qs": applY_Q, "Qmarks": applY_Ql}
    return jsonify(applY_dict)

@app.route("/IBMY")
def ibmY():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/IBM_y_y'
    mongo = PyMongo(app)
    db = mongo.db

    ibmY = db.ibm_y_o_y.find_one()
    print(ibmY)
    ibmY_title = ibmY["labels"]
    ibmY_numbers = ibmY["numbers"]
    imbY_Dates = ibmY["Dates"]
    imbY_DatesN = ibmY["Dates_Normal"]
    imbY_Vol = ibmY["Volume"]
    imbY_Close = ibmY["Close"]
    ibmY_dict  = {"title":ibmY_title, "Change":ibmY_numbers, "Dates":imbY_Dates, "DatesN": imbY_DatesN, "Volume": imbY_Vol, "Close":imbY_Close}
    return jsonify(ibmY_dict)

@app.route("/IntelY")
def intelY():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/Intel_y_y'
    mongo = PyMongo(app)
    db = mongo.db

    intelY = db.intel_y_o_y.find_one()
    print(intelY)
    intelY_title = intelY["labels"]
    intelY_numbers = intelY["numbers"]
    intelY_Dates = intelY["Dates"]
    intelY_DatesN = intelY["Dates_Normal"]
    intelY_Vol = intelY["Volume"]
    intelY_Close = intelY["Close"]
    intelY_dict  = {"title":intelY_title, "Change":intelY_numbers, "Dates": intelY_Dates, "DatesN": intelY_DatesN, "Volume": intelY_Vol, "Close":intelY_Close}
    return jsonify(intelY_dict)


@app.route("/MSFTY")
def msftY():
    app.config["MONGO_URI"] = 'mongodb://localhost:27017/MSFT_y_y'
    mongo = PyMongo(app)
    db = mongo.db

    msftlY = db.msft_y_o_y.find_one()
    print(msftlY)
    msftlY_title = msftlY["labels"]
    msftlY_numbers = msftlY["numbers"]
    msftlY_Date = msftlY["Dates"]
    msftlYY_DatesN = msftlY["Dates_Normal"]
    msftlY_Vol = msftlY["Volume"]
    msftlYY_Close = msftlY["Close"]
    msftlY_dict  = {"title":msftlY_title, "Change":msftlY_numbers, "Dates": msftlY_Date, "DatesN": msftlYY_DatesN, "Volume": msftlY_Vol, "Close":msftlYY_Close}
    return jsonify(msftlY_dict)

# create a index route
@app.route('/')
def index():
    # Return the template with the teams list passed in
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
