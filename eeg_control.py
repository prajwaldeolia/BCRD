# Importing the packages and the libraries
from unittest import result
import json
from websocket import create_connection
import ssl
import time
import requests

# Create object of class create_connection
ws = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})
auth = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS5kaXlhZWMzLmJjcmQiLCJhcHBWZXJzaW9uIjoiMS4wIiwiZXhwIjoxNjU0MDYwMDg2LCJuYmYiOjE2NTM4MDA4ODYsInVzZXJJZCI6ImUzNWNjN2QwLWM3ZjAtNGYwMC05NzAwLWI1M2MwMTU2YWQ0YSIsInVzZXJuYW1lIjoiZGl5YWVjMyIsInZlcnNpb24iOiIyLjAifQ==.EVYYtNaDy/lUmbgh+cIS+cO37RwRmPleBrncSCz8th4="
# Create a session with the Emotiv Insight
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "createSession",
 "params": {
     "cortexToken": auth,
     "headset":"EPOCX-E20202EC",
     "status": "open"
 },
 "id": 1
 }))

# print(ws.recv())
var1 = ws.recv()
# #print(json.loads(var1))
var1 = json.loads(var1)
#print(var1)
print("this is the ID::::-->>>",list(var1['result'].items())[2][1])
# print(type(var1))
ws.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "requestAccess",
    "params": {
        "clientId": "ntNO4UEFpBYQ7gX3UtEVDPvt3cgCzuYVmlIBWWCE",
        "clientSecret": "qGtgK36GiOIpLde2R8x7GF9Bhxo8RGENrEHlNYeJHbWCIe06U01YaFlAjtoYOLbEYVAqcOnczUuJ9NuFZVFEVWiWv4pQyXcyuDX1NTrPbc6lajUWf9DR2phsjaTIyJtq"
    }
}))
print(ws.recv())

# # to generate token
# ws.send(json.dumps({      
#     "id": 1,
#     "jsonrpc": "2.0",
#     "method": "authorize",
#     "params": {
#         "license":"4fc43ebf-78fd-4db3-af4c-14dc6ace2463",
#         "clientId": "ntNO4UEFpBYQ7gX3UtEVDPvt3cgCzuYVmlIBWWCE",
#         "clientSecret": "qGtgK36GiOIpLde2R8x7GF9Bhxo8RGENrEHlNYeJHbWCIe06U01YaFlAjtoYOLbEYVAqcOnczUuJ9NuFZVFEVWiWv4pQyXcyuDX1NTrPbc6lajUWf9DR2phsjaTIyJtq"
#     }
#  }))

# print(ws.recv())

# # Subscribe to sys stream
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "subscribe", 
 "params": {
     "cortexToken":auth,
     "session": list(var1['result'].items())[2][1],
     "streams":[
     "sys"
     ]
 },
 "id": 1
 }))

print(ws.recv())
print("line 72")
# Begin training mental commands

# Training neutral
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "cortexToken":auth,
   "detection":"mentalCommand",
   "action":"neutral",
   "session":list(var1['result'].items())[2][1],
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "cortexToken":auth,
     "detection":"mentalCommand",
     "session":list(var1['result'].items())[2][1],
     "action":"neutral",
     "status":"accept"
 }, 
 "id": 1
 }
))
print("line 107 ------->>>>")
print(ws.recv())
time.sleep(2)
print(ws.recv())
print("line 111 ----->>>")

# # Training push (forward)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "cortexToken":auth,
   "detection":"mentalCommand",
   "session":list(var1['result'].items())[2][1],
   "action":"push",
   "status":"start"
 }, 
 "id": 1
 }))
print("line 126 ---->>>")
print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "cortexToken":auth,
     "detection":"mentalCommand",
     "session":list(var1['result'].items())[2][1],
     "action":"push",
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())



# # Training left (pivot left)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "cortexToken":auth,
   "detection":"mentalCommand",
   "session":list(var1['result'].items())[2][1],
   "action":"left",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "cortexToken":auth,
     "detection":"mentalCommand",
     "session":list(var1['result'].items())[2][1],
     "action":"left",
     "status":"accept"
 }, 
 "id
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())

# Training neutral
# ws.send(json.dumps( {
#  "jsonrpc": "2.0", 
#  "method": "training", 
#  "params": {
#    "cortexToken":auth,
#    "detection":"mentalCommand",
#    "action":"neutral",
#    "session":list(var1['result'].items())[2][1],
#    "status":"start"
#  }, 
#  "id": 1
#  }))

# print(ws.recv())
# time.sleep(5)
# print(ws.recv())
# time.sleep(10)

# # Training right (pivot right)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "cortexToken":auth,
   "detection":"mentalCommand",
   "session":list(var1['result'].items())[2][1],
   "action":"right",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "cortexToken":auth,
     "detection":"mentalCommand",
     "action":"right",
     "session":list(var1['result'].items())[2][1],
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(5)
print(ws.recv())

# # Obtain stream of mental commands

# # Subscribe to com stream
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "subscribe", 
 "params": {
     "cortexToken":auth,
     "session":list(var1['result'].items())[2][1],
     "streams":[
     "com"
 ]
 },
 "id": 1
 }))

print(ws.recv())

# loop for rover control
thought = None
while True:
    thought_Dict = json.loads(ws.recv())
    var2= list(thought_Dict.items())[0][1]
    if(not(isinstance(var2,int))):
        print(var2[0])
        thought = var2[0]
    if(thought == "push"):
        url_get = "http://169.254.184.200:5000/forward"
        res = requests.get(url_get, headers={"Content-Type":"text"})
    elif(thought == "left"):
        url_get = "http://169.254.184.200:5000/pivot_left"
        res = requests.get(url_get, headers={"Content-Type":"text"})
    elif(thought == "right"):
        url_get = "http://169.254.184.200:5000/pivot_right"
        res = requests.get(url_get, headers={"Content-Type":"text"})