import os
from flask import Flask, render_template, request, url_for, flash
import pymongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "ms3_seriesdb"
COLLECTION = "series"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/post_delete")
def post_delete():
    return render_template("post_delete.html")


@app.route("/cards")
def cards():
    return render_template("cards.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/show")
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
