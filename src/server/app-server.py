#!/usr/bin/env python3

# Toute la partie du code concernant les interactions client / serveur proviennent de ce site https://realpython.com/python-sockets/#application-client-and-server
# Elle a seulement ete legerement adaptee pour ce projet

import sys
import socket
import selectors
import traceback

import libserver
import Server
import VehicleFactory

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)



if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

###TESTS###
JEN ETAIS, A TESTER
serv = server.Server()
vehi = VehicleFactory.VehicleFactory()
vehi.NewVehicles(1, (0,0))
serv.vehicules = vehi
#############


host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        #print("Boucle")
        events = sel.select(timeout=None)
        #print("events = ", events)
        for key, mask in events:
            #print("key.data = ", key.data)
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                message = key.data
                #print("message = ", message)
                #print("rcv_buffer = ", message._recv_buffer)
                try:
                    #print("mask =", mask)
                    message.process_events(mask)
                    #print("message processed")
                    #if message._send_buffer == b'' and message.response_created :
                     #   message.responde_created = False
                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                        f"{traceback.format_exc()}"
                    )
                    message.close()
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
