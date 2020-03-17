import yaml


def read_file(fname):
    contents = []
    with open(fname, "r") as _file:
        for line in _file:
            if line != '\n':
                contents.append(line.strip('\n'))
    return contents


def read_yaml_file(fn):
    with open(fn, "r") as stream:
        try:
            contents = yaml.safe_load(stream)
            stream.close()
            return contents
        except yaml.YAMLError as exec:
            print("Exception: ")
            print(exec)
