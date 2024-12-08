import os
import shutil
import logging
from file_utils import get_file_hash, backup_file, manage_backups
from directory_utils import check_directory

def sync_files(dir1, dir2, filenames, backup_dir):
    """
    Synchronizes the files in two directories based on content hashes.
    """
    for filename in filenames:
        file1 = os.path.join(dir1, filename)
        file2 = os.path.join(dir2, filename)

        if not check_directory(dir1) or not check_directory(dir2) or not check_directory(backup_dir, is_backup=True):
            return  # Exit if directories are not valid

        if not os.path.exists(file1) or not os.path.exists(file2):
            logging.error(f"Error: {filename} is missing in one of the directories.")
            continue

        hash1 = get_file_hash(file1)
        hash2 = get_file_hash(file2)

        if hash1 != hash2:
            if os.path.getmtime(file1) > os.path.getmtime(file2):
                backup_file(file2, backup_dir)
                shutil.copy2(file1, file2)
                logging.info(f"Updated {filename} from {dir1} to {dir2}.")
            else:
                backup_file(file1, backup_dir)
                shutil.copy2(file2, file1)
                logging.info(f"Updated {filename} from {dir2} to {dir1}.")
            
            manage_backups(filename, backup_dir)
        else:
            logging.info(f"{filename} is already up to date in both directories.")
