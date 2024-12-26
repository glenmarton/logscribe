import sys

from logscribe.cli_argv import CmdLineArgv
from logscribe.configurator import configure
from logscribe.add_milestone2changelog import add_milestone_to_changelog


def main():
    argv = CmdLineArgv()
    configuration = configure(argv.conf_file(), argv.milestone())
    add_milestone_to_changelog(configuration)


if __name__ == "__main__":
    main()
