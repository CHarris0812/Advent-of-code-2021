def part1():
    dice = 1
    player1 = 8
    player2 = 4
    player1Score = 0
    player2Score = 0
    turn = 1
    rolls = 0
    while player1Score < 1000 and player2Score < 1000:
        print(player1, player2, rolls, dice)
        if turn == 1:
            for i in range(3):
                rolls += 1
                player1 += dice
                while player1 > 10:
                    player1 = player1 - 10
                dice += 1
                if dice == 101:
                    dice = 1
            player1Score += player1
            print("Player 1: ", player1Score)
        else:
            for i in range(3):
                rolls += 1
                player2 += dice
                while player2 > 10:
                    player2 = player2 - 10
                dice += 1
                if dice == 101:
                    dice = 1
            player2Score += player2
            print("Player 2: ", player2Score)
        if turn == 1:
            turn = 2
        else:
            turn = 1
    if player1Score >= 1000:
        return rolls * player2Score
    return rolls * player1Score

def part2():
    games = {}
    gameResults = {}
    games[(4, 0, 8, 0, 1)] = 1
    games[(4, 0, 8, 0, 1)] = None

def simulateGames()



if __name__ == "__main__":
    print(part1())
    #print(part2())

