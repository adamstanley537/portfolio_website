from flask import Flask, render_template, url_for, request, redirect
import smtplib
import os
from pathlib import Path

PASSWORD = os.environ.get("PWORD", "Key does not exist")
EMAIL = os.environ.get("EMAIL", "Key does not exist")

app = Flask(__name__)
photos=['/static/images/travel/IMG_3224.jpeg', '/static/images/travel/IMG_2474.jpeg', '/static/images/travel/IMG_2638.jpeg', '/static/images/travel/IMG_0407.JPG', '/static/images/travel/IMG_2584.jpeg', '/static/images/travel/3bbef144-1990-47db-b780-c6518c3a4e29.JPG', '/static/images/travel/IMG_1668.jpg', '/static/images/travel/IMG_3287.jpeg', '/static/images/travel/IMG_3194.jpeg', '/static/images/travel/IMG_2506.jpeg', '/static/images/travel/IMG_3086.jpeg', '/static/images/travel/IMG_3439.jpeg', '/static/images/travel/IMG_2814.jpeg', '/static/images/travel/IMG_1457.JPG', '/static/images/travel/IMG_1455.JPG', '/static/images/travel/IMG_0720.jpeg', '/static/images/travel/IMG_2662.jpeg', '/static/images/travel/IMG_1012.jpeg', '/static/images/travel/IMG_2393.jpeg', '/static/images/travel/IMG_2501.jpeg', '/static/images/travel/IMG_1213.jpeg', '/static/images/travel/IMG_1090.jpeg', '/static/images/travel/IMG_0822.jpeg', '/static/images/travel/IMG_1225.jpeg', '/static/images/travel/IMG_2389.jpeg', '/static/images/travel/6ab5db1a-f93b-4c81-a98e-ab2f64b24f01.JPG', '/static/images/travel/IMG_0730.jpeg', '/static/images/travel/IMG_0771.jpeg', '/static/images/travel/b2f1254f-4025-432b-ba73-20ebc1c70fbf.JPG', '/static/images/travel/IMG_1588.jpeg', '/static/images/travel/IMG_1072.jpeg', '/static/images/travel/IMG_0970.jpeg', '/static/images/travel/img_resize.jpeg', '/static/images/travel/IMG_2582.jpeg', '/static/images/travel/IMG_0792.jpeg', '/static/images/travel/IMG_3385.jpeg', '/static/images/travel/IMG_2828.jpeg', '/static/images/travel/IMG_1189.JPG', '/static/images/travel/IMG_2485.jpeg', '/static/images/travel/IMG_3410.jpeg', '/static/images/travel/IMG_1573.JPG', '/static/images/travel/d4330b6b-8bc5-4d6a-94bf-df338c008924.JPG', '/static/images/travel/19b0a524-7120-42f2-9dc4-947ee1a4eac0.JPG', '/static/images/travel/IMG_0986.jpeg', '/static/images/travel/f538ab83-4895-4eee-80b4-7de49408f311.JPG', '/static/images/travel/IMG_1026.jpeg', '/static/images/travel/IMG_1134.jpeg', '/static/images/travel/IMG_0965.jpeg', '/static/images/travel/IMG_0877.jpeg', '/static/images/travel/IMG_1267.jpeg', '/static/images/travel/IMG_2125.jpeg', '/static/images/travel/IMG_0991.jpeg', '/static/images/travel/5c007da5-d4a6-4190-be0a-78a30a2da523.JPG', '/static/images/travel/IMG_2596.jpeg', '/static/images/travel/003cc78a-464f-4990-9334-fb460671ec99.JPG', '/static/images/travel/IMG_0051.jpeg', '/static/images/travel/IMG_1465.JPG', '/static/images/travel/IMG_3322.jpeg', '/static/images/travel/IMG_1077.jpeg', '/static/images/travel/e5b192e7-2e22-4819-b1a9-1b75c0fe51c6.JPG', '/static/images/travel/IMG_1333.jpeg', '/static/images/travel/IMG_0943.jpeg', '/static/images/travel/IMG_2753.jpeg', '/static/images/travel/IMG_0810.jpeg', '/static/images/travel/IMG_2694.jpeg', '/static/images/travel/IMG_1016.jpeg', '/static/images/travel/IMG_1295.jpeg', '/static/images/travel/IMG_0893.jpeg', '/static/images/travel/IMG_2945.jpeg', '/static/images/travel/IMG_0755.jpeg', '/static/images/travel/IMG_3026.jpeg', '/static/images/travel/IMG_2908.jpeg', '/static/images/travel/IMG_2748.jpeg', '/static/images/travel/IMG_3374.jpeg']

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
    # p = Path.cwd() / "static" / "images" / "travel"
    # photos = [file_path._str.replace("/Users/adam/Portfolio/Website/portfolio website","") for file_path in p.iterdir() if file_path._str != "/Users/adam/Portfolio/Website/portfolio website/static/images/travel/.DS_Store"]
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
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=False)


