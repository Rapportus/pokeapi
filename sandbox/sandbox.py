import requests
import json
import pokebase as pb
import asyncio
import aiopoke

SANDBOX_ADDRESS = "localhost:9080"


class PokeAPI:
    server_url = f"http://{SANDBOX_ADDRESS}/api/v2"

    def __init__(self):
        pass

    def get_pokemon(self, name_or_id):
        url = f"{self.server_url}/pokemon/{name_or_id}"
        response = requests.get(url)  # TODO: headers?
        response.raise_for_status()
        return response.json()


def manual_rest_query():
    """
    Manually query the REST API locally
    """
    api = PokeAPI()
    r = api.get_pokemon("bulbasaur")
    print(json.dumps(r, indent=2))


def pokebase_query():
    """
    Query using pokebase
    Note this uses http://pokeapi.co/api/v2
    """

    bulb = pb.APIResource("pokemon", "bulbasaur")
    print(bulb)


async def aio_pokeapi_query():
    """
    Query using asyncio
    Note this uses https://pokeapi.co/api/v2
    """
    client = aiopoke.AiopokeClient()
    bulb = await client.get_pokemon("bulbasaur")
    print(bulb.name)
    ability = await bulb.abilities[0].ability.fetch()
    print(ability.name)
    await client.close()


def aio_main():
    asyncio.run(aio_pokeapi_query())


def main():
    # manual_rest_query()
    pokebase_query()


if __name__ == "__main__":
    # main()
    aio_main()
