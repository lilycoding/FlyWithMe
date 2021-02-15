import unittest

from app.models import User
from app import db

class TestUserModel(unittest.TestCase):
    """ test all aspects of the user model """

    def setUp(self):
        """ this is run before each test """
        # alice's attributes
        self.alice_first_name = 'Alice'
        self.alice_last_name = 'Wonderland'
        self.alice_email = 'student@example.com'
        # hatter's attributes
        self.hatter_first_name = 'Mad'
        self.hatter_last_name = 'Hatter'
        self.hatter_email = 'professor@example.com'
    
    def tearDown(self):
        """ this is run after each test. You always want to run cleanup after testing
        so your database doesn't have irrelevant data, and so that you can run the
        tests again and again without issue. """
        # therefor, we dont' want to keep the hatter in the database
        # first, we check to see that the hatter is in the database
        hatter = User.query.filter_by(email=self.hatter_email).first()
        # if the hatter is in the database, we delete the hatter
        # this makes our database identical to when we started out
        if hatter:
            db.session.delete(hatter)
            db.session.commit()

    def test_users_in_databsae(self):
        """ test that our first user, Alice Wonderland, is in the database """
        # get the first user from the database, as defined in our seed_db.py file
        alice = User.query.first()
        self.assertEqual(self.alice_first_name, alice.first_name)
        self.assertEqual(self.alice_last_name, alice.last_name)
        self.assertEqual(self.alice_email, alice.email)
    
    def test_create_new_user(self):
        """ test that you can create a new user, Mad Hatter """
        # first, set up what we need to create a new user
        # you can find this in the User model's __init__ method
        # in this case, these attributes are defined in our setUp function
        # create the new user
        hatter = User(
            self.hatter_first_name,
            self.hatter_last_name,
            self.hatter_email
        )
        # add the new user to the session
        db.session.add(hatter)
        # commit the new user to the database
        db.session.commit()
        # use the previously defined variables to find the user we just created
        hatter_from_db = User.query.filter_by(email=self.hatter_email).first()
        # test that they are equal, or that the user was created with the correct attributes
        self.assertEqual(self.hatter_first_name, hatter_from_db.first_name)
        self.assertEqual(self.hatter_last_name, hatter_from_db.last_name)
        self.assertEqual(self.hatter_email, hatter_from_db.email)
