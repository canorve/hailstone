#! /usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

## program that returns the Collatz (hailstone) conjeture



def main():

    if len(sys.argv[1:]) != 1:
        print ('Collatz conjeture')
        print ('Missing arguments')
        print ("Usage: %s [Number] " % (sys.argv[0]))
        print ("Example: %s 5 " % (sys.argv[0]))
        sys.exit()
    else:
        print ('Collatz conjeture:')

    Number = np.round(np.float(sys.argv[1]))

    hailstone(Number)

    print("Done. ")



def hailstone(n):
    "Return the Hailstone conjeture"

    n=np.int(n)
    print (n)

    if n == 1:
        return

    mod = n % 2

    if mod == 1:
         hailstone(3*n+1)
    else:
        hailstone(n/2)


#############################################################################
######################### End of program  ###################################
#     ______________________________________________________________________
#    /___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/_/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/
##############################################################################
if __name__ == '__main__':
    main()
