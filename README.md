Text Game
=========

This project is a general layout for a text-based game similar to [Zork](http://textadventures.co.uk/games/view/5zyoqrsugeopel3ffhz_vq/zork). In the files, there will be comments that provide guidance on what code should be put there. Be creative, and build your own, unique, text-based game!

Installation
------------

To test your code, you will need to download the Python library `mock`. The easiest way to do this is to download [pip](https://pip.pypa.io/en/stable/installing.html) and call `pip install -r requirements.txt` or just simply `pip install mock`.

Running
-------

The main file is `main.py`. To see the commands available from the command line, run `python main.py`. You can either play the game or test your code against unit tests provided in the `test/` directory.

File Layout
-----------

In this project, the following files are provided:

- `main.py`: This is the entrypoint where you can run the game or test your code on the command line. It also contains the `play()` function that will run the game.
- `test/`: This directory contains the unittests used for checking the code.

### `game/` directory

- `gamestate.py`: This is the file containing the GameState class that tracks the player's progress in the game.
- `commands.py`: This is the file containing the commands that will be available for use in the game.
- `locations.py`: This is the file containing the locations available in the game.
- `items.py`: This is the file containing items available for use in the game.
- `constants.py`: This is the file containing constants used in the code.
- `exceptions.py`: This is the file containing the game-specific Exception classes that will be passed around.
- `utils.py`: This is the file containing helper functions that make certain tasks easier.

Directions
----------

The following functions are necessary to the game infrastructure and are necessary in order to make the game work:

- `commands.py`: Implement the `Command.execute` function for the following commands: `Examine`, `Look`, `Use`
- `locations.py`: Implement the functions in the `Location` class
- `gamestate.py`: Implement the `get_item` and `remove_item` functions in the `GameState` class

The following steps customize the various aspects of your game:

- `commands.py`: Place all commands users may use in the game in this file. To make a new Command, make a new subclass of Command and add the command to `ALL_COMMANDS`
- `initialize_locations` in `gamestate.py`: This function sets up the locations for a new game, using the `Location` constructor and the `Location.add_neighbors` function, and adds items to their starting locations
- `locations.py`: Make new `Location` subclasses if you wish to make specialized locations.
- `items.py`: Make new `Item` subclasses if you wish to make specialized items
- `GameState` in `gamestate.py`: Set up instance variables that track any progress for the game. This class is the object that will be saved when a user saves their progress, so put everything necessary between saves into this class
