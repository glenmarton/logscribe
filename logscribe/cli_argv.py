import argparse
from os import getcwd


class CmdLineArgv:
    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument('-c', '--conf', required=False,
                        help='configuration file')
        ap.add_argument('milestone', type=str, help='Milestone to report on')

        self.args = vars(ap.parse_args())

    def conf_file(self):
        if self.args['conf'] is None:
            return getcwd() + '/logscribe.conf'
        else:
            return self.args['conf']

    def milestone(self):
        return self.args['milestone']
