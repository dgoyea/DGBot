#!/usr/bin/env python
# WS client example

import json
import asyncio
import websockets
import time

class DGPoloniexWebsocket: 

    def __init__(self):
        self.plxaddress = "wss://api2.poloniex.com"
        return
    
    async def plxConnect(self, command, channel):
        async with websockets.connect(
                self.plxaddress) as websocket:
        
                    prejsonconn = {"command": self.command,
                                   "channel": self.channel
                                   } 
        
                    jsonconn = json.dumps(prejsonconn)
                    
                    await websocket.send(jsonconn)
                    print('Connecting')
                    
                    while True:
                        plxResp = await websocket.recv()
                        print(plxResp)
                        #time.sleep(10)
        
    
    def TickerData(self):
        self.command = 'subscribe'
        self.channel = '1002'
    
        asyncio.get_event_loop().run_until_complete(self.plxConnect(self.command, self.channel))
    
    
    
#     def __init__(self):
#         #websocket.enableTrace
#         ws = websocket.WebSocketApp("wss://api2.poloniex.com",
#                                   on_message = self.on_message,
#                                   on_error = self.on_error,
#                                   on_close = self.on_close)
#         self.ws.on_open = self.on_open
#         self.ws.run_forever()    
#     
#     def on_message(self, ws, message):
#         print(message)
#     
#     def on_error(self, ws, error):
#         print(error)
#     
#     def on_close(self, ws):
#         print("### closed ###")
#     
#     def on_open(self, ws):
#         tickSubscribe = {"command": "subscribe",
#                          "channel": "1002"
#                         }
#         
#         msgJson = json.dumps(tickSubscribe)
#         
#         ws.send(msgJson)
#         time.sleep(100)
#         ws.close()
#         print("thread terminating...")
        
    #    thread.start_new_thread(run, ())
