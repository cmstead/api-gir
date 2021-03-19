import os
from shutil import copy2

config_name = "api-gir-config.json"

def get_file_path():
    return os.path.dirname(os.path.realpath(__file__))


def copy_base_config():
    cwd = os.getcwd()
    file_path = get_file_path()

    source_config_path = os.path.realpath(
        os.path.join(file_path, config_name))
    destination_config_path = os.path.realpath(
        os.path.join(cwd, config_name))

    copy2(source_config_path, destination_config_path)
