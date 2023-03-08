
import socket

class Client:
    def __init__(self, host, port, gameId):
        # Connexion au serveur
        self.host = host
        self.port = port
        self.gameId = gameId
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))


    def __del__(self):
        # Fermeture de la connexion
        self.close()

    def __str__(self):
        # Affichage de l'objet / Surtout pour le debug
        return "Client: %s:%s" % (self.host, self.port)

############################################################################
    def send(self, dataTab):
        # Concatenation du tableau d'entiers en binaire de 4 octects
        concatene = ""
        for elt in dataTab:
            concatene += str(format(elt, '08b'))
        

        # TODO : A modifier pour envoyer un tableau de bits 
        # Envoie des données au serveur en binaire
        self.socket.send(data.encode())

    def receive(self):

        # TODO : Verifier que la traduction se fait bien (faire un petit serveur en python pour tester)
        # Reception des donnée en binaire et les decompose en tableau d'entiers


        data = self.socket.recv(1024).decode()
        bits = data
        blocs = [bits[i:i+32] for i in range(0, len(bits), 32)] # Divise la chaîne en blocs de 32 bits
        chiffres = [int(bloc, 2) for bloc in blocs] # Convertit chaque bloc en chiffre décimal



        # Envoie des données au serveur en binaire
        return data

    def close(self):
        # Fermeture de la connexion
        self.socket.close()

############################################################################

    # TODO : Recuperation du gameId




bits = "000000000000000000000000000000010000000000000000000000000000001000000000000000000000000000000011"


