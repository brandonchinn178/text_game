from mock import patch

def suppress_input(func):
    """
    Always sends 'y' to the standard input
    """
    return patch('__builtin__.raw_input', return_value='y')(func)

def suppress_output(func):
    """
    Suppress any messages to the standard output
    """
    return patch('sys.stdout')(func)
