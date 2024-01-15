"""Deep lists, all valid."""
import sys


MY_VAL = (
    val.lower()
    for val in ('a', 'b', *sys.argv)
)

# The outer list is single-line style, but the inner list is multi-line style.
STRANGE_LIST = [1, 2, (
    'a', 'b',
), 'c']
