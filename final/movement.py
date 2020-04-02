from player import player


class movement(player):

    def __init__(self, keywords, restrictions, amountMoved):
        self.keywords = keywords
        self.restrictions = restrictions
        self.amountMoved = amountMoved

    def goWhere(self, direction, returnValues):
        # set a count
        # loop through the moveKeywords dictionary keys
        for i in movements.values():
            # check if the direction is in the current key's value
            if direction in i.keywords:
                # return restriction and amount based off current dictonary item looping order
                if returnValues == True:
                    self.movePlayer(i.restrictions, i.amountMoved)
                    return True
                else:
                    return True
                # add one to the count


movements = {
    'north': movement(['north', 'up', 'forwards'], [0, 1, 2, 3], -3),
    'south': movement(['south', 'down', 'backwards'], [12, 13, 14, 15], 3),
    'east': movement(['east', 'right'], [3, 7, 11, 15], 1),
    'west': movement(['west', 'left'], [0, 4, 8, 12], -1)

}
