from flask import Flask, render_template
import requests
import time


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_blog_posts = requests.get(blog_url).json()


@app.route('/')
def home():
    global all_blog_posts
    year = time.gmtime().tm_year
    return render_template("index.html", CURRENT_YEAR=year, posts=all_blog_posts)


@app.route("/blog/<num>")
def get_blog(num):
    global all_blog_posts
    return render_template("post.html", posts=all_blog_posts, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)

