from application import db 
from application.models import Teams, Players

db.drop_all()
db.create_all()