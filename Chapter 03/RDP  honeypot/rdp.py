import socket
import logging
import datetime  # Added for timestamp

def rdp_honeypot():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # RDP port (default: 3389)
    rdp_port = 3389

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to all available interfaces and the RDP port
        server_socket.bind(('0.0.0.0', rdp_port))
        logging.info("RDP honeypot is listening on port %d", rdp_port)

        # Listen for incoming connections
        server_socket.listen(1)

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()

            # Log the connection attempt with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info("[%s] Connection attempt from: %s", timestamp, client_address[0])

            # Close the connection
            client_socket.close()

    except KeyboardInterrupt:
        logging.info("Exiting RDP honeypot.")
    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    rdp_honeypot()

