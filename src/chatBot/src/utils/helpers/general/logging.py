import logging.config
import logging
import json
import os 


def setup_logging(default_path='src/utils/configs/log_config.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(
            level=default_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %H:%M:%S')

def return_format(message):
    
    return message
