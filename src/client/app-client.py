# Toute la partie du code concernant les interactions client / serveur proviennent de ce site https://realpython.com/python-sockets/#application-client-and-server
# Elle a seulement ete legerement adaptee pour ce projet

import sys
import selectors
import libclient as lc
import authentification as auth


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

events = selectors.EVENT_READ | selectors.EVENT_WRITE
host, port = sys.argv[1], int(sys.argv[2])
addr = (host, port)
sock, message = lc.start_connection(host, port, events)

#----TESTS-----
test = auth.Authentification()
test.login('truc', 'muche')
#---------------

lc.sel.close()  #Fermeture du selector, a deplacer dans deconnexion() des que possible


