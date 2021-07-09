from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
Bootstrap(app)

birthyear = 1987


@app.route("/")
def home():
    age = datetime.now().year - birthyear
    return render_template("index.html", age=age)


if __name__ == "__main__":
    app.run(debug=True)
