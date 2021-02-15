class Credential:
    """
    a class to ogenerate new credentials for  users
    """
    credential_array = []

    def __init__(self, url, password):
        self.url = url
        self.password = password
