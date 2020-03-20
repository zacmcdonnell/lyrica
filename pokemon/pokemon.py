import random
import os
# import static data to delcutter main file
from pokemonData import *

'''
MAKE POKEMON MUSIC PLAY
'''


class Game:
    def __init__(self):
        self.gamePlaying = True

    def start(self):
        # intialise the game and display welcome screen
        os.system('cls')

        for i in range(len(tutorial)):
            # print(i)
            print("-----------------WELCOME TO POKEMON----------------- \n")
            print('PROFFESSOR OAK:', tutorial[i])
            if i == 7:
                player1.name = input('> ')
                print('Right! So your name is ' + player1.name + '!')

            elif i == 10:
                cousin = player()
                cousin.name = input()
                print("That's right! I remember now! His name is " +
                      cousin.name + '!')
            input()
            os.system('cls')

    def MainGame(self):
        os.system('cls')

        while True:
            if self.movePlayer():
                os.system('cls')
                print("You have arrived at the", player1.location)
                input('.....')
                os.system('cls')
                player1.area.get(player1.location)()
                input('.....')

            else:
                os.system('cls')

    def movePlayer(self):
        print('Go To:')
        for i in player1.area:
            if i != player1.location:
                print(' -', i)
        userInput = input("> ").lower()
        for i in player1.area:
            if userInput == i:
                player1.location = i
                return True


# program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
