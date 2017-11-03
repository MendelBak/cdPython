from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "mendelIsBatman"

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template("index.html")

@app.route("/add_two")
def add_two():
    session["counter"] += 1
    return redirect("/")

@app.route("/reset_button")
def reset_button():
    session.clear()
    return redirect("/")
    




app.run(debug=True)