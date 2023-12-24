import random
import smtplib
from flask import Flask,render_template, request
import requests

my_email = "bdiop8683@gmail.com"
password = ""

app = Flask(__name__)
reponse = requests.get(url="https://api.npoint.io/8ab1fb320ec3fe1518bd")
reponse.raise_for_status()
posts = reponse.json()


@app.route("/")
def home():
    return render_template("index.html",posts = posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",  methods = ['POST', 'GET'])
def contact():
    if request.method == "POST":

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr= my_email, to_addrs={request.form['email']}, msg=f"Subject: Contact from {request.form['name']}\n\n {request.form['message']}\n"
                                                                                           f"My phone number {request.form['phone']}")
        return render_template("contact.html", method = "post")
    else:
        return render_template("contact.html", method = "get")


@app.route("/<int:id>")
def post(id):
    # post_test = posts[0]
    for post_test in posts:
        if post_test["id"]==id:
            return render_template("post.html", post = post_test)

# @app.route("/form-entry", methods = ['POST'])
# def receive_data():
#     if request.method == "POST":
#         print(f"{request.form['name']}\n{request.form['email']}\n{request.form['phone']}\n{request.form['message']}")
#         return render_template("contact.html")