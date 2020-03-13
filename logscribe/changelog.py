import datetime

from logscribe.eprint import eprint
from logscribe.milestone import Milestone
from logscribe.vcmp import compare_versions
from logscribe.vcmp import cmp_to_key


class Changelog:
    def __init__(self, model):
        self.model = model
        self.selected_milestone = ""
        self.milestones = {}

    def append(self, entry):
        version = entry["milestone"]
        del entry["milestone"]
        if version not in self.milestones:
            milestone = Milestone(version)
            self.milestones.update({version: milestone})
        self.milestones[version].append(entry)

    def set_milestone_to_release(self, milestone):
        if milestone == "":
            return
        release = self.milestones[milestone]
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        release.set_release_date(today)

    def issue_count(self):
        count = 0
        for version in self.milestones:
            count += self.milestones[version].issue_count()
        return count

    def show(self):
        eprint("model: " + self.model)
        for version in self.milestones:
            self.milestones[version].show()

    def to_markdown(self):
        markdown = """# {}
----

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Change Log
""".format(
            self.model
        )
        markdown += self.markdown_from_milestones()
        return markdown

    def only_report_on(self, milestone):
        if milestone:
            self.selected_milestone = milestone

    def markdown_from_milestones(self):
        markdown = ""
        if self.selected_milestone == "":
            markdown += self.markdown_for_all_milestones()
        else:
            markdown += self.milestones[self.selected_milestone].to_markdown()
        return markdown

    def markdown_for_all_milestones(self):
        markdown = ""
        sorted_milestones = sorted(
            self.milestones, key=cmp_to_key(compare_versions), reverse=True
        )
        for milestone in sorted_milestones:
            markdown += self.milestones[milestone].to_markdown()
        return markdown

    @property
    def entry_count(self):
        total = 0
        for release in self.releases:
            total += release.count()
        return total
