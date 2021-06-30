'''Two players are trying to reach 100 points first.
On a player's turn, they roll a die over and over until they roll a 1 (a "pig") or they choose to hold.
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

import random 

score = 0 
maxscore = 100

def main():
    greeting()
    game=PIG()
    game.play()
    end_of_game()
    
 
def greeting(): 
    print("Welcome to the Momentum Pig Game?") 

#the first player is chosen randomly
player = ["human_player", "computer_player"]
print(random.choice(player))
    
class Player:
#defines player1 which is human_player and Player2 which is computer_player  
    def__init__(self,title, human_player = False):
        self.name=title
        self.is_human = human_player
        self.score = 0
        self.die = Die(6)

   #human vs computer moves
   #create while loops 
    def human_move(self):
        score = 0
    def computer_move(self):
        score = 0
class Die:
    
    def__init__(self,n=6)
        self.sides=n
        self.roll()
        
    def roll(self):
        self.die_face
        
'''def playgame(): 
    while (player1_score < 100 and player2_score < 100):
    player1_score = 0
    player2_score = 0'''  
        
        
        
        
        '''player1dice=random.randrange(1,6)
        Player1 = player1dice
        print("Player 1 dice 1 =",player1dice)
        print("Does player 1 want to roll or hold?")
        choose1 = input("Enter y for yes or n for no.")
        if(choose1=="n"):
            print("Player 1 dice 1 =",player1dice)
            print("Player 1 dice 2 =",player1dice2)
            print("Player 1 dice total =",Player1)
            print("Does player 1 want to hold?")
            choose1 = input("Enter y for yes or n for no.")
        elif(choose1=="y"):

            print("It's player 2's turn.")
            print("Player 2 dice 2 =",player2dice)
            print("Player 2 dice 2 =",player2dice2)
            print("Player 2 dice total =",Player2)
            print("Does player 2 want to hold?")
            choose2 = input("Enter y for yes or n for no.")'''
 
        





def end_of_game():
    print("Thank you for playing the Momentum Pig Game!")
    
main()