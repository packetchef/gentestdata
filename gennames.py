#!/usr/bin/env python

import sys
import csv
from random import randrange

DELIMITER = ','
QUOTECHAR = '"'

def getNames(count, source):
    # This should return the same names everytime it is called with the same count and source file
    names = []
    with open(source, 'rb') as csvfile:
        namereader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
        # skip header
        namereader.next()
        for row in namereader:
            if len(names) < count:
                names.append(row[2])
    return names


def getCSVRecordCount(source):
    count = 0
    with open(source, 'rb') as csvfile:
        namereader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
        # skip header
        namereader.next()
        for row in namereader:
            count += 1
    return count


def getAllNames(source):
    names = []
    with open(source, 'rb') as csvfile:
        namereader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
        # skip header
        namereader.next()
        for row in namereader:
            names.append(row[2])
    return names


def getRandomNames(count, source):
    allNames = getAllNames(source)
    # csvRecordCount = getCSVRecordCount(source)
    csvRecordCount = len(allNames)
    names = []
    while len(names) < count:
        randNameInt = randrange(1, csvRecordCount-1, 1)
        names.append(allNames[randNameInt])
    return names


def main(args):
    requestNameCount = int(args[0])
    namefile =args[1]
    outfile = args[2]

    nameSet = getNames(requestNameCount, namefile)

    with open(outfile, 'wb') as fs:
        for name in nameSet:
            fs.write(name + "\n")


if __name__ == '__main__':
    main(sys.argv[1:])



