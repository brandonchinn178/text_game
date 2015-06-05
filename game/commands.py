# Our packages
from game.exceptions import UnimplementedException, QuitGame
from utils import capture_input, colorize
from constants import DIRECTION_ALIASES

class Command(object):
    """
    The base class for every command in the game
    """
    # every command must have a description
    description = ''

    @staticmethod
    def execute(user_input, game_state):
        """
        The function that will be called when a user calls this command. All Commands
        need to overwrite this function. To quit the game, call `raise QuitGame` in this
        function (See Quit for an example).

        @param user_input (List<String>) -- the user's input split by whitespace
        @param game_state (GameState) -- the current game state
        """
        raise UnimplementedException

def make_alias(cls):
    """
    Generates an Alias class from the provided Command. Usage:
        class Help(Command):
            description = 'Some command'
            @staticmethod
            def execute(user_input, game_state):
                # do something

        ALL_COMMANDS = {
            'help': Help,
            'h': make_alias(Help),
        }
    """
    name = cls.__name__
    description = 'An alias for the `%s` command' % name.lower()
    return type('%sAlias' % name, (cls,), {'description': description})

class Help(Command):
    """
    Display the description for the next command in the input. If there is no command
    provided in the input, displays all available commands. Commands will be displayed with
    a "column" of 7 spaces for the actual command, then a hyphen, then the description, e.g.

        h       - An alias for the `help` command
        help    - Displays the description of a command, or lists all available commands
    """
    description = 'Displays the description of a command, or lists all available commands'

    @staticmethod
    def execute(user_input, game_state):
        if len(user_input) == 1:
            for command, cls in sorted(ALL_COMMANDS.items()):
                print '{:<7} - {}'.format(command, cls.description)
        else:
            command = user_input[1]
            print '{:<7} - {}'.format(command, ALL_COMMANDS[command].description)

class Quit(Command):
    """
    Quit the game by sending back a "quit" response
    """
    description = 'Quits the game'

    @staticmethod
    def execute(user_input, game_state):
        user_input = capture_input(
            colorize('Are you sure you would like to quit? (y/n) ', 'red')
        )
        if user_input[0] == 'y':
            raise QuitGame
        else:
            print 'Aborting quit'

class Save(Command):
    """
    Saves the game by sending back a "save" response
    """
    description = 'Saves the game'

    @staticmethod
    def execute(user_input, game_state):
        user_input = capture_input(
            colorize('Are you sure you would like to overwrite any saved games? (y/n) ', 'red')
        )
        if user_input[0] == 'y':
            game_state.save()
        else:
            print 'Aborting save'

class Go(Command):
    """
    Travel in the specified direction
    """
    description = 'Move in the specified direction'

    @staticmethod
    def execute(user_input, game_state):
        location = game_state.curr_location
        if len(user_input) == 1:
            print 'Available directions: %s' % ', '.join(location.get_directions())
        else:
            direction = user_input[1]
            try:
                # convert if direction is an alias
                direction = DIRECTION_ALIASES[direction]
            except KeyError:
                pass

            game_state.curr_location = location.go(direction)

class Examine(Command):
    """
    Prints the description of the given item
    """
    description = 'Show the description of the specified item'

    @staticmethod
    def execute(user_input, game_state):
        raise UnimplementedException

class Look(Command):
    """
    Prints the long description of a location
    """
    description = 'Look around at your location'

    @staticmethod
    def execute(user_input, game_state):
        raise UnimplementedException

class Use(Command):
    """
    Calls an item's `use` function
    """
    description = 'Uses an item'

    @staticmethod
    def execute(user_input, game_state):
        raise UnimplementedException

"""
ADD MORE COMMANDS HERE
"""

# a dictionary mapping user commands to the correct Command class
ALL_COMMANDS = {
    'h': make_alias(Help),
    'help': Help,
    'q': make_alias(Quit),
    'quit': Quit,
    's': make_alias(Save),
    'save': Save,
    'go': Go,
    'examine': Examine,
    'look': Look,
    'use': Use,
    # ADD MORE COMMANDS HERE
}
