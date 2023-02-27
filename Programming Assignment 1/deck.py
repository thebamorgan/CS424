from cards import *
from players import *
import random

#4 cards
#explodingKitten, favor, attack, shuffle, skip, cattermelon, tacocat, hairycat, rainbowcat, beardcat

#5 cards
#future, nope, 
class deck:
    def build(self):
        play = players()
        self.deck = []
        self.deck += (
            4 * hairyCat +
            4 * favor +
            4 * shuffle +
            4 * skip +
            4 * catterMelon +
            4 * tacoCat +
            4 * hairyCat +
            4 * rainbowCat +
            4 * beardCat +
            5 * seeFuture + 
            5 * nope + 
           1 (6 - play.count) * [defuse] + 
            (play.count - 1) * [explodingKitten]
        )

    def shuffle(self):
        random.shuffle(self.deck)





