import socket

HOST = '127.0.0.1' #Server's IP
PORT = 5555 #Port the server is listening on 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"Connected to server at {HOST}:{PORT}")
try:
    while True:
        message = input("You: ")
        if message.lower() in ['exit', 'quit']:
            break
        client.sendall(message.encode('utf-8'))
finally:
    print("Disconnected.")
    client.close()