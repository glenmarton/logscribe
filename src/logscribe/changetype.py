from __future__ import print_function
from logscribe.lineformat import LineFormat


class ChangeType:
    def __init__(self, name):
        self.name = name
        self.changes = []
        self._lineformat = LineFormat(75)
        self._lineformat.prefix("  ")

    def append(self, change):
        self.changes.append(change)

    def length(self):
        return len(self.changes)

    def remove_changes_not_associated_with(self, model):
        for i, change in enumerate(self.changes):
            if model not in change["model"]:
                del self.changes[i]

    def to_markdown(self):
        markdown = self.name_to_markdown()
        markdown += self.changes_to_markdown()
        return markdown

    def String(self):
        s = "name: " + self.name + " "
        for change in self.changes:
            s += str(change)
        return s

    #
    #   P r i v a t e
    #   M e t h o d s
    #
    def name_to_markdown(self):
        return "\n#### " + self.name + "\n"

    def changes_to_markdown(self):
        markdown = ""
        for change in self.changes:
            markdown += self.one_change_to_markdown(change)
            markdown += "\n"
        return markdown

    def one_change_to_markdown(self, change):
        description = change["description"]
        markdown = "- {}\n".format(self._lineformat.layout(description))
        markdown += "  - " + self.model_to_str(change["model"]) + "\n"
        markdown += "  - VMASS-" + str(change["issue"])
        return markdown

    def model_to_str(self, models):
        str = ""
        for model in models:
            str += model + ", "
        return str.rstrip(", ")
