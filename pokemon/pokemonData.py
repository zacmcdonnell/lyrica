import os
import random
quests = ['Find professor OAK', 'fill this in zac u idoit']

'''
class area:
    def __init__(self, locations):
        self.locations = locations
'''

tutorial = ['Hello there! Welcome to the world of POKEMON!',
            'This world is inhabited by creatures called POKEMON!',
            'My name is OAK! People call me the POKEMON PROF!',
            'For some people, POKEMON are pets',
            'Others use them for fights.',
            'Myself...',
            'I study POKEMON as a profession.',
            'But first, whats your name? ',
            'This is my grandson.',
            "He's been your rival since you were a baby.",
            '...Erm, what is his name again? ',
            "Your very own POKEMON legend is about to unfold!",
            'A world of dreams and adventures with POKEMON awaits!',
            "Let's go!"
            ]

livingRoomDialog = ['Right. All boys leave home one day',
                    'It said so on TV.',
                    'PROF OAK, next door is looking for you.']

mysteriousPathDialog = ["OAK: HEY WAIT, DON'T GO OUT ",
                        'Whew, That was close!',
                        'Wild pokemon live in tall grass']


class player:
    # create the class atributes of the player class
    def __init__(self):
        self.name = 'Red'
        self.health = 3
        self.stamina = 10
        self.location = 'bedroom'
        self.area = house
        self.completedQuests = 0
        self.currentQuest = quests[self.completedQuests]
        self.pokemons = []

    # define the move player method

    def quests(self, complete):
        if complete:
            self.completedQuests += 1
            print('\nCongrats, your next quest is',
                  quests[self.completedQuests])
            self.currentQuest = quests[self.completedQuests]


def bedroom():
    print('yeet')


def livingRoom():
    for i in range(len(livingRoomDialog)):
        print('----------', player1.location.upper(), '----------',)
        print('MUM:', livingRoomDialog[i])
        input()
        os.system('cls')

    print('YOU WALK OUTSIDE AND YOU EYES ARE BLINDED BY SUNLIGHT')
    input()
    print('----------PALET TOWN----------',)
    player1.area = paletTown
    print('SHADES OF YOUR JOURNEY AWAIT')


def profsLab():
    print('BLUE: Yo ' + player1.name + " Gramps isn't around?" +
          "\nI ran here cos' he said he had a pokemon for me.")


def cosinsHouse():
    print('----------', player1.location.upper(), '----------',)
    print("BLUES SISTER: Hi", player1.name + "! BLUE is out at Grandpa's lab.")


def yourHouse():
    player1.area = house
    player1.location = livingRoom


def mysteriousPath():
    for i in range(len(mysteriousPathDialog)):
        print('TALL GRASS SUROUNDS YOU\n')
        print('PROFFESSOR OAK:', mysteriousPathDialog[i])
        input()
        os.system('cls')
    print('now we attack')


house = {
    'living room': livingRoom,
    'bedroom': bedroom
}

paletTown = {
    'oak pokemon research lab': profsLab,
    "cousins' house": cosinsHouse,
    'your house': yourHouse,
    'mysterious path': mysteriousPath
}


class pokemon:
    def __init__(self, name, level, health, maxHealth, experience, possibleAttacks, attack, defense, speed, special):
        self.name = name
        self.level = level
        self.health = health
        self.maxHealth = maxHealth
        self.experience = experience
        self.possibleAttacks = possibleAttacks
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special = special

    def displayHealth(self, health, maxHealth):
        healthDashes = maxHealth
        # Get the number to divide by to convert health to dashes (being 10)
        dashConvert = int(maxHealth/healthDashes)
        # Convert health to dash count: 80/10 => 8 dashes
        currentDashes = int(health/dashConvert)
        # Get the health remaining to fill as space => 12 spaces
        remainingHealth = healthDashes - currentDashes
        # Convert 8 to 8 dashes as a string:   "--------"
        healthDisplay = '-' * currentDashes
        # Convert 12 to 12 spaces as a string: "            "
        remainingDisplay = ' ' * remainingHealth
        percent = str(int((health/maxHealth)*100)) + "%"
        # Print out textbased healthbar
        print("   -Health   : |" + healthDisplay + remainingDisplay + "|")
        print('                ', percent, 'remaining')

    def displayBattle(self):
        print('\n------------------------------------------------------')
        print(self.name.upper())
        print('\nSTATS:')
        print("   -LEVEL", self.level)
        self.displayHealth(self.health, self.maxHealth)


pikauchu = pokemon('pikauchu', 5, 19, 20, 0, [
                   "THUNDERSHOCK", "GROWL"], 12, 9, 15, 10)


currentPokemon = pikauchu


class enemyPokemon(pokemon):

    def fight(self):

        for i in currentPokemon.possibleAttacks:
            print(' -', i.upper())

        userInput = input("> ").lower()

        if userInput == 'thundershock':
            self.health -= 5
            print("DAMMMM U GOTEM GOOD")
            input()

    def options(self):
        global fight
        print('WHAT DO YOU DO?:')
        options = ['fight', 'run', 'item', 'switch']
        for i in options:
            print(' -', i.upper())

        userInput = input("> ").lower()

        if userInput == 'fight':
            self.fight()

        elif userInput == 'run':
            fight = False
            print('you got away saftley')
        elif userInput == 'item':
            # DO THIS SOON
            # showBackpack()
            print("SHOW BACKPACK FUNCTION")
        elif 'switch':
            # SHOW POKEMON
            print('SHOW POKEMON FUNCTION')

    def battle(self):
        global fight
        os.system('cls')

        fight = True
        print('A wild', self.name, 'has appeared')
        input('......')
        while fight:
            os.system('cls')
            currentPokemon.displayBattle()
            self.displayBattle()
            input('......')
            self.options()

    def chooseAttack(self):
        random.choice(self.possibleAttacks)


jojo = enemyPokemon('EEVEE', 5, 19, 20, 0, [
    "THUNDERSHOCK", "GROWL"], 12, 9, 15, 10)

jojo.battle()
player1 = player()


'''


class item:
    # define attributes for the item class
    def __init__(self, name, location, inBackpack):
        # attach to self construct for later use in the methods of the class
        self.what = 'item'
        self.name = name
        self.location = location
        self.inBackpack = inBackpack
        self.keywords()

# define isItem Method
    def isItem(self):
        # if the player is at the same location
        if self.location == player1.location:
            print("You see a", self.name, "here.")

    # define get method
    def getItem(self, verb):
        if verb in dropCommands:
            # if the item is in the backpack set it to false and display to user
            if self.inBackpack:
                self.inBackpack = False
                # change location to where the player dropped it
                self.location = player1.location
                print("The", self.name, "has been dropped")
            else:
                print("You can't drop something you don't have!")

        elif verb in collectCommands:
            # if the player location is the same as the item location and the item isn't in the backpack
            if player1.location == self.location and self.inBackpack == False:
                # put the item in the backpack
                self.inBackpack = True
                # display to user
                print("The", self.name, "has been added to your inventory")
            else:
                print("You can't take something thats not there")

    def keywords(self):
        # when an item object is created the function attaches the name to a list for later use
        return itemKeywords.append(self.name)
'''
