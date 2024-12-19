import httpx


class API:
    def __init__(self, host: str, port: int, tls: bool):
        self._base_url = f"http{'s' if tls else ''}://{host}:{port}/"
        self._base_url_v2 = f"{self._base_url}api/v2/"
        self._headers = dict()
        self._token = ""

    def token(self, value: str):
        self._token = value
        self._headers = {"Authorization": f"Bearer {self._token}"}

    token = property(lambda self: self._token, token)

    def authenticate(self, username: str, password: str):
        """
        response example: {"access_token":"...","token_type":"bearer"}
        :return:
        """
        r = httpx.post(f"{self._base_url}token", data={"username": username, "password": password})
        return r.json()["access_token"]

    def listener_templates(self):
        r = httpx.get(f"{self._base_url_v2}listener-templates", headers=self._headers)
        return r.json()
