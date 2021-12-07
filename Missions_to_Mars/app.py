# Dependencies
from flask import Flask, render_template
import pymongo
import scrape_mars

# Creating app
app= Flask(__name__)

# Connecting to database
conn="mongodb://localhost:27017"
client= pymongo.MongoClient(conn)
db=client.mars_db

# Creating route
@app.route("/")
def homepage():
    mars=db.mars.find_one()
    return render_template("index.html", mars=mars)

# Creating route
@app.route("/scrape")
def scrape():
    mars_info=db.mars_info
    mars_data=scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)

if __name__ == "__main__":
    app.run(debug=True)



