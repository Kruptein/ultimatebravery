# ultimatebravery
A ultimate bravery implementation that is a tad bit different.

This implementation builds upon the core of ultimate bravery and takes additional steps to raise the stakes.

Change 1: Item purchases
There is no set list of items you are going to build upon starting a game.  The command get_item() will return the next item to build.
Due to this change a default filter of only items with a price above 1k are returned by default, originally any item could be returned but
this is a pain late game as will be clear later.
Whether you broadcast what the next item available will be to give competition between your friends or to only announce it when you actually
purchased your last item is up to you.

Change 2: Leveling
The command get_skills() returns the leveling order of your skills throughout the entire game.
No maxing of a particular skill and then free choice no no.
You follow the level list.  You'll be lucky to get your ult at 6 ;).
For some general balancing in regards to ult unlocking it is advised to use the same level order for all players.

Change 3: masteries/runes
None should be used, no masteries, no runes.
