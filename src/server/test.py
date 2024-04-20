import vehicleFactory
import userFactory
import environment

UP=0
RIGHT=1
DOWN=2
LEFT=3

v = vehicleFactory.VehicleFactory()

v.newVehicles(1, (0,0))
v.newVehicles(2, (0,0))
v.newVehicles(3, (0,0))
v.delVehicle(2,'Helico')

print(v.helicoList[1])
v.helicoList[1].move('down', 10)
print(v.helicoList[1])

print(v)

uf = userFactory.UserFactory()
uf.addUser(1,'bob','1234')
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
