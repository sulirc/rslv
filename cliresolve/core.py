from . import __doc__, __version__
from .const import ExitStatus
from .argparser import RslvArgumentParser
from .action import RslvAction

parser = RslvArgumentParser(
    prog="rslv",
    description="%s ⛳️" % __doc__,
    epilog='''
    Enjoy rslv and have fun.
    More information please refer to https://github.com/sulirc/rslv
    ''')

rslv = RslvAction()


def main():
    parser.add_argument('-v', '--version', action="version",
                        version="%(prog)s {}".format(__version__))
    parser.add_argument('-e', '--expand', nargs=1, help="expand alias")
    parser.add_argument('-l', '--list', action="store_true",
                        help='List all registered alias')
    parser.add_argument('-r', '--register', nargs=2, help='Register an alias')
    parser.add_argument('-R', '--unregister', help='Unregister an alias')

    args = parser.parse_args()

    if args.register:
        rslv.handle_cli_register(*args.register)

    if args.unregister:
        rslv.handle_cli_unregister(*args.unregister)

    if args.expand:
        rslv.handle_cli_exec(*args.expand)

    if args.list:
        rslv.handle_cli_list()

    return ExitStatus.SUCCESS
