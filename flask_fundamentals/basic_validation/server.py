from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form["email"]) < 1:
        flash("Email is too short. Try again.")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email")
    else:
        flash("Good email")
    return redirect('/')
app.run(debug=True)