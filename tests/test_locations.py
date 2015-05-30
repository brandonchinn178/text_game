import unittest
from mock import patch
from game.exceptions import UnimplementedException
from game import locations

class TestLocation(unittest.TestCase):
    """
    Tests the Location class
    """
    def setUp(self):
        self.location = locations.Location('Test Location', 'This is a test location.')
        self.location2 = locations.Location('Test Location 2', 'Another location for testing')

    @unittest.skip('Unskip this test when making the game')
    def test_add_neighbor(self):
        """
        Tests the add_neighbor function
        """
        self.location.add_neighbor('north', self.location2)
        self.assertIn('north', self.location.neighbors)
        self.assertEqual(self.location.neighbors['north'], self.location2)

    @unittest.skip('Unskip this test when making the game')
    def test_get_directions(self):
        """
        Tests the get_directions function
        """
        directions = self.location.get_directions()
        self.assertIsInstance(directions, list)

        self.location.add_neighbor('north', self.location2)
        directions = self.location.get_directions()
        self.assertEqual(directions, ['north'])

    @unittest.skip('Unskip this test when making the game')
    def test_go(self):
        """
        Tests the go function
        """
        self.location.add_neighbor('north', self.location2)
        loc = self.location.go('north')
        self.assertIs(loc, self.location2)
        loc = self.location.go('south')
        self.assertIs(loc, self.location)

    @unittest.skip('Unskip this test when making the game')
    def test_get_long_description(self):
        result = self.location.get_long_description()
        self.assertIsInstance(result, str)
