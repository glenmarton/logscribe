import unittest
from logscribe.conf import Conf

class TestConf(unittest.TestCase):
  def setUp(self):
    self.conf = Conf()
    self.conf.read('data/logscribe.conf')

  def test_dict(self):
    actual = self.conf.dictionary['CHANGELOG']
    expect = './data/test_CHANGELOG.md'
    self.assertEqual(actual, expect)

    actual = self.conf.dictionary['YAML_PATH']
    expect = './data'
    self.assertEqual(actual, expect)

  def test_append(self):
    self.conf.append('milestone', '5.0.0-rc.12')
    actual = self.conf.dictionary['milestone']
    expect = '5.0.0-rc.12'
    self.assertEqual(actual, expect)

