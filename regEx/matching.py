import re

# mo -- Match Object

# ? -- appear zero or 1 time

# d -- digit character

batRegex = re.compile(r'Bat(wo)?man') # wo appear zero or 1 time
mo = batRegex.search('The Adventures of Batwoman')

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('555-1234')

# * -- 0 or more

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowoman')

# + -- 1 or more

# { } -- specific number of times