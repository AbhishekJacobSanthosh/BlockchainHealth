import socket
import threading

nodes = []

def start_node(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen(5)
    print(f"🌐 Node started on port {port}... Waiting for connections.")

    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"📩 Received: {message}")
                for node in nodes:
                    if node != client_socket:  # Prevent sending back to sender
                        node.send(message.encode())
            except:
                break

    while True:
        client_socket, addr = server.accept()
        print(f"✅ New connection from {addr}")
        nodes.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def connect_to_node(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("localhost", port))
        nodes.append(client)
        print(f"🔗 Connected to node on port {port}.")
    except ConnectionRefusedError:
        print("⚠️ Unable to connect. Make sure the node is running.")

def send_message(message):
    for node in nodes:
        node.send(message.encode())

if __name__ == "__main__":
    print("\n🌍 Blockchain Node Manager")
    print("1️⃣ Start a New Node (Server)")
    print("2️⃣ Connect to an Existing Node")
    
    choice = input("🔷 Choose an option: ")

    if choice == "1":
        port = int(input("🛠️ Enter the port number to start the node on: "))
        start_node(port)
    elif choice == "2":
        port = int(input("🔗 Enter the port number to connect to: "))
        connect_to_node(port)
    else:
        print("⚠️ Invalid option! Exiting...")
