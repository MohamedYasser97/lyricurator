import argparse


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt', '--notwitter', action= 'store_true', help='Prints lyrics to console instead of tweeting them')
    parser.add_argument('-la', '--listartists', action= 'store_true', help='Gets a list of all artists')
    parser.add_argument('-a', '--artist', help='Specifies artist to get lyrics for')
    parser.add_argument('-fs','--fullsong',action='store_true',help='Prints entire lyrics of song to console')
    return parser.parse_args()

CONSOLE_ARGS = _parse_arguments()

del _parse_arguments