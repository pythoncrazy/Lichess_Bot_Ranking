# importing flask
from flask import Flask, render_template

# importing pandas
import pandas as pd


app = Flask(__name__)


# route to the bullet current ratings
#TODO: expand to all rating systems, as well as current and maximum rating
#DONE :)
#TODO: make homepage
@app.route('/')
def welcome_page():
    return render_template('Welcome.html')

@app.route('/bullet_current')
def bullet_current_rating():
	
	# converting csv to html
	data = pd.read_csv('bullet/bullet_sorted_by_current_rating.csv',header=0)
	return render_template('Current.html', tables=[data.to_html()], titles=[''])

@app.route('/bullet_max')
def bullet_max_rating():
	
	# converting csv to html
	data = pd.read_csv('bullet/bullet_sorted_by_max_rating.csv',header=0)
	return render_template('Maximum.html', tables=[data.to_html()], titles=[''])

@app.route('/blitz_current')
def blitz_current_rating():
	
	# converting csv to html
	data = pd.read_csv('blitz/blitz_sorted_by_current_rating.csv',header=0)
	return render_template('Maximum.html', tables=[data.to_html()], titles=[''])

@app.route('/blitz_max')
def blitz_max_rating():
	
	# converting csv to html
	data = pd.read_csv('blitz/blitz_sorted_by_max_rating.csv',header=0)
	return render_template('Maximum.html', tables=[data.to_html()], titles=[''])

@app.route('/rapid_current')
def rapid_current_rating():
	
	# converting csv to html
	data = pd.read_csv('rapid/rapid_sorted_by_current_rating.csv',header=0)
	return render_template('Maximum.html', tables=[data.to_html()], titles=[''])

@app.route('/rapid_max')
def rapid_max_rating():
	
	# converting csv to html
	data = pd.read_csv('rapid/rapid_sorted_by_max_rating.csv',header=0)
	return render_template('Maximum.html', tables=[data.to_html()], titles=[''])


if __name__ == "__main__":
	app.run(host="localhost", port=int("5000"))
