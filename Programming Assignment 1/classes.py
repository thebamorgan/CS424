class cards:
    def explodingKitten(): #4 cards
        #Discard all of your cards unless you have a defuse card
        print("explodingKitten")

    def defuse(): #6 cards
        #If you drew an Exploding Kitten, you can play this card instead of dying. Place your Defuse Card in the Discard Pile.
        #Then take the Exploding Kitten, and without reordering or viewing the other cards, secretly put it back in the Draw Pile anywhere you’d like
        #Turn over after playing this card
        print("defuse")
 
    def attack(): #4 cards
        #Do not draw any cards. Instead, immediately force the next player to take 2 turns in a row. Play then continues from that player. The victim of this card takes a turn as normal (play-or-pass then draw). Then, when their first turn is over, it's their         turn again.  If the victim of an Attack Card plays an Attack Card on any of their turns, the new target must take any remaining turns plus the number of attacks on the Attack Card just played (e.g. 4turns, then 6, and so on)
        print("attack")

    def favor(): #4 cards
        #Force any other player to give you 1 card from their hand. They choose which card to give you.
        print("favor")

    def nope(): #5 cards
        #Stop any action except for an Exploding Kitten or a Defuse Card. Imagine that any card beneath a Nope Card never existed.A Nope can also be played on another Nope to negate it and create a Yup, and so on. A Nope can be played at any time before an action has begun, even if it’s not your turn. Any cards that have been Noped are lost. Leave them in the Discard Pile
        print("nope")

    def shuffle(): #4 cards
        #Shuffle the Draw Pile thoroughly. 
        print("shuffle")

    def skip(): #4 cards
        #Immediately end your turn without drawing a card. If you play a Skip Card as a defense to an Attack Card, it oinly ends 1 of the 2 turns. 2 Skip Cards would end both turns.
        print("skip")

    def seeFuture(): #5 cards
        #Privately view the top 3 cards from the Draw Pile and put them back in the same order. Don’t show the cards to the other players.
        print("future")

class catCards: #Must be played as a pair to steal a random card from any player
    def cattermelon(): #4 cards
        print("cattermelon")
    def tacocat(): #4 cards
        print("tacocat")
    def hairyCat(): #4 cards
        print("hairy")
    def rainbowCat(): #4 cards
        print("rainbow")
    def beardCat(): #4 cards
        print("beard")
