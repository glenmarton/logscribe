import unittest
from logscribe.process_argv import process_argv

class TestProcessArgs(unittest.TestCase):
    def setUp(self):
        pass
    
    def _test_no_milestone(self):
        args = [ 'data/test_CHANGELOG.md' ]
        dictionary = process_argv(args)
        actual = dictionary

        self.assertEqual(actual['YAML_PATH'], './data')
        self.assertEqual(actual['CHANGELOG'], 'data/test_CHANGELOG.md')
        self.assertEqual(actual['milestone'], '')

    def test_args(self):
        args = [ 'data/test_CHANGELOG.md', '1.0.0' ]
        dictionary = process_argv(args)
        actual = dictionary

        self.assertEqual(actual['YAML_PATH'], './data')
        self.assertEqual(actual['CHANGELOG'], './data/test_CHANGELOG.md')
        self.assertEqual(actual['milestone'], '1.0.0')
