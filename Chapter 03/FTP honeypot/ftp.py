from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

def main():
    # Create a dummy authorizer for managing FTP users and permissions
    authorizer = DummyAuthorizer()

    # Add a read-only anonymous user
    authorizer.add_anonymous("/tmp")

    # Define the FTP handler and pass the authorizer to it
    handler = FTPHandler
    handler.authorizer = authorizer

    # Bind the FTP server to a specific IP and port
    server = ThreadedFTPServer(("0.0.0.0", 21), handler)

    # Set the maximum number of threads to handle incoming connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # Start the FTP server
    print("FTP honeypot is running...")
    server.serve_forever()

if __name__ == "__main__":
    main()

