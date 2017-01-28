# ultimatebravery
A ultimate bravery implementation that is a tad bit different.

This implementation builds upon the core of ultimate bravery and takes additional steps to raise the stakes.

So what's it all about?

## Give me an item!

The general idea behind ultimate bravery is getting random items for a random champion. Usually the items you have to built are determined before the match begins.

We do things differently.

At the start of the game you request your first item to build with `get_item()`.  You buy those item components you can (if you can buy any at all ;) and you continue to wherever you want to go on the map.  The next time when you're in base and are able to purchase the complete item, you request the next item.

Some additional rules
* If for whatever reason you are unable to purchase a certain item even though you would have enough gold. (e.g. jungle items without smite), you buy every component that you are able to buy and then go on to the next item as usual.
* If you completed your 6th item, you sell exactly one item to free up an item slot, and request the next item as usual.
* The above rule is the only occassion on which you can sell an item.

## What do I level?

Instead of the usual 'max ability X', the leveling order is fixed and can be retrieved with `get_skills()`.
(Tip: `from pprint import pprint pprint(get_skills())` for a nicer view)

This can create some interesting situations like leveling your ult for the first time at 11 or not having access to your e untill late in the game.

## Masteries / Runes

True bravery players use no masteries and no runes.  We often find ourselves in the loading screens without any empty rune page though so we just use the one that makes least sense.  Mastery pages though are an easy 0/0/0.

You can use any of the other classic bravery calculators to get some random masteries.

## Summoner spells

todo

## Some general Rules

* No recalling bitch.  Survival of the fittest.
* No suicidal acts for the sake of buying items.
* DON'T BE A DICK. DO NOT USE THIS SHIT IF NOT EVERYONE ON THE TEAM IS OK WITH THE CONCEPT.
