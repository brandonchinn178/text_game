import unittest

def run():
    suite = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner().run(suite)
