from application import db

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    stadium = db.Column(db.String(30), nullable=False)
    players = db.relationship('Players', backref='Teams')

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    fk_team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)