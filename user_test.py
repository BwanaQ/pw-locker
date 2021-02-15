from user import User
import pyperclip
import unittest


class TestUser(unittest.TestCase):
    def tearDown(self):
        User.user_list = []
