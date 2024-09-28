# Manual Honeypot Setup: Server Honeypot

This guide outlines the manual setup of an Server honeypot on Ubuntu, allowing the simulation and detection of Server connection attempts.

## Installation

1. Clone the GitHub repository:
```bash
git clone REPOSITORY_LINK
```
## Usage

1. Make the Python3 script executable:
```bash
chmod +x honeypot.py
```

3. Run the provided Python script to set up the Server honeypot:
```bash
sudo python3 honeypot.py
```

3. Monitor the honeypot for incoming Server connections:
```bash
server honeypot listening on port 8080...
```

4. If an attacker attempts connection, their IP address will be logged:
```bash
== NEW CONNECTION FROM ('10.0.2.4', 58080) AT 2023-10-20 11:34:54.436230 ==
```

