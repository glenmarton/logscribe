import unittest
from logscribe.changetype import ChangeType

class TestChangeType(unittest.TestCase):
  def setUp(self):
    self.group = ChangeType('Added')

  def test_name(self):
    actual = self.group.name
    expect = 'Added'
    self.assertEqual(actual, expect)

  def test_can_append_change(self):
    self.group.append('my issue')
    self.group.append('your issue')
    actual = self.group.length()
    expect = 2
    self.assertEqual(actual, expect)

  def test_remove_not_model(self):
    self.group.append({'issue': 398,
      'description': 'Ntp to work on VECAP',
      'model': ['VE6024']})
    self.group.append({'issue': 223,
      'description': 'Text events created from quickpage still showing up with '
      'invalid font code',
      'model': ['CCServer', 'VE6021', 'VE6023', 'VE6025']})
    self.group.remove_changes_not_associated_with('VE6025')
    actual = self.group.length()
    expect = 1
    self.assertEqual(actual, expect)

  def test_markdown(self):
    self.group.append({'issue': 223,
      'description': 'DEFCON 5 to emergency alert system.',
      'model': ['CCServer', 'VE6025']})
    actual = self.group.to_markdown()
    expect = """
#### Added
- DEFCON 5 to emergency alert system.
  - CCServer, VE6025
  - VMASS-223
"""
    self.assertEqual(actual, expect)

if __name__ == '__main__':
  unittest.main()
