import asyncio
from aiohttp import ClientSession
import json

base_url = "http://httpbin.org/"

async def count():
    for i in [1, 2, 3, 4, 5]:
        print(i)
        await asyncio.sleep(1)
        (i + 1)

async def get_delay(seconds):
    endpoint = f"/delay/{seconds}"

    print(f"Getting with {seconds} delay...")

    async   with    ClientSession() as  session:
        async with session.get(base_url + endpoint) as response:
            response = await response.read()
            data = json.loads(response)
            print(json.dumps(data, indent=4))

async def main():
    await asyncio.gather(get_delay(5),  count())

asyncio.run(main())

print("Finished GETting")
