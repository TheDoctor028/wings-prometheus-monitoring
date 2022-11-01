from prometheus_client import start_http_server, Enum
import time
import http.client
import dotenv
import os
import asyncio
import aiohttp

WINGS_STATUS = Enum("wings_status_1", "Wings status", states=["online", "offline"])


async def updateStatuses():
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://{0}/api/system".format(os.environ.get("WINGS_URL")),
                headers={"Authorization": "Bearer " + os.environ.get("WINGS_TOKEN")}) as response:
            if response.status == 200:
                WINGS_STATUS.state("online")
            else:
                WINGS_STATUS.state("offline")
    pass

if __name__ == '__main__':
    dotenv.load_dotenv()
    print()
    print("Starting server...")
    start_http_server(int(os.environ.get("PORT")))
    print("Server started!")
    while True:
        asyncio.run(updateStatuses())
        time.sleep(int(os.environ.get("CHECK_INTERVAL_MS")))
