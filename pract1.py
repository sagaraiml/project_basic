"""s = list(input('string: '))
l = len(s)
asc = [ord(x) for x in s]
for i in range(l):
    if asc[i]"""
"""import sys
import math
from intertools import groupby
from operator import itegetter
str = list(input())
#o = ('').join(l)
data = [ord(x) for x in str]
#ch = [chr(x) for x in i]
for k, g in groupby(enumerate(data), lambda i, x: i -x):
    print(map(itemgetter(1), g))"""

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('---------Start-----------')
str = list('abcdlxyzmno')
data = [ord(x) for x in str]
logging.debug(data)
want = []
for i in range(len(data) - 1):
    logging.debug('{} iteration \nvalues of\ndata[i+1] {}\n  data[i] {}'.format(i+1, data[i+1], data[i]))
    logging.debug('want b4 append {}'.format(want))
    if data[i+1] - data[i] == 1:
        if data[i] not in want:
            want.append(data[i])
        if data[i+1] not in want:
            want.append(data[i+1])
    else:
        #else condition
    logging.debug('want after append {}'.format(want))
logging.debug(set(data))
logging.debug(set(want))
num = list(set(data) - set(want))
logging.debug(num)
ch = [chr(x) for x in num]
op = ('').join(ch)
logging.debug(op)
logging.debug('---------Finish-----------')
