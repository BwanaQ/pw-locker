from user import User
import pyperclip
import unittest


class TestUser(unittest.TestCase):
    def tearDown(self):
        User.user_list = []

    def setUp(self):
        self.new_user = User("Tom", "Hunja", "BwanaQ", "str0ngpwd")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Tom")
        self.assertEqual(self.new_user.last_name, "Hunja")
        self.assertEqual(self.new_user.user_name, "BwanaQ")
        self.assertEqual(self.new_user.password, "str0ngpwd")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
