import os


class FileList:
    def __init__(self, path):
        if path == "":
            self.path = "."
        else:
            self.path = path

        self.files = self._read(path)

    def _read(self, path):
        return os.listdir(path)

    def count(self):
        return len(self.files)

    def keep_files(self, has):
        files = []
        for _file in self.files:
            if has in _file:
                files.append(_file)
        self.files = files

    def remove_files(self, has):
        files = []
        for _file in self.files:
            if has not in _file:
                files.append(_file)
        self.files = files

    def to_str(self):
        return str(self.files)

    def array(self):
        return self.files

    def sort_by(self, order):
        table = self._populate_table(order)
        for _file in self.files:
            self._add_to(table, _file)
        self.files = self._extract_list_from(table)

    def _populate_table(self, order):
        table = []
        for issue in order:
            name = "change-" + issue + ".yml"
            table.append([name, False])
        return table

    def _add_to(self, table, name):
        for array in table:
            if array[0] == name:
                array[1] = True
                return
        table.append([name, True])

    def _extract_list_from(self, table):
        sorted_list = []
        for array in table:
            if array[1]:
                sorted_list.append(array[0])
        return sorted_list


if __name__ == "__main__":
    changes = FileList(".")
    print(changes.to_str())
