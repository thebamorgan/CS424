class card:
    number = None
    description = ""
    amount = None

explodingKitten = card()
explodingKitten.number = 0
explodingKitten.description = "Discard all of your cards unless you have a defuse card"
explodingKitten.amount = 4

defuse = card()
defuse.number = 1
defuse.description = "If you drew an Exploding Kitten, you can play this card instead of dying. Place your Defuse Card in the Discard Pile. Then take the Exploding Kitten, and without reordering or viewing the other cards, secretly put it back in the Draw Pile anywhere you’d like. Your turn is over after playing this card"
defuse.amount = 6

attack = card()
attack.number = 2
attack.description = "Do not draw any cards. Instead, immediately force the next player to take 2 turns in a row. Play then continues from that player. The victim of this card takes a turn as normal (play-or-pass then draw). Then, when their first turn is over, it's their         turn again.  If the victim of an Attack Card plays an Attack Card on any of their turns, the new target must take any remaining turns plus the number of attacks on the Attack Card just played (e.g. 4turns, then 6, and so on)"
attack.amount = 4

favor = card()
favor.number = 3
favor.description = "Force any other player to give you 1 card from their hand. They choose which card to give you."
favor.amount = 4

nope = card()
nope.number = 4
nope.description = "Stop any action except for an Exploding Kitten or a Defuse Card. Imagine that any card beneath a Nope Card never existed.A Nope can also be played on another Nope to negate it and create a Yup, and so on. A Nope can be played at any time before an action has begun, even if it’s not your turn. Any cards that have been Noped are lost. Leave them in the Discard Pile."
nope.amount = 5

shuffle = card()
shuffle.number = 5
shuffle.description = "Shuffle the Draw Pile thoroughly."
shuffle.amount = 4

skip = card()
skip.number = 6
skip.description = "Immediately end your turn without drawing a card. If you play a Skip Card as a defense to an Attack Card, it oinly ends 1 of the 2 turns. 2 Skip Cards would end both turns."
skip.amount = 4

seeFuture = card()
seeFuture.number = 7
seeFuture.description = "Privately view the top 3 cards from the Draw Pile and put them back in the same order. Don’t show the cards to the other players."
seeFuture.amount = 5

catterMelon = card()
catterMelon.number = 8
catterMelon.description = "Must be played as a pair to steal a random card from any player"
catterMelon.amount = 4

tacoCat = card()
tacoCat.number = 9
tacoCat.description = "Must be played as a pair to steal a random card from any player"
tacoCat.amount = 4

hairyCat = card()
hairyCat.number = 10
hairyCat.description = "Must be played as a pair to steal a random card from any player"
hairyCat.amount = 4

rainbowCat = card()
rainbowCat.number = 11
rainbowCat.description = "Must be played as a pair to steal a random card from any player"
rainbowCat.amount = 4

beardCat = card()
beardCat.number = 12
beardCat.description = "Must be played as a pair to steal a random card from any player"
beardCat.amount = 4