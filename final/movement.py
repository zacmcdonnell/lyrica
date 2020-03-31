class movement:

    def __init__(self, keywords, restrictions, amountMoved):
        self.keywords = keywords
        self.restrictions = restrictions
        self.amountMoved = amountMoved

    @staticmethod
    def movePlayer(player, restriction, amountMoved):
        # if the player location is not in the restrictions
        if player.location not in restriction:
            # then move the player by the specified amount
            player.location += amountMoved
            # call the describle location method inside the gameMap class
            return True

    @staticmethod
    def goWhere(direction, returnValues):
        # set a count
        # loop through the moveKeywords dictionary keys
        for i in movements.values():
            # check if the direction is in the current key's value
            if direction in i.keywords:
                # return restriction and amount based off current dictonary item looping order
                if returnValues == True:
                    return i.restrictions, i.amountMoved
                else:
                    return True
                # add one to the count


movements = {
    'north': movement(['north', 'up', 'forwards'], [0, 1, 2, 3], -3),
    'south': movement(['south', 'down', 'backwards'], [12, 13, 14, 15], 3),
    'east': movement(['east', 'right'], [3, 7, 11, 15], 1),
    'west': movement(['west', 'left'], [0, 4, 8, 12], -1)

}
