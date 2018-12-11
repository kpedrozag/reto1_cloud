#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, redirect, url_for
app = Flask(__name__) 


@app.route("/")
def index():
	return redirect(url_for("about"))

@app.route("/about")
def about():
	return "Kevin Pedroza Goenaga"


@app.route("/<string:op>/<int:a>/<int:b>")
def ophtml(a,b,op):
	if op == "sum":
		return "a = "+str(a)+", b = "+str(b)+", result = "+str(a+b)
	elif op == "divide":
		if b != 0:
			return "a = "+str(a)+", b = "+str(b)+", result = "+str(a/b)
		else:
			return "Error: Division by zero not supported"
	else:
		return "Error in operation"


@app.route("/<string:op>/<int:a>/<int:b>/json")
def opjson(a,b,op):
	if op == "sum":
		return jsonify(a=a, b=b, result=a+b)
	elif op == "divide":
		if b != 0:
			return jsonify(a=a, b=b, result=a/b)
		else:
			return jsonify(message="Error: Division by zero not supported")
	else:
		return jsonify(message="Error in operation")




if __name__ == "__main__":
	app.run(debug=True)