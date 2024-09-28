# Octopus Honeypot Setup Guide  
## Installation & Setup 

1. Install Git and clone Octopus repository: 
```bash
sudo apt-get install git && git clone https://github.com/qeeqbox/octopus.git && cd octopus && chmod +x setup.sh
```

2. Run setup script with desired services:
```bash
sudo ./setup.sh "ssh,rdp,ldap,ftp,samba,mongodb,redis,vnc"
```

## Network Configuration

View open ports:
```bash
netstat -a
```

## Intrusion Detection System (IDS) Setup

1. Install Snort for network traffic analysis and threat detection:
```bash
sudo apt-get update && sudo apt-get -y install snort
```

2. Add custom SNORT rules in `/etc/snort/rules/local.rules`:
```
alert tcp any any -> $HOME_NET 21 (msg:"FTP Authentication Attempt"; sid:100001; rev:1) 
alert tcp any any -> $HOME_NET 139 (msg:"SMB over netbios Authentication Attempt"; sid:100002; rev:1) 
alert tcp any any -> $HOME_NET 389 (msg:"ldap Authentication Attempt"; sid:100003; rev:1) 
alert tcp any any -> $HOME_NET 445 (msg:"SMB Authentication Attempt"; sid:100004; rev:1) 
alert tcp any any -> $HOME_NET 3389 (msg:"RDP Authentication Attempt"; sid:100005; rev:1)
```

3. Start Snort for SIEM monitoring:
```bash
sudo snort -q -l /var/log/snort -l enp0s3 -A console -c /etc/snort/snort.conf
```