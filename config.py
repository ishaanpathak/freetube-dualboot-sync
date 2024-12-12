import os
import toml
import logging
from directory_utils import check_directory

DEFAULT_CONFIG_PATH = os.path.expanduser("~/.config/ft-sync/config.toml")

def check_config():
    if not os.path.exists(DEFAULT_CONFIG_PATH):
        config = {
            'sync': {
                'linux_dir': input("Enter the path to the Linux directory: "),
                'windows_dir': input("Enter the path to the Windows directory: "),
                'backup_dir': input("Enter the path to the backup directory: ")
            }
        }
        os.makedirs(os.path.dirname(DEFAULT_CONFIG_PATH), exist_ok=True)
        with open(DEFAULT_CONFIG_PATH, "w") as config_file:
            toml.dump(config, config_file)
        logging.info("Configuration file created.")
    else:
        with open(DEFAULT_CONFIG_PATH, "r") as config_file:
            config = toml.load(config_file)
        
        if not check_directory(config['sync']['linux_dir']) or not check_directory(config['sync']['windows_dir']) or not check_directory(config['sync']['backup_dir']):
            raise ValueError("Invalid paths in the configuration file.")
        else:
            logging.info("Configuration file exists and paths are valid.")
