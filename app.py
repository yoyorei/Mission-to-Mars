from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

@app.route("/")
def home():

    mars_data = mongo.db.collection.find()

    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
def scrape():

    scrape_data = scrape_mars.scrape()

    mongo.db.collection.drop()
    mongo.db.collection.insert_one(scrape_data)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)