import pyperclip


class Credential:
    """
    a class to ogenerate new credentials for  users
    """
    credential_list = []

    def __init__(self, title, url, user_name, password):
        self.title = title
        self.url = url
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_title(cls, title):
        for credential in cls.credential_list:
            if credential.title == title:
                return credential

    @classmethod
    def credential_exist(cls, title):
        for credential in cls.credential_list:
            if credential.title == title:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credential_list

    @classmethod
    def copy_password(cls, title):
        credential_found = Credential.find_by_title(title)
        pyperclip.copy(credential_found.password)
