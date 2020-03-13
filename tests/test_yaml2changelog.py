import unittest
from logscribe.yaml2changelog import Yaml2Changelog
from logscribe.conf import Conf
from logscribe.eprint import eprint

class TestYaml2Changelog(unittest.TestCase):
  def setUp(self):
    self.conf = Conf()
    self.conf.read('./data/logscribe.conf')
    self.conf.append('milestone', '5.0.0-rc.12')
    self.conf.append('TESTING', 'True')
    self.yaml2ch = Yaml2Changelog(self.conf.dictionary)

  def test_read_in_changes(self):
    self.yaml2ch.read_in_changes()
    actual = self.yaml2ch.count()
    expect = 22
    self.assertEqual(actual, expect)
