import os
os.environ['MNE_LAZY_LOADING'] = 'false'
from opencortex.application import run


def run_cli():
    run()


if __name__ == '__main__':
    run()
