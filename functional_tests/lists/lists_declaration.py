"""Declare lists"""

EMPTY_LIST = []
ONE_ITEM_LIST = [1]
ONE_LINE_LIST = [1, 3, 5, 17]

ONE_ITEM_BAD_LIST = [
    1  # [closing-comma]
]

ONE_ITEM_LINED_COMMA_LIST = [
    1,
]

TWO_ITEM_LINED_BAD_LIST = [
    1,
    2  # [closing-comma]
]

TWO_ITEM_LINED_COMMA_LIST = [
    1,
    2,
]

ONE_ITEM_LINED_COMMA_COMMENT_LIST = [
    1,
    # comments don't throw off the references
]

MULTI_ITEM_LINED_COMMA_LIST = [
    1,
    2,
    3,
    4,
]

MULTI_ITEM_LINED_BAD_LIST = [
    1,
    2,
    3,
    4  # [closing-comma]
]
