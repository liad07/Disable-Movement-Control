import os
import socket
import sys

BOT_IP = 'bot_ip'  # Replace with the bot's IP address
PORT = 55555

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the bot
client_socket.connect((BOT_IP, PORT))

# Read the script file
with open("DISABLEMOVMENT.py", "rb") as f:
    script_data = f.read(1024)
    while script_data:
        client_socket.send(script_data)
        script_data = f.read(1024)

print("Script file sent successfully!")

# Close the connection
client_socket.close()
