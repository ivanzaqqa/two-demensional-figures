from flask import Flask, jsonify, request
from math import pi

class DiagonalController():

	def getSquare(request):
		side = request.json['side']
		area = side * 2
		result = {"result": area}
		return jsonify(result)

	def getCircle(request):
		r = request.json['radius']
		area = pi * r * r
		result = {"result": area}
		return jsonify(result)

	def getRectangle(request):
		w = request.json['width']
		l = request.json['length']
		area = w * l
		result = {"result": area}
		return jsonify(result)

	def getTriangle(request):
		b = request.json['base']
		h = request.json['height']
		area = b * h / 2
		result = {"result": area}
		return jsonify(result)