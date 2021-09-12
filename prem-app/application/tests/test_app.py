from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Teams(name="Manchester United", stadium='Old Trafford')
        db.session.add(sample1)
        db.session.commit()
        sample2 = Players(first_name= 'Bruno', surname= 'Fernandes', fk_team_id= 1)
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
