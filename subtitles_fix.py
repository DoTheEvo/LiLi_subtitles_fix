#!/usr/bin/python3
# -*- coding: utf-8 -*-

import enchant
import re
import sys


def find_and_check_possible_fix(word):
    fixed = word.replace('I', 'l')

    if any(x in word for x in ['I\'', 'It\'']):
        fixed = fixed.replace('l', 'I', 1)

    return (d.check(fixed), word, fixed)

try:
    file_name = sys.argv[1]
except:
    print('PASS SUBTITLE FILE AS AN ARGUMENT')
    sys.exit()

with open(file_name) as f:
    data = f.read()
    split_words = re.findall(r"[\w'-]+", data)

d = enchant.Dict("en_US")
broad_suspects = []
narrow_suspects = []
good = []
bad = []

# GET WORDS CONTAINING CAPITAL I
for x in split_words:
    if 'I' in x:
        broad_suspects.append(x)

# FIND ONES NOT BEING RECOGNIZED AS KNOWN WORDS
for x in broad_suspects:
    if d.check(x) is False:
        narrow_suspects.append(x)

# FIX IF WORD AFTER THE I->l SWITCH IS RECOGNIZED
for x in narrow_suspects:
        f = find_and_check_possible_fix(x)
        if f[0] is True:
            good.append(f)
        else:
            bad.append(f)

for x in good:
    rx = re.compile("(?<![-'])\\b{}\\b(?![-'])".format(x[1]))
    data = re.sub(rx, x[2], data)


# MANUAL REPLACEMENT OF NONRECOGNIZED WORDS
print('{} fixed\n{} words unknown'.format(len(good),len(set(bad))))
print('-------------------------------------------')
for x in set(bad):
    print('\"{}\" --> \"{}\"'.format(x[1], x[2]))
    r = input('[y]/n/custom: ') or 'y'
    if r == 'y':
        data = data.replace(x[1], x[2])
    elif r == 'n':
        pass
    else:
        data = data.replace(x[1], r)


with open("fixed_subtitles.srt", "w+") as f:
    f.write(data)
