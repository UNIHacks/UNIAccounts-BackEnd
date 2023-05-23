# import unittest
# from models.user import *

# class TestUser(unittest.TestCase):

#     def setUp(self):
#         self.user = User(nick_name='user1', password='1234', email='user1@example.com',
#                          name='John', last_name_fathers='Doe', last_name_mothers='Smith',
#                          account_number='0123456789', careers='Computer Science',
#                          half_year=3, role='Student', role_key='1234')

#     def test_dict_attributes(self):
#         # Check that attributes are correct
#         expected_data = {
#             'nick_name'         : 'user1',
#             'password'          : '1234',
#             'email'             : 'user1@example.com',
#             'name'              : 'John',
#             'last_name_fathers' : 'Doe',
#             'last_name_mothers' : 'Smith',
#             'account_number'    : '0123456789',
#             'careers'           : 'Computer Science',
#             'half_year'         : 3,
#             'role'              : 'Student',
#             'role_key'          : '1234',
#         }
#         self.assertEqual(self.user.__dict__(), expected_data)

#     def test_dict_key_found(self):
#         # Check that the correct value returns if the key exists
#         self.assertEqual(self.user.__dict__().get('nick_name'), 'user1')

#     def test_from_dict_method_with_valid_data(self):
#         # Create a dictionary with valid data
#         data = {
#             'nick_name': 'test_user',
#             'password': 'test_password',
#             'email': 'test_email@test.com',
#             'name': 'Test',
#             'last_name_fathers': 'User',
#             'last_name_mothers': 'TestUser',
#             'account_number': '123456789',
#             'careers': 'Computer Science',
#             'half_year': 2,
#             'role': 'admin',
#             'role_key': 'admin123'
#         }

#         # Call the from_dict() method with the dictionary
#         user = User.from_dict(data)

#         # Verify that the user object has been created correctly
#         self.assertEqual(user.nick_name, 'test_user')
#         self.assertEqual(user.email, 'test_email@test.com')
#         self.assertEqual(user.name, 'TEST')
#         self.assertEqual(user.last_name_fathers, 'USER')
#         self.assertEqual(user.last_name_mothers, 'TESTUSER')
#         self.assertEqual(user.account_number, '123456789')
#         self.assertEqual(user.careers, 'Computer Science')
#         self.assertEqual(user.half_year, 2)
#         self.assertEqual(user.role, 'admin')
#         self.assertEqual(user.role_key, 'admin123')


#     def test_from_dict_method_with_missing_data(self):
#         # Create a dictionary with missing data
#         data = {
#             'nick_name': 'test_user',
#             'password': 'test_password',
#             'email': 'test_email@test.com',
#             'name': 'Test',
#             'account_number': '123456789',
#             'half_year': 2,
#             'role': 'admin',
#             'role_key': 'admin123'
#         }

#         # Call the from_dict() method with the dictionary
#         user = User.from_dict(data)

#         # Verify that the user object has been created correctly
#         self.assertEqual(user.nick_name, 'test_user')
#         self.assertEqual(user.email, 'test_email@test.com')
#         self.assertEqual(user.name, 'TEST')
#         self.assertEqual(user.last_name_fathers, '')
#         self.assertEqual(user.last_name_mothers, '')
#         self.assertEqual(user.account_number, '123456789')
#         self.assertEqual(user.careers, '')
#         self.assertEqual(user.half_year, 2)
#         self.assertEqual(user.role, 'admin')
#         self.assertEqual(user.role_key, 'admin123')


#     def test_from_dict_method_with_invalid_data(self):
#         # Create a dictionary with invalid data
#         data = {
#             'nick_name': 'test_user',
#             'password': 'test_password',
#             'email': 'test_email@test.com',
#             'name': 'Test',
#             'last_name_fathers': 'User',
#             'last_name_mothers': 'TestUser',
#             'account_number': '123456789',
#             'careers': 'Computer Science',
#             'half_year': 5,
#             'role': 'admin',
#             'role_key': 'admin123'
#         }

#         self.assertEqual(type(User.from_dict(data)), User)
