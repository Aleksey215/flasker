"""
Main page application
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from settings_management import settings


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = settings['SECRET_KEY']


# Create a form class
class NameForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
@app.route('/')
def index():
    """
    render template for main page
    """
    return render_template("index.html")


# localhost:5000/user/Alex
@app.route('/user/<name>')
def user(name: str):
    """
    render template with variable user_name

    Args:
        name (str): name input from browser
    """
    return render_template("user.html", user_name=name)


# create custom error pages
# Invalid url
@app.errorhandler(404)
def page_not_found(error):
    """
    Render 404 page error

    Args:
        error (_type_): exception

    """
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


# Create Name Page
@app.route(rule='/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)
