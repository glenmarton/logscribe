from logscribe.eprint import eprint


class LineFormat:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Must provide segment length.")
        self._segment_length = size
        self.fudge_factor_for_first_calculation_of_starting_point = -1
        self._starting_point = 0
        # self._starting_point = size * -1
        self._endpoint = \
            self.fudge_factor_for_first_calculation_of_starting_point
        self._line_prefix = ""

    def prefix(self, str):
        self._line_prefix = str

    def layout(self, line):
        self._endpoint = \
            self.fudge_factor_for_first_calculation_of_starting_point
        output = ""
        debug = False

        if debug:
            eprint("LineFormat.layout({})".format(line))
        while self.segment_in_line_exists(line):
            output += self.copy_segment_from(line)
            output += "\n" + self._line_prefix
        output += line[self._starting_point:]
        if debug:
            eprint("lineformat.layout() = " + output)
        return output

    def segment_in_line_exists(self, line):
        self.point_to_next_possible_line_segment_in(line)
        if self.reached_end_of(line):
            return False
        self.find_index_of_last_space_in_this_segment(line)
        return True

    def point_to_next_possible_line_segment_in(self, line):
        self._starting_point = self._endpoint + 1
        self._endpoint += self._segment_length

    def reached_end_of(self, line):
        end_of_line = len(line)
        return self._endpoint >= end_of_line

    def copy_segment_from(self, line):
        return line[self._starting_point: self._endpoint]

    def find_index_of_last_space_in_this_segment(self, line):
        while self._endpoint > self._starting_point:
            if line[self._endpoint].isspace():
                return
            self._endpoint -= 1
        raise ValueError(
            "Segment length must be longer than longest word in line.")
