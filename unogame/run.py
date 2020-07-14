import logging
import click

from unogame.config import config, load_logging
from unogame.utils import func_def

logger = logging.getLogger(__name__)


@click.group()
def cli():
    load_logging()
    logger.info(f"Loaded general config from {config.config_file}")
    logger.info(f"Loaded logging config from {config.log_file}")


@cli.command("start")
@click.argument("instance")
def start_instance(instance):
    # Call start method of the class given in config
    inst_config = config[instance]
    logger.info(f"Starting {instance} instance.")
    logger.info(f"Using {inst_config.module}.{inst_config.name}")
    instance = func_def(**inst_config)
    instance().start()
