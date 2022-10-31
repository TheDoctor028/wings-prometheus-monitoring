from prometheus_client import start_http_server, Enum
import time
import http.client
import dotenv
import os

# Create a metric to track time spent and requests made.
WINGS_STATUS = Enum("wings_status_1", "Wings status", states=["online", "offline"])


def getStatus() -> int:
    # TODO move to env and create config
    connection = http.client.HTTPSConnection("fqnd.wings.replace", port=8080)
    connection.request("GET", "/api/system", headers={"Authorization": "Bearer " + os.getenv("WINGS_TOKEN")})
    res_status = connection.getresponse().getcode()
    return res_status


def updateStatus():
    if getStatus() == 200:
        WINGS_STATUS.state("online")
    else:
        WINGS_STATUS.state("offline")


if __name__ == '__main__':
    dotenv.load_dotenv()
    print()
    print("Starting server...")
    start_http_server(int(os.environ.get("PORT")))
    print("Server started!")
    while True:
        updateStatus()
        time.sleep(100)
