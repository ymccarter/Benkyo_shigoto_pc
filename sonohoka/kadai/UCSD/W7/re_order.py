"""Homework 7 re_order for CSE-41273"""
# Yukie McCarter

import csv
import sys


def re_order(in_file, out_file):
    with open(in_file, mode='r') as infile:
        reader = csv.reader(infile)
        with open(out_file, mode='w') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                temp = row[0]
                row[0] = row[1]
                row[1] = temp
                writer.writerow(row)


if __name__ == "__main__":
    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        re_order(in_file, out_file)
    except:
        pass
