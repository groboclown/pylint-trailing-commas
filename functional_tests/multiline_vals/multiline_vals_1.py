"""Regression test for multi-line condition, wrapped in parentheses to
avoid backslash EOL."""

VAL1 = "2"
VAL2 = "3"
VAL3 = "4"

VAL4 = (
        VAL1 in "123"
        and VAL2 in "345"
        and VAL3 in "567"
)
