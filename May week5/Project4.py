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
class Player:
  def __init__(self,player):
		self.player = player
	def dice_roll(self):
		self.start = 1
		self.current_position = 1
		self.random_roll = rd.randint(1,6)
class Board:
	def __init__(self,position_of_snakes,position_of_ladders):
		self.position_of_snakes = position_of_snakes
		self.position_of_ladders = position_of_ladders
		
  





