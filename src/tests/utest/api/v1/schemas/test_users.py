import unittest
from datetime import datetime
from pydantic import ValidationError
from api.v1.schemas.users import UserSchema

class UserSchemaTestCase(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'user_name': 'johndoe',
            'phone_number': '1234567890',
            'date_of_birth': '01-01-1990',
            'password': 'password123',
            'role': 'user'
        }

    def test_valid_user_schema(self):
        user = UserSchema(**self.user_data)
        self.assertIsInstance(user, UserSchema)
        self.assertEqual(user.name, self.user_data['name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.user_name, self.user_data['user_name'])
        self.assertEqual(user.phone_number, self.user_data['phone_number'])
        self.assertEqual(user.date_of_birth, datetime.strptime(self.user_data['date_of_birth'], "%d-%m-%Y"))
        self.assertEqual(user.password, self.user_data['password'])
        self.assertEqual(user.role, self.user_data['role'])

    def test_required_fields(self):
        required_fields = ['name', 'last_name', 'email', 'user_name', 'phone_number', 'date_of_birth', 'password', 'role']
        for field in required_fields:
            user_data = self.user_data.copy()
            del user_data[field]
            with self.assertRaises(ValidationError):
                UserSchema(**user_data)

    def test_invalid_date_of_birth(self):
        user_data = self.user_data.copy()
        user_data['date_of_birth'] = 'Invalid Date'
        with self.assertRaises(ValidationError):
            UserSchema(**user_data)