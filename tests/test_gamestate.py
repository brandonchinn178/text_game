import unittest
from mock import patch, mock_open, call
from game import gamestate
from game.constants import SAVE_LOCATION
from game.locations import Location
from tests.utils import suppress_output

class TestGameState(unittest.TestCase):
    """
    Tests functions of the GameState
    """
    @suppress_output
    @patch('game.locations.Location.add_neighbor')
    def setUp(self, *mocks):
        self.game_state = gamestate.GameState()

    @suppress_output
    @patch('__builtin__.open')
    def test_save(self, *mocks):
        """
        Tests saving the game
        """
        saved_file = mocks[0]
        self.game_state.save()
        open_file_command = call(SAVE_LOCATION, 'w')
        self.assertIn(open_file_command, saved_file.call_args_list)

        # mocked_file().__enter__().write
        self.assertTrue(saved_file.return_value.__enter__.return_value.write.called)

    def test_locations(self):
        """
        Tests that locations and curr_locations is initialized correctly
        """
        self.assertIsInstance(self.game_state.locations, dict)
        self.assertIsInstance(self.game_state.locations.keys()[0], str)
        self.assertIsInstance(self.game_state.locations.values()[0], Location)
        self.assertIsInstance(self.game_state.curr_location, Location)
