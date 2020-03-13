import unittest
from logscribe.milestone import Milestone

class TestMilestone(unittest.TestCase):
  def setUp(self):
    self.milestone = Milestone('5.0.0-rc.12')

  def test_version(self):
    actual = self.milestone.version
    expect = '5.0.0-rc.12'
    self.assertEqual(actual, expect)

  def test_initial_release_date(self):
    actual = self.milestone.release_date
    expect = 'Unreleased'
    self.assertEqual(actual, expect)

  def test_set_release_date(self):
    self.milestone.set_release_date('2019-09-12')
    actual = self.milestone.release_date
    expect = '2019-09-12'
    self.assertEqual(actual, expect)

  def test_appending_issues(self):
    self.milestone.append({'issue': 223, 'type': 'Fixed',
      'description': 'Emergency alert system to use DEFCON 5.',
      'model': ['CCServer', 'VE6025']})
    self.milestone.append({'issue': 224, 'type': 'Fixed',
      'description': 'Emergency alert system to use stubbed toe.',
      'model': ['CCServer',]})
    self.milestone.append({'issue': 225, 'type': 'Added',
      'description': 'Easy button for ease of use.',
      'model': ['CCServer',]})

    actual = self.milestone.issue_count()
    expect = 3
    self.assertEqual(actual, expect)

  def test_to_markdown(self):
    self.milestone.append({'issue': 223, 'type': 'Fixed',
      'description': 'Use DEFCON 5.',
      'model': ['CCServer', 'VE6025']})
    self.milestone.append({'issue': 224, 'type': 'Fixed',
      'description': 'Use stubbed toe.',
      'model': ['CCServer',]})
    self.milestone.append({'issue': 225, 'type': 'Added',
      'description': 'Easy button.',
      'model': ['CCServer',]})

    actual = self.milestone.to_markdown()
    expect = '\n### [5.0.0-rc.12] - Unreleased\n\n#### Added\n- Easy button.\n  - CCServer\n  - VMASS-225\n\n#### Fixed\n- Use DEFCON 5.\n  - CCServer, VE6025\n  - VMASS-223\n- Use stubbed toe.\n  - CCServer\n  - VMASS-224\n\n----\n'
    self.assertEqual(actual, expect)
