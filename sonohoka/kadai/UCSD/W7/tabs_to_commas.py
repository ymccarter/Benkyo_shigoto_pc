"""Homework 7 tabs_to_commas for CSE-41273"""
# Yukie McCarter

import csv
import sys

OUTPUT_FILE = "_commas.csv"


def tab_to_comma(in_file, out_file):
    with open(in_file) as inputFile:
        with open(out_file, 'w') as outputFile:
            reader = csv.DictReader(inputFile, delimiter='\t')
            writer = csv.DictWriter(outputFile,
                                    reader.fieldnames,
                                    delimiter=',')
            writer.writeheader()
            writer.writerows(reader)


if __name__ == "__main__":
    try:
        in_file = sys.argv[1]
        if "." in in_file:
            out_file = in_file.split('.')[0] + OUTPUT_FILE
            tab_to_comma(in_file, out_file)
        else:
            print("You need a file extention")
    except:
        pass
