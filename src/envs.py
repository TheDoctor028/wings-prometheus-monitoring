import os
import dotenv
import logger

ENVS = {
    "PORT": "9001",
    "CHECK_INTERVAL_S": "5",
    "WINGS_COUNT": "99"
}

WINGS_COUNT = 0


def init():
    global ENVS
    dotenv.load_dotenv()
    logger.envs.info("DotEnv loaded!")
    loadWingsInstances()
    for env in ENVS.keys():
        ENVS[env] = os.environ.get(env) if os.environ.get(env) else ENVS[env]
        logger.envs.info("Env {0} set to {1}".format(env, ENVS[env]))
    logger.envs.info("Envs updated!")
    pass


def loadWingsInstances():
    global ENVS
    global WINGS_COUNT
    logger.envs.info("Loading Wings instances...")

    for i in range(1, int(ENVS["WINGS_COUNT"])):
        url = os.environ.get(WINGS_URL(i))
        api_token = os.environ.get(WINGS_API_TOKEN(i))

        if url and api_token:
            ENVS[WINGS_URL(i)] = url
            ENVS[WINGS_API_TOKEN(i)] = api_token
            logger.envs.info("Wings instance {0} ({1}) loaded!".format(i, url))
        else:
            WINGS_COUNT = i - 1
            ENVS["WINGS_COUNT"] = str(WINGS_COUNT)
            break

    logger.envs.info("{0} Wings instances loaded!".format(WINGS_COUNT))
    pass


def WINGS_URL(i):
    return "WINGS_{0}_URL".format(i)


def WINGS_API_TOKEN(i):
    return "WINGS_{0}_TOKEN".format(i)


def GET_WINGS_COUNT():
    return int(ENVS["WINGS_COUNT"])
