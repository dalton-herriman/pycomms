import socket
import threading

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5555       # Arbitrary non-privileged port

def handle_client(client_socket, addr):
    print(f"[+] New connection from {addr}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{addr}] {message}")
        except:
            break
    print(f"[-] Connection closed from {addr}")
    client_socket.close()

def start_server():
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