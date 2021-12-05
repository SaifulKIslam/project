from flask import Flask, render_template, request
import requests
from application import app, db


@app.route('/', methods=['GET','POST'])
def index():
    #get make
    make = requests.get("http://service2:5001/make")
    #get shape
    shape = requests.get("http://service3:5002/shape")
    #post model
    info = str(make.text) + " " + str(shape.text)
    model = requests.post("http://service4:5003/model", data=info)


    return render_template('index.html', title='model shape', make=make.text, shape=shape.text, info=info, model=model.text)