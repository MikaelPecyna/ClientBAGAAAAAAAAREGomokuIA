import player as p 


# TODO : Recuperation du gameId
############################################################################################################
gameId = 123
addresse = "localhost"
port = 1234
############################################################################################################

myPlayer = p.Player(addresse, port , gameId)

myPlayer.register()

whille (True): # TODO : A modifier pour quitter la boucle quand la partie est finie 
    # TODO : Savoir qui commence la partie

    if(start):
        # TODO : Demander au joueur de dessiner
        myPlayer.emitStroke(x, y)
    else:
        # TODO : Recuperer le coup du joueur adverse
        (x,y) = myPlayer.recvStroke()




