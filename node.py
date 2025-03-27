import socket
import threading

nodes = []

def start_node():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5001))
    server.listen(5)
    print("🌐 Node started on port 5001...")

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

def connect_to_node():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5001))
    nodes.append(client)
    print("🔗 Connected to node.")

def send_message(message):
    for node in nodes:
        node.send(message.encode())
