from constants import GAME_PROMPT

def capture_input(prompt=GAME_PROMPT):
    """
    Helper function that prompts and returns user input. Catches all KeyboardInterrupt signals
    """
    user_input = ''
    while not user_input:
        try:
            user_input = raw_input(prompt)
        except (KeyboardInterrupt, EOFError):
            # add newline
            print
            user_input = 'quit'
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
    Turns the message into a message in the given color. The available colors are available
    in the COLORS dictionary above. Example usage:
        print colorize('This is red!', 'red')
        print colorize('This is cyan!', 'cyan')
    """
    return "\x1b[3%dm%s\x1b[0m" % (COLORS[color], message)
