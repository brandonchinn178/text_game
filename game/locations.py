from game_exceptions import UnimplementedException

class Location(object):
    """
    The base class for every location in the game. To make a new Location, simply call
    the constructor: Location(name, description, *items) and a new Location with the
    specified information will be created.

    You may subclass Location to create other types of locations, such as DungeonLocation
    or something.
    """
    # name of this location
    name = ''

    # description of this location
    description = ''

    def __init__(self, name, description, *items):
        """
        Initialize changeable properties of a location here. Accepts any number of arguments
        that represents the items in this location initially

        Location()               -> items: []
        Location(Item())         -> items: [<Item>]
        Location(Item(), Item()) -> items: [<Item>, <Item>]
        """
        self.name = name
        self.description = description
        # dictionary mapping direction to name of Location
        self.neighbors = {}
        # list of items in this room
        self.items = items

    def __str__(self):
        """
        Returns a print-friendly version of this location.
        """
        return "<Location: %s>" % self.name

    def add_neighbor(self, direction, location):
        """
        Adds the provided location in the specified direction
        """
        self.neighbors[direction] = location

    def get_directions(self):
        """
        Returns the available directions to move
        """
        raise UnimplementedException

    def go(self, direction):
        """
        Returns the Location in the given direction. If there is no neighbor in that
        direction, print out a message and return self.
        """
        raise UnimplementedException

    def get_long_description(self):
        """
        Returns a String containing information about this location on the `look` command.
        Should include the location's name, description, available items, and directions
        the player can move in.
        """
        raise UnimplementedException

class ExampleLocation(Location):
    """
    An example subclass of Location
    """
    def __init__(self, *items):
        # call the super class's __init__ function
        super(ExampleLocation, self).__init__(
            'Example',
            'This is an example location',
            *items
        )
