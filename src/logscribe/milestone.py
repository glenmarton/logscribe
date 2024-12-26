from logscribe.changetype import ChangeType
from logscribe.eprint import eprint


class Milestone:
    def __init__(self, version):
        self.version = version
        self.release_date = "Unreleased"
        self._change_types = {}

    def append(self, entry):
        change_type = entry["type"]
        if change_type == "Undocumented":
            del entry
            return
        del entry["type"]
        group = self._change_types.get(change_type, ChangeType(change_type))
        group.append(entry)
        self._change_types.update({change_type: group})

    def set_release_date(self, date):
        self.release_date = date

    def issue_count(self):
        count = 0
        for _type in self._change_types:
            count += self._change_types[_type].length()
        return count

    def to_markdown(self):
        if self.issue_count() <= 0:
            return ""
        markdown = "\n### [{}] - {}\n".format(self.version, self.release_date)
        markdown += self.change_types_to_markdown()
        markdown += "\n----\n"
        return markdown

    def show(self):
        eprint("\nversion: " + self.version)
        eprint("release: " + self.release_date)
        eprint("change_types: " + str(self._change_types.keys()))
        for group in sorted(self._change_types.keys()):
            eprint("  " + self._change_types[group].String())

    #
    #   p r i v a t e
    #   m e t h o d s
    #
    def change_types_to_markdown(self):
        markdown = ""
        for _type in self.change_types_names_sorted():
            entry = self._change_types[_type]
            markdown += entry.to_markdown()
        return markdown

    def change_types_names_sorted(self):
        return sorted(self._change_types.keys())
