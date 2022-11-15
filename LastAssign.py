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

        # prompts the player to choose an option
        userChoice = input("\nWhat would you like to do?")

        #validates the users choice 
        while userChoice != "r" and userChoice != "s" and userChoice != "p" and userChoice != "q":
            print("\nInvalid input - try again") 
            userChoice = input("What would you like to do [r, s, p, q]")

        # if the user chooses to exit the game, it will display a message
        if userChoice == "q":
            print("Thank you for playing All-That-Dice!")

        return userChoice
            
# This player class will register all the new players 
# playerList[] will add all the names of the players into a list 
# If the new player name is already registered, it will display a message and the player will be asked to re-enter the name

class players:
    playerList = []
    def __init__(self, playerName):
        self.__playerName = playerName
        
    def getPlayerName(self):
        input("What is the name of the new player? ")
        
        #self.__playerName.append[]






atd = all_That_Dice
atd.run()

