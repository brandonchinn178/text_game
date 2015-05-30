Text Game
=========

This project is a general layout for a text-based game similar to Zork. In the files, there will be comments that provide guidance on what code should be put there. Be creative, and build your own, unique, text-based game!

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
