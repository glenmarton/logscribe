import unittest
from logscribe.configurator import configure


class TestProcessArgs(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_milestone(self):
        dictionary = configure('./data/conftest.conf', '')
        actual = dictionary

        self.assertEqual(actual['YAML_PATH'], './yaml_dir')
        self.assertEqual(actual['CHANGELOG'], 'test_path/test_CHANGELOG.md')
        self.assertEqual(actual['milestone'], '')

    def test_args(self):
        dictionary = configure('./data/conftest.conf', '1.0.0')
        actual = dictionary

        self.assertEqual(actual['YAML_PATH'], './yaml_dir')
        self.assertEqual(actual['CHANGELOG'], 'test_path/test_CHANGELOG.md')
        self.assertEqual(actual['milestone'], '1.0.0')
