#!/usr/bin/env python3
# Now do chmod +x имя_файла
from random import choice
from string import (ascii_lowercase as low,
                    ascii_uppercase as high)

from sys import argv
# import sys
# print(sys.argv)

# TODO: find proper functions in random module
#       to build random sequences
#       i.e ''.join(sample(low, 5))

def gen_name(length=5):
    length = int(length)
    if length <= 0:
        raise TypeError('length should be > 0')
    return ''.join(choice(high) if i == 0 else choice(low) for i in range(length))

print('ARGV:', argv)

# Now let's make first command-line argument
# represent a desired name length

namelen = argv[1]
print('Random Name:', gen_name(namelen))
