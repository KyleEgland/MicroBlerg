#! python
#
from app import app
from app.forms import LoginForm
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Kyle"}
    posts = [
        {
            "author": {"username": "Jimbo"},
            "body": "This is a twitter, I guess?"
        },
        {
            "author": {"username": "Steve-erino"},
            "body": "Yay, more places to put my thoughts!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, "
            f"remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign in", form=form)
