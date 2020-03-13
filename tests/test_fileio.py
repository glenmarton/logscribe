import unittest
import sys
from logscribe.eprint import eprint
from logscribe.fileio import read_yaml_file

class TestFileio(unittest.TestCase):

  def test_read_file(self):
    fname = './data/template.yml'
    contents = read_yaml_file(fname)
    actual = contents.keys()
    expect = "dict_keys(['issue', 'type', 'description', 'model', 'milestone'])"
    self.assertEqual(str(actual), str(expect))
