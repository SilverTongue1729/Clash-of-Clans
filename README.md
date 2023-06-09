# Assignment 3

2021111019 Sriteja Pashya

- Everything mentioned in the assignment has been implemented.
- **Bonus** :
  - King’s Leviathan Axe has also been implemented.  
  - Dragon Character has been added, it can fly over walls.
  - Queen's Eagle Arrow has been added.
  - Movement avoiding walls has also been implemented.

- To run the game : `python3 game.py`
- To view replays : `python3 replay.py`  and select the replay you want to watch according to mentioned date and time.
- For **Victory** : All buildings apart from walls get destroyed from the map in all three levels.
- For **Defeat** : If all troops and King die before destroying all buildings apart from walls.

## Extensions

- Sneaky Archers have been added
- Healers have been added
- Levels have been added to walls, wizard tower and cannons

### Assumptions

- Healer doesn't heal while the healer is moving
- Dead Troops don't heal
- healers can't heal each other
- splash radius of heal spell is a 3x3 square
- Each Healer will move towards the closest troop not at full health
- The limit of total number of archers applies to both normal and sneaky archers
- The level of buildings matches the level of the game

## Controls

### Hero &#129464;

- `w` - move up
- `a` - move left
- `d` - move right
- `s` - move down
- `1` - Special Attack
- `space` - Normal Attack

### Barbarian &#128481;

- `z` - spawn at point 1
- `x` - spawn at point 2
- `c` - spawn at point 3

### Dragon &#128009;

- `v` - spawn at point 1
- `b` - spawn at point 2
- `n` - spawn at point 3

### Archer &#127993;

- `i` - spawn at point 1
- `o` - spawn at point 2
- `p` - spawn at point 3

### Balloon &#127880;

- `j` - spawn at point 1
- `k` - spawn at point 2
- `l` - spawn at point 3

### Sneaky Archer &#127993;

- `t` - spawn at point 1
- `y` - spawn at point 2
- `u` - spawn at point 3

### Healer &#9877;

- `m` - spawn at point 1
- `,` - spawn at point 2
- `.` - spawn at point 3

`q` - Quit Game

## Assumptions

- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
  - Barbarians - 10
  - Archers - 7
  - Balloon - 5
  - Dragon - 3
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.
