import random

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
legalMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
bestMoves = [4, 0, 2, 6, 8, 1, 3, 5, 7] # najlepsze ruchy komputera
win = False
global WAYS_TO_WIN
WAYS_TO_WIN = ()
pos = None
global i
i = 0
draw = 0
global licznikRemisu
licznikRemisu = 0


def characterSelection(): # wybór kto ma zacząć
    kółkoCzyKrzyżyk = ("X", "O")
    global currentPlayer
    print("Kto ma zaczynać? Komputer, człowiek czy mam zdecydować za Ciebie?")
    global choice
    choice = 0

    while choice == 0:
        CHARACTER = input("Więc kto zaczyna?")
        if CHARACTER == "komputer":
            currentPlayer = 0
            choice += 1
        elif CHARACTER == "człowiek":
            currentPlayer = 1
            choice += 1
        elif CHARACTER == "los":
            currentPlayer = random.randrange(2)
            choice += 1
        else:
            print("Musisz wybrać spośród: komputer, człowiek lub los ")


def printBoard(board):
    print(board)


def humanMove(board):# ruch człowieka :)
    global bestMoves
    j = 0
    while j != 1:
        pos = input('Wybierz pole: ')
        try:
            pos = int(pos)

        except ValueError:
            print("Musisz wpisać liczbę pomiędzy 0 a 8!!!")
            continue
        if (pos < 0 or pos > 8):
            print("Wyszedłeś za plansze!!!")
        else:
            j += 1
            board[pos] = 'O'
            legalMoves.remove(pos)

    checkForWin(board)


def checkForWin(board):# sprawdzenie czy ktoś wygrał
    global win
    global WAYS_TO_WIN
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]]:
            global win
            win = True
            break

def funcX(board, WTW, legalMoves): # jest to funkcja wykorzystywana podczas ruchu koputera, sprawdzamy czy na ruchu dającym wygrane nie ma kólka czyli ruchu człowieka
    FWTW = []

    for move in WTW:
        if (board[move[0]] != 'O' and board[move[1]] != 'O' and board[move[2]] != 'O'):
            FWTW.append(move)

    return FWTW


def funcY(board, WTW, legalMoves):# kolejna funkcja wykorzystywana podczas ruchu komputera, sprawdza ona czy ruch dający wygranę jest możliwy do wykonania czyli czy nie ma tam już postawionego innego znaku
    FWTW2 = []

    for move in WTW:
        if (move[0] in legalMoves and move[1] in legalMoves and move[2] in legalMoves):
            FWTW2.append(move)

    return FWTW2


def computerMove(board, legalMoves, bestMoves): # ruch komputera
    simulatedBoard = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    for i in range(9):
        simulatedBoard[i] = board[i]
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    FINAL_WTW = funcX(board, WAYS_TO_WIN, legalMoves)
    FINAL_WTW2 = funcY(board, WAYS_TO_WIN, legalMoves)

    for move in FINAL_WTW:# ruch umożliwiający wygrraną
        if (simulatedBoard[move[0]] == simulatedBoard[move[1]] == 'X'):
            board[move[2]] = 'X'
            return
        elif (simulatedBoard[move[0]] == simulatedBoard[move[2]] == 'X'):
            board[move[1]] = 'X'
            return

        elif (simulatedBoard[move[1]] == simulatedBoard[move[2]] == 'X'):
            board[move[0]] = 'X'
            return

    for move in WAYS_TO_WIN:# ruch blokujący wygraną człowieka
        if (simulatedBoard[move[0]] == simulatedBoard[move[1]] == 'O' and board[move[2]] != 'X'):
            board[move[2]] = 'X'
            legalMoves.remove(move[2])
            return
        elif (simulatedBoard[move[1]] == simulatedBoard[move[2]] == 'O' and board[move[0]] != 'X'):
            board[move[0]] = 'X'
            legalMoves.remove(move[0])
            return
        elif (simulatedBoard[move[0]] == simulatedBoard[move[2]] == 'O' and board[move[1]] != 'X'):
            board[move[1]] = 'X'
            legalMoves.remove(move[1])
            return

    for move in bestMoves:# a jeśli komuter nie może ani wygrać ani nie musi blokować ruchu człowieka wybiera swój najlepszy ruch
        if move in legalMoves:
            board[move] = 'X'
            legalMoves.remove(move)
            return


print("\n\t", board[0], "|", board[1], "|", board[2])
print("\n\t", board[3], "|", board[4], "|", board[5])
print("\n\t", board[6], "|", board[7], "|", board[8])
characterSelection()
while (win == False): # główna pętla programu
    if currentPlayer == 0:
        computerMove(board, legalMoves, bestMoves)
        licznikRemisu += 1
        checkForWin(board)
        if win == True:
            print("komputer wygrał")
            break
        if licznikRemisu > 8:
            print('Nikt nie wygrał, mamy remis')
            break
        print("komputer wykonuje ruch: ")
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\n\t", board[3], "|", board[4], "|", board[5])
        print("\n\t", board[6], "|", board[7], "|", board[8])
        humanMove(board)
        licznikRemisu += 1
        checkForWin(board)
        if win == True:
            print("człowiek wygrał")
            break
        if licznikRemisu > 8:
            print('Nikt nie wygrał, mamy remis')
            break

        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\n\t", board[3], "|", board[4], "|", board[5])
        print("\n\t", board[6], "|", board[7], "|", board[8])

    else:
        humanMove(board)
        licznikRemisu += 1
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\n\t", board[3], "|", board[4], "|", board[5])
        print("\n\t", board[6], "|", board[7], "|", board[8])
        checkForWin(board)
        if win == True:
            print("człowiek wygrał")
            break
        if licznikRemisu > 8:
            print('Nikt nie wygrał, mamy remis')
            break
        computerMove(board, legalMoves, bestMoves)
        licznikRemisu += 1
        checkForWin(board)
        if win == True:
            print("komputer wygrał")
            break
        if licznikRemisu > 8:
            print('Nikt nie wygrał, mamy remis')
            break
        print("komputer wykonuje ruch: ")
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\n\t", board[3], "|", board[4], "|", board[5])
        print("\n\t", board[6], "|", board[7], "|", board[8])

print("\n\t", board[0], "|", board[1], "|", board[2])
print("\n\t", board[3], "|", board[4], "|", board[5])
print("\n\t", board[6], "|", board[7], "|", board[8])

print('\n\nKoniec rundy, aby zakończyć wciśnij enter')
