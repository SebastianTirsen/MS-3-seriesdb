import os
from flask import (
    Flask, render_template, redirect, 
    request, session, url_for, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


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
    users = mongo.db.users.find()
    return render_template("profile.html", users=users)


@app.route("/show")
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
