import os

from logscribe.conf import Conf


def process_argv(args):
    configuration = Conf()
    filename = os.path.dirname(args[0]) + '/logscribe.conf'
    configuration.read(filename)

    if len(args) > 1:
        configuration.append("milestone", args[1])

    return configuration.get_dictionary()
