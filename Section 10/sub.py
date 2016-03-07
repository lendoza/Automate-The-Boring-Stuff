import re

namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave secret documents to Agent Bob.')

# sub() finds and replaces

namesRegex.sub('REDACTED', 'Agent Alice gave secret documents to Agent Bob.')

# re.VERBOSE removes white space

re.compile(r'''
\d\d\d # area code
-      # first dash
\d\d\d # first 3 digits
-      # second dash
\d\d\d\d # last 4 digits
''', re.VERBOSE)

