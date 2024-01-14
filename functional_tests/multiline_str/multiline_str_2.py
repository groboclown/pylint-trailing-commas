"""Regression test for invoking a function with a multi-line string.  Bad"""


print(
    """
    This requires a trailing comma.
    """,
    "another argument",
    2  # [closing-comma]
)
