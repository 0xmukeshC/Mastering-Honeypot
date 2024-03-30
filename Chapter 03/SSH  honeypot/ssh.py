import paramiko
import socket
import time

def handle_connection(client):
    # Get current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Incoming connection at {timestamp} from: {addr[0]}:{addr[1]}")

    client_handler = paramiko.Transport(client)
    try:
        client_handler.set_gss_host(socket.getfqdn(""))
        client_handler.load_server_moduli()
        client_handler.add_server_key(host_key)
        client_handler.start_server(server=server)

        # Accept the SSH connection
        channel = client_handler.accept(20)

        if channel is None:
            print("SSH handshake failed")
            return

        # Capture login attempts
        username = channel.recv(1024).decode().strip()
        password = channel.recv(1024).decode().strip()

        # Log the login attempt with timestamp
        log_attempt(timestamp, username, password)

        # Reset the connection upon request
        if should_reset_connection(username, password):
            print("Connection reset requested. Resetting connection...")
            return

        # Reject the login attempt to mimic authentication failure
        channel.send("Authentication failed.\r\n")
        client_handler.close()

    except paramiko.SSHException as e:
        print(f"SSH negotiation failed: {e}")
    except EOFError:
        print("Connection closed by client.")
    finally:
        client.close()

def should_reset_connection(username, password):
    # Add your condition to determine when to reset the connection
    # For example, reset connection if a specific username/password is attempted
    return username == "reset_user" and password == "reset_password"

def log_attempt(timestamp, username, password):
    # Print the log on the console/terminal
    print(f"{timestamp} - Login attempt - Username: {username}, Password: {password}")

# Generate an RSA key for the honeypot (replace with your own key if needed)
host_key = paramiko.RSAKey.generate(2048)

# Create an SSH server
server = "SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8"

# Listen for incoming SSH connections
ssh_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ssh_socket.bind(("0.0.0.0", 22))
ssh_socket.listen(5)

print("SSH honeypot listening on port 22...")

while True:
    client, addr = ssh_socket.accept()
    handle_connection(client)

