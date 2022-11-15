#
# File: Assign2.py
# Descrition: All that Dice is a game designed and developed by Alan Turing. There are three games, Bunco, Maxi, and Odd and Even dice game. 
# Author: Nisha Kafley
# Student ID: 110373752
# Email ID: Kafny002
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 


class all_That_Dice:
    def run():
        print("Welcome to All-That-Dice") 
        print("Developed by Alan Turning")
        print("COMP 1048 Object-Oriented Programming")
        
        print("\nWhat would you like to do?")
        print("(r) register a new player")
        print("(s) show the leader board")
        print("(p) play a game")
        print("(q) quit")
        #made changes

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

# This player class will register all the new players 
# playerList[] will add all the names of the new players into a list 

class players:
    def __init__(self):
        self.playerList = []   

    def getPlayerName(self):
        newPlayer = input("\nWhat is the name of the new player? ")
        # validates if the new player name exists in playerList
        # if the playerName exists, then the player is asked to re-enter their name

        
        while newPlayer not in self.playerList:
            self.playerList.append(newPlayer)
            print("Welcome", newPlayer)
        newPlayer = input("\nWhat is the name of the new player? ")

        for newPlayer in self.playerList:
            print("Welcome", newPlayer)
        

        if newPlayer in self.playerList:
            print("\nSorry, the name is already taken")
            


atd = all_That_Dice
atd.run()

p = players()
p.getPlayerName()


