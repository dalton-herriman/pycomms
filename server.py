import socket
import threading

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5555         # Arbitrary non-privileged port

clients = []  # List to store client sockets and usernames

def broadcast(message, sender_socket=None):
    """Send a message to all connected clients except the sender."""
    for client, username in clients:
        if client != sender_socket:
            try:
                client.send(f"[BROADCAST] {message}".encode('utf-8'))
            except:
                client.close()
                clients.remove((client, username))

def handle_client(client_socket, addr):
    """Handle communication with a single client."""
    print(f"[+] New connection from {addr}")
    try:
        # Request and store the username
        username = client_socket.recv(1024).decode('utf-8').strip()
        clients.append((client_socket, username))
        print(f"[+] {username} joined from {addr}")
        broadcast(f"{username} has joined the chat!", client_socket)

        # Send a message back to the client
        client_socket.send("[PRIVATE] Welcome to the server!".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{username}] {message}")
            broadcast(f"[{username}] {message}", client_socket)
    except:
        pass
    finally:
        print(f"[-] Connection closed from {addr}")
        broadcast(f"{username} has left the chat!", client_socket)
        client_socket.close()
        clients.remove((client_socket, username))

def start_server():
    """Start the server and listen for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[=] Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()