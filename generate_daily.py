#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import os
import glob
import zipfile
import datetime
import json
from collections import Counter,defaultdict

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_tag',required=True)
parser.add_argument('--input_country', required=True)
args = parser.parse_args()
all_files = sorted(glob.glob('outputs/geoTwitter*.zip.country'))

time = np.arange(0.0, 366.0, 1.0)
numbers = []
for filee in all_files:
    body = json.loads(open(filee, 'r').readlines()[0])
    add_number = body[args.input_tag][args.input_country]
    numbers.append(add_number)
fig, ax = plt.subplots()
ax.plot(time, numbers)
ax.set(xlabel='time (s)', ylabel='number of tweets with ' + args.input_tag, title='Days')
plt.show()
