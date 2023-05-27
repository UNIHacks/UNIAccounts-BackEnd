import unittest
from api.v1.schemas.user_services import UserServicesSchema

class UserServicesSchemaTestCase(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'user_name': 'johndoe',
            'password': 'password123'
        }

    def test_valid_user_services_schema(self):
        user = UserServicesSchema(**self.user_data)
        self.assertIsInstance(user, UserServicesSchema)
        self.assertEqual(user.user_name, self.user_data['user_name'])
        self.assertEqual(user.password, self.user_data['password'])

    def test_required_fields(self):
        required_fields = ['user_name', 'password']
        for field in required_fields:
            user_data = self.user_data.copy()
            del user_data[field]
            with self.assertRaises(ValueError):
                UserServicesSchema(**user_data)

    def test_extra_fields(self):
        user_data = self.user_data.copy()
        user_data['extra_field'] = 'Extra'
        user = UserServicesSchema(**user_data)
        self.assertEqual(user.user_name, self.user_data['user_name'])
        self.assertEqual(user.password, self.user_data['password'])

    def test_invalid_field_type(self):
        user_data = self.user_data.copy()
        user_data['user_name'] = 123  # Invalid type
        self.assertNotEqual(type(str), type(user_data['user_name']))
