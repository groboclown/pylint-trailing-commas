"""comma-always-after-last-tuple set to true"""

# Everything on a single line is fine.
TUPLE_1 = (1, 'a', 2, True)
TUPLE_2 = ()

# Not really a tuple, so trailing comma not required.
TUPLE_4 = ('a')
TUPLE_5 = (
    'a'
)
