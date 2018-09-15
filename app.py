# import dependencies
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

# init the Flask
app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/nhl_db'
mongo = PyMongo(app)

# Pass connection to the pymongo instance.


# Connect to a database. Will create one if not already available.
db = mongo.db

# create a route for scraping
@app.route("/apple")
##### Give new name
def Apple():
    appl = db.articles.find_one()
    print(appl)
    appl_title = appl["title"]
    appl_dict = {"titel":appl_title}
    print(appl_title)
    # return appl_title
    return jsonify(appl_dict)
    

# @app.route("/amazon")
# ##### Give new name
# def AMZA():
#     amaz = list(db.collection_name.find())
#     return jsonify(amaz)   

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