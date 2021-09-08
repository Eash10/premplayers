from application import db

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    stadium = db.Column(db.String(30), nullable=False)
    players = db.relationship('Players', backref='team')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    surname_name = db.Column(db.String(30), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams`.id'), nullable=False)