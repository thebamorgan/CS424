class players:
    playerCount = 0

    def __init__(self):
        self.count = int(input('How many players are playing?:\t'))

    def printCount(self):
        print(self.count)