# Keycloak Systemd Service Configuration

This README file provides instructions on how to configure Keycloak to run automatically at system startup or restart on failure using systemd on Ubuntu.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Keycloak server installed and configured.
- A user with sudo privileges.

## Step 1: Create the Systemd Service File

1. Open a terminal window and navigate to the `/etc/systemd/system` directory.
2. Create a new service file named `keycloak.service` using your preferred text editor (e.g., `sudo nano keycloak.service`).
3. Open the file `keycloak.service`
4. Copy and paste the following configuration into the `keycloak.service` file.


> [!NOTE]
IP Address and other settings should be change according to your setup and needs. <br>
For more details about the keycloak server setup kindly check the official website: https://www.keycloak.org/guides#server
