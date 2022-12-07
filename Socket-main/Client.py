import time
import socket
import threading

host = "10.4.1.215"
port = 7778

def receive_message(socket):
    while True:
        data = socket.recv(1024)
        print(f"{data}".encode('utf-8'))

        if not data:
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((host, port))
    my_thread = threading.Thread(target=receive_message, args=(socket,))
    my_thread.start()

    while True:
        message = input("Votre message: \n")
        socket.sendall(message.encode("utf-8"))
        time.sleep(10)

