import unittest
from logscribe.compare_link import CompareLink

class TestCompareLink(unittest.TestCase):
  def setUp(self):
    self.link = '[5.0.0-rc.11]: https://gitlab.valcom.com/servers/vmass/compare/6025-v5.0.0-rc.10...6025-v5.0.0-rc.11'
    self.compare_link = CompareLink('5.0.0-rc.12')

  def test_init(self):
    actual = self.compare_link.to_str()
    expect = ''
    self.assertEqual(actual, expect)

  def test_extract_previous_milestone(self):
    actual = self.compare_link.extract_previous_milestone(self.link)
    expect = '5.0.0-rc.10'
    self.assertEqual(actual, expect)

  def test_extract_current_milestone(self):
    actual = self.compare_link.extract_previous_milestone(self.link)
    expect = '5.0.0-rc.10'
    self.assertEqual(actual, expect)

  def test_generate_using(self):
    self.compare_link.generate_using(self.link)
    actual = self.compare_link.to_str()
    expect = '[5.0.0-rc.12]: https://gitlab.valcom.com/servers/vmass/compare/6025-v5.0.0-rc.11...6025-v5.0.0-rc.12'
    self.assertEqual(actual, expect)
