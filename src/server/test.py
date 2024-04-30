import vehicleFactory
import userFactory
import environment
import random
#import server

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

#serv = server.Server()
#serv.userF = uf
#serv.vehicleF = v
#serv.load()
#print(serv.vehicleF.roverList[1])

#print(uf.UserDict[1].__dict__)
#print(v.__dict__)
m = environment.MAP_SIZE
seed = 156478
env = environment.Environment(m)
#env.generate_topography()
env.generate_meteoMap(seed, 5000000)
env.placeCurrentMeteos(30)
print(env.meteoMap,'\n\n\n')
print(env.currentMeteos,'\n')
env.updateMeteo(31)
print(env.currentMeteos)
