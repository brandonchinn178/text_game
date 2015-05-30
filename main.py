# Python packages
import os, pickle
# Our packages
import tests
from game.constants import SAVE_LOCATION
from game.gamestate import GameState
from game.utils import capture_input

def play(args):
    """
    Setup and starts the game
    """
    if args.load:
        try:
            with open(SAVE_LOCATION, 'r') as f:
                game = pickle.load(f)
        except IOError:
            print 'No saved games found.'
            return
        if game.finished:
            user_input = capture_input(
                "You completed the game! Would you like to start a new game? (y/n) "
            )
            if user_input[0] == 'y':
                game = GameState()
            else:
                print 'Playing on saved file...'
    else:
        game = GameState()
    game.run()

def test(args):
    tests.run()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="""
        Welcome to your text-based adventure game! This file will allow you to play the
        game you have developed in the project. Available commands are provided below.
        Call `python main.py {command} -h` to view the help screen for the given command.
    """)
    commands = parser.add_subparsers(title='Available commands')
    
    play_parser = commands.add_parser('play', description='Start the game')
    play_parser.add_argument(
        '-l', '--load', help='Load a saved game', action='store_true'
    )
    play_parser.set_defaults(func=play)
    test_parser = commands.add_parser('test', description='Test code against unit tests')
    test_parser.set_defaults(func=test)

    args = parser.parse_args()
    args.func(args)
