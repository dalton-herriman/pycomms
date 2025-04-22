import socket

HOST = input("Enter the server IP address: ")
PORT = int(input("Enter the server port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = input("Enter your username: ")
client.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT} as {username}")

# Wait for the server to ask for username, then send it
server_prompt = client.recv(1024).decode('utf-8')
print(server_prompt)
client.sendall(username.encode('utf-8'))

try:
    while True:
        message = input("You: ")
        if message.lower() in ['exit', 'quit']:
            break
        client.sendall(message.encode('utf-8'))
finally:
    print("Disconnected.")
    client.close()