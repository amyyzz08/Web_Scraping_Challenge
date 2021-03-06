# Dependencies
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Creating app
app= Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Creating route for homepage
@app.route("/")
def homepage():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data = mars_data)

# Creating route when button is clicked
@app.route("/scrape")
def do_scrape():
    mars_info = mongo.db.mars_data
    mars_data = scrape_mars.scrape_all()
    mars_info.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)



