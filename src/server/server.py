import serverInstructions
import userFactory
import environment
import vehicleFactory

'''
TODO: BDD

'''
class Server:
    def __init__(self):
        self.userF = userFactory.UserFactory()
        self.vehicleF = vehicleFactory.VehicleFactory()
        self.environment = environment.Environment()
