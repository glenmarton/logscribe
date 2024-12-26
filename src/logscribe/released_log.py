import re


class ReleasedLog:
    def __init__(self, filename):
        self.filename = filename
        self.contents = ""
        self.log = ""

    def read(self):
        with open(self.filename) as f:
            self.contents = f.read()

    def set_contents(self, contents):
        self.contents = contents

    def extract_released_portion(self):
        regex = r'### \[[-.0-9a-z]+\] - [0-9]'
        index = re.search(regex, self.contents, re.M).start()
        released_log = self.contents[index:]
        self.contents = released_log
        return released_log

    def last_line(self):
        index = self.contents.rindex("\n", 0, self._stop_index())
        one_past_CR = index + 1
        return self.contents[one_past_CR:]

    def to_str(self):
        return self.contents

    def _stop_index(self):
        for_range_0_to_end_of_str = 1
        for_last_CR_of_str = 1
        adjust_stoping_point = for_last_CR_of_str + for_range_0_to_end_of_str
        return len(self.contents) - adjust_stoping_point
