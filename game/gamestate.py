# Python packages
import pickle
# Our packages
from commands import ALL_COMMANDS
from constants import SAVE_LOCATION
from utils import capture_input, colorize
from game_exceptions import QuitGame

import locations

class GameState(object):
    """
    This is the class that will track the state of a player through the game. The GameState
    should carry all of the information that will be carried over on saved games, such as the
    player's score or lives. This class will also run the game.
    """
    def __init__(self):
        """
        This function initializes an empty GameState for a new game.
        """
        # a dictionary mapping location name to Location instance
        self.locations, self.curr_location = initialize_locations()

        # True when game is finished
        self.finished = False

        ### INITIALIZE OTHER VARIABLES HERE ###

        self.do_intro()

    def save(self):
        """
        Save the current game state in the file determined by SAVE_LOCATION.
        """
        with open(SAVE_LOCATION, 'w') as f:
            pickle.dump(self, f)
        print 'Successfully saved your game!'

    def run(self):
        """
        Runs a loop that accepts the user's input, executes the appropriate command, and
        exits the game with an exit message when finished.
        """
        while True:
            # print out location information
            print colorize('\n%s:' % self.curr_location.name, 'cyan')
            print colorize(self.curr_location.description, 'yellow')

            user_input = capture_input()

            # the primary command is the first word in the user input
            command = user_input[0]
            try:
                command_class = ALL_COMMANDS[command]
            except KeyError:
                print colorize("Command '%s' does not exist" % command, 'red')
                continue

            # call the appropriate function
            try:
                command_class.execute(user_input, self)
            except QuitGame:
                break

            if self.finished:
                self.do_finish()
                return

        print colorize('Exiting the game...', 'red')

    def do_intro(self):
        """
        Does any start-of-game actions for the player. Initializing GameState variables
        should be done in the __init__ function
        """
        lines = [
            "Welcome to your text game!",
            "To view the help screen, type `h` or `help`."
        ]
        print colorize('\n'.join(lines), 'yellow')

    def do_finish(self):
        """
        Does any end-of-game actions
        """
        print 'You finished the game!'

def initialize_locations():
    """
    A helper function that initializes all of the locations, and their neighbors and items.
    Returns a tuple, with two elements:
        - a dictionary mapping location name to Location
        - the starting point
    """
    import locations as l, items as i
    all_locations = {}

    # INITIALIZE ALL LOCATIONS HERE WITH INITIAL ITEMS
    example_location1 = l.Location('A Location', 'This is a location.', i.ExampleItem())
    example_location2 = l.Location('Special Location', 'This is a special location.')
    example_location3 = l.ExampleLocation(i.Item('Shoe', 'Wear this for comfort.'))
    example_location4 = l.ExampleLocation()

    # ADD ALL NEIGHBORS/ITEMS TO A LOCATION AND ADD LOCATION TO ALL_LOCATIONS
    example_location1.add_neighbor('north', example_location2)
    example_location1.add_neighbor('east', example_location3)
    all_locations[example_location1.name] = example_location1

    example_location2.add_neighbor('south', example_location1)
    example_location2.add_neighbor('east', example_location4)
    all_locations[example_location2.name] = example_location2

    example_location3.add_neighbor('west', example_location1)
    example_location3.add_neighbor('north', example_location4)
    all_locations[example_location3.name] = example_location3

    example_location4.add_neighbor('west', example_location2)
    example_location4.add_neighbor('south', example_location3)
    all_locations[example_location4.name] = example_location4

    return (all_locations, example_location1)
