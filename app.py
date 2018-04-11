from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

app=Flask(__name__)
db=SQLAlchemy(app)
app.config.from_object(Config)
login=LoginManager(app)
login.login_view='login'

#migrate=Migrate(app, db)


from views import *

if __name__=='__main__':
	app.run(port=80)