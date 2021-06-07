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

#improved
import random as rd
import sys


#Player class

class Player:

    def __init__(self, player, current_position = 1):
        self.player = player
        self.current_position = current_position
 #       print("Running Player __init__")

    def dice_roll(self):
 #       print("Running Player dice_roll")
  #      print("roll count ----------")
        a = rd.randint(1,6)
        print("random roll = ",a)
        return  a
    
#Board class
class Board(Player):
    
    def __init__(self,position_of_snakes,position_of_ladders,class_player):
        self.position_of_snakes = position_of_snakes
        self.position_of_ladders = position_of_ladders
        self.current_position = class_player.current_position
  #      print("Running Board __init__")
        
    
    def is_snake(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
  #      print("Running Board is_snake")
  #      print(current_position)
        if current_position in heads:
            print("True")
            return True
        else:
            return False
        
    def go_down(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
#        print("Running Board go_down")
 #       print(current_position)
        
        for ele in heads:
            if current_position == ele:
                from_index = heads.index(ele)
                current_position = tails[from_index]
                return current_position
        return current_position
    
    def is_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
 #       print("Running Board is_ladder")
#        print(current_position)
        if current_position in bottom:
            return True
            print("True")
        else:
            return False
        
    def climb_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
  #      print("Running Board climb_ladder")
  #      print(current_position)
        
        for ele in bottom:
            if current_position == ele:
                from_index = bottom.index(ele)
                current_position = top[from_index]
                return current_position
        return current_position
    
#Game Sub-Class for Board.
class Game(Board,Player):
    def __init__(self,class_player, class_board):
        self.player = class_player.player
        self.current_position = class_player.current_position
        self.position_of_snakes = class_board.position_of_snakes
        self.position_of_ladders = class_board.position_of_ladders
        self.current_position = class_board.current_position
        
   #     print("Running Game __init__")
    
    def start_game(class_player,class_board):
#        print("Running Game Class")
#        print(class_player.player, class_player.current_position)
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

                print("----------------------------------1")

            else:#lesser tha 100
                b = class_player.dice_roll()
                class_player.current_position += b 
                
                print("{} Position after roll == {}".format(class_player.player,class_player.current_position))
                if class_board.is_snake(class_player.current_position) == True:
                    class_board.go_down(class_player.current_position)
                    return class_player.current_position                    
                if class_board.is_ladder(class_player.current_position) == True:
                    class_board.climb_ladder(class_player.current_position)
                    return class_player.current_position                
                if class_player.current_position == 100:
                    print("We have a WINNER", class_player.player) 
                    sys.exit() 
                if class_player.current_position > 100:
                    class_player.current_position -= b
                    
                    if class_player.current_position == 100:
                        print("We have a WINNER", class_player.player)
                        sys.exit()
                print("----------------------------------2")


#player_details               
player_1 = Player("P1 --> Hari")
player_2 = Player("P2 --> Ganesh")
#board_details
position_of_snakes = {5: 1, 35 : 3}
position_of_ladders = {7 : 81, 41 : 53}
board_1 = Board(position_of_snakes, position_of_ladders, player_1)
board_2 = Board(position_of_snakes, position_of_ladders, player_2)
#game_details
Game(player_1,board_1)
Game(player_2,board_2)

for k in range(300):
   if k%2 == 0:
       game_1 = Game.start_game(player_1, board_1)

   else:
       game_2 = Game.start_game(player_2, board_2)









"""
import random as rd
import sys


#Player class

class Player:

    def __init__(self, player, current_position = 1):
        self.player = player
        self.current_position = current_position
 #       print("Running Player __init__")

    def dice_roll(self):
 #       print("Running Player dice_roll")
  #      print("roll count ----------")
        a = rd.randint(1,6)
        print("random roll = ",a)
        return  a
    
#Board class
class Board(Player):
    
    def __init__(self,position_of_snakes,position_of_ladders,class_player):
        self.position_of_snakes = position_of_snakes
        self.position_of_ladders = position_of_ladders
        self.current_position = class_player.current_position
  #      print("Running Board __init__")
        
    
    def is_snake(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
  #      print("Running Board is_snake")
   #     print(current_position)
        if current_position in heads:
            return True
        else:
            return False
        
    def go_down(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
#        print("Running Board go_down")
#        print(current_position)
        
        for ele in heads:
            if current_position == ele:
                from_index = heads.index(ele)
                current_position = tails[from_index]
                return current_position
        return current_position
    
    def is_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
 #       print("Running Board is_ladder")
 #       print(current_position)
        if current_position in bottom:
            return True
        else:
            return False
        
    def climb_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
  #      print("Running Board climb_ladder")
  #      print(current_position)
        
        for ele in bottom:
            if current_position == ele:
                from_index = bottom.index(ele)
                current_position = top[from_index]
                return current_position
        return current_position
    
#Game Sub-Class for Board.
class Game(Board,Player):
    def __init__(self,class_player, class_board):
        self.player = class_player.player
        self.current_position = class_player.current_position
        self.position_of_snakes = class_board.position_of_snakes
        self.position_of_ladders = class_board.position_of_ladders
        self.current_position = class_board.current_position
        
   #     print("Running Game __init__")
    
    def start_game(class_player,class_board):
#        print("Running Game Class")
 #       print(class_player.player, class_player.current_position)
        print("{} Position rn == {}".format(class_player.player,class_player.current_position)) #--------------------
        if class_player.current_position == 100:
            print("We have a WINNER")
            sys.exit()

        if class_player.current_position != 100:
            if class_player.current_position > 100:
                print(class_player.player, class_player.current_position)
                class_player.current_position -= class_player.dice_roll()
                print("{} Position after roll == {}".format(class_player.player,class_player.current_position)) 
                if class_player.current_position == 100:
                    print("We have a WINNER", class_player.player)
                    sys.exit()
                print("----------------------------------1")

            else:
                class_player.current_position += class_player.dice_roll()
                print("{} Position after roll == {}".format(class_player.player,class_player.current_position)) 
                print("----------------------------------2")
                if class_player.current_position == 100:
                    print("We have a WINNER", class_player.player)
                    sys.exit()
                if class_player.current_position > 100:
                    class_player.current_position -= class_player.dice_roll()
                if class_board.is_snake(class_player.current_position) == True:
                    class_board.go_down(class_player.current_position)
                    
                if class_board.is_ladder(class_player.current_position) == True:
                    class_board.climb_ladder(class_player.current_position)
                    class_player.current_position = class_player.dice_roll()
                    print("{} Position after roll == {}".format(class_player.player,class_player.current_position))
                    print("----------------------------------3")              ​
               ​

#player_details               
player_1 = Player("P1 --> Hari")
player_2 = Player("P2 --> Ganesh")
#board_details
position_of_snakes = {5: 1, 35 : 3}
position_of_ladders = {7 : 81, 41 : 53}
board_1 = Board(position_of_snakes, position_of_ladders, player_1)
board_2 = Board(position_of_snakes, position_of_ladders, player_2)
#game_details
Game(player_1,board_1)
Game(player_2,board_2)

for k in range(300):
   if k%2 == 0:
       game_1 = Game.start_game(player_1, board_1)

   else:
       game_2 = Game.start_game(player_2, board_2)

    

"""
#unusable
"""
import random as rd

#Player class
class Player:

    def __init__(self, player, current_position = 1):
        self.player = player
        self.current_position = current_position
        print("Running Player __init__")
    
    def dice_roll(self,i = 0):
        print("Running Player dice_roll")
        i+=1
        print("roll count",i)
        a = rd.randint(1,6)
        print("random roll = ",a)
        return  a

#Board class
class Board:
    
    def __init__(self,position_of_snakes,position_of_ladders):
        self.position_of_snakes = position_of_snakes
        self.position_of_ladders = position_of_ladders
        print("Running Board __init__")
        
    
    def is_snake(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        print("Running Board is_snake")
        print(current_position)
        if current_position in heads:
            return True
        else:
            return False
        
    def go_down(self, current_position):
        heads = list(self.position_of_snakes.keys())
        tails = list(self.position_of_snakes.values())
        add_list = [(heads[i]-tails[i])  for i in range(len(heads))]
        print("Running Board go_down")
        print(current_position)
        
        for ele in heads:
            if current_position == ele:
                from_index = heads.index(ele)
                current_position += add_list[from_index]
        
        return current_position
    
    def is_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        print("Running Board is_ladder")
        print(current_position)
        if current_position in bottom:
            return True
        else:
            return False
        
    def climb_ladder(self, current_position):
        bottom = list(self.position_of_ladders.keys())
        top = list(self.position_of_ladders.values())
        add_list = [(bottom[i]-top[i])  for i in range(len(bottom))]
        print("Running Board climb_ladder")
        print(current_position)
        
        for ele in bottom:
            if current_position == ele:
                from_index = bottom.index(ele)
                current_position += add_list[from_index]
        
        return current_position
    
#Game Sub-Class for Board.
class Game(Board,Player):
    def __init__(self,class_player, class_board):
        self.player = class_player.player
        self.current_position = class_player.current_position
        self.position_of_snakes = class_board.position_of_snakes
        self.position_of_ladders = class_board.position_of_ladders
        
        print("Running Game __init__")
    
    def start_game(class_player,class_board):
        print("Running Game Class")
        while (class_player.current_position == 100) == False:
            print(class_player.current_position)
            if class_player.current_position < 100:
                class_player.current_position += class_player.dice_roll()
                if class_board.is_snake(class_player.current_position) == True:
                    class_board.go_down(class_player.current_position)
                if class_board.is_ladder(class_player.current_position) == True:
                    class_board.climb_ladder(class_player.current_position)
            if class_player.current_position > 100:
                print(class_player.current_position)
                class_player.current_position -= class_player.dice_roll()
        else:
            print("We have a WINNER")
                
                
                
                
player_1 = Player("Hari")

player_2 = Player("Ganesh")

position_of_snakes = {5: 1, 35 : 3}

position_of_ladders = {7 : 81, 41 : 53}

board_1 = Board(position_of_snakes, position_of_ladders)
print(player_1.dice_roll()) 
Game(player_1,board_1)
game_1 = Game.start_game(player_1, board_1)
"""
"""
import random as rd


#Player class
class Player:

	def __init__(self, player, current_position = 0):
		self.player = player
		self.current_position = current_position
		print("Running Player __init__")
	
	def dice_roll(self):
		print("Running Player dice_roll")
		return  rd.randint(1,6)

#Board class
class Board:
	
	def __init__(self,position_of_snakes,position_of_ladders):
		self.position_of_snakes = position_of_snakes
		self.position_of_ladders = position_of_ladders
		print("Running Board __init__")
		
	
	def is_snake(self, current_position):
		heads = list(self.position_of_snakes.keys())
		tails = list(self.position_of_snakes.values())
		print("Running Board is_snake")
		if current_position in heads:
			return True
		else:
			return False
		
	def go_down(self, current_position):
		heads = list(self.position_of_snakes.keys())
		tails = list(self.position_of_snakes.values())
		add_list = [(heads[i]-tails[i])  for i in range(len(heads))]
		print("Running Board go_down")
		
		for ele in heads:
			if current_position == ele:
				from_index = heads.index(ele)
				current_position += add_list[from_index]
		
		return current_position
	
	def is_ladder(self, current_position):
		bottom = list(self.position_of_ladders.keys())
		top = list(self.position_of_ladders.values())
		print("Running Board is_ladder")
		if current_position in bottom:
			return True
		else:
			return False
		
	def climb_ladder(self, current_position):
		bottom = list(self.position_of_ladders.keys())
		top = list(self.position_of_ladders.values())
		add_list = [(bottom[i]-top[i])  for i in range(len(bottom))]
		print("Running Board climb_ladder")
		
		for ele in bottom:
			if current_position == ele:
				from_index = bottom.index(ele)
				current_position += add_list[from_index]
		
		return current_position
	
#Game Sub-Class for Board.
class Game(Board,Player):
	def start_game(self):
		print("Running Game Class")
		while (self.current_position == 100) == False:
			if self.current_position < 100:
				self.current_position += Player.dice_roll(self)
				if Board.is_snake(self, self.current_position) == True:
					Board.go_down(self, self.current_position)
				if Board.is_ladder(self, self.current_position) == True:
					Board.climb_ladder(self, self.current_position)
			if self.current_position > 100:
				self.current_position -= Player.dice_roll(self)
		else:
			print("We have a WINNER")
				
				
				
				
player_1 = Player("Hari")

player_2 = Player("Ganesh")

position_of_snakes = {5: 1, 35 : 3}

position_of_ladders = {7 : 81, 41 : 53}

start = 0
board = Board(position_of_snakes, position_of_ladders)
print(player_1.dice_roll()) 
"""

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
		
		
  





