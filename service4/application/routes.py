from flask import Flask, Response, request
import random
from application import app

@app.route('/model', methods=['GET','POST'])
def model():

    info = request.data.decode('utf-8')
    data = info.split(" ")
    shape = data[0]
    make = data[1]

    if make == "Audi":
        if shape == 'Hatchback':
            model = 'A3'
        elif shape == 'Saloon':
            model = 'A6'
        elif shape == 'SUV':
            model = 'Q7'
    elif make == "BMW":
        if shape == 'Hatchback':
            model = '1-Series'
        elif shape == 'Saloon':
            model = '5-Series'
        elif shape == 'SUV':
            model = 'X5'
    elif make == "Mercedes":
        if shape == 'Hatchback':
            model = 'A-Class'
        elif shape == 'Saloon':
            model = 'E-Class'
        elif shape == 'SUV':
            model = 'GLE'
    else:
        return "model not found"

    
    return Response(model, mimetype="text/plain")