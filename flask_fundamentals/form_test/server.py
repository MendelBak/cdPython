from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Baka Flocka Flame',  phrase='Hello', times='5')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got POST info"

    name = request.form['name']
    email = request.form['email']

    return redirect('/')
app.run(debug=True)

