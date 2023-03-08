import client as c 

# Classe Player qui herite de la classe Client

class Player(c.Client):        

        def emitStroke(self, x, y):
            #Envoie du coup au serveur
            self.send([this.gameId , this.playerId , x , y])


        def register(self):
            #Envoie du gameId au serveur
            self.send([this.gameId])

            # On attend la reponse du serveur pour savoir si le joueur est bien enregistré
            recv = self.receive()

            """
            Si le serveur renvoie un message de type C_PLAYER_REGISTERED => le joueur est bien enregistré
            On verifie que les gameId sont bien identiques
            On recupere le playerId
            """

            if(recv[0] == Client.C_REGISTER_PLAYER and recv[1] == this.gameId):
                this.playerId = recv[2]
            else: 
                self.catchError("Erreur lors de la reception du playerId")
        



        def recvStroke(self):
            
            recv = self.receive()

            """
            Si le serveur envoie un message de type S_SEND_STROKE => On recoit le coup d'un autre joueur
            On verifie que les gameId sont bien identiques
            On retourne les coordonnees du coup sous forme de tuple
            """
            if(recv[0] == Client.S_SEND_STROKE and recv[1] == this.gameId):
                return (recv[2] , recv[3])
            else:
                self.catchError("Erreur lors de la reception du coup")

        
