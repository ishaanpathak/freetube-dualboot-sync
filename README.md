# freetube-dualboot-sync

`freetube-dualboot-sync` is a file synchronization tool designed to sync files between a Linux and Windows machine, specifically for FreeTube data. It compares file contents using hashing, creates backups before updating files, and automatically deletes older backups based on a configurable limit. The script also monitors specified directories for changes and syncs them in real-time.

## Features:
- Synchronizes specific files between Linux and Windows directories.
- Creates backups of files before updating them.
- Automatically deletes older backups beyond a configurable limit.
- Monitors directories for changes and syncs them in real-time.

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/freetube-dualboot-sync.git
   cd freetube-dualboot-sync
   ```

2. Install dependencies:
   ```bash
   pip install watchdog toml
   ```

## Usage:

1. Configure your sync directories by editing the `~/.config/ft-sync/config.toml` file. If the file doesn't exist, the script will prompt you to input the necessary paths.

2. Run the script:
   ```bash
   python main.py
   ```

The script will start syncing the specified files and monitor the directories for changes.

## Running the Script at Boot using systemd:

To run the script at boot as a systemd service, follow these steps:

1. **Create a systemd user unit file**:
   
   Create a file called `freetube-dualboot-sync.service` in the `~/.config/systemd/user/` directory. If the directory does not exist, create it:

   ```bash
   mkdir -p ~/.config/systemd/user
   ```

   Then create and edit the `freetube-dualboot-sync.service` file:
   
   ```bash
   nano ~/.config/systemd/user/freetube-dualboot-sync.service
   ```

2. **Add the following content to the service file**:

   ```ini
   [Unit]
   Description=FreeTube Dualboot Sync
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/freetube-dualboot-sync/main.py
   WorkingDirectory=/path/to/your/freetube-dualboot-sync
   User=yourusername
   Group=yourusername
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=default.target
   ```

   Replace `/path/to/your/freetube-dualboot-sync/` with the actual path where your script is located and `yourusername` with your system's username.

3. **Reload systemd and enable the service**:

   After saving the file, reload systemd to recognize the new service:

   ```bash
   systemctl --user daemon-reload
   ```

   Enable the service to start at boot:

   ```bash
   systemctl --user enable freetube-dualboot-sync.service
   ```

4. **Start the service**:

   Now, you can start the service immediately:

   ```bash
   systemctl --user start freetube-dualboot-sync.service
   ```

   The script will run at boot automatically from now on.

## NOTE: I have used LLM to refactor this script

- This README has been created by an LLM based on the context of the script.
- Also, the script was refactored and split into parts using LLM too.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
