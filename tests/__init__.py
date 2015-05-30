import unittest

def run():
    suite = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner().run(suite)

    if result.skipped:
        print '\nSkipped tests:'
        for test, reason in result.skipped:
            test_name = test.id().split('.')[2]
            print '%s: %s' % (test_name, reason)
