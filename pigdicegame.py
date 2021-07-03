'''Two players are trying to reach 100 points first.

If they hold, they add the sum of their rolls to their score. If they roll a 1, they get no points.
After a 1 is rolled or the player holds, the other player takes their turn.
The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)
In your implementation, there will be one human player and one computer player. The computer player will always hold until they roll a total of 20 points.'''
# Roll the dice to play the game
# Player1 = human player
# Player2 = computer player
# Player1 takes a  turn
# Player2 takes a turn
# Repeat turns until one player wins
# Winning score = 100 points
# Display the results, you win (player1, player2)

from icecream import ic
import random 

maxscore = 100

def greeting(): 
    print("Welcome to the Momentum Pig Game!") 

#the first player is chosen randomly
def create_players():
    player_types = ["human_player", "computer_player"]
    player1 = Player(random.choice(player_types))
    if player1.type == "human_player":
        player2 = Player("computer_player")
    else:
        player2 = Player("human_player")




class Player:
#defines player1 which is human_player and Player2 which is computer_player  
    def __init__(self, type):
        self.type = type
        self.score = 0

    
class Die:
    
    def __init__(self,n=6):
        self.sides=n
            
    def roll(self):
        return random.randint(1,self.sides)



class Game():
    def __init__(self):
        self.winner = None
        self.player1 = Player("human_player")
        self.player2 = Player("computer_player")
        self.die = Die()
        
        
    def playgame(self):
        player_choice = None 
        while self.player1.score <= 100 and player_choice != "H":
            player_choice = input ("Would you like to roll(R) or hold (H)? ")
            if player_choice == 'R':
                roll = self.die.roll()
                self.player1.score += roll
                ic(roll)
            ic(self.player1.score)
            
            print("")
            
        
        while self.player2.score <= 100:
            roll = self.die.roll()
            ic(roll, self.player2.score) 
            print("")
            self.player2.score += roll
            
        
        
#  #human vs computer moves
# # #create while loops 
#     def human_move(self):
#         while
#         score = 0
#         def computer_move(self):
# #         while 
# #         score = 0
                


        # (player1_score < 100 and player2_score < 100):
        #     player1_score = 0
        #     player2_score = 0 






def end_of_game():
    print("Thank you for playing the Momentum Pig Game!")
    

def main():
    greeting()
    end_of_game()
    new_game=Game()
    new_game.playgame()
    
    
main()