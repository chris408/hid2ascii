#Capture with: `cat /sys/kernel/debug/hid/<device_id>/events > ~/hidlog.txt`
import sys
import re

def main():
  if len(sys.argv) != 2:
    print("Usage: python hid2acii.py <hidlog.txt>")
    sys.exit(1)

  charmap = {'04': 'a',  '05': 'b',  '06': 'c',  '07': 'd',  '08': 'e',
    '09': 'f',  '0a': 'g',  '0b': 'h',  '0c': 'i',  '0d': 'j',  '0e': 'k',
    '0f': 'l',  '10': 'm',  '11': 'n',  '12': 'o',  '13': 'p',  '14': 'q',
    '15': 'r',  '16': 's',  '17': 't',  '18': 'u',  '19': 'v',  '1a': 'w',
    '1b': 'x',  '1c': 'y',  '1d': 'z', '1e': '1',  '1f': '2',  '20': '3',
    '21': '4',  '22': '5',  '23': '6',  '24': '7',  '25': '8',  '26': '9',
    '27': '0',  '28': 'NewLine',  '29': 'Escape',  '2a': 'Backspace',
    '2b': 'Tab', '2c': 'Space',  '2d': '-',  '2e': '=',  '2f': '[',  '30': ']',
    '31': 'Backslash',  '32': 'Euro',  '33': ';',  '34': 'Quote',  '35': '`',
    '36': ',',  '37': '.',  '38': '/',  '39': 'Caps',  '3a': 'F1',  '3b': 'F2',
    '3c': 'F3',  '3d': 'F4',  '3e': 'F5',  '3f': 'F6',  '40': 'F7',  '41': 'F8',
    '42': 'F9',  '43': 'F10',  '44': 'F11',  '45': 'F12',  '46': 'PrintS',
    '47': 'Scroll',  '48': 'Break',  '48': 'Pause'}

  dump = loadhid()
  parsehid(dump, charmap)

def loadhid():
  file = sys.argv[1]
  with open(file) as f:
     return(f.read().splitlines())

def parsehid(dump, charmap):
  for line in dump:
    match = re.search('00 00 ([0-9a-z]+) 00 00 00 00 00', line)
    if match:
      if(match.group(1) != '00'):
        try:
          print(charmap[match.group(1)].rstrip('\n'), end='', flush=True)
        except:
          print('failed char lookup')

  print('')

if __name__ == '__main__':
    main()

