# coding=UTF-8


from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')

@app.route('/')
def homePage():
	# logging.debug(dir(request.args))
	return render_template('index.html')
	
@app.route('/traffic')
def test():
	return render_template('traffic.html')