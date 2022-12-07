import socket
import threading
import time

host = "10.4.1.215"
port = 7778

conn_list = []

def thread_function(sender_conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = sender_conn.recv(1024)

        for conn in conn_list:
            if conn.getpeername() != addr:
                conn.sendall(f"{addr}: {data}".encode("UTF-8"))

        if not data:
            break
        print(f"Adresse: {addr} sent message {data}")



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(3)
    while True:
        conn, addr = s.accept()
        conn_list.append(conn)
        my_thread = threading.Thread(target=thread_function, args=(conn, addr))
        my_thread.start()



