import vehicleFactory


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
