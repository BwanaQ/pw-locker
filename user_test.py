from user import User
import pyperclip
import unittest


class TestUser(unittest.TestCase):
    def tearDown(self):
        """
        resets the user_list array
        """
        User.user_list = []

    def setUp(self):
        """
        creates a test User
        """

        self.new_user = User("Tom", "Hunja", "BwanaQ", "str0ngpwd")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Tom")
        self.assertEqual(self.new_user.last_name, "Hunja")
        self.assertEqual(self.new_user.user_name, "BwanaQ")
        self.assertEqual(self.new_user.password, "str0ngpwd")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Test", "user", "test", "dr0w55ap")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user = User("Test", "user", "test", "dr0w55ap")
        test_user.save_user()
        user_exists = User.user_exist("test")
        self.assertTrue(user_exists)

    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "test", "dr0w55ap")
        test_user.save_user()
        test_user.check_user("test", "dr0w55ap")


if __name__ == '__main__':
    unittest.main()
