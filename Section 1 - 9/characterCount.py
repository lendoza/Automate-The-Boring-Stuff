import pprint

message = 'We on an ultra light beam. This is a god dream.'

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)