import vehicleFactory
import userFactory
import environment
import random
import numpy as np
import json
import server

UP=0
RIGHT=1
DOWN=2
LEFT=3
'''
v = vehicleFactory.VehicleFactory()

v.newVehicles(1, (0,0))
v.newVehicles(2, (0,0))


print(v.helicoList[1])
v.helicoList[1].move('down', 10)
print(v.helicoList[1])

print(v)

uf = userFactory.UserFactory()
uf.addUser(1,'bob','1234')
uf.addUser(2,'alice','5678')

print(uf.UserDict[1])
uf.UserDict[1].discover(150, 150, 50)
uf.UserDict[1].discover(151, 151, 51)
print(uf.UserDict[1].discoveredMap[150,150])
print(uf.UserDict[1].discoveredMap[151,151])
print('oui')
uf.UserDict[1].discover(151, 152, 56)
print(uf.UserDict[1].discoveredMap[151, 152])


e = environment.Environment()
e.generate_topography()
e.topography.print()
'''

serv = server.Server()
#serv.userF = uf
#serv.vehicleF = v
serv.load()
'''
nombre de tick server, 10 000 000 tick a 144 tick/secondes (fps ?)
cela genere TOUTES les meteos pour cette duree de service
-> 69444 secondes -> 19 heures
'''
serv.start(100000)
serv.loginRequest({"username":"bob","password":"1234"})
print(serv.vehicleF.roverList[1])
serv.moveRoverRequest(1,0)
print("up  (y-1)",serv.vehicleF.roverList[1])

serv.moveRoverRequest(1,1)
print("right(x+1)",serv.vehicleF.roverList[1])
serv.moveRoverRequest(1,2)
print("down (y+1)",serv.vehicleF.roverList[1])
serv.moveRoverRequest(1,2)
print("down (y+1)",serv.vehicleF.roverList[1])
serv.moveRoverRequest(1,3)
print("left (x-1)",serv.vehicleF.roverList[1])
#print(serv.vehicleF.roverList[1])

#print(uf.UserDict[1].__dict__)
#print(v.__dict__)
#seed = 156478
#env = environment.Environment()
#serv.environment = env
#env.generate_topography()
#print(env.topography[601][69])
#print(env.topography[602][69])
#env.generate_meteoMap(seed, 5000000)
#env.placeCurrentMeteos(30)
#serv.save()

#print(env.meteoMap,'\n\n\n')
#print(env.currentMeteos,'\n')
#env.updateMeteo(31)
#print(env.currentMeteos)

# a = np.zeros((10,10), dtype = int)
# a = a.tolist()
# dic = {'a' : a}
# json_object = json.dumps(dic, indent=4)
# try :
#             with open("src/server/test.json", "w") as outfile:
#                 outfile.write(json_object)
# except :
#             with open("test.json", "w") as outfile:
#                 outfile.write(json_object)
