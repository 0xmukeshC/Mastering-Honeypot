
# Manual Honeypot Setup: RDP Honeypot

This guide outlines the manual setup of an RDP honeypot on Ubuntu, allowing the simulation and detection of RDP login attempts.
## Installation 
1. Clone the GitHub repository:
```bash
git clone REPOSITORY_LINK
```
## Usage

1. Make the Python3 script executable:
```bash
chmod +x rdp.py
```

2. Run the provided Python script to set up the RDP honeypot:
```bash
sudo python3 rdp.py
```

3. Monitor the honeypot for incoming RDP connections:
```bash
INFO:root:RDP honeypot is listening on port 3389
```

4. If an attacker attempts authentication, their IP address will be logged:
```bash
INFO:root:[2023-11-23 15:33:56] Connection attempt from: 10.0.2.4
INFO:root:[2023-11-23 15:33:56] Connection attempt from: 10.0.2.4
```