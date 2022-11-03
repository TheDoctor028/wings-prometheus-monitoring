import json.decoder
from prometheus_client import Enum, Info
import aiohttp


class Wings:
    """
     Represents a Wings server, and it's state, version, etc.

    ...

    Attributes
    ----------
    name: str
        The name of the Wings instance
    url: str
        The url of the Wings instance (with protocol & port) (e.g. "https://wings.example.com:8080")
    apiToken: str
        The (Bearer) token used to authenticate
        to the Wings API (Can be found in the Node's configuration at the panel)
    status: Enum
        The status of the Wings instance (online/offline).
        This can be used in prometheus queries to check if the instance is online or not.
    info: Info
        The info of the Wings instance (version, etc.)
    Methods
    -------
    updateStatus()
    :return: None
        Updates the status of the Wings instance. Making a http request to the Wings API.

    update(response)
    :return: None
    :param aiohttp.ClientResponse: response The response of the http request.
        If the response status is 200, the status will be set to online, otherwise offline.
    """

    name: str
    url: str
    apiToken: str
    status: Enum
    info: Info

    def __init__(self, name, url, api_token) -> None:
        self.name = name
        self.url = url
        self.apiToken = api_token
        self.status = Enum("wings_status_{0}".format(name), "Wings status", states=["online", "offline"])
        self.info = Info("wings_info_{0}".format(name), "Wings info")
        pass

    async def updateStatus(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.request("GET", "{0}/api/system".format(self.url),
                                       headers={"Authorization": "Bearer " + self.apiToken}) as response:
                # Update the status
                await self.update(response)

                # Update the info
                body = await response.content.readany()
                data = json.decoder.JSONDecoder().decode(body.decode("utf-8"))
                self.info.info(mapDictToStrStrDict(data))

    async def update(self, response) -> None:
        if response.status == 200:
            self.status.state("online")
        else:
            self.status.state("offline")


def mapDictToStrStrDict(d) -> dict:
    return {str(k): str(v) for k, v in d.items()}
