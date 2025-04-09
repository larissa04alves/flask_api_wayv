import email
from . import db

class Pessoa(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(100), nullable=False)
    nascimento= db.Column(db.Date, nullable=False)
    sexo= db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    telefone= db.Column(db.String(20), nullable=False)

    