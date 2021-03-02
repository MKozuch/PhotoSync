#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 3:
	print("Usage: [source, target]")

srcfile = sys.argv[1]
destfile = sys.argv[2]

with open(destfile) as f:
	dest_hash_list = [line.split('  ')[0] for line in f]
with open(srcfile) as f:
	for line in f:
		if line.split('  ')[0].strip() not in dest_hash_list:
			print(f"\"{line.split('  ')[1].strip()}\"")
