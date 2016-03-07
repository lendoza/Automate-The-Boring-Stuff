import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# badRes = requests.get('https://automatetheboringstuff.com/asdoasd')
# badRes.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    print (playFile.write(chunk))
