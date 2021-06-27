from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		"author": "david",
		"title": "blog post 1",
		"content": "this is my first blog",
		"date_posted": "June 6 2021"
	},
	{	"author": "brad",
		"title": "blog post 2",
		"content": "this is my blog post",
		"date_posted": "June 7 2021"
	},
	{	"author": "bryan",
		"title": "blog post 3",
		"content": "brad saw bruno today",
		"date_posted": "June 7 2021"
	}
]
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About") 

if __name__ == "__main__":
	app.run(debug=True)