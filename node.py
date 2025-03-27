import socket
import threading

nodes = []

def start_node(port):
    """Start a new node on the given port."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen(5)
    print(f"🌐 Node started on port {port}...")

    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"📩 Received: {message}")
                for node in nodes:
                    node.send(message.encode())
            except:
                break

    while True:
        client_socket, addr = server.accept()
        print(f"✅ New connection from {addr}")
        nodes.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def connect_to_node(port):
    """Connect to an existing node."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", port))
    nodes.append(client)
    print(f"🔗 Connected to node on port {port}.")
