from flaskblog.models import User, Post
from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, db, bcrypt

posts=[
	{
		'author':'Chirag Bellara',
		'title':'Blog Post One',
		'content':'Content of Post 1',
		'date_posted':'September 21, 2018'
	},
	{
		'author':'Avantika Kapoor',
		'title':'Blog Post Two',
		'content':'Content of Post 2',
		'date_posted':'September 20, 2018'
	}
]


@app.route("/")			#Routes to various pages on the website
@app.route("/home")		#To set multile routes to a single page, just stack  
						#the @app.routes() followed by the function definition
def home():
    return render_template("homepage.html",posts=posts,title="Home Page")

@app.route("/about")
def about():
	return render_template("aboutpage.html", title="About Page")

@app.route("/register",methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been successfully created. You are now able to Login','success')
		return redirect(url_for('login'))
	return render_template('register.html', title="Register", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check Username and Password','danger')
	return render_template('login.html', title="Login", form=form)

