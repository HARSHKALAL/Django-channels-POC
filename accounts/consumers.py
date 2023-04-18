from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket connected...",event)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print("websocket received...",event)
        self.send({
            'type':'websocket.send',
            'text':"Hello world",
        })
    
    def websocket_disconnect(self,event):
        print("websocket Disconnect...",event)

