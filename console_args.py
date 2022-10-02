import argparse


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt', '--notwitter', action= 'store_true', help='Prints lyrics to console instead of tweeting them')
    parser.add_argument('-a', '--artist', help='Specifies artist to get lyrics for')

    return parser.parse_args()

CONSOLE_ARGS = _parse_arguments()

del _parse_arguments