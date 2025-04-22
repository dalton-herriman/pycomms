import socket

HOST = input("Enter the server's IP address: ")
PORT = int(input("Enter the server's port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")
print(f"Connected to server at {HOST}:{PORT} as {username}")
client.sendall(f"{username} has joined the chat.".encode('utf-8'))

try:
    while True:
        message = input("You: ")
        if message.lower() in ['exit', 'quit']:
            break
        client.sendall(message.encode('utf-8'))
finally:
    print("Disconnected.")
    client.close()