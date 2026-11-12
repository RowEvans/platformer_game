# Platformer Game

A small 2D platformer built in 4 days with Python and Pygame. Control a knight, collect every coin, dodge the spikes, and clear all three levels.

I built this as a short project to practice object-oriented programming before moving on to larger projects.

## Gameplay

- Collect all the coins in a level to advance to the next one.
- Touch a spike and you die. The level resets.
- Clear all 3 levels to reach the end screen, where you can restart or quit.

## Controls

| Key / Input | Action |
|---|---|
| `A` | Move left |
| `D` | Move right |
| `W` | Jump |
| `Esc` | Quit the game |
| Left mouse click | Press the **START** / **QUIT** buttons on the end screen |

## Getting Started

### Requirements

- Python 3.10 or newer
- [Pygame](https://www.pygame.org/)

### Install

```bash
git clone https://github.com/RowEvans/platformer_game.git
pip install pygame
```

### Run

The asset paths in the code start with `platformer_game/`, so run the game from the folder that **contains** the repo, not from inside it:

```bash
python platformer_game/platformer.py
```

## Project Structure

```
platformer_game/
├── platformer.py   # Entry point: game loop, level switching, end screen
├── player.py       # Player class: movement, physics, animation
├── levels.py       # Level base class, Level_01-03, Platform, Coin, Enemy (spike), Transition
├── buttons.py      # Clickable Button class (START / QUIT)
├── state.py        # Shared game state (game_over flag)
└── assets/
    ├── sprites/    # Knight, slimes, coins, spikes, platforms, tilesets
    ├── sounds/     # Sound effects (.wav)
    ├── music/      # Background music
    └── fonts/      # Pixel Operator 8 font
```
