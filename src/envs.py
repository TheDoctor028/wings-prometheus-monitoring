import os
import dotenv

PORT = os.environ.get("PORT")
CHECK_INTERVAL_S = os.environ.get("CHECK_INTERVAL_S")


def init():
    global PORT
    global CHECK_INTERVAL_S

    dotenv.load_dotenv()
    print("DotEnv loaded!")
    PORT = os.environ.get("PORT")
    CHECK_INTERVAL_S = os.environ.get("CHECK_INTERVAL_S")
    print("Envs updated!")
    pass
