#Real-time application with WebSockets
#tornado.websocket — Bidirectional communication
#doc: http://tornado.readthedocs.org/en/latest/websocket.html

#unterstützt Websocket-Protokoll RFC 6455
#getestet mit Google chrome Version 43.0.2357.124 m


# -*- coding: utf-8 -*-
import logging
import tornado.websocket
import tornado.httpserver
import socket

class EchoWebsocketServer(tornado.websocket.WebSocketHandler):

    websockets = set()

    #Datenherkunft, von welchen host kommen die daten?
    #hier kann die Herkunft der Daten eingeschränkt werden, siehe nächste untere Methode als Bsp.
    def check_origin(self, origin):
        print(origin)
        EchoWebsocketServer.websockets.add(self)
        print(EchoWebsocketServer.websockets)
        return True

    #def check_origin(self, origin):
    #parsed_origin = urllib.parse.urlparse(origin)
    #return parsed_origin.netloc.endswith(".mydomain.com")

    #Wenn Client Verbindung aufbaut zum Websocket-Server
    #dann wird hier open aufgerufen
    def open(self):
        print("WebSocket opened")
        print()


    #Hier werden Nachrichten vom Websocket-Client empfangen
    #in message steht die Nachricht und kann weiter gehandelt werden
    #hier wird die empfangene Nachricht zurück zum Client gesendet
    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print ("angekommene Nachricht " + message)
        EchoWebsocketServer.broadcast("halllooooo")

    #Wenn Websocket-Client verbindung beendet,
    #dann wird hier on_close aufgerufen
    def on_close(self):
        print("WebSocket closed")
        EchoWebsocketServer.websockets.remove(self)
        print(EchoWebsocketServer.websockets)

   # @classmethod
    #def broadcast(cls,msg):
    #    for ws in cls.websockets:
    #        try:
    #           ws.write_message(msg)
    #        except:
     #           logging.error("Error sending message", exc_info=True)



application = tornado.web.Application([
    ('/ws', EchoWebsocketServer),
])


if __name__ == "__main__":

    #lokaler server von tornado
    http_server = tornado.httpserver.HTTPServer(application)

    #auf Port 8888 horchen
    http_server.listen(8888)

    #IP-Adresse über socket-Modul holen
    myIP = socket.gethostbyname(socket.gethostname())
    print ("***Websocket Server Started at " + myIP +" ***")

    #starte server
    tornado.ioloop.IOLoop.instance().start()