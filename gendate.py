#!/usr/bin/env python

# Date generation courtesy of Stackoverflow:
# From https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates

import sys
import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def getRandomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)


def main(args):
    requestDateCount = int(args[0])
    
    for rdc in range(1, requestDateCount):
        # Date will be >= start and < end
        randomDate = getRandomDate('2000-01-01', '2018-08-02', random.random())    
        print(randomDate)


if __name__ == '__main__':
    main(sys.argv[1:])




