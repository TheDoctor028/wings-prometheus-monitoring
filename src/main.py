from prometheus_client import start_http_server, Enum
from envs import ENVS, WINGS_COUNT, WINGS_URL, WINGS_API_TOKEN, GET_WINGS_COUNT
import time
import asyncio
import envs
import logging
import logger
from models.wings import Wings

wings = []


async def updateStatuses():
    for wing in wings:
        await asyncio.create_task(wing.updateStatus(), name="wings_status_{0}_update".format(wing.name))
    pass


def loadWings():
    return [Wings("wings_{0}".format(i), ENVS[WINGS_URL(i)], ENVS[WINGS_API_TOKEN(i)]) for i in range(1, GET_WINGS_COUNT())]


if __name__ == '__main__':
    envs.init()
    logger.init()
    wings = loadWings()
    logging.info("Starting...")
    start_http_server(int(ENVS["PORT"]))
    logging.info("Metrics server started on {0}...".format(ENVS["PORT"]))
    logging.info("Starting update loop...")
    while True:
        logging.log(logging.INFO, "Updating statuses...")
        asyncio.run(updateStatuses())
        logging.log(logging.INFO, "Statuses updated!")
        time.sleep(int(ENVS["CHECK_INTERVAL_S"]))
