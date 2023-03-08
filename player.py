import client as c 

# Classe Player qui herite de la classe Client

class Player(c.Client):        

        def emitStroke(self, x, y):
            #Envoie du coup au serveur
            self.send([this.gameId , this.playerId , x , y])

        def register(self):
            #Envoie du gameId au serveur
            self.send([this.gameId])

            #Reception du playerId
            recv = self.receive()


            """Verification de la reception du playerId
            Si l'ordre recu est C_REGISTER_PLAYER , le serveur renvoie le playerId
            Si le gameId est correct, le serveur renvoie un tableau de 2 entiers

            """
            if(recv[0] == Client.C_REGISTER_PLAYER and recv[1] == this.gameId):
                this.playerId = self.receive()[2]
            else: 
                print("Erreur lors de la reception du playerId")
        
