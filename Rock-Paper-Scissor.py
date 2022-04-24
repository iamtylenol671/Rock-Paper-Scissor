import random

gameRunner = True
pointP1 = 0
pointP2 = 0
rounder = 1


def checkWinner(player1, player2):

    global pointP1, pointP2

    if player1 == player2:
        return 'Ties'
    elif player1 == 'rock':
        if player2 == 'scissor':
            pointP1 += 1
            return 'Player_1 is winner'
        else:
            pointP2 += 1
            return 'Player_2 is winner'

    elif player1 == 'scissor':
        if player2 == 'paper':
            pointP1 += 1
            return 'Player_1 is winner'
        else:
            pointP2 += 1
            return 'Player_2 is winner'

    elif player1 == 'paper':
        if player2 == 'rock':
            pointP1 += 1
            return 'Player_1 is winner'
        else:
            pointP2 += 1
            return 'Player_2 is winner'
    else:
        return 'Invalid valur'


def botPlayer():
    choice_list = ['rock', 'scissor', 'paper']
    return random.choice(choice_list)


def checkPointWinner(point1, point2):
    global gameRunner
    if point1 == 5 or point2 == 5:
        if point1 > point2:
            print(f"Score Player_1 = {point1}")
            print('Player_1 is Score Winner!!!!')
            gameRunner = False
        else:
            print(f"Score Player_2 = {point2}")
            print('Player_2 is Score Winner!!!!')
            gameRunner = False


while gameRunner:
    print(f'Round: {rounder}')
    p1 = str(input('Player_1: ').strip()).lower()
    p2 = botPlayer()
    get_winner = checkWinner(p1, p2)
    print('------')
    print(f"Player_1: {p1}")
    print(f"Player_2: {p2}")
    print('------')
    print(f"Player_1 score: {pointP1}")
    print(f"Player_2 score: {pointP2}")
    print('------')
    print(get_winner)
    print('------')
    checkPointWinner(pointP1, pointP2)
    print('------')
    rounder += 1