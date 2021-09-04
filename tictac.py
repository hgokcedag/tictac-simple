gameon = True
values = ["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]
winnerPositions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
playedPositions = []


def newgamestart():
    global gameon
    clearvalues()
    while gameon:
        drawboard()
        makeamove()
        if not gameon:
            break
    print("Game Over!")
    print(playedPositions)


def checkIfWon(letter):
    global gameon
    won = False
    for i in winnerPositions:
        if not won:
            matches = 0
            matchLetter = " " + letter + " "
            for x in i:
                if values[x] == matchLetter:
                    matches += 1
                else:
                    break
            if matches == 3:
                print(letter + " won!")
                gameon = False


def makeamove():
    legalmove = False
    global gameon
    while not legalmove:
        moveposition = (input("Choose a cell to play -> "))
        if not moveposition.isdigit():
            print("Please enter a digit!")
            continue
        else:
            moveposition = int(moveposition)
            if moveposition == 0:
                print("exiting")
                gameon = False
                break
            elif not moveposition in range(1, 10):
                print("Please enter a number between 1 and 9! -> ")
                continue
            elif moveposition in playedPositions:
                print("This position is already filled! Enter another position")
                continue
            else:
                move = input("Draw X or O ? -> ")
                if move != "X" and move != "O":
                    print("please enter X or O -> ")
                    continue
                else:
                    values[moveposition] = " " + move + " "
                    playedPositions.append(moveposition)
                    checkIfWon("O")
                    checkIfWon("X")
                    if len(playedPositions) == 9 and gameon==True:
                        print("No more empty cells! No winner!")
                        gameon = False
                    break


def clearvalues():
    global playedPositions
    for b in range(10):
        if b != 0:
            values[b] = "   "
    playedPositions = []


def drawboard():
    text = "\n"
    for idx, b in enumerate(values):
        if idx != 0:
            newtext = "|" + " " + str(idx) + " "
            text += newtext
            if idx % 3 == 0:
                text += "|\n"
    print(text)

    text = "\n"
    for b in range(10):
        if b != 0:
            text += "|" + values[b]
            if b % 3 == 0:
                text += "|\n"
    print(text)


newGame = "Y"
while newGame == "Y":
    newGame = input("Yeni oyuna başlamak ister misiniz? Y or N -> ")
    if newGame == "Y":
        gameon = True
        newgamestart()
    elif newGame == "N":
        print("Oyun bitti!")
        break
