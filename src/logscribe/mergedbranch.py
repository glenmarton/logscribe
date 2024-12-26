from datetime import date
import subprocess

from logscribe.eprint import eprint
from logscribe.fileio import read_file


class MergedBranch:
    def __init__(self):
        self.testing = False
        now = date.today()
        self.start = "{}-{}-{}".format(now.year - 1, now.month, now.day)
        self.stop = now.isoformat()
        self.merges = []

    def set_changelog(self, changelog):
        self.start = self.find_date_of_last_release_in(changelog)

    def set_starting(self, starting_point):
        self.start = starting_point

    def set_ending(self, ending_point):
        self.stop = ending_point

    def list(self):
        pass

    def issues(self):
        return self.list_merged_issues_since_last_release(self.start)

    def set_testing(self, status):
        self.testing = status

    def find_merges(self):
        git_log = self._run_git_log(self.start)
        self.merges = self._process_log(git_log)

    def find_date_of_last_release_in(self, changelog):
        contents = read_file(changelog)
        release_line = self._find_latest_release(contents)
        release_date = self._extract_date(release_line)
        return release_date

    def list_merged_issues_since_last_release(self, start):
        git_log = self._run_git_log(start)
        issues = self._process_log(git_log)
        reverse_list = issues[::-1]
        if self.testing == 3:
            eprint(str(type(issues)) + " - list: " + str(issues))
            eprint(str(type(reverse_list)) + " - revr: " + str(reverse_list))
        return reverse_list

    def _run_git_log(self, start):
        if self.testing:
            output = self._git_output_for_testing()
        else:
            output = subprocess.check_output(
                ["git", "log", "--oneline", "--since", start, "--until",
                    self.stop]
            )
        return output

    # # #   find_date_of_last_release_in() methods   # # #
    def _find_latest_release(self, contents):
        try:
            for line in contents:
                if self._contains_a_release_in(line):
                    return line
        except MergedBranch.MBError as exec:
            eprint("Exception: No release present in file.")
            eprint(exec)
            return ""

    def _extract_date(self, line):
        try:
            index = line.find("] - ")
            date = line[index + 4:]
            return date
        except AttributeError:
            emsg = "Exception: File has no released versions"
            raise emsg

    # # #   list_merged_issues_since_last_release() methods   # # #
    def _process_log(self, log):
        merges = []
        for line in log:
            merged = str(line)
            if "Merge branch" in merged:
                issue = self._extract_issue_from(merged)
                merges.append(issue)
        return merges

    def _extract_issue_from(self, line):
        index = line.find("-", 23)
        return line[23:index]

    # # #   _find_latest_release() methods   # # #
    def _contains_a_release_in(self, line):
        has_version = self._line_contains_a_version(line)
        return has_version and self._is_released(line)

    def _line_contains_a_version(self, line):
        return line.find("### [", 0, 5) != -1

    def _is_released(self, line):
        index = line.find("] - Unreleased")
        return index == -1

    # # #   _run_git_log() methods   # # #
    def _git_output_for_testing(self):
        output = []
        fname = "./data/gitlog.txt"
        with open(fname) as f:
            for line in f:
                output.append(line.rstrip("\n"))
        return output
