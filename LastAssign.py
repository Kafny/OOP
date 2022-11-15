#
# File: Assign2.py
# Descrition: All that Dice is a game designed and developed by Alan Turing. There are three games, Bunco, Maxi, and Odd and Even dice game. 
# Author: Nisha Kafley
# Student ID: 110373752
# Email ID: Kafny002
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 

'''The all_That_Dice class runs the game, this class accesses the player
class to add players to the game.'''
class allThatDice:
    '''The run method shows all the possible options. 
    The run method also validates the player input.
    '''
    def run():
        print("Welcome to All-That-Dice") 
        print("Developed by Alan Turning")
        print("COMP 1048 Object-Oriented Programming")

    '''This method will display all the options
    It will also prompt and validate user choices
    '''
    def menu():
        print("\nWhat would you like to do?")
        print("(r) register a new player")
        print("(s) show the leader board")
        print("(p) play a game")
        print("(q) quit")

         # prompts the player to choose an option
        userChoice = input("\nWhat would you like to do?")

        #validates the users choice 
        while userChoice != "r" and userChoice != "s" and userChoice != "p" and userChoice != "q":
            print("\nInvalid input - try again") 
            userChoice = input("What would you like to do [r, s, p, q]")

        # if the user chooses to exit the game, it will display a message
        if userChoice == "q":
            print("Thank you for playing All-That-Dice!")

        while (userChoice != 'q'):
            if (userChoice == 'r'):
                print("Registering a new user")
            elif (userChoice == 's'):
                print("Showing the leader board")
            elif (userChoice == 'p'):
                print("Playing a game")
            return userChoice

    '''This method will display all three game options. 
    It will also prompt the user to choose of the the option'''

    def gameOption():
        print("\nWhich game would you like to play?")
        print("(o) Odd-or-Even")
        print("(m) Maxi")
        print("(b) Bunco")

        choice = input("\nWhat would you like to do?")

        if choice == "o":
            pass

        elif choice == "m":
            pass

        if choice == "b":
           pass



'''This player class will register all the new players.
 playerList[] will add all the names of the new players into a list 
'''
class players:
    def __init__(self):
        self.playerList = []   


    '''This method prompts the player to enter the name
    It also validates if the new player name exists in playerList
    If the playerName exists, then the player is asked to re-enter'''
    
    def getPlayerName(self):
        newPlayer = input("\nWhat is the name of the new player? ")
        
        while newPlayer not in self.playerList:
            self.playerList.append(newPlayer)
            print("Welcome", newPlayer)
        newPlayer = input("\nWhat is the name of the new player? ")

        for newPlayer in self.playerList:
            print("Welcome", newPlayer)
    

        if newPlayer in self.playerList:
            print("\nSorry, the name is already taken")
    
'''Dice class is the parent class as all the other 3 games will inherit its attributes
'''
class diceGame:
    def __init__(self, players, minPlayers, maxPlayers, chipsToBid):
        self.players = players 
        self.minPlayers = minPlayers
        self.minPlayers = maxPlayers
        self.chipsToBid = chipsToBid
    
    '''This method will run the game'''
    def playGame(self):
        pass

    '''This method will prompt the player to place a bid'''
    def askToBid(self):
        pass

    '''This method will set the chips'''

    def setChips(self):
        pass 





'''played by 2-4 playees 
If the registered players are not enough, then an error message will display and players will be redirected to main menu
players name must match the registered name, if not error message will display and players are asked to re-enter thier name
Players will bid the chips'''

class bunco():
    pass 


'''played by 3-5 players 
Each player will roll a pair of dice
The player with the higest number of face up values of the dice will win the game 
If both players have the same higest die value, then they will play the game again'''

class maxi():
    pass




'''Odd or Even only has 1 player
The player has to guess if the die will be odd or even.
If the player's guess corrosponds with the die, then the player wins'''

#r
# class oddOrEven():

    
    #def __init__(self, guess):
        #self.__guess = guess 
    
    #def getGuess(self):
        
        
        

            


# Leaderboard class will show the results which inclues the namee, games played, won, and chips. 
# class leaderboard:
    #def __init__(self, Playername, gamePlayed, gameWon, chips):
        #self.playerName = Playername 
        #self.gamePlayed = gamePlayed
        #self.gameWon = gameWon
        #self.chips = chips
    
    


#class Die:
    #pass


atd = allThatDice
atd.run()

atd.menu()

p = players()
p.getPlayerName()


atd.gameOption()


