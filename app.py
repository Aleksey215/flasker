"""
Main page application
"""
from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
    """
    render template for main page
    """
    return render_template("index.html")


# localhost:5000/user/Alex
@app.route('/user/<name>')
def user(name):
    """
    render template with variable user_name
    name input from browser
    """
    return render_template("user.html", user_name=name)


# create custom error pages
# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
