import Client as c 

# Classe GameOwner qui herite de la classe Client

class GameOwner(c.Client):

    def initGame(self, type):
        self.send([Client.C_INIT_GAME, type])

    def getGameId(self):
        recv = self.receive()

        if recv[0] == Client.S_GAME_CREATED and recv[1] == self.gameId:
            print("Game created")
        else:
            self.catchError("Erreur lors de la creation de la partie")