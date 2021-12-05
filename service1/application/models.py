from application import db

class car(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    make= db.Column(db.String(50), nullable=False,)
    shape= db.Column(db.String(50), nullable=False) 
    model =  db.Column(db.String(50), nullable=False)