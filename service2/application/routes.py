from flask import Flask, Response, request
import random
from application import app

@app.route('/make', methods=['GET'])
def make():
    
    makes = ["Audi", "BMW", "Mercedes"]
    make = makes[random.randrange(0,3)]

    return Response(make, mimetype="text/plain")