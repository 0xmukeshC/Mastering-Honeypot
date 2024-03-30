
# Manual Honeypot Setup: FTP Honeypot

This guide outlines the manual setup of an FTP honeypot on Ubuntu, allowing the simulation and detection of FTP login attempts.

## Installation 
1. Install pyftpdlib library for FTP server simulation:
```bash
sudo pip install pyftpdlib
```
2. Clone the GitHub repository:
```bash
git clone REPOSITORY_LINK
```
## Usage

1. Make the Python3 script executable:
```bash
chmod +x ftp.py
```

2. Run the provided Python script to set up the FTP honeypot:
```bash
sudo python3 ftp.py
```

3. Monitor the honeypot for incoming FTP connections:
```bash
FTP honeypot is running...  
[I 2023-10-13 14:42:20] concurrency model: multi-thread
[I 2023-10-13 14:42:20] masquerade (NAT) address: None 
[I 2023-10-13 14:42:20] passive ports: None
```

4. If an attacker attempts authentication, their IP address will be logged:
```bash
[I 2023-10-13 14:45:14] 10.0.2.4:48870-[] FTP session opened (connect)
[I 2023-10-13 14:45:20] 10.0.2.4:48870-[anonymous] USER 'anonymous' logged in.
```