#!/usr/bin/env python3

# Toute la partie du code concernant les interactions client / serveur proviennent de ce site https://realpython.com/python-sockets/#application-client-and-server
# Elle a seulement ete legerement adaptee pour ce projet

import sys
import socket
import selectors
import traceback
from time import sleep

import libclient

sock = None
events = selectors.EVENT_READ | selectors.EVENT_WRITE
message = None
sel = selectors.DefaultSelector()


def create_request(idjoueur, action, value):      #ici que c'est interessant
    global message, events
    req =  dict(
        type="text/json",
        encoding="utf-8",
        content=dict(idjoueur = idjoueur,
                     action = action,
                     value = value),
        )
    message.request = req
    message.state = False
    message.queue_request()
    #print("SEND = ", message._send_buffer)  #ON est bon

    message.state = False
    try:
        while not message.state:                                    #PROBLEME ICI j'arrive pas a sortir de la boucle
            #print("Boucle")
            events = sel.select(timeout=1)
            #print("events = ",events)
            for key, mask in events:
                message = key.data
                #print("Send buffer = ", message._send_buffer)
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                        f"{traceback.format_exc()}"
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")

    #print("sorti")


def start_connection(host, port):
    global sock, events
    addr = (host, port)
    print(f"Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)






if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
addr = (host, port)
start_connection(host, port)

message = libclient.Message(sel, sock, addr, None)
sel.register(sock, events, data=message)                #On register qu'une fois le socket, on va le reutiliser apres

create_request(0,"move_rover", "up")

sel.close()


#finally:
#    sel.close()
