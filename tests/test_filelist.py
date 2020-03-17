import unittest
from logscribe.eprint import eprint
from logscribe.filelist import FileList
from logscribe.mergedbranch import MergedBranch

class TestMergedbranch(unittest.TestCase):
  def setUp(self):
    self.file_list = FileList('./data')

  def test_read(self):
    actual = self.file_list.count()
    expect = 49
    self.assertEqual(actual, expect)

  def test_keep_files(self):
    self.file_list.keep_files('.yml')
    actual = self.file_list.count()
    expect = 43
    self.assertEqual(actual, expect)

  def test_remove_files(self):
    self.file_list.remove_files('template')
    actual = self.file_list.count()
    expect = 48
    self.assertEqual(actual, expect)

    def test_to_str(self):
        expect = [
            'change-904.yml', 'change-929.yml', 'change-911.yml', \
            'change-928.yml', 'change-936.yml', 'change-901.yml', \
            'change-914.yml', 'change-902.yml', 'change-903.yml', \
            'test_CHANGELOG.md', 'change-909.yml', 'change-917.yml', \
            'change-938.yml', 'change-933.yml', 'template.yml', \
            'change-910.yml', 'change-918.yml', 'change-931.yml', \
            'change-937.yml', 'change-916.yml', 'minichange.md', \
            'change-930.yml', 'change-939.yml', 'change-934.yml', \
            'this_file_should_be_excluded.txt', 'change-920.yml', \
            'change-923.yml', 'change-927.yml', 'change-926.yml', \
            'change-915.yml', 'change-907.yml', 'change-935.yml', \
            'conftest.conf', 'change-900.yml', 'logscribe.conf', \
            'change-912.yml', 'change-906.yml', 'change-919.yml', \
            'change-908.yml', 'change-913.yml', 'change-905.yml', \
            'gitlog.txt', 'change-925.yml', 'change-940.yml', \
            'change-939-mr749.yml', 'change-932.yml', 'change-922.yml', \
            'change-921.yml', 'change-924.yml'
        ]
        actual = self.file_list.str()

        for i in range(len(actual)):
            self.assertEqual(actual[i], expect[i])

  def test_sort_by(self):
    order = [ 'this_file_should_be_excluded', 'template.yml', '900', \
        '901', '903', '905', '907', '909', '902', '904', '906', '908', '910', \
        '911', '913', '915', '917', '919', '912', '914', '916', '918', '920', \
        '921', '923', '925', '927', '929', '922', '924', '926', '928', '930', \
        '931', '933', '935', '937', '939', '932', '934', '936', '938', '940', \
        'test_CHANGELOG.md', 'minichange.md', 'gitlog.txt']
    self.file_list.sort_by(order)

    expect = [
        'change-900.yml', 'change-901.yml', 'change-903.yml', 'change-905.yml',\
        'change-907.yml', 'change-909.yml', 'change-902.yml', 'change-904.yml',\
        'change-906.yml', 'change-908.yml', 'change-910.yml', 'change-911.yml',\
        'change-913.yml', 'change-915.yml', 'change-917.yml', 'change-919.yml',\
        'change-912.yml', 'change-914.yml', 'change-916.yml', 'change-918.yml',\
        'change-920.yml', 'change-921.yml', 'change-923.yml', 'change-925.yml',\
        'change-927.yml', 'change-929.yml', 'change-922.yml', 'change-924.yml',\
        'change-926.yml', 'change-928.yml', 'change-930.yml', 'change-931.yml',\
        'change-933.yml', 'change-935.yml', 'change-937.yml', 'change-939.yml',\
        'change-932.yml', 'change-934.yml', 'change-936.yml', 'change-938.yml',\
        'change-940.yml', 'logscribe.conf', 'conftest.conf', 'gitlog.txt', \
        'this_file_should_be_excluded.txt', 'minichange.md', 'template.yml', \
        'test_CHANGELOG.md', 'change-939-mr749.yml'
    ]
    actual = self.file_list.array()

    for i in range(len(actual)):
      self.assertEqual(actual[i], expect[i])
