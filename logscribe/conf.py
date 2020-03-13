from logscribe.fileio import read_file


class Conf:
    def __init__(self):
        self.dictionary = {"milestone": ""}

    def append(self, key, value):
        self.dictionary[key] = value

    def read(self, fname):
        contents = read_file(fname)
        for line in contents:
            array = line.split("=")
            if array:
                self.append(array[0], array[1].strip("'"))

    def get_dictionary(self):
        return self.dictionary
