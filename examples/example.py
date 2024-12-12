from pyempire.client import Client


client = Client("localhost", 1337, False, "empireadmin", "password123")
client.authenticate()
client.listener_templates()