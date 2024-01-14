"""Regression test for invoking a function with a multi-line string.  All good."""

print(
    """
    Multi-line string does not require an end comma if it is a single argument.
    """
)


print(
    """
    Multi-line string requires end comma if there are multiple arguments.
    """,
    "another argument",
)
