import argparse

def _parse_arguments():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--twitter', action='store_true', help='Share lyrics on Twitter')
    group.add_argument('-nt', '--notwitter', action= 'store_true', help='Prints lyrics to console instead of tweeting them')
    group.add_argument('-la', '--listartists', action= 'store_true', help='Gets a list of all artists')
    group.add_argument('-ls', '--listsongs', action= 'store_true', help='Prints all songs for the randomly selected artist or the one selected by the user')
    group.add_argument('-hs','--hotsongs',action='store_true', help='Gets the list of hot songs')
    group.add_argument('-hal','--hotalbums',action='store_true', help='Gets the list of hot albums')

    
    parser.add_argument('-a', '--artist', help='Specifies artist to get lyrics for')
    parser.add_argument('-fs', '--fullsong',action='store_true',help='Prints entire lyrics of song to console')
    
    parser.add_argument('-i', '--interval', type=int, help='The interval in minutes between lyrics')
    
    try:
        return parser.parse_args(), parser
    except SystemExit:
        parser.usage=argparse.SUPPRESS
        parser.print_help()
        raise

CONSOLE_ARGS = _parse_arguments()[0]
PARSER = _parse_arguments()[1]

del _parse_arguments