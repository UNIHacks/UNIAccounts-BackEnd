# import unittest

# from src.tools.functions_dict import get_from_dict

# class TestFunctionDict(unittest.TestCase):
#     def test_get_from_dict_key_exists(self):
#         dictionary = {'a': 1, 'b': 2, 'c': 3}
#         key = 'b'
#         result = get_from_dict(dictionary, key)
#         assert result == 2

#     def test_get_from_dict_key_does_not_exist(self):
#         dictionary = {'a': 1, 'b': 2, 'c': 3}
#         key = 'd'
#         default_value = 0
#         result = get_from_dict(dictionary, key, default_value)
#         assert result == default_value

#     def test_get_from_dict_empty_dictionary(self):
#         dictionary = {}
#         key = 'a'
#         default_value = None
#         result = get_from_dict(dictionary, key, default_value)
#         assert result == default_value
