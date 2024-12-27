#!/bin/python3
from logscribe.compare_link import CompareLink
from logscribe.released_log import ReleasedLog
from logscribe.yaml2changelog import Yaml2Changelog


def extract_entries_from(changelog_file):
    entries = ReleasedLog(changelog_file)
    entries.read()
    entries.extract_released_portion()
    return entries


def add_milestone_to_changelog(configuration):
    issues = Yaml2Changelog(configuration)
    issues.read_in_changes()

    released_log = extract_entries_from(configuration["CHANGELOG"])

    compare_link = CompareLink(configuration["milestone"])
    compare_link.generate_using(released_log.last_line())

    print(issues.to_markdown() + released_log.to_str() + compare_link.to_str())
