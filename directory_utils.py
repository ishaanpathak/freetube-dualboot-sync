import os
import subprocess
import logging

def check_directory(path, is_backup=False):
    """Check if a directory exists and is writable."""
    if not os.path.exists(path):
        send_notification("Directory Not Found", f"The directory {path} does not exist.")
        logging.error(f"Directory {path} does not exist.")
        return False
    if not os.access(path, os.W_OK):
        send_notification("Directory Not Writable", f"The directory {path} is not writable.")
        logging.error(f"Directory {path} is not writable.")
        return False
    return True

def send_notification(title, message):
    """Send a system notification."""
    if os.name == 'nt':  # Windows
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=10)
    else:  # Linux
        subprocess.run(['notify-send', title, message])
