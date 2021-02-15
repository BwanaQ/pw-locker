import pyperclip
import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    def tearDown(self):
        Credential.credential_list = []

    def setUp(self):
        self.new_credential = Credential(
            "Facebook", "https://www.facebook.com/login/web/", "BwanaQ", "pa55w0rd")

    def test_init(self):
        self.assertEqual(self.new_credential.title, "Facebook")
        self.assertEqual(self.new_credential.url,
                         "https://www.facebook.com/login/web/")
        self.assertEqual(self.new_credential.user_name, "BwanaQ")
        self.assertEqual(self.new_credential.password, "pa55w0rd")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Gmail", "https://gmail.com/signup/", "thunjaworks", "1@usercom")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Gmail", "https://gmail.com/signup/", "thunjaworks", "1@usercom")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_title(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Gmail", "https://gmail.com/signup/", "thunjaworks", "1@usercom")
        test_credential.save_credential()

        found_credential = Credential.find_by_title("Gmail")

        self.assertEqual(found_credential.title, test_credential.title)

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Gmail", "https://gmail.com/signup/", "thunjaworks", "1@usercom")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        self.assertEqual(Credential.display_credentials(),
                         Credential.credential_list)

    def test_copy_email(self):
        self.new_credential.save_credential()
        Credential.copy_password("Facebook")
        self.assertEqual(self.new_credential.password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
