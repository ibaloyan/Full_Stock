# import dependencies
from flask import Flask, render_template, jsonify
import pymongo

# init the Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.team_db

# create a route for scraping
@app.route("/apple")
##### Give new name
def Apple():
    appl = db.team.find()
    print(appl)
    return jsonify(appl)
    

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