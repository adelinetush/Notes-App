from flask import Flask
from app.models import db




app = Flask(__name__)



POSTGRES = {
    'user': 'ujunsnkoqsoxle',
    'pw': 'dc931a20cb777d5baa5060c4061b608ae41f51564112e9616d5b845662cea0d7',
    'db': 'deve9bdv2opfal',
    'host': 'ec2-23-21-216-174.compute-1.amazonaws.com',
    'port': '5432',
}

POSTGRESTEST = {
    'user': 'postgres',
    'pw': 'root',
    'db': 'diary',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/diary'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)


