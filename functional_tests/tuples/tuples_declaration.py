"""Declare lists"""

EMPTY_TUPLE = ()
ONE_ITEM_TUPLE = (1,)
ONE_LINE_TUPLE = (1, 3, 5, 17)

ONE_ITEM_NOT_TUPLE = (
    # No trailing comma means not a tuple
    1
)

ONE_ITEM_LINED_COMMA_TUPLE = (
    1,
)

TWO_ITEM_LINED_COMMA_TUPLE = (
    1,
    2,
)

ONE_ITEM_LINED_COMMA_COMMENT_TUPLE = (
    1,
    # comments don't throw off the references
)

MULTI_ITEM_LINED_COMMA_TUPLE = (
    1,
    2,
    3,
    4,
)
