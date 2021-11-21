#!/usr/bin/env python3

import argparse
import sys

import config
import utils
from command1 import command1

__version__ = '1.0.0'  # major.minor.patch
NAME = 'Script name'
DESCRIPTION = 'Script description.'

parser = config.configured_parser(NAME, __version__, DESCRIPTION)

parser.add_argument(
    '-o', '--optional',
    action='store_const', const='optional',
    help='Description of the optional flag.'
)

subparser = parser.add_subparsers(
    dest='command',
    metavar='[COMMAND]',
    title='Commands',
    prog=sys.argv[0]
)
commands = dict(
    command1=dict(
        help='Description of the command1.',
        command=command1
    ),
)
# automatically alphabetically sort commands
commands = dict(sorted(commands.items()))

for name, actions in commands.items():
    command = config.configured_command(subparser, name, actions)

    group = command.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-t', '--text',
        metavar='str', type=str,
        help='Example of argument that receives a string.'
    )
    group.add_argument(
        '-n', '--number',
        metavar='int', type=int,
        help='Example of argument that receives a integer.'
    )

    command.add_argument(
        dest='arguments',
        nargs=argparse.REMAINDER,
        help='Arbitrary arguments for a command.'
    )


def main():
    """Run script on user call."""
    args = config.initialize_parser(parser)
    if args.optional:
        utils.print_flashy('Optional flag called.')
    if args.command:
        commands.get(args.command).get('command')(**dict(args._get_kwargs()))


if __name__ == '__main__':
    main()  # pragma: no cover
