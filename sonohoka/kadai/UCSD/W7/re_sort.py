"""Homework 7 re_sort for CSE-41273"""
# Yukie McCarter

import csv
import sys

OUTPUT_FILE = "_sort.csv"


def re_sort(in_file, out_file):
    csv.register_dialect('myDialect',
                         delimiter=',',
                         skipinitialspace=True)
    with open(in_file, 'r') as inputFile:
        with open(out_file, 'w') as outputFile:
            reader = csv.reader(inputFile, dialect='myDialect')
            headers = next(reader)
            csv_writer = csv.writer(outputFile)
            csv_writer.writerow(headers)
            sortedlist = sorted(reader, key=lambda row: row[1], reverse=False)
            for row in sortedlist:
                csv_writer.writerow(row)


if __name__ == "__main__":
    try:
        in_file = sys.argv[1]
        if "." in in_file:
            out_file = in_file.split('.')[0] + OUTPUT_FILE
            re_sort(in_file, out_file)
        else:
            print("You need a file extention")
    except:
        pass
