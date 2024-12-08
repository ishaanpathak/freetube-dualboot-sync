import os
import shutil
import hashlib
from datetime import datetime
import logging

# Set up logging to record actions in a log file
logging.basicConfig(filename='sync_files.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_file_hash(file_path):
    """Returns the SHA256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
    return hash_sha256.hexdigest()

def backup_file(file_path, backup_dir):
    """Creates a backup of the file in the backup directory with a timestamp."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"{os.path.basename(file_path)}_{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    shutil.copy2(file_path, backup_path)  # Backup the file
    logging.info(f"Backup created for {file_path} at {backup_path}")
    return backup_path

def manage_backups(file_name, backup_dir, max_backups=5):
    """Keeps track of the last 'max_backups' backups and deletes older ones."""
    backups = [f for f in os.listdir(backup_dir) if f.startswith(file_name)]
    backups.sort(reverse=True)  # Sort backups by timestamp
    
    # Remove backups if we have more than the max allowed
    if len(backups) > max_backups:
        for old_backup in backups[max_backups:]:
            os.remove(os.path.join(backup_dir, old_backup))
            logging.info(f"Old backup {old_backup} deleted.")
