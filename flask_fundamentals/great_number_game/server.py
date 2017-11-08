from flask import Flask, render_template, redirect, session, request, flash
import random
app = Flask(__name__)
app.secret_key = "im_batman"

@app.route("/")
def index():
    session.clear()
    session["random_num"] = random.randint(1, 100)
    print session["random_num"]
    return render_template("/index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["picked_num"] = int(request.form["picked_num"])
    print "This is the session variable for picked_num", session["picked_num"] # check the session variable
    return redirect("/guess_response")

@app.route("/guess_response")
def guess_response():
    if session["random_num"] > session["picked_num"]:
        print "Too low. Try a higher number"
    elif session["random_num"] < session["picked_num"]:
        print "Too high. Try a lower number"
    else:
        flash("You Win! The random number was {}".format(session["random_num"]))
        print "You Win!"
    return render_template("/guess_response.html")
app.run(debug=True)