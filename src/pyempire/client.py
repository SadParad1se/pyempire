from pyempire.api import API


class EmpireClient:
    def __init__(self, host: str, port: int, tls: bool, username: str, password: str, log_in: bool = True):
        self.api = API(host, port, tls)
        self.username = username
        self.password = password

        if log_in:
            self.login()

    def login(self):
        self.api.token = self.api.authenticate(self.username, self.password)
