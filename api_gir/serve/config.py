import json
import os

def get_config():
    config_name = "api-gir-config.json"
    cwd = os.getcwd()
    
    config_path = os.path.realpath(os.path.join(cwd, config_name))

    with open(config_path, "r") as config:
        return json.loads(config.read())