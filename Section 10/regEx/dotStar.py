import re

helloRegex = re.compile(r'^Hello')
helloRegex.search('Hello There!')

# ^ to find a char that is at the beginning
# $ to find a char that is at the end
# . to find anything

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat')

# .* any char except new line (greedy)
# .*? any char except new line (non-greedy)

greedyNameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
greedyNameRegex.findall('First Name: Al Last Name: Sweigart')

serve = '<To serve humans for dinner.>'
nonGreedy = re.compile(r'<(.*?)>')
nonGreedy.findall(serve)

# Add re.DOTALL to match any char including new line
# Add re.I to return lower and upper case char