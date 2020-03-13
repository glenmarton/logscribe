import datetime
import unittest

from logscribe.changelog import Changelog
from logscribe.eprint import eprint

class TestChangelog(unittest.TestCase):
  def setUp(self):
    self.changelog = Changelog('VE6025')

  def test_model(self):
    actual = self.changelog.model
    expect = 'VE6025'
    self.assertEqual(actual, expect)

  def test_set_release_date(self):
    self.changelog.append({'milestone': '1.0.0', 'issue': 223, 'type': 'Fixed',
      'description': 'Flag tire.', 'model': ['VE6025']})
    self.changelog.set_milestone_to_release('1.0.0')
    actual = self.changelog.to_markdown()
    expect = datetime.datetime.now().strftime("%Y-%m-%d")
    self.assertIn(expect, actual, msg = "Expect release date is included")

  def test_appending_issues(self):
    self.changelog.append({'milestone': '1.0.0', 'issue': 223, 'type': 'Fixed',
      'description': 'Emergency alert system to use DEFCON 5.',
      'model': ['CCServer', 'VE6025']})
    self.changelog.append({'milestone': '1.0.0', 'issue': 224, 'type': 'Fixed',
      'description': 'Emergency alert system to use stubbed toe.',
      'model': ['CCServer',]})
    self.changelog.append({'milestone': '1.0.0', 'issue': 225, 'type': 'Added',
      'description': 'Easy button for ease of use.',
      'model': ['CCServer',]})

    actual = self.changelog.issue_count()
    expect = 3
    self.assertEqual(actual, expect)

  def test_to_markdown(self):
    self.changelog.append({'milestone': '1.0.0', 'issue': 223, 'type': 'Fixed',
      'description': 'Use DEFCON 5.',
      'model': ['CCServer', 'VE6025']})
    self.changelog.append({'milestone': '1.0.0', 'issue': 224, 'type': 'Fixed',
      'description': 'Use stubbed toe.',
      'model': ['CCServer',]})
    self.changelog.append({'milestone': '1.0.0', 'issue': 225, 'type': 'Added',
      'description': 'Easy button.',
      'model': ['CCServer',]})

    actual = self.changelog.to_markdown()
    datestamp = datetime.datetime.now().strftime("%Y-%m-%d")

    expect = "# VE6025\n----\n\nAll notable changes to this project will be " \
       "documented in this file.\n\nThe format is based on [Keep a Changelog]" \
       "(https://keepachangelog.com/en/1.0.0/).\nThis project adheres to " \
       "[Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n" \
       "## Change Log\n\n### [1.0.0] - Unreleased\n\n" \
       "#### Added\n- Easy button.\n  - CCServer\n  - VMASS-225\n\n#### Fixed\n" \
       "- Use DEFCON 5.\n  - CCServer, VE6025\n  - VMASS-223\n" \
       "- Use stubbed toe.\n  - CCServer\n  - VMASS-224\n\n----\n"

    self.assertEqual(actual, expect)

  def test_only_report_on(self):
    self.changelog.append({'milestone': '1.1.0', 'issue': 223, 'type': 'Fixed',
      'description': 'Use DEFCON 5.',
      'model': ['CCServer', 'VE6025']})
    self.changelog.append({'milestone': '1.0.0', 'issue': 224, 'type': 'Fixed',
      'description': 'Use stubbed toe.',
      'model': ['CCServer',]})
    self.changelog.append({'milestone': '1.0.0', 'issue': 225, 'type': 'Added',
      'description': 'Easy button.',
      'model': ['CCServer',]})

    self.changelog.only_report_on('1.0.0')

    actual = self.changelog.to_markdown()
    expect = "# VE6025\n----\n\n" \
      "All notable changes to this project will be documented in this file.\n\n" \
      "The format is based on [Keep a Changelog]" \
      "(https://keepachangelog.com/en/1.0.0/).\nThis project adheres to " \
      "[Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n" \
      "## Change Log\n\n### [1.0.0] - Unreleased\n\n" \
       "#### Added\n- Easy button.\n  - CCServer\n  - VMASS-225\n\n#### Fixed\n" \
       "- Use stubbed toe.\n  - CCServer\n  - VMASS-224\n\n----\n"
    self.assertEqual(actual, expect)

