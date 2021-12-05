from flask import Flask, Response, request
import random
from application import app

@app.route('/shape', methods=['GET'])
def team():

    teams = ["Hatchback", "Saloon", "SUV"]

    team = teams[random.randrange(0,3)]
    
    return Response(team, mimetype="text/plain")