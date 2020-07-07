import os

import yaml
from box import Box
from dotenv import load_dotenv


def box_yaml(file: str) -> Box:
    """
    Load yaml file and Box it.

    Args:
        file: path to yaml file.

    Returns:
        boxed yaml file.
    """
    with open(file, "r") as yml_file:
        cfg = Box(
            yaml.safe_load(yml_file),
            default_box=True,
            default_box_attr=None
        )
    return cfg


# Adding .env variables to environment
load_dotenv(dotenv_path=".env")

# Read .env variables.
CONFIG_FILE = os.getenv("CONFIG_FILE")
LOG_FILE = os.getenv("LOG_FILE")

# Build config object.
full_config = box_yaml(CONFIG_FILE)
config = Box({
    **full_config,
    }, default_box=True, default_box_attr=None)
config.config_file = CONFIG_FILE
config.log_file = LOG_FILE
