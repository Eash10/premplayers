from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Teams, Players
from application.forms import TeamsForm, PlayersForm, UpdatePlayersForm, UpdateTeamsForm

@app.route('/')
@app.route('/home')

def home():

    return render_template('home.html')

@app.route('/addteam', methods=['GET', 'POST'])
def addteam():
    form = TeamsForm()
    if form.validate_on_submit():
        team_data = Teams(
                team_name = form.team_name.data,
                stadium = form.stadium.data
        )
        db.session.add(team_data)
        db.session.commit()
        return redirect(url_for('teams'))
    return render_template('addteam.html', form=form)

@app.route('/addplayer/<int:id>', methods=['GET', 'POST'])
def addplayer(id):
    form = PlayersForm()
    all_teams = Teams.query.all()
    if form.validate_on_submit() and id<=len(all_teams):
        player_data = Players(
            first_name = form.first_name.data,
            surname = form.surname.data,
            fk_team_id = id
        )
        db.session.add(player_data)
        db.session.commit()
        return redirect(url_for('players'))
    return render_template('addplayer.html', form=form)

@app.route('/delteam/<int:id>')
def delteam(id):
    team_to_delete = Teams.query.filter_by(team_id=id).first()
    db.session.delete(team_to_delete)
    db.session.commit()
    return redirect(url_for('teams'))

@app.route('/delplayer/<int:id>')
def delplayer(id):
    player_to_delete = Players.query.filter_by(player_id=id).first()
    db.session.delete(player_to_delete)
    db.session.commit()
    return redirect(url_for('players'))

@app.route('/teams')
def teams():
    teams_data = Teams.query.all()
    return render_template('teams.html', teams=teams_data)

@app.route('/players')
def players():
    players_data = Players.query.all()
    return render_template('players.html', players=players_data)

@app.route('/updateteam/<int:id>', methods=['GET', 'POST'])
def updateteam(id):
    team = Teams.query.filter_by(team_id=id).first()
    form = UpdateTeamsForm()
    if form.validate_on_submit():
        team.team_name = form.team_name.data
        team.stadium = form.stadium.data
        db.session.commit()
        return redirect(url_for('teams'))
    return render_template('updateteam.html', form=form)

@app.route('/updateplayer/<int:pid>/<int:tid>', methods=['GET', 'POST'])
def updateplayer(pid,tid):
    player = Players.query.filter_by(player_id=pid).first()
    form = UpdatePlayersForm()
    all_teams = Teams.query.all()
    if form.validate_on_submit() and tid<=len(all_teams):
        if form.validate_on_submit():
            player.first_name = form.first_name.data
            player.surname = form.surname.data
            player.fk_team_id = tid
            db.session.commit()
            return redirect(url_for('players'))
    return render_template('updateplayer.html', form=form)