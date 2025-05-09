import socket
import threading

HOST = input("Enter the server IP address: ")
PORT = int(input("Enter the server port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = input("Enter your username: ")
client.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT} as {username}")
client.sendall(username.encode('utf-8'))

# This will recieve messages from the server
def listen_for_server():
    while True:
        try:
            server_message = client.recv(1024).decode('utf-8')
            if server_message.startswith("[BROADCAST]"):
                message = server_message[len("[BROADCAST] "):]
                print(f"\r{message}\n[You]: ", end="")
            elif server_message.startswith("[PRIVATE]"):
                message = server_message[len("[PRIVATE] "):]
                print(f"\r(Private) {message}\n[You]: ", end="")
            else:
                print(f"\r{server_message}\n[You]: ", end="")
        except:
            break

# Starts the thread to listen to the server
thread = threading.Thread(target=listen_for_server)
thread.start()


try:
    while True:
        message = input("[You]: ")
        if message.lower() in ['exit', 'quit']:
            break
        client.sendall(message.encode('utf-8'))
finally:
    print("Disconnected.")
    client.close()