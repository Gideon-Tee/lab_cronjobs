import os
import subprocess

service_name = "clear_temp_folder"
service_file_path = f"/etc/systemd/system/{service_name}.service"
script_path = "/home/dansarpong/cron_jobs/manage_service.py"
service_config = f"""
[Unit]
Description=Clear Temp Folder Lab Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {script_path}
Restart=always

[Install]
WantedBy=multi-user.target
"""


def create_service():
    '''
    Write the service config to systemd, enable, and start service
    '''
    try:
        # Write service configuration
        with open(service_file_path, 'w') as service_file:
            service_file.write(service_config)
        print(f"Service file created at {service_file_path}")

        # Reload systemd daemon
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
        print("Systemd daemon reloaded.")

        # Enable the service
        subprocess.run(["sudo", "systemctl", "enable", service_name], check=True)
        print(f"Service {service_name} enabled.")

        # Start the service
        subprocess.run(["sudo", "systemctl", "start", service_name], check=True)
        print(f"Service {service_name} started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' failed with exit code {e.returncode}.")
        print(f"Output: {e.output}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_service()
