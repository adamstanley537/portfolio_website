from flask import Flask, render_template, url_for, request, redirect
import smtplib
import os
from pathlib import Path

PASSWORD = os.environ.get("PWORD", "Key does not exist")

app = Flask(__name__)

key = {
    "datascience": "Data Science",
    "actuarial": "Actuarial",
    "about_me": "About Me",
}

posts = [
    {
        "element": "datascience",
        "title": "River Pollution Investigation",
        "description": "I have put together a detailed breakdown of the Ocean Clean-Ups study into riverine plastic pollution.",
        "image": "/static/images/TheOceanCleanup.jpg",
        "date": "June 14, 2024",
        "html": "river_pollution",
    },
    {
        "element": "actuarial",
        "title": "Machine Learning in Reserving",
        "description": "This page details the article I wrote when volunteering for the IFoA's Machine Learning in Reserving working party.",
        "image": "/static/images/mlr_img.png",
        "date": "October 31, 2023",
        "html": "ifoa_ml",
    },
    {
        "element": "datascience",
        "title": "Build Your Own - Linear Regression",
        "description": "Here is my attempt at building a linear regression model from scratch in Python.",
        "image": "/static/images/lin_reg.png",
        "date": "June 1, 2023",
        "html": "linear_regression",
    },
    {
        "element": "datascience",
        "title": "Build Your Own - Logistic Regression",
        "description": "Here is my attempt at building a logistic regression model from scratch in Python.",
        "image": "/static/images/log_reg.png",
        "date": "June 25, 2023",
        "html": "logistic_regression",
    },
]

# @app.route("/home")
# def home2():
#     global key
#     category = ""
#     return render_template("elements_base.html", key=key, category=category)

@app.route("/")
def home():
    global key, posts
    category = ""
    return render_template("index.html", key=key, category=category, posts=posts)


@app.route("/<category>")
def elements(category):
    global key, posts
    p = Path.cwd() / "static" / "images" / "travel"
    photos = [file_path._str.replace("/Users/adam/Portfolio/Website/portfolio website","") for file_path in p.iterdir() if file_path._str != "/Users/adam/Portfolio/Website/portfolio website/static/images/travel/.DS_Store"]
    return render_template(f"elements/{category}.html", key=key, category=category, posts=posts, photos=photos)


@app.route("/<category>/<post>")
def post(category, post):
    global key
    return render_template(f"page/{post}.html", key=key, category=category, post=post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return redirect(url_for("home"))
    return redirect(url_for("home"))

def send_email(name, email, message):
    email_message = f"Subject:New Message from portfolio\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("adamstanley537@gmail.com", PASSWORD)
        connection.sendmail("adamstanley537@gmail.com", "adamstanley537@gmail.com", email_message)


if __name__ == "__main__":
    app.run(debug=True)


