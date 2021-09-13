from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Teams(team_name="Manchester United", stadium='Old Trafford')
        db.session.add(sample1)
        db.session.commit()
        sample2 = Players(first_name= 'Bruno', surname= 'Fernandes', fk_team_id= 1)
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_teams_get(self):
        response = self.client.get(url_for('teams'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manchester United', response.data)
    
    def test_add_team_get(self):
        response = self.client.get(url_for('addteam'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Liverpool', response.data)
    
    def test_add_player_get(self):
        response = self.client.get(url_for('addplayer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'James', response.data)
    
class TestAddTeam():
    def test_add_team(self):
        response = self.client.post(
            url_for('addteam'),
            data = dict(team_name='Liverpool', stadium='Anfield'),
            follow_redirects = True
        )
        self.assertIn(b'Liverpool', response.data)

class TestAddPlayer():
    def test_add_player(self):
        response = self.client.post(
            url_for('addplayer', id=1),
            data = dict(first_name='Marcus', surname='Rashford'),
            follow_redirects = True
        )
        self.assertIn(b'Marcus', response.data)   

class TestUpdateTeam():
    def test_Update_team(self):
        response = self.client.post(
            url_for('updateteam', id=1),
            data = dict(team_name='Manchester City', stadium='Ethiad'),
            follow_redirects = True
        )
        self.assertIn(b'Manchester City', response.data)

class TestUpdatePlayer():
    def test_update_player(self):
        response = self.client.post(
            url_for('updateplayer', pid=1, tid=1),
            data = dict(frist_name='Steven', surname='Gerrard'),
            follow_redirects = True
        )
        self.assertIn(b'Steven', response.data)

class TestDeleteTeam():
    def test_del_team(self):
        response = self.client.post(
            url_for('delteam', id=1),
            follow_redirects = True
        )
        self.assertNotIn(b'Manchester United', response.data)

class TestDeletePlayer():
    def test_del_player(self):
        response = self.client.post(
            url_for('delplayer', id=1),
            follow_redirects = True
        )
        self.assertNotIn(b'Steven', response.data)
