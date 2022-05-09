from sys import argv
import os.path
from os import path
import sys


# Check for Usage
if len(argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)
elif not path.exists(argv[1]):
    print("Missing {}".format(argv[1]), file=sys.stderr)
    exit(1)

html = []
