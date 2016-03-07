import webbrowser
import sys

# webbrowser.open('http://leonardlabita.com')

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)
