import dataUser
import libclient

class ControleHelico:
    def __ini__(self):
        self.helico = dataUser.data.helico
    
    def deployreq(self):
        return libclient.create_request(dataUser.data.userid, "deploy_helico", 0)

    def movereq(self, dir):
        return libclient.create_request(dataUser.data.userid, 'move_helico', dir)