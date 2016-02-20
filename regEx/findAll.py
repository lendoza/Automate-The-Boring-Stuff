import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = """Leonard Labita Phone number: 347-280-8652 Adress:247 Elvin St
Web Developer, Beast, Ultra Light Beamin, Enjoys Ramen 347-280-8652"""
# print phoneRegex.findall(resume)

# Two or more groups will return a list of tuples

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
resume = """Leonard Labita Phone number: 347-280-8652 Adress:247 Elvin St
Web Developer, Beast, Ultra Light Beamin, Enjoys Ramen 347-280-8652"""
# print phoneRegex.findall(resume)

# \d -- Any numeric digit from 0 to 9
# \w -- Any letter, numeric digt, or the underscore character
# \s -- Any space, tab, or newline character

# Capatalize (\W, \S, \D) to get the opposite

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords\
 a leaping, 9 ladies dancing, 8 maids milking...'

xmasRegex = re.compile(r'\d+\s\w+')
# print xmasRegex.findall(lyrics)

vowelRegex = re.compile(r'[aeiou]') # [0-9] same as (0|1|2...)
print vowelRegex.findall('We on an ultra light beam')

# [^...] will give you the negative of the character class