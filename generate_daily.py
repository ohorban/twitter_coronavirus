#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import glob
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_tag',required=True)
parser.add_argument('--input_country', required=True)
args = parser.parse_args()
all_files = sorted(glob.glob('outputs/geoTwitter*.zip.country'))

time = [] 
numbers = []
for filee in all_files:
    time.append(filee[21:26])
    body = json.loads(open(filee, 'r').readlines()[0])
    try:
        add_number = body[args.input_tag][args.input_country]
    except:
        add_number = 0
    numbers.append(add_number)
fig, ax = plt.subplots()
ax.plot(time, numbers)
count = 0
for label in ax.get_xticklabels():
    count = count + 1
    label.set_rotation(60)
    if count != 10:
        label.set_visible(False)
    else:
        count = 0
ax.set(xlabel='Date', ylabel='number of tweets with ' + args.input_tag + ' in ' + args.input_country)
plt.show()
