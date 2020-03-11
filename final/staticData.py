locationMessage = ["stone keep", "well", "sunny glade", "sleeping dragon", "path",
                   "ancient gate", "river's edge", "wooden bench", "cottage",
                   "underground cave", "clif side", "desert", "snowy mountains",
                   "beach", "wood forest", "lake"]

blockedMessages = ["It's too dangerous to go that way.", "A mysterious force holds you back.",
                   "A tangle of thorns blocks your way.", "You can't step over the dragon."
                   "", "The gate locks shut.", "The river is too deep to cross.",
                   "The trees are too thick to pass.", "You're too scared to go that way.", "The path doesn't lead anywhere"]

restrictionList = [[0, 1, 2, 3], [12, 13, 14, 15],
                   [3, 7, 11, 15], [0, 4, 8, 12]]

amountMovedList = [-3, 3, 1, -1]

weatherOptions = ['sunny', 'rainy', 'fine', 'windy', 'bushfires',
                  'tsunami', 'snow storm', 'icey winds', 'partly cloudy', 'thunderstorms', 'lighting']

itemKeywords = []

moveKeywords = {
    'northKeywords': ['north', 'up', 'forwards'],
    'southKeywords': ['south', 'down', 'backwards'],
    'eastKeywords': ['east', 'right'],
    'westKeywords': ['west', 'left']
}
moveCommands = ["go", "travel", "journey", "walk", "run"]
collectCommands = ["pickup", "take", "grab", "collect"]
dropCommands = ['drop', 'leave']

joiningWords = ['and', 'on', 'the']

verbs = []
verbs.extend(moveCommands)
verbs.extend(collectCommands)
verbs.extend(dropCommands)

startingLocations = [5, 6, 9, 10]
