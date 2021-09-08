from application import db 
# from application.models import Songs, Setlist

db.drop_all()
db.create_all()