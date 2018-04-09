from app import db

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	password=db.Column(db.String(30))
	comment=db.relationship('Comment', backref='author', lazy='dynamic')

	def __repr__(self):
		return self.id

class Comment(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	timestamp=db.Column(db.DataTime)
	comment=db.Column(db.String(500))
	user=db.Column(db.Integer, db.ForeignKey('user'))

	def __repr__(self):
		return self.comment
		