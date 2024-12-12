import httpx


class Client:
    def __init__(self, host: str, port: int, tls: bool, username: str, password: str):
        self.host = host
        self.port = port
        self.tls = tls
        self.username = username
        self.password = password
        self._base_url = f"http{'s' if tls else ''}://{host}:{port}/"
        self._base_url_v2 = f"{self._base_url}api/v2/"
        self._access_token: str | None = None

    def authenticate(self):
        """
        response example: {"access_token":"...","token_type":"bearer"}
        :return:
        """
        r = httpx.post(f"{self._base_url}token", data={"username": self.username, "password": self.password})
        self._access_token = r.json()["access_token"]

    def listener_templates(self):
        r = httpx.get(f"{self._base_url_v2}listener-templates", headers={"Authorization": f"Bearer {self._access_token}"})
        print(r.text)
