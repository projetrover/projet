#!/usr/bin/env python3

# Toute la partie du code concernant les interactions client / serveur proviennent de ce site https://realpython.com/python-sockets/#application-client-and-server
# Elle a seulement ete legerement adaptee pour ce projet

import sys
import socket
import selectors
import traceback

import libclient

sock = None
events = None
sel = selectors.DefaultSelector()


def create_request(action, value):      #ici que c'est interessant
    global events
    req =  dict(
        type="text/json",
        encoding="utf-8",
        content=dict(action=action, value=value),
        )
    message = libclient.Message(sel, sock, addr, req)
    sel.register(sock, events, data=message)

    state = False
    try:
        while not state:                                    #PROBLEME ICI j'arrive pas a sortir de la boucle
            print("Boucle", state)
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                state = message.state
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


def start_connection(host, port):
    global sock, events
    addr = (host, port)
    print(f"Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE





if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
addr = (host, port)
start_connection(host, port)
create_request("move_rover", "up")
create_request("move_rover", "down")
#sel.close()


#finally:
#    sel.close()
