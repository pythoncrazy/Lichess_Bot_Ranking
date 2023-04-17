# importing flask
from flask import Flask, render_template

# importing pandas
import pandas as pd


app = Flask(__name__)


# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
	
	# converting csv to html
	data = pd.read_csv('bullet.csv',header=0)
	return render_template('table.html', tables=[data.to_html()], titles=[''])


if __name__ == "__main__":
	app.run(host="localhost", port=int("5000"))
