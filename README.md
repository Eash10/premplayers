# Premier League players 
## Description
This is a CRUD application which allows you to add Premier League teams and players and link the teams to players
## Installation
This is assuming that you are working on an Ubuntu VM, at least version 18.04 LTS. This is a Flask application so Python3, a virtual environment and pip3 will need to be installed.
```bash
sudo apt install python3 python3-venv python3-pip
```
To install the requirements you will need to create and activate a virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate
```
And then install the requirements
```bash
pip3 install -r requirements.txt
```
And you can then create the database and run the app
```bash
python3 create.py
python3 app.py
```

## Tests
you can run coverage tests by using pytest --cov.
```bash
python3 -m pytest --cov=app
```

## License
[MIT](https://choosealicense.com/licenses/mit/)