#!/usr/bin/env python

import sys
from time import time
from genssn import genSSN
from gennames import getRandomNames
from gendate import getRandomDate
from random import random

DELIMITER=','

def main(args):
    count = int(args[0])
    namefile = args[1]

    try:
        outfile = args[2]
    except:
        outfile = 'testdata.{0}.csv'.format(int(time()))

    ssns = genSSN(count)
    names = getRandomNames(count, namefile)

    dates = []
    while len(dates) < count:
        dates.append(getRandomDate('1970-01-01','2018-08-01',random()))

    records = 0
    with open(outfile, 'wb') as fs:
        while records < count:
            record = '{0}{1}{2}{3}{4}'.format(ssns[records], DELIMITER, dates[records], DELIMITER, names[records])
            fs.write(record + "\n")
            records += 1

if __name__ == '__main__':
    # run as:
    # buildtestdata.py 50 names.csv output.csv
    # or
    # buildtestdata.py 50 names.csv
    main(sys.argv[1:])


