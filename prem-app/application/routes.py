from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Teams, Players
from application.forms import TeamsForm, PlayersForm, UpdatePlayersForm, UpdateTeamsForm