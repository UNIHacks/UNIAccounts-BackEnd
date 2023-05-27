import unittest
from api.v1.schemas.forgot_codes import ForgotCodesSchema, ForgotCodesPasswordSchema

class ForgotCodesSchemaTestCase(unittest.TestCase):
    def setUp(self):
        self.forgot_code_data = {
            'code': 'ABC123',
            'user_name': 'johndoe'
        }

    def test_valid_forgot_codes_schema(self):
        forgot_code = ForgotCodesSchema(**self.forgot_code_data)
        self.assertIsInstance(forgot_code, ForgotCodesSchema)
        self.assertEqual(forgot_code.code, self.forgot_code_data['code'])
        self.assertEqual(forgot_code.user_name, self.forgot_code_data['user_name'])

    def test_required_fields(self):
        required_fields = ['code', 'user_name']
        for field in required_fields:
            forgot_code_data = self.forgot_code_data.copy()
            del forgot_code_data[field]
            with self.assertRaises(ValueError):
                ForgotCodesSchema(**forgot_code_data)

    def test_extra_fields(self):
        forgot_code_data = self.forgot_code_data.copy()
        forgot_code_data['extra_field'] = 'Extra'
        forgot_code = ForgotCodesSchema(**forgot_code_data)
        self.assertEqual(forgot_code.code, self.forgot_code_data['code'])
        self.assertEqual(forgot_code.user_name, self.forgot_code_data['user_name'])

class ForgotCodesPasswordSchemaTestCase(unittest.TestCase):
    def setUp(self):
        self.forgot_password_data = {
            'code': 'ABC123',
            'user_name': 'johndoe',
            'password': 'newpassword'
        }

    def test_valid_forgot_codes_password_schema(self):
        forgot_password = ForgotCodesPasswordSchema(**self.forgot_password_data)
        self.assertIsInstance(forgot_password, ForgotCodesPasswordSchema)
        self.assertEqual(forgot_password.code, self.forgot_password_data['code'])
        self.assertEqual(forgot_password.user_name, self.forgot_password_data['user_name'])
        self.assertEqual(forgot_password.password, self.forgot_password_data['password'])

    def test_required_fields(self):
        required_fields = ['code', 'user_name', 'password']
        for field in required_fields:
            forgot_password_data = self.forgot_password_data.copy()
            del forgot_password_data[field]
            with self.assertRaises(ValueError):
                ForgotCodesPasswordSchema(**forgot_password_data)

    def test_extra_fields(self):
        forgot_password_data = self.forgot_password_data.copy()
        forgot_password_data['extra_field'] = 'Extra'
        forgot_password = ForgotCodesPasswordSchema(**forgot_password_data)
        self.assertEqual(forgot_password.code, self.forgot_password_data['code'])
        self.assertEqual(forgot_password.user_name, self.forgot_password_data['user_name'])
        self.assertEqual(forgot_password.password, self.forgot_password_data['password'])
