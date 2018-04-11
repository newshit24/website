from app import app, db
from flask import redirect, url_for, request, render_template, flash
from models import User, Comment
from forms import LoginForm, RegistrationForm, CommentForm
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.route('/misshit')
def misshit():
	return render_template('misshit.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/about')
def about():
	return render_template('about.html')

@login_required
@app.route('/topics', methods=['POST', 'GET'])
def topics():
	
	form=CommentForm()
	if form.validate_on_submit():
		comment=Comment(comment=form.comment.data, author=current_user)
		db.session.add(comment)
		db.session.commit()
		flash('Your comment is now live!')
		return redirect(url_for('topics'))

	comments=Comment.query.all()
	return render_template('topics.html', commentForm=form, comments=comments)


	'''comments=[{'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]'''



@app.route('/login', methods=['GET', 'POST'])
def login():
	form=LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('topics'))
	if form.validate_on_submit():
		user=User.query.filter_by(id=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return render_template('login.html', form=form)
		login_user(user, remember=form.remember_me.data)
		#return url_for('topics')	
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(id=form.username.data)
        user.set_password(form.password.data)
        print(user.set_password(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

