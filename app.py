# import dependencies
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# init the Flask
app = Flask(__name__)

# create a route for scraping
@app.route("/scrape")
##### Give new name
def testing():
    # call the scrape_mars.py
    scraped_info = scrape_mars.scrape()
    # create a dictionary of the scraped info from it
    ### EDIT AFTER VARAIBLES ARE CREATED
    use = {
        "var1":scraped_info["var1"],
        "var2":scraped_info["var2"],
        "var3":scraped_info["var3"],
        "var4":scraped_info["var4"],
        "var5":scraped_info['var5'],
        "var6":scraped_info["var16"]
    }
    ### EDIT AFTER VARAIBLES ARE CREATED
    


    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.youtube_db

    # Drops collection if available to remove duplicates
    db.youtube_info.drop()

    # Creates a collection in the database and insert document
    db.youtube_info.insert_one(
        use
    )
    # Redirect back to home page
    return redirect("/", code=302)

# create a index route
@app.route('/')
def index():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.mars_db
    # Store the entire team collection in a list
    info = list(db.youtube_info.find())
    print(info)
    

    # Return the template with the teams list passed in
    #### Change INFO22 to new name
    return render_template('index.html', htmlRefVar=info)


if __name__ == "__main__":
    app.run(debug=True)