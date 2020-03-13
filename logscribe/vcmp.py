#!/usr/bin/python3
import sys


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def attempt_converting_to_int(x):
    return int(x) if x.isdecimal() else x


def compare_ver_strings(a, b):
    a = attempt_converting_to_int(a)
    b = attempt_converting_to_int(b)
    return compare(a, b)


def compare_array(a, b):
    for i in range(0, len(a)):
        result = compare_ver_strings(a[i], b[i])
        if result:
            break
    return result


def to_array(_str):
    _str = _str.replace("-", ".")
    _str = _str.replace("/", ".")
    return _str.split(".")


def compare_versions(ver1, ver2):
    a = to_array(ver1)
    b = to_array(ver2)
    return compare_array(a, b)


def cmp_to_key(mycmp):
    "Convert a cmp= function into a key= function"

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


if __name__ == "__main__":
    if compare_versions(sys.argv[1], sys.argv[2]) > 0:
        print(sys.argv[1] + " A is newer")
    else:
        print(sys.argv[2] + " B is newer than A")
