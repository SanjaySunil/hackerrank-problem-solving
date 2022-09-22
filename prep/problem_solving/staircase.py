#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    string = ''
    for i in range(1, n+1):
        tag = ''
        space = ''
        for _ in range(0, i):
            tag = tag + '#'
        for _ in range(0, n-i):
            space = space + ' '
        
        if i == n:
            string += space + tag
        else:
            string += space + tag + "\n"

    print(string)
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
