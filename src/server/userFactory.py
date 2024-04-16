import user

class UserFactory:
    def __init__(self):
        '''
        suit le format {Id:User}
        cet Id est le meme que les vehicules attribues a l'User concerne
        '''
        self.UserDict = {}


    def newUser(self, name, password):
        user.User( name, password)

    
