import Client as c 

# Classe GameOwner qui herite de la classe Client

class GameOwner(c.Client):

    def initGame(self, type):
        self.send([Client.C_INIT_GAME, type])

        recv = self.receive()

        if recv[0] == Client.S_GAME_CREATED and recv[1] == self.gameId:
            print("Game created")
        else:
            self.catchError("Erreur lors de la creation de la partie")
        

    def startGame(self):
        self.send([Client.C_START_GAME, self.gameId])

    def receiveValidation(self):
        recv = self.receive()

        if recv[0] == Client.S_REQUEST_VALIDATION and recv[1] == self.gameId:
            return (recv[2], recv[3])

    def sendValidation(self, validation):
        if validation in [0, 1, 2]:
            self.send([Client.C_ANSWER_VALIDATION, self.gameId, validation])
        else:
            self.catchError("Erreur lors de l'envoi de la validation [validation = 0, 1 ou 2]")
    


 
