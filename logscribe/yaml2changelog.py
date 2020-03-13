#!/usr/bin/python3
from logscribe.changelog import Changelog
from logscribe.filelist import FileList
from logscribe.fileio import read_yaml_file
from logscribe.mergedbranch import MergedBranch
from logscribe.vcmp import compare_versions


#
#   f u n c t i o n s
#
class Yaml2Changelog:
    def __init__(self, conf):
        title = self._guess_title_from(conf["milestone"])
        self.changelog = Changelog(title)
        self.conf = conf

    def read_in_changes(self):
        self._process_yaml_files(self.conf["YAML_PATH"])
        milestone = self.conf['milestone']
        self.changelog.set_milestone_to_release(milestone)
        self.changelog.only_report_on(milestone)

    def to_markdown(self):
        return self.changelog.to_markdown()

    def count(self):
        return self.changelog.issue_count()

    def _guess_title_from(self, version):
        if compare_versions(version, "4.0.0") < 0:
            return "VECAP"
        else:
            return "VMASS"

    def _process_yaml_files(self, yaml_path):
        files = self._list_input_files(yaml_path)
        for _file in files:
            entry = read_yaml_file(yaml_path + "/" + _file)
            if entry:
                self.changelog.append(entry)

    def _list_input_files(self, search_path):
        file_list = FileList(search_path)
        file_list.keep_files("change-")

        merge_order = self._build_merge_order()
        file_list.sort_by(merge_order)
        return file_list.array()

    def _build_merge_order(self):
        merged = MergedBranch()
        try:
            merged.set_testing(True)
        except KeyError:
            merged.set_testing(False)

        merged.set_changelog(self.conf["CHANGELOG"])
        return merged.issues()
