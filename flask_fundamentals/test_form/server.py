from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "MYSECRETKEY"

@app.route('/')
def index():
    return render_template('index.html', name='Baka Flocka Flame',  phrase='Hello', times='5')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got POST info"
    session["name"] = request.form['name']
    session["email"] = request.form['email']
    return render_template('/show.html')



app.run(debug=True)

