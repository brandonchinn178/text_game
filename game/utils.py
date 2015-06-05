from constants import GAME_PROMPT
from exceptions import QuitGame

def capture_input(prompt=GAME_PROMPT):
    """
    Helper function that prompts and returns user input. Catches all KeyboardInterrupt signals

    @param prompt (String) -- the String used to prompt the user

    @returns (List<String>) the user input, split by whitespace
    """
    user_input = ''
    while not user_input:
        try:
            user_input = raw_input(prompt)
        except (KeyboardInterrupt, EOFError):
            raise QuitGame
    return user_input.lower().split()

COLORS = {
    'black': 0,
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7
}

def colorize(message, color):
    """
    Turns the message into a message in the given color.

    @param message (String) -- the message to transform
    @param color (String) -- the color to turn the message into. The available colors are
        given in the COLORS dictionary above.

    @returns (String) the color transformed message
    """
    return "\x1b[3%dm%s\x1b[0m" % (COLORS[color], message)
