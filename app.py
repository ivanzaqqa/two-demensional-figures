from flask import Flask, render_template, request, jsonify
from diagonal_controller import DiagonalController

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/square", methods=['GET', 'POST'])
def getsquare():
	if request.method == 'GET':
		return render_template("square.html")
	else:
		return DiagonalController.getSquare(request)

@app.route("/circle", methods=['GET', 'POST'])
def getcircle():
	if request.method == 'POST':
		return DiagonalController.getCircle(request)
	else:
		return render_template("circle.html")

@app.route("/rectangle", methods=['GET', 'POST'])
def getrectangle():
	if request.method == 'POST':
		return DiagonalController.getRectangle(request)
	else:
		return render_template("rectangle.html")

@app.route("/triangle", methods=['GET', 'POST'])
def gettriangle():
	if request.method == 'POST':
		return DiagonalController.getTriangle(request)
	else:
		return render_template("triangle.html")

if __name__ == '__main__':
	app.run(debug=True)