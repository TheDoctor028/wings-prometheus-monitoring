import os
import dotenv
import logging

ENVS = {
    "PORT": "9001",
    "CHECK_INTERVAL_S": "5",
}


def init():
    global ENVS

    dotenv.load_dotenv()
    logging.info("DotEnv loaded!")
    for env in ENVS.keys():
        ENVS[env] = os.environ.get(env) if os.environ.get(env) else ENVS[env]
        logging.info("Env {0} set to {1}".format(env, ENVS[env]))
    logging.info("Envs updated!")
    pass
