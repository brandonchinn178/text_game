from game.exceptions import UnimplementedException

class Location(object):
    """
    The base class for every location in the game. To make a new Location, simply call
    the constructor: Location(name, description, *items) and a new Location with the
    specified information will be created.

    You may subclass Location to create other types of locations, such as DungeonLocation
    or something.
    """
    def __init__(self, name, description):
        """
        Creates a new Location with the given name and description

        @param name (String) -- the name of this Location
        @param description (String) -- the description for this Location
        """
        self.name = name
        self.description = description
        # dictionary mapping direction to name of Location
        self.neighbors = {}
        # list of items in this room
        self.items = []

    def __str__(self):
        """
        @returns (String) a print-friendly version of this location.
        """
        return "<Location: %s>" % self.name

    def add_neighbor(self, direction, location):
        """
        Adds the provided location in the specified direction

        @param direction (String) -- the full name of the direction to add the Location
        @param location (Location) -- the Location object to add as a neighbor
        """
        raise UnimplementedException

    def add_item(self, item):
        """
        Adds the provided item to this Location's list of items

        @param item (Item) -- the Item to add to the list of items
        """
        raise UnimplementedException

    def get_directions(self):
        """
        @returns (List<String>) the available directions to move
        """
        raise UnimplementedException

    def go(self, direction):
        """
        Returns the Location in the given direction. If there is no neighbor in that
        direction, print out a message and return self.

        @param direction (String) -- the full name of the direction to go (not alias)

        @returns (Location) the Location in the given direction, or self if None
        """
        raise UnimplementedException

    def get_long_description(self):
        """
        @returns (String) all information about this location on the `look` command.
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
