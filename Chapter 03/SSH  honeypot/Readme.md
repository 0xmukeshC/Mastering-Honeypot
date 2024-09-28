# Manual Honeypot Setup: SSH Honeypot

This guide outlines the manual setup of an SSH honeypot on Ubuntu, allowing the simulation and detection of SSH login attempts.

## Installation

1. Install Paramiko library for SSH server simulation:
```bash
sudo apt-get update && sudo apt-get install python3-pip -y && sudo pip install paramiko
```

2. Clone the GitHub repository:
```bash
git clone REPOSITORY_LINK
```
## Usage

1. Make the Python3 script executable:
```bash
chmod +x ssh.py
```

3. Run the provided Python script to set up the SSH honeypot:
```bash
sudo python3 ssh.py
```

3. Monitor the honeypot for incoming SSH connections:
```bash
SSH honeypot listening on port 22...
```

4. If an attacker attempts authentication, their IP address will be logged:
```bash
Incoming connection at 2023-11-23 14:46:20 from: 10.0.2.4:43454 Connection closed by client.
```

