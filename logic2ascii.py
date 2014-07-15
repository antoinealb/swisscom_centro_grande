#!/usr/bin/env python3

import sys

path = sys.argv[1]


data = [l.split(",")[1] for l in open(path)]
data = data[1:]
data = [int(x, 16) for x in data]

data = [chr(x) for x in data]

print("".join(data))


