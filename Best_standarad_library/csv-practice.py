import csv

with open('example.csv') as f:
    rows = csv.reader(f, delimiter= '.')
    header = next(rows); header[0] = 'last'
    for row in rows:
        print(row)
    print(header)