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
        # intialise the game and display welcome screen
        os.system('cls')
        print("-----------------WELCOME TO POKEMON----------------- \n")

        print(
            'PROFFESSOR OAK: Hello there! Welcome to the world of POKEMON! My name is OAK! People call me the POKEMON PROF!')
        print('This world is inhabited by creatures called POKEMON! For some',
              'people, POKEMON are pets. Others use them for fights. Myself... I study POKEMON as a profession.')
        player1.name = input('But first, whats your name? ')
        print('Right! So your name is', player1.name + '!')
        print(
            "\nThis is my grandson. He's been your rival since you were a baby.")
        cousin = player()
        cousin.name = input('...Erm, what is his name again? ')
        print("That's right! I remember now! His name is " + cousin.name + '!')
        print("Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!")
        self.hint = "to leave the bedroom, type 'go south'"
        self.verb = 'Go to:'

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
            for i in player1.area:
                if i.name != player1.location.name and i.name not in self.possibleActions:
                    self.possibleActions.append(i.name)
            self.getInput()

            for i in player1.area:
                if i.name in userInput and i.name in self.possibleActions:
                    player1.location = i
                    self.possibleActions = []

            if player1.location == livingRoom:
                print('You run into the living room')

                print('\nMUM: Right. All boys leave home one day ')
                print('Tt said so on TV.')
                print('PROF OAK, next door is looking for you.')

                print(
                    '\nYou walk outside and your eyes are blinded by the bright sunlight ')
                player1.area = paletTown
                print('\nPALET TOWN: SHADES OF YOUR JOURNEY AWAIT')

            if player1.location == profsLab:
                if profsLab.available:
                    print('yeet')
                else:
                    print('BLUE: Yo' + player1.name + "Gramps isn't around?" +
                          "\nI ran here cos' he said he had a pokemon for me.")

            if player1.location == mysteriousPath:
                print("OAK: HEY WAIT, DON'T GO OUT ")
                print('Whew, That was close!')
                print('Wild pokemon live in tall grass')


                # program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
