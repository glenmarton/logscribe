import unittest
from tests.env import data_dir
from logscribe.eprint import eprint
from logscribe.released_log import ReleasedLog

class TestReleasedLog(unittest.TestCase):
  def setUp(self):
    self.filename = 'data/minichange.md'
    self.released = ReleasedLog(self.filename)

  def test_reads_file(self):
    self.released.read()
    actual = self.released.contents
    expect = """## Change Log

### [5.0.1-rc.5] - Unreleased

#### Fixed
- Login button

### [5.0.0-rc.11] - 2019-09-04

#### Fixed
- Fix a crash

----
"""
    self.assertEqual(actual, expect)


  def test_extract_released_portion(self):
    _input = """## Change Log

### [5.0.1-rc.5] - Unreleased

#### Fixed
- Login button

### [5.0.0-rc.11] - 2019-09-05

#### Fixed
- Fix a crash

----
"""

    self.released.set_contents(_input)
    actual = self.released.extract_released_portion()
    expect =  """### [5.0.0-rc.11] - 2019-09-05

#### Fixed
- Fix a crash

----
"""
    self.assertEqual(actual, expect)

  def test_last_line(self):
    _input = """- Fix a crash

----
[5.0.0-rc.11]: https://gitlab.valcom.com/servers/vmass"""
    self.released.set_contents(_input)
    actual = self.released.last_line()
    expect = '[5.0.0-rc.11]: https://gitlab.valcom.com/servers/vmass'
    self.assertEqual(actual, expect)
