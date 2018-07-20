from flask import Flask
from app.models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'root',
    'db': 'diary',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/diary'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

