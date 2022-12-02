## The game project

- The player has to collect a treasure from a cave and avoid being eaten by the monster;
- 2D-realm (top-view), 10×10 grid;
- the player can move up/down/left/right, one step at a time;
- the monster can move as well, one step at a time. The step direction is random. The case when the step direction heads towards a forbidden place is to be considered;
- the moves are synchronous (i.e. the monster does not move if the player doesn't);
- the realm is randomized at the beginning -- the initial position of Monster and Player, as well position of Treasure and forbidden places, is random;
- fog of war: the player can only see in a radius of 3 (a square/rhombus/circle). The fog of war meeting the edge of the cave is to be taken care of;
- marking scheme: among the 4 crucial features (player move, monster move, randomized realm, fog of war), the marking scheme is A=4/4, B=3/4, C=2/4, D=1/4.
- the graphics is only a command-line graphics, i.e. printing characters representing appropriate type of fields (empty, forbidden, field with player, field with monster, field with treasure, field covered by the fog of war)

Topics to consider if one wants to expand this project:
- parametrizable radius of fog of war;
- get to know the package `pygame` to change vizualization from command-line to a proper view;
- monster moves following some more advanced heuristics. 