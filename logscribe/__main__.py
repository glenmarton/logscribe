import sys

from logscribe.process_argv import process_argv
from logscribe.add_milestone2changelog import add_milestone_to_changelog


def main():
    configuration = process_argv(sys.argv)
    add_milestone_to_changelog(configuration)


if __name__ == "__main__":
    main()
