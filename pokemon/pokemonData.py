

quests = ['Find professor OAK', 'fill this in zac u idoit']

'''
class area:
    def __init__(self, locations):
        self.locations = locations
'''


class player:
    # create the class atributes of the player class
    def __init__(self):
        self.name = 'Red'
        self.health = 3
        self.stamina = 10
        self.location = bedroom
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


class mapLocation:
    def __init__(self, name, available, blockedMessage):
        self.name = name
        self.available = available
        self.blockedMessage = blockedMessage


bedroom = mapLocation('Bedroom', True, None)
livingRoom = mapLocation('Living room', True, None)
house = [bedroom, livingRoom]

profsLab = mapLocation('Oak Pokemon Research Lab', True, None)
consinsHouse = mapLocation("Cousins' House", True, None)
yourHouse = mapLocation('Your House', True, None)
mysteriousPath = mapLocation('Mysterious Path', True, None)
paletTown = [profsLab, consinsHouse, yourHouse, mysteriousPath]


class pokemon:
    def __init__(self, name, level, health, experience, possibleAttacks, attack, defense, speed, special):
        self.name = name
        self.level = level
        self.health = health
        self.experience = experience
        self.possibleAttacks = possibleAttacks
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special = special

    def battle(self):
        print("a wild", self.name, 'appeared')
        print('STATS:')
        print('LEVEL:', self.level)
        print('HEALTH:', self.health)


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
