#!/usr/bin/env python3.4 

from flask import Flask, render_template
import calculations

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html", DistList=calculations.DistanceList(), DistRelList=calculations.DistanceRelationList())

@app.route("/sources")
def sources():
    return render_template("sources.html")

if __name__=="__main__":
    app.run()
