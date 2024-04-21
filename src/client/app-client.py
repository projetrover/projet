#!/usr/bin/env python3

# Toute la partie du code concernant les interactions client / serveur proviennent de ce site https://realpython.com/python-sockets/#application-client-and-server
# Elle a seulement ete legerement adaptee pour ce projet

import sys
import selectors
import libclient as lc


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

events = selectors.EVENT_READ | selectors.EVENT_WRITE
host, port = sys.argv[1], int(sys.argv[2])
addr = (host, port)
sock, message = lc.start_connection(host, port, events)

lc.create_request(1,"move_rover", "up")

lc.sel.close()  #Fermeture du selector, a deplacer dans deconnexion() des que possible


