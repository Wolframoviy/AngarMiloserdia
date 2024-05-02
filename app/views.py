from flask import render_template, request, flash, session, redirect
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("angar/index.html")

@app.route("/infinitypvp")
def infinitypvp_index():
    return render_template("infpvp/index.html")