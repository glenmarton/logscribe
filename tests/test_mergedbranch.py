import unittest
from logscribe.mergedbranch import MergedBranch

class TestMergedbranch(unittest.TestCase):
  def setUp(self):
    self.changelog = './data/test_CHANGELOG.md'
    self.merged_branches = MergedBranch()

  def test_find_date_of_last_release_in(self):
    actual = self.merged_branches.find_date_of_last_release_in(self.changelog)
    expect = '2019-09-04'
    self.assertEqual(actual, expect)

  # Fixed this test with https://ongspxm.github.io/blog/2016/11/assertraises
  # -testing-for-errors-in-unittest/
  def test_throws_exception_without_release_date(self):
    fname = 'mergedbranch.py'
    with self.assertRaises(Exception): \
        self.merged_branches.find_date_of_last_release_in(fname)

  def test_issues(self):
    start = '2019-06-12'

    self.merged_branches.set_testing(True)
    self.merged_branches.set_starting(start)
    merges = self.merged_branches.issues()
    actual = len(merges)
    expect = 25

    self.assertEqual(actual, expect)
    expect = ['875', '824', '925', '707', '901', '920', '928', '741', '793', \
        '823', '934', '930', '929', '932', '933', '936', '921', '935', '931', \
        '940', '939', '568', '887', '926', '939']
    self.assertEqual(merges, expect)

  def test_find_merges(self):
    self.merged_branches.set_testing(True)
    self.merged_branches.find_merges()
    expect = 25
    actual = len(self.merged_branches.merges)
    self.assertEqual(actual, expect)
