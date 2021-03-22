#!/usr/bin/env python3
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_file',required=True)
args = parser.parse_args()

f = open(args.input_file, 'r')
contents = f.readlines()

labels = []
sizes = []
for entry in contents:
    label = entry[:entry.index(':')-1]
    size = entry[entry.index(':')+1:]
    labels.append(label)
    sizes.append(size)

fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()
