from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/ninja")
def ninja():
    return render_template("/ninja.html")

@app.route("/ninja_blue")
def ninja_blue():
    return render_template("/ninja_blue.html")

@app.route("/ninja_orange")
def ninja_orange():
    return render_template("/ninja_orange.html")

@app.route("/ninja_red")
def ninja_red():
    return render_template("/ninja_red.html")

@app.route("/ninja_purple")
def ninja_purple():
    return render_template("/ninja_red.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/notapril.html")

app.run(debug=True)