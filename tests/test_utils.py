import unittest
from mock import patch
from game import utils
from game.exceptions import QuitGame

class TestCaptureInput(unittest.TestCase):
    """
    Tests the capture_input function in game/utils.py
    """
    @patch('__builtin__.raw_input', side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt(self, *mocks):
        """
        Tests that KeyboardInterrupt raises a QuitGame exception
        """
        self.assertRaises(QuitGame, utils.capture_input)

    @patch('__builtin__.raw_input', side_effect=EOFError)
    def test_eof_error(self, *mocks):
        """
        Tests that EOFError raises a QuitGame exception
        """
        self.assertRaises(QuitGame, utils.capture_input)
