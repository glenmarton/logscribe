import yaml


def read_file(fname):
    with open(fname, "r") as _file:
        contents = _file.read()
    data = contents.split("\n")
    return remove_blank_entry_at_end(data)


def read_yaml_file(fn):
    with open(fn, "r") as stream:
        try:
            contents = yaml.safe_load(stream)
            stream.close()
            return contents
        except yaml.YAMLError as exec:
            print("Exception: ")
            print(exec)


def remove_blank_entry_at_end(data):
    if data[-1] == "":
        del data[-1]
    return data
