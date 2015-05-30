class UnimplementedException(Exception):
    """
    The Exception raised when a function is not implemented
    """
    def __str__(self):
        return 'You have not implemented a function!'

class QuitGame(Exception):
    """
    The Exception raised when the player wishes to exit a game
    """
    pass
