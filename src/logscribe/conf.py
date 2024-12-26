from logscribe.fileio import read_file


class Conf:
    def __init__(self):
        self.dictionary = {"milestone": ""}

    def append(self, key, value):
        self.dictionary[key] = value

    def read(self, fname):
        contents = read_file(fname)
        for line in contents:
            pair = line.split("=")
            if(len(pair) >= 2):
                self.append(pair[0], pair[1].strip("'"))

    def get_dictionary(self):
        return self.dictionary
