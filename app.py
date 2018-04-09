from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
	return "<h1>HIT Protest"

if __name__=='__main__':
	app.run()