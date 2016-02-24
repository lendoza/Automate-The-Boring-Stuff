import shelve

helloFile = open('/Users/leonardlabita/Desktop/ATBS/Section 11/hello.txt', 'w')

# r is read mode - no writing/appending
# w is write mode - overwrites content
# a is append mode - adds to content already there

helloFile.write('HELLO SUCKA!')

# Binary Shelf Files - Used for variables, dictonaries, lists

shelfFile = shelve.open('mydata')

shelfFile['cats'] = ['Bob', 'Duke', 'Bae']

print shelfFile['cats']