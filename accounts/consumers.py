from channels.consumer import SyncConsumer
from time import sleep

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type":'websocket.accept'
        })
    
    def websocket_receive(self, event):
        self.send({
            "type": 'websocket.send',
            "text": event['text'],
        })

    def websocket_disconnect(self, event):
        pass
