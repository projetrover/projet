import user

class UserFactory:
    def __init__(self):
        '''
        suit le format {Id:User}
        cet Id est le meme que les vehicules attribues a l'User concerne
        '''
        self.UserDict = {}


    def addUser(self, Id, name, password):
        #TODO pour acceder le bon user avec son nom en + de l'ID
        self.UserDict[Id] = user.User( name, password)
