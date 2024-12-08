import logging
import toml
from config import check_config
from sync import sync_files
from monitor import monitor_changes_with_watchdog

if __name__ == "__main__":
    # Load configuration
    check_config()
    with open('~/.config/ft-sync/config.toml', "r") as config_file:
        config = toml.load(config_file)
    
    filenames = ['history.db', 'settings.db', 'profiles.db', 'playlists.db']
    linux_dir = config['sync']['linux_dir']
    windows_dir = config['sync']['windows_dir']
    backup_dir = config['sync']['backup_dir']
    
    sync_files(linux_dir, windows_dir, filenames, backup_dir)
    
    monitor_changes_with_watchdog(linux_dir, windows_dir, filenames, backup_dir)
