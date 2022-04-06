"""comma-always-after-last-tuple set to true"""

TUPLE_1 = (1, 'a', 2, True,)
TUPLE_2 = ()
TUPLE_3 = (
    1, 'a',
    True,
)

# Not really a tuple, so trailing comma not required.
TUPLE_4 = ('a')
TUPLE_5 = (
    'a'
)
