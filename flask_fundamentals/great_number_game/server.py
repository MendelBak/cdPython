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
    session["picked_num"] = request.form["picked_num"]
    return redirect("/guess_response")

@app.route("/guess_response")
def guess_response():
    if session["picked_num"] > session["random_num"]:
        print "Your guess was too high!"
    elif session["picked_num"] < session["random_num"]:
        print "Your guess was too low!"
    else:
        print "You Win!"
    return render_template("/guess_response.html")
    
    

app.run(debug=True)
