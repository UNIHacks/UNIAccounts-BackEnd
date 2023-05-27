import unittest
from models.users import UsersModel
from datetime import datetime
from pydantic import ValidationError
from api.v1.schemas.users import UserSchema

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = UsersModel(
            name='John', 
            last_name='userlast', 
            email='user1@example.com',
            user_name='user1', 
            phone_number='5513784059', 
            date_of_birth='21-01-1999',
            password='paswwordSegura',
            role='Student'
        )
    def test_dict_attributes(self):
        # Check that attributes are correct
        expected_data = {
            'name'              : 'John',
            'last_name'         : 'userlast',
            'email'             : 'user1@example.com',
            'user_name'         : 'user1',
            'phone_number'      : '5513784059',
            'date_of_birth'     : '21-01-1999',
            'password'          : '',
            'role'              : 'Student',
        }
        
        real_user = {
            'name'              : self.user.name,
            'last_name'         : self.user.last_name,
            'email'             : self.user.email,
            'user_name'         : self.user.user_name,
            'phone_number'      : self.user.phone_number,
            'date_of_birth'     : self.user.date_of_birth,
            'password'          : '',
            'role'              : self.user.role,
        }
     
        self.assertEqual(real_user, expected_data)

    def test_dict_key_found(self):
        # Check that the correct value returns if the key exists
        self.assertEqual(self.user.user_name, 'user1')