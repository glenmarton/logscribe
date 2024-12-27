
class CompareLink:
    def __init__(self, milestone):
        self.link = ""
        self.milestone = milestone

    def generate_using(self, link):
        prev_milestone = self.extract_previous_milestone(link)
        cur_milestone = self.extract_current_milestone(link)
        next_milestone = self.milestone
        new_link = link.replace(cur_milestone, next_milestone)
        self.link = new_link.replace(prev_milestone, cur_milestone)

    def to_str(self):
        return self.link

    def extract_previous_milestone(self, link):
        start = link.index("compare/6025-v") + len("compare/6025-v")
        stop = link.index("...")
        return link[start:stop]

    def extract_current_milestone(self, link):
        start = link.index("[") + len("[")
        stop = link.index("]")
        return link[start:stop]
