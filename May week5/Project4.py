"""
Create following classes
1. Player class
2. Board class
3. Game class

Board Class:
1. Constructor which takes positions_of_snakes (dictionary where head is key, tail is value),
positions_of_ladders (dictionary where key is start of ladder, value is end of ladder)
2. Method is_snake(position) -> Return True if it is snake box else return False.
3. Method is_ladder(position) -> Return True if it is ladder box else return False.
4. Method climb_ladder(ladder_start_box) -> Return the respective index to jump using
position_of_ladders.
5. Method go_down(snake_position) -> Return the respective index to go down using
positions_of_snakes.

Player Class:
1. Constructor which takes name of player, initialise current position as 1 (as player need to
start from 1)
2. roll_dice() method, which will roll dice, on rolling dice it should return random number
between 1 to 6.

Game Class:
1. Create a method start_game() inside which create 2 player objects (say player_1 and
player_2) and board class.
2. Put a while loop and check whether any of the player reaches the box 100, if not continue
the loop, roll dice for player_1, player_2, player_1, player_2 and so on….(check for snake
and ladders using Board class and perform ups and downs accordingly) Until any one
player reaches the box 100. If reached 100, print the winner declaration. Saying “Player
<Player name> wins the game!”.
3. Note that: If player is in 96th box, and his roll gives 5 then 96+5 = 101 (Invalid) at this time,
you should not declare him as winner! He has to exactly to go to 100th box to become
winner.
"""

import random as rd
import sys
class Player:
    def __init__(self, player, current_position = 1):
        self.player = player
        self.current_position = current_position
    def dice_roll(self):
        a = rd.randint(1,6)
        print("random roll = ",a)
        return  a
class Board(Player): 
    def __init__(self,position_of_snakes,position_of_ladders,class_player):
        self.position_of_snakes = position_of_snakes
        self.position_of_ladders = position_of_ladders
        self.current_position = class_player.current_position
    def is_snake(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        if current_position in heads:
            return True
        else:
            return False  
    def go_down(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        for ele in heads:
            if current_position == ele:
                from_index = heads.index(ele)
                self.current_position = tails[from_index]
                print("Encountered snake at {} and moved to {}".format(current_position,self.current_position))
                return self.current_position
    def is_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        if current_position in bottom:
            return True
        else:
            return False
    def climb_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        for ele in bottom:
            if current_position == ele:
                from_index = bottom.index(ele)
                self.current_position = top[from_index]
                print("Encountered ladder at {} and moved to {}".format(current_position,self.current_position))
                return self.current_position
class Game(Board,Player):
    def __init__(self,class_player, class_board):
        self.player = class_player.player
        self.current_position = class_player.current_position
        self.position_of_snakes = class_board.position_of_snakes
        self.position_of_ladders = class_board.position_of_ladders
        self.current_position = class_board.current_position
    def start_game(class_player,class_board):
        print("{} Position rn == {}".format(class_player.player,class_player.current_position)) #--------------------
        if class_player.current_position == 100:
            print("We have a WINNER")
        if class_player.current_position != 100:
            if class_player.current_position > 100:
                print(class_player.player, class_player.current_position)
                class_player.current_position -= class_player.dice_roll()
                print("{} Position after roll == {}".format(class_player.player,class_player.current_position)) 
                if class_player.current_position == 100:
                    print("We have a WINNER", class_player.player)
                print("----------------------------------")
            else:#lesser tha 100
                b = class_player.dice_roll()
                class_player.current_position += b 
                print("{} Position after roll == {}".format(class_player.player,class_player.current_position))
                if class_board.is_snake(class_player.current_position) == True:
                    class_board.go_down(class_player.current_position)
                    class_player.current_position = class_board.current_position
                if class_board.is_ladder(class_player.current_position) == True:
                    class_board.climb_ladder(class_player.current_position)
                    class_player.current_position = class_board.current_position                
                if class_player.current_position == 100:
                    print("We have a WINNER", class_player.player) 
                    sys.exit() 
                if class_player.current_position > 100:
                    class_player.current_position -= b
                    if class_player.current_position == 100:
                        print("We have a WINNER", class_player.player)
                        sys.exit()
                print("----------------------------------")            


player_1 = Player("P1 --> Hari")
player_2 = Player("P2 --> Ganesh")
position_of_snakes = {5: 2, 35 : 3}
position_of_ladders = {7 : 81, 41 : 53}
board_1 = Board(position_of_snakes, position_of_ladders, player_1)
board_2 = Board(position_of_snakes, position_of_ladders, player_2)
Game(player_1,board_1)
Game(player_2,board_2)
for k in range(300):
   if k%2 == 0:
       game_1 = Game.start_game(player_1, board_1)
   else:
       game_2 = Game.start_game(player_2, board_2)
