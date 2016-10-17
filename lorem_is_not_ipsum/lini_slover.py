"""
Loremipsum Diff Buster by imn00
Sunday - Oct 16, 2016
"""

r = ''
for i in range(1, 63):
    m = open('0.loremipsum').read().split()
    c = open(str(i) + '.loremipsum').read().split()
    for j in range(len(m)):
        if c[j] != m[j]:
            r += c[j].replace('semper', '')

print r[r.find('ITRACE'):r.find('}') + 1]
