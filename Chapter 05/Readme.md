# Web Honeypot Setup

This guide demonstrates setting up a web honeypot environment using XAMPP on Ubuntu 22.04 LTS to simulate attacker interactions for analysis.

## Installation

### Clone the GitHub repository:
```bash
git clone REPOSITORY_LINK
```
### Acquire XAMPP for Ubuntu Linux

1. Visit the [XAMPP download page](https://www.apachefriends.org/download.html).
2. Scroll down to the Linux section.
3. Choose version 8.2.12 / PHP 8.2.12 and download it.

### Launch Command Terminal

Use the shortcut `CTRL+ALT+T` or navigate to Applications in the Activities menu and search for Terminal.

### Alter permissions and execute the XAMPP installer

```bash
cd ~/Downloads 
```

```bash
chmod 755 xampp-linux-*-installer.run 
```

```bash
sudo ./xampp-linux-*-installer.run
```
### Configure Installation Wizard

Follow the installation wizard:

- Click "Next."
- Choose both components "XAMPP Core files" and "XAMPP Developer files."
- Click "Next."
- Select "Forward" and complete the installation.

## Setup
1. Start XAMPP:
```bash
sudo /opt/lampp/manager-linux-x64.run
```
    
2. Initiate Apache and MySQL servers:
    
    - Navigate to the "Manage Server" tab.
    - Click "Start" for both the Web server and Database.
3. Access phpMyAdmin:
    
    - Visit [http://localhost/phpmyadmin](http://localhost/phpmyadmin).
    - Create a database titled "honeypot."
4. Import the honeypot.sql file:
    
    - Click "Import" and select the honeypot.sql file.
5. Replace contents in `/opt/lampp/htdocs` folder with the cloned “htdocs” folder from the repository.
    
6. Make files executable:
```bash
sudo chmod +x /opt/lampp/htdocs/index.php /opt/lampp/htdocs/dbconnection.php
```
    

## Attack Scenarios

### Attack on Search Service Functionality

1. Access the URL: [http://192.168.1.8/index.php](http://192.168.1.8/index.php).
2. In the "About Us" section, execute a directory traversal attack.
3. Payload: `../../../../../../etc/passwd`.

### Attack on Subscribe Functionality

1. In the "Subscribe" functionality, attempt a SQL Injection attack.
2. Payload: `' OR 1=1 -- //`.
