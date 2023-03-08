import gameOwnner as GO

# TODO : Recuperation du gameId
############################################################################################################
gameId = 123
addresse = "localhost"
port = 1234
type = 1
############################################################################################################


go = GO.GameOwnner(addresse, port , gameId)

go.initGame(gameId, type)

go.startGame()

while (True):# TODO : A modifier pour quitter la boucle quand la partie est finie
    (x,y) = go.receiveValidation()
    go.sendValidation(1)



