import unittest

def run():
    suite = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner().run(suite)

    if result.skipped:
        print '\nSkipped tests:'
        for test, reason in result.skipped:
            test_id = test.id().split('.')
            print '%s (%s): %s' % (test_id[2], test_id[1], reason)
