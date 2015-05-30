import unittest

def run():
    suite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(suite)
