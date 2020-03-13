class MergeEntry:
    def __init__(self, log_entry):
        self.sha1 = ''
        self.action = ''
        self.description = ''
        self.issue = 0

    def set_with(self, log_entry):
        self.sha1 = log_entry[0:8]

    def extract_substring_surrounded_by(self, char):
        pass
