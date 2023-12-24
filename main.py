from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=blog_url)
response.raise_for_status()
blogs = response.json()

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route("/post/<int:id>")
def post(id):
    for post in blogs:
        if post["id"] == id:
            return render_template("post.html", post = post)



if __name__ == "__main__":
    app.run(debug=True)
