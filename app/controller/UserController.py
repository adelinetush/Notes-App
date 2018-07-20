from app.models.model.Model import User
from app.models import db

class UserController:
    global users


    
    def __init__(self):
        print('ini self')
        self.users = []
    
    def register(self,username,email,password):
        if not db.session.query(User).filter(User.email==email).count():
            u = User(username, email, password)
            db.session.add(u)
            db.session.commit()
            return u.serialize()
        return None

    def login(self, email, password):
        for user in User.query.filter(User.email == email):
            if(user.email == email and user.password== password):
                return True;
        return False;


    def authenticate(self, username, password):
        for user in User.query.filter(User.email == username):
            return user;
        return False;

    def identity(self, payload):
        user_id = payload['identity']
        for user in User.query.filter(User.id==user_id):
            return user