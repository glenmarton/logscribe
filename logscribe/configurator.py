from logscribe.conf import Conf


def configure(filename, milestone):
    configuration = Conf()

    configuration.read(filename)

    configuration.append("milestone", milestone)

    return configuration.get_dictionary()
