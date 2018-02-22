from os import path

CURRENT_PATH = path.dirname(path.abspath(__file__))


def get_path(name):
    return path.join(CURRENT_PATH, name)
