from classes import *
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
            4 * [cards.attack()] +
            4 * [cards.favor()] +
            4 * [cards.shuffle()] +
            4 * [cards.skip()] +
            4 * [catCards.cattermelon()] +
            4 * [catCards.tacocat()] +
            4 * [catCards.hairyCat()] +
            4 * [catCards.rainbowCat()] +
            4 * [catCards.beardCat()] +
            5 * [cards.seeFuture()] + 
            5 * [cards.nope()] + 
           1 (6 - play.count) * [cards.defuse()] + 
            (play.count - 1) * [cards.explodingKitten()]
        )

    def shuffle(self):
        random.shuffle(self.deck)





