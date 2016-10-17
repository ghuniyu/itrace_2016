"""
PixelRacist by imn00
Sunday - Oct 16, 2016
"""

import itertools
from PIL import Image
from itertools import groupby

img = Image.open('sample.png', 'r')
pix_val = sorted(list(img.getdata()))

color_list = list(pix_val for pix_val, _ in groupby(pix_val))
dup = ([len(list(group)) for key, group in groupby(pix_val)])

print color_list
print dup
least = color_list[dup.index(min(dup))]

post = 'color=' + format(least[0], 'x').zfill(2) + format(least[1], 'x').zfill(2) + format(least[2], 'x').zfill(2)
print post
