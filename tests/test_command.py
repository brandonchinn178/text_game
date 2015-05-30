import unittest
from mock import patch
from game import commands
from game.exceptions import QuitGame
from tests.utils import suppress_input, suppress_output

class TestCommands(unittest.TestCase):
    """
    Sanity checks that running any command returns a String.
    """
    def test_key_commands(self):
        """
        Make sure all the key commands exist: Help, Go, Save, Quit
        """
        self.assertTrue(hasattr(commands, 'Help'))
        self.assertTrue(hasattr(commands, 'Go'))
        self.assertTrue(hasattr(commands, 'Save'))
        self.assertTrue(hasattr(commands, 'Quit'))

    @suppress_output
    @suppress_input
    @patch('game.gamestate.GameState')
    def test_execute(self, *mocks):
        """
        Test that all Commands' execute function is implemented
        """
        game_state = mocks[0]
        for cmd, cls in commands.ALL_COMMANDS.items():
            try:
                cls.execute([cmd], game_state)
            except QuitGame:
                pass

    def test_make_alias(self):
        """
        Tests the make_alias function
        """
        class Foo(commands.Command):
            description = 'Foo description'

        alias = commands.make_alias(Foo)
        self.assertEqual(alias.__name__, 'FooAlias')
        self.assertEqual(alias.description, 'An alias for the `foo` command')
        self.assertTrue(hasattr(alias, 'execute'))

    @patch('game.locations.Location')
    @patch('game.locations.Location')
    @patch('game.gamestate.GameState')
    def test_go_command(self, *mocks):
        """
        Tests that the Go command works
        """
        game_state, loc1, loc2 = mocks
        loc1.go.return_value = loc2
        game_state.curr_location = loc1

        commands.Go.execute(['go', 'north'], game_state)
        self.assertEqual(loc1.go.call_args, (('north',),))
        self.assertEqual(game_state.curr_location, loc2)

        # check alias converts before sending to Location.go()
        commands.Go.execute(['go', 'n'], game_state)
        self.assertEqual(loc1.go.call_args, (('north',),))

    @suppress_input
    @patch('game.gamestate.GameState')
    def test_save_command(self, *mocks):
        game_state = mocks[0]
        commands.Save.execute(['save'], game_state)
        self.assertTrue(game_state.save.called)
