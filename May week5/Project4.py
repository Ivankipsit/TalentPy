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


#Player class
class Player:
  start = 0
	def __init__(self,player):
		self.player = player
	
	def dice_roll(self):
		self.current_position = start
		return  rd.randint(1,6)

#Board class
class Board:
	play_board = [i for i in range(1,101)]
	
	def __init__(self,position_of_snakes,position_of_ladders):
		self.position_of_snakes = position_of_snakes
		self.position_of_ladders = position_of_ladders
	
	def is_snake(current_position):
		heads = list(self.position_of_snakes.keys())
		tails = list(self.position_of_snakes.values())
		if self.current_position in heads:
			return True
		else:
			return False
		
	def go_down(current_position):
		heads = list(self.position_of_snakes.keys())
		tails = list(self.position_of_snakes.values())
		add_list = [(heads[i]-tails[i])  for i in range(len(heads))]
		
		for ele in heads:
			if self.current_position == ele:
				from_index = heads.index(ele)
				self.current_position += add_list[from_index]
		
		return self.current_position
	
	def is_ladder(current_position):
		bottom = list(self.position_of_ladders.keys())
		top = list(self.position_of_ladders.values())
		if self.current_position in bottom:
			return True
		else:
			return False
		
	def climb_ladder(current_position):
		bottom = list(self.position_of_ladders.keys())
		top = list(self.position_of_ladders.values())
		add_list = [(bottom[i]-top[i])  for i in range(len(bottom))]
		
		for ele in bottom:
			if self.current_position == ele:
				from_index = bottom.index(ele)
				self.current_position += add_list[from_index]
		
		return self.current_position
	
#Game Sub-Class for Board.
class Game(Board,Player):
	def start_game(self):
		while (self.current_position == 100) == False:
			if self.current_position < 100:
				dice_roll()
				#print(dice_roll())
				self.current_position += dice_roll
				if is_snake(self.current_position) == True:
					go_down(self.current_position)
				if is_ladder(self.current_position) == True:
					climb_ladder(self.current_position)
			if self.current_position > 100:
				self.current_position -= dice_roll
		else:
			print("We have a WINNER")
				
		
	"""
	reserve code
	import random as rd


#Player class
class Player:
    start = 0
    def __init__(self,player):
        self.player = player
        print("Running Player __init__")
    
    def dice_roll(self):
        self.current_position = start
        return  rd.randint(1,6)
        print("Running Player dice_roll")

#Board class
class Board:
    play_board = [i for i in range(1,101)]
    
    def __init__(self,position_of_snakes,position_of_ladders):
        self.position_of_snakes = position_of_snakes
        self.position_of_ladders = position_of_ladders
        print("Running Board __init__")
    
    def is_snake(current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        if self.current_position in heads:
            return True
        else:
            return False
        print("Running Board is_snake")
        
    def go_down(current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        add_list = [(heads[i]-tails[i])  for i in range(len(heads))]
        
        for ele in heads:
            if self.current_position == ele:
                from_index = heads.index(ele)
                self.current_position += add_list[from_index]
        
        return self.current_position
        print("Running Board go_down")
    def is_ladder(current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        if self.current_position in bottom:
            return True
        else:
            return False
        print("Running Board is_ladder")
    def climb_ladder(current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        add_list = [(bottom[i]-top[i])  for i in range(len(bottom))]
        
        for ele in bottom:
            if self.current_position == ele:
                from_index = bottom.index(ele)
                self.current_position += add_list[from_index]
        
        return self.current_position
        print("Running Board climb_ladder")
#Game Sub-Class for Board.
class Game(Board,Player):
    def start_game(self):
        print(self.Current_position)
        while (Player.self.current_position == 100) == False:
            if self.current_position < 100:
                dice_roll()
                #print(dice_roll())
                self.current_position += dice_roll
                if is_snake(self.current_position) == True:
                    go_down(self.current_position)
                if is_ladder(self.current_position) == True:
                    climb_ladder(self.current_position)
            if self.current_position > 100:
                self.current_position -= dice_roll
        else:
            return "We have a WINNER" 
        print("Running Game")    
#objA1            
player_1 = Player("Hari")
#objB1
player_2 = Player("Ganesh")
#objA2
position_of_snakes = {5: 1, 35 : 3}
#objB2
position_of_ladders = {7 : 81, 41 : 53}

board_ok = Board(position_of_snakes, position_of_ladders)
player_1.Game(Player,Board)
	"""
		
		
  





