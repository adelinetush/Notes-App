#!flask/bin/python
# 
import os 
from app import app

#app.run(debug=True)
port = int(os.environ.get('PORT',8080))
if(__name__=="__main__"):
    app.config['DEBUG'] = True

    app.debug = True
    app.run()