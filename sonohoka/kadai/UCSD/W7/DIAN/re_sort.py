"""HW7 answers for CSE-41273 re_sort.py
    Module re_sort that includes re_sort function.
    $ python re_sort.py in_file.csv
    Sorts by second of the CSV columns into in_file_sort.csv
"""
import csv
import sys


def re_sort(in_file, out_file):
    """Re-sort the given CSV file by the second column."""
    # First, read all the rows into a list
    with open(in_file, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
        # Or, rows = list(reader)
    # Get the key of the second column
    second_column = reader.fieldnames[1]
    # Sort all the rows. sorted() returns a new list
    sorted_rows = sorted(rows, key=lambda r: r[second_column])
    # Write it out to the new file
    with open(out_file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)


if __name__ == "__main__":
    filename = sys.argv[1]
    # Splits 'books.csv' into ['books', 'csv']
    file_parts = filename.rsplit('.', maxsplit=1)
    # Maintain the previous file extension
    sorted_file = file_parts[0] + "_sort." + file_parts[1]
    re_sort(in_file=filename, out_file=sorted_file)
