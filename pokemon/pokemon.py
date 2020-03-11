import random
import os
# import static data to delcutter main file
from pokemonData import *

'''
MAKE POKEMON MUSIC PLAY
'''


class Game:
    # define attributes for the NPC class
    def __init__(self):
        self.gamePlaying = True
        self.possibleActions = []
        self.start()
        self.gameMessage = 'You jump out of bed and rush into the living room'

    def start(self):
        global player1
        # intialise the game and display welcome screen
        os.system('cls')
        print("-----------------WELCOME TO POKEMON----------------- \n")

        print(
            'PROFFESSOR OAK: Hello there! Welcome to the world of POKEMON! My name is OAK! People call me the POKEMON PROF!')
        print('This world is inhabited by creatures called POKEMON! For some',
              'people, POKEMON are pets. Others use them for fights. Myself... I study POKEMON as a profession.')
        player1 = player()
        player1.name = input('But first, whats your name? ')
        print('Right! So your name is', player1.name + '!')
        print(
            "\nThis is my grandson. He's been your rival since you were a baby.")
        cousin = player()
        cousin.name = input('...Erm, what is his name again? ')
        print("That's right! I remember now! His name is " + cousin.name + '!')
        print("Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!")
        self.hint = "to leave the bedroom, type 'go south'"
        self.whereTo()

        # create the player object

        # create the game objects and describe the location

   # handle the user input
    def getInput(self):
        global userInput
        print()
        print(self.verb)
        for i in self.possibleActions:
            print(' -', i)

        userInput = input("> ").lower()
        os.system('cls')
        return userInput

    def MainGame(self):
        while True:
            self.getInput()
            if player1.location == bedroom:
                if userInput == 'living room':
                    print(self.gameMessage)
                    player1.location = livingRoom
                else:
                    print("That action wasn't vaild")

            if player1.location == livingRoom:
                print('\nMUM: Right. All boys leave home one day ')
                print('Tt said so on TV.')
                print('PROF OAK, next door is looking for you.')
                player1.area = paletTown

                self.whereTo()
                if userInput == 'mysterious path':
                    print("PROF: WAIT UP MY DUDEEE")
                else:
                    print("That action wasn't vaild")

    def whereTo(self, area):
        self.verb = 'Go to:'
        for i in player1.area:
            if i.available and i != player1.location:
                self.possibleActions.append(i.name)


        # program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
