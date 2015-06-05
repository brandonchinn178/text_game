class Item(object):
    """
    The base class for every item in the game
    """
    # name of the item
    name = ''

    # description of the item
    description = ''

    def __init__(self, name, description):
        """
        Creates a new Item with the given name and description

        @param name (String) -- the name of this Item
        @param description (String) -- the description for this Item
        """
        self.name = name
        self.description = description

    def __str__(self):
        """
        @returns (String) a print-friendly string representing this item
        """
        return "<Item: %s>" % self.name

    def use(game_state):
        """
        Every item that does something must overwrite this function. By default, an item
        does not do anything when used.

        @param game_state (GameState) -- the game state that contains information about the
            current game
        """
        pass

class ExampleItem(Item):
    """
    An example subclass of Item
    """
    def __init__(self):
        # call the super class's __init__ function
        super(ExampleItem, self).__init__(
            name='Example Item',
            description='This item will be absolutely pointless in the game'
        )

    def use(game_state):
        print 'You used an example item!'
