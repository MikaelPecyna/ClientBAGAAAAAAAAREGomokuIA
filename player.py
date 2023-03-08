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


            
            # TODO  : Expliquer le fonctionnement de cette condition

            if(recv[0] == Client.C_REGISTER_PLAYER and recv[1] == this.gameId):
                this.playerId = recv[2]
            else: 
                # TODO : Gestion de l'erreur
                print("Erreur lors de la reception du playerId")
        
        def recvStroke(self):
            
            recv = self.receive()

            # TODO  : Expliquer le fonctionnement de cette condition
            if(recv[0] == Client.S_SEND_STROKE and recv[1] == this.gameId):
                return (recv[2] , recv[3])
            else:
                # TODO : Gestion de l'erreur
                print("Erreur lors de la reception du coup")

        
