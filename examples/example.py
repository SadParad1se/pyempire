from pyempire.client import EmpireClient


client = EmpireClient("localhost", 1337, False, "empireadmin", "password123")
client.login()
client.api.listener_templates()
