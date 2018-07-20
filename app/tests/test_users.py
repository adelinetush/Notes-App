import unittest
from app.models.User import User

class test_user(unittest.TestCase):
    
    def test_get_username(self):
        u = User("arnold","arinold@gmail.com","youwish")
        self.assertEqual("arnold", u.get_username())

    def test_get_password(self):
        u = User("arnold","arinold@gmail.com","youwish")
        self.assertEqual("youwish", u.get_password())
        
    def test_get_email(self):
        u = User("arinold","arinold@gmail.com","youwish")
        self.assertEqual("arinold@gmail.com", u.get_email())

if(__name__=='__main__'):
    unittest.main()