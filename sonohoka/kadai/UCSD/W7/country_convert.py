"""Homework 7 country_convert for CSE-41273"""
# Yukie McCarter
import csv


FILENAME = 'countryInfo.csv'
OUTPUT = 'country_simple_info.csv'


def convert():
    newlist = []
    with open(FILENAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            newdict = {}
            for k, v in row.items():
                if k == "name" or k == "capital" or k == "population":
                    newdict[k] = v
                    # print("{}:{}".format(k,v))
            newlist.append(newdict)
    # sort the new list
    sortedlist = sorted(newlist,
                        key=lambda d: int(d['population']),
                        reverse=True)

    with open(OUTPUT, 'w') as f:
        fieldnames = ['name', 'capital', 'population']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)


if __name__ == "__main__":
    convert()
