import socket
import os

HOST = ''   # Use an empty string to accept connections from any available address
PORT = 55555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print("Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive the script
name = "received_script.py"
with open(name, "wb") as f:
    script_data = client_socket.recv(1024)
    while script_data:
        f.write(script_data)
        script_data = client_socket.recv(1024)

print("Script received successfully!")
os.system(f"python {name}")
# Close the connection
client_socket.close()
server_socket.close()
