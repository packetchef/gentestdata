#!/usr/bin/env python

from random import randrange
import sys

def genSSN(count):
    ssns = []
    while len(ssns) < count:
        ssn1 = randrange(1, 999, 1)
        ssn2 = randrange(1, 99, 1)
        ssn3 = randrange(1, 9999, 1)
        ssns.append('{0:0>3}-{1:0>2}-{2:0>4}'.format(ssn1, ssn2, ssn3))
    return ssns


def main(args):
    ssnCount = int(args[0])
    outfile = args[1]

    with open(outfile, 'wb') as fs:
        for ssn in genSSN(ssnCount):
            fs.write(ssn + "\n")

if __name__ == '__main__':
    main(sys.argv[1:])


