import argparse


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--twitter', action='store_true', help='Share lyrics on Twitter')
    parser.add_argument('-nt', '--notwitter', action= 'store_true', help='Prints lyrics to console instead of tweeting them')
    parser.add_argument('-la', '--listartists', action= 'store_true', help='Gets a list of all artists')
    parser.add_argument('-a', '--artist', help='Specifies artist to get lyrics for')
    parser.add_argument('-fs','--fullsong',action='store_true',help='Prints entire lyrics of song to console')
    return parser.parse_args(), parser

CONSOLE_ARGS = _parse_arguments()[0]
PARSER = _parse_arguments()[1]

del _parse_arguments