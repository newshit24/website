from app import db, app, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.query.get(id)

class User(db.Model, UserMixin):
	id=db.Column(db.String(30), primary_key=True)
	password=db.Column(db.String(30))
	comment=db.relationship('Comment', backref='author', lazy='dynamic')

	def __repr__(self):
		return self.id

	def set_password(self, password):
		self.password=generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

class Comment(db.Model, UserMixin):
	id=db.Column(db.Integer, primary_key=True)
	timestamp=db.Column(db.DateTime)
	comment=db.Column(db.String(500))
	user=db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return self.comment



		