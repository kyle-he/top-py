import argparse
import os

from .top import from_top, to_top

parser = argparse.ArgumentParser(
    description='Tool for translating between top and human readable text'
)
parser.add_argument(
    '--from-top',
    default=False,
    const=True,
    action='store_const'
)
if os.isatty(0):
    parser.add_argument('text')

args = parser.parse_args()

while True:
    try:
        text = args.text or input()

        if args.from_top:
            print(from_top(text))
        else:
            print(to_top(text))

        if os.isatty(0):
            break
    except EOFError:
        break
