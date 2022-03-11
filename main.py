# Building a blog with jinja + flask! Awesome!

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:postid>')
def get_post(postid):
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", posts=all_posts, postid=postid)


if __name__ == "__main__":
    app.run(debug=True)



