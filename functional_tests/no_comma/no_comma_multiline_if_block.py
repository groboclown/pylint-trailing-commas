"""Regression testing for multi-line if block."""
import sys

if (
    len(sys.argv) > 2
    and sys.argv[1] == 'foo'
):
    pass
