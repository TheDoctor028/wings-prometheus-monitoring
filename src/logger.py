import logging
import sys

root = logging.getLogger("root")
envs = logging.getLogger("envs")


def initRootLogger():
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    pass


def initEnvsLogger():
    envs.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    envs.addHandler(handler)
    pass


def init():
    initRootLogger()
    initEnvsLogger()
    pass
