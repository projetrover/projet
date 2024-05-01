import vehicle

class Rover(vehicle.Vehicle):
    def __init__(self, pos, Height, durability, battery, analysisDict):
        self.analysisDict = analysisDict
        vehicle.Vehicle.__init__(self, pos, Height, durability, battery)

    def analyze(self, material):
        if material in self.analysisDict.keys():
            self.analysisDict[material] += 1
        else:
            self.analysisDict[material] = 1
