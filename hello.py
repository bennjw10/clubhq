from flask import Flask, render_template


#create a flask instance
app = Flask(__name__, static_folder='static')


#create a route decorator
@app.route ('/')


def index():
    first_name = "Benn"
    stuff = "this is <strong>bold</strong> text"
    return render_template("index.html", first_name=first_name, stuff=stuff)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

