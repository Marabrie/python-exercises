# 1. Visualize the game somehow
# 2. Allow players to enter moves
# 3. Make sure moves are valid and handle if not.
# 4. Determine of there is a winner.

game = [[0,0,0],[0,0,0],[0,0,0,]]


def game_board(current_game,player=0,row=0, column=0, just_display=False):
    print("  A   B  C")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count,row)
    return current_game
 

game_board(game)
game_board(game,player=2, row=0,column=0) 


print(game)
print(id(game))

#game[0][1]=1
#game_board() 





