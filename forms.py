from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo, Length
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	"""docstring for RegistrationForm"FlaskFormf __init__(self, arg):
		super(RegistrationForm,FlaskForm.__init__()
		self.arg = arg"""

	username=StringField('Username', validators=[DataRequired()])
	password=PasswordField('Password', validators=[DataRequired()])
	password2=PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Register')

	def validate_username(self, username):
		user=User.query.filter_by(id=username.data).first()
		if user is not None:
			raise ValidationError('Please use a differnt username.')

class CommentForm(FlaskForm):
	comment=TextAreaField('Comment', validators=[DataRequired(), Length(min=1, max=500)])
	submit=SubmitField('Submit')


		
