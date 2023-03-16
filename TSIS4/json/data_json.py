import json

file = open('data.json', 'r')
data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

#for i in data:
   # print(data[i])
for i in data["imdata"]:
   DN = i["l1PhysIf"]["attributes"]["dn"]
   Descr = i["l1PhysIf"]["attributes"]["descr"]
   Speed = i["l1PhysIf"]["attributes"]["speed"]
   MTU = i["l1PhysIf"]["attributes"]["mtu"]
   print(DN, Descr, Speed, MTU, sep = "\t")
   