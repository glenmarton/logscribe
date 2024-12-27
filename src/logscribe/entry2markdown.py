def break_line_up(Line):
    line_limit = 75
    prefix_of_next_line = "  "
    line_len = len(Line)
    head = line_limit
    tail = 0
    broken_up = ""
    while head < line_len:
        while head > tail:
            if Line[head].isspace():
                break
            head -= 1
        broken_up += Line[tail:head] + "\n" + prefix_of_next_line
        tail = head + 1
        head += line_limit
    if tail < line_len:
        broken_up += Line[tail:]
    return broken_up


def model_to_str(models):
    str = ""
    for model in models:
        str += model + ", "
    return str.rstrip(", ")


def entry2markdown(entry):
    markdown = "- " + break_line_up(entry["description"]) + "\n"
    markdown += "  - " + model_to_str(entry["model"]) + "\n"
    markdown += "  - VMASS-" + str(entry["issue"])

    return markdown
