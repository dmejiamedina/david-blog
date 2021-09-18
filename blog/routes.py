from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

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


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password','danger')
	return render_template('login.html', title='Login', form=form)