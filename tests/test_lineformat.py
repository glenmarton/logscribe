# Python code to demonstrate working of unittest
import unittest
from logscribe.lineformat import LineFormat

class TestLineFormat(unittest.TestCase):
    def setUp(self):
        self.ln_format = LineFormat(15)

    def test_line_broken_into_segments(self):
        _input = 'This is my sentence which I hope you will read.'
        actual = self.ln_format.layout(_input)
        expect = 'This is my\nsentence which\nI hope you\nwill read.'
        self.assertEqual( actual, expect)

    def test_new_line_contains_prefix(self):
      _input = 'This is my sentence which I hope you will read.'
      self.ln_format.prefix('->')
      actual = self.ln_format.layout(_input)
      expect = 'This is my\n->sentence which\n->I hope you\n->will read.'
      self.assertEqual( actual, expect)

    def test_short_line(self):
      _input = 'Hello world!'
      actual = self.ln_format.layout(_input)
      expect = 'Hello world!'
      self.assertEqual( actual, expect)

    def test_empty_line(self):
      _input = ''
      actual = self.ln_format.layout(_input)
      expect = ''
      self.assertEqual(actual, expect)

    def test_segment_length_zero(self):
      with self.assertRaises(ValueError): LineFormat(0)

    def test_segment_to_short(self):
      lf = LineFormat(5)
      _input = 'mississippi'
      with self.assertRaises(ValueError): lf.layout(_input)

    def test_multiple_lines(self):
      _input = 'This is my sentence which I hope you will read.'
      actual = self.ln_format.layout(_input)
      expect = 'This is my\nsentence which\nI hope you\nwill read.'
      self.assertEqual(actual, expect)
      _input = 'mississippi'
      actual = self.ln_format.layout(_input)
      expect = 'mississippi'
      self.assertEqual(actual, expect)

if __name__ == '__main__':
  unittest.main()
