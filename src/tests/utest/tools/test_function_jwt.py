# import unittest
# from datetime import datetime, timedelta
# from src.tools.funtions_jwt import expire_date

# class TestExpireDate(unittest.TestCase):

#     def test_expire_date_day(self):
#         # Check if the date is correct with one day
#         expected_date = datetime.now() + timedelta(days=1)
#         self.assertEqual(expire_date(1).date(), expected_date.date())

#     def test_expire_date_week(self):
#         # Check if the date is correct with a week
#         expected_date = datetime.now() + timedelta(days=7)
#         self.assertEqual(expire_date(7).date(), expected_date.date())

#     def test_expire_date_month(self):
#         # Check if the date is correct with a month
#         expected_date = datetime.now() + timedelta(days=30)
#         self.assertEqual(expire_date(30).date(), expected_date.date())
