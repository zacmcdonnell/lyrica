locationMessage = ["stone keep", "well", "sunny glade", "sleeping dragon", "path",
                   "ancient gate", "river's edge", "wooden bench", "cottage",
                   "underground cave", "clif side", "desert", "snowy mountains",
                   "beach", "wood forest", "lake"]

blockedMessages = ["It's too dangerous to go that way.", "A mysterious force holds you back.",
                   "A tangle of thorns blocks your way.", "You can't step over the dragon."
                   "", "The gate locks shut.", "The river is too deep to cross.",
                   "The trees are too thick to pass.", "You're too scared to go that way.", "The path doesn't lead anywhere"]

weatherOptions = ['sunny', 'rainy', 'fine', 'windy', 'bushfires',
                  'tsunami', 'snow storm', 'icey winds', 'partly cloudy', 'thunderstorms', 'lighting']


moveCommands = ["go", "travel", "journey", "walk", "run"]
collectCommands = ["pickup", "take", "grab", "collect"]
dropCommands = ['drop', 'leave']

joiningWords = ['and', 'on', 'the']

verbs = []
verbs.extend(moveCommands)
verbs.extend(collectCommands)
verbs.extend(dropCommands)

startingLocations = [5, 6, 9, 10]


class movement:
    def __init__(self, keywords, restrictions, amountMoved):
        self.keywords = keywords
        self.restrictions = restrictions
        self.amountMoved = amountMoved


movements = {
    'north': movement(['north', 'up', 'forwards'], [0, 1, 2, 3], -3),
    'south': movement(['south', 'down', 'backwards'], [12, 13, 14, 15], 3),
    'east': movement(['east', 'right'], [3, 7, 11, 15], 1),
    'west': movement(['west', 'left'], [0, 4, 8, 12], -1)

}
