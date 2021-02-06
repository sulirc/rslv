from textwrap import dedent

from . import __doc__, __version__
from .const import ExitStatus
from .argparser import RslvArgumentParser

parser = RslvArgumentParser(
    prog="rslv",
    description="%s ⛳️" % __doc__,
    epilog=dedent('''
    Enjoy rslv and have fun.
    More information please refer to README.md:

    https://github.com/sulirc/rslv
    '''))


def main():
    parser.add_argument('--list', '-l', help='List all registered alias')
    parser.add_argument('--register', '-r', help='Register an alias')
    parser.add_argument('--unregister', '-R', help='Unregister an alias')
    parser.add_argument(
        '--wrap', help='Wrap a shell command with the rslv ability')

    args = parser.parse_args()
    print(args)

    return ExitStatus.SUCCESS
