import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sync import sync_files

class FileChangeHandler(FileSystemEventHandler):
    """Handler to react to file changes in directories."""
    def __init__(self, dir1, dir2, filenames, backup_dir):
        self.dir1 = dir1
        self.dir2 = dir2
        self.filenames = filenames
        self.backup_dir = backup_dir

    def on_modified(self, event):
        """Triggered when a file is modified."""
        if event.src_path.endswith(tuple(self.filenames)):
            logging.info(f"File changed: {event.src_path}")
            sync_files(self.dir1, self.dir2, self.filenames, self.backup_dir)

def monitor_changes_with_watchdog(dir1, dir2, filenames, backup_dir):
    """Continuously monitors the directories for changes using Watchdog."""
    event_handler = FileChangeHandler(dir1, dir2, filenames, backup_dir)
    observer = Observer()
    
    observer.schedule(event_handler, dir1, recursive=False)
    observer.schedule(event_handler, dir2, recursive=False)

    observer.start()
    logging.info("Monitoring started.")
    
    try:
        while True:
            time.sleep(10)  # Sleep to prevent busy waiting; watchdog handles the events.
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Monitoring stopped.")
    observer.join()
