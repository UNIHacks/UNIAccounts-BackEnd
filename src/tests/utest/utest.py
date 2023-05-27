import os
import sys


BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__)))) + '/..'

LIST_PATH_TO_ADD = [BASE_DIR]
sys.path.extend(LIST_PATH_TO_ADD)

import unittest

from tests.utest.models.test_user import TestUser

from tests.utest.api.v1.schemas.test_users import UserSchemaTestCase

from tests.utest.api.v1.schemas.test_forgot_codes import ForgotCodesPasswordSchemaTestCase, ForgotCodesSchemaTestCase


if __name__ == '__main__':
    unittest.main(verbosity=2)
