# coding=utf-8
import re

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)  # first seperator
\d\d\d  # first 3 digits
-  # seperator
\d\d\d\d # last 4 digits
(((ext(\.)?\s) | x) # extension word-part (optional)
(\d{2,5}))? # extensions number-part (optional)
)
''', re.VERBOSE)

# TODO: Create a regex about for email addresses

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+ # name part
@ # at symbol
[a-zA-Z0-9_.+]+ # domain name part

''', re.VERBOSE)

# TODO: Get the text off the clipboard

text = '''Jeffner M Allen Professor of Philosophy/PIC/Africana Studies    607-777-3616    jeffn@binghamton.edu
Anne C Bailey   Associate Professor 607-777-6113    abailey@binghamton.edu
Moulay Ali Bouânani Lecturer    607-777-2537    bouanani@binghamton.edu
James Burns Associate Professor 607-777-2595    jburns@binghamton.edu
Anthony Ephirim-Donkor  Chair, Associate Professor  607-777-4248    aephirim@binghamton.edu
Patricia Lespinasse Assistant Professor 607-777-2623    plespina@binghamton.edu
Lisa Norris Secretary 1 607-777-2635    lnorris@binghamton.edu
Samuel Elikem Kwame Nyamuame    Visiting Assistant Professor    607-777-6951    nyamuame@binghamton.edu
Nkiru Nzegwu    Professor   607-777-3082    panap@binghamton.edu
'''


# TODO: Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print (allPhoneNumbers)

# TODO: Format results

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

print results