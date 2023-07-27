import requests
import json


# REST API Query
class PokeAPI:
    server_url = "http://localhost:9080/api/v2"

    def __init__(self):
        pass

    def get_pokemon(self, name_or_id):
        url = f"{self.server_url}/pokemon/{name_or_id}"
        response = requests.get(url)  # TODO: headers?
        response.raise_for_status()
        return response.json()


api = PokeAPI()

r = api.get_pokemon("bulbasaur")
print(json.dumps(r, indent=2))
