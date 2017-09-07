#!/usr/bin/env python

import sys
from time import time
from genssn import genSSN
from gennames import getRandomNames

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

    records = 0
    with open(outfile, 'wb') as fs:
        while records < count:
            record = '{0}{1}{2}'.format(ssns[records], DELIMITER, names[records])
            fs.write(record + "\n")
            records += 1

if __name__ == '__main__':
    # run as:
    # buildtestdata.py 50 names.csv output.csv
    # or
    # buildtestdata.py 50 names.csv
    main(sys.argv[1:])


