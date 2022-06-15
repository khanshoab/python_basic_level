#            $$$$$$$$$$$$$TUPLE$$$$$$$$$$$$$$
# Tuple is an order sequence of the items same as a list.
# It is defined within parentheses () where items are separated by commas.
# It is fast and immutable.
# We can not perform the changes.

t = (10, 40, 'hello', 00, 'what')
print(type(t), t)

#           ##############DICTIONARY############
# Dictionary is an unordered collection of key-value pairs.
# In python, dictionary are defined within braces {} with each item being a pair in the form key:value.
d = {
    'name': 'khan akhtar',
    78: 'work_hard',
    'age': '21',
    'dob': '15-11-2022',
    "study": "BE-CO",
    'roll': "19co33",
    20: 'hello_world'
}
print(type(d), d)
print(d['name'])
print(d[78])

# &&&&&&&&&&&&&&&&&&&&&&&& SET &&&&&&&&&&&&&&&&&&
# A set is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable.
# It is written in {}.
# It is not repeat the value.

s = {10, 'khan', 78, 'hello', 90, 10, "world", 90}
print(type(s), s)



