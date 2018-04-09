import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'Thisisasecret'
	SQLALCHEMY_DATABASE_URI = 'postgresql://hitnews:newshit@localhost' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	DEBUG=True