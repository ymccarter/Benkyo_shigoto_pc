"""HW7 answers for CSE-41273 re_order.py
    Module re_order that includes the re_order function.
    $ python re_order.py in_file, out_file
    Where in_file is a CSV file.
"""
import csv
import sys


def re_order(in_file, out_file):
    """Read CSV file, swap first two columns, and output new file."""
    with open(in_file, mode='r', newline='') as old_file:
        # We don't have to worry about headers since those need to
        # be switched the same as data rows.
        reordered_rows = [
            [row[1], row[0]] + row[2:]
            for row in csv.reader(old_file)
        ]
    with open(out_file, mode='w', newline='') as new_file:
        csv.writer(new_file).writerows(reordered_rows)


# Or, you can combine it all this way:
def re_order2(in_file, out_file):
    """Read CSV file, swap first two columns, and output new file."""
    with open(in_file, mode='r', newline='') as old_file:
        with open(out_file, mode='w', newline='') as new_file:
            csv.writer(new_file).writerows(
                [row[1], row[0]] + row[2:]
                for row in csv.reader(old_file)
            )


# Or, if the file is potentially very large, read and write it
# one row at a time.
# This is probably more practical for a general-purpose program.
def re_order3(in_file, out_file):
    """Read CSV file, swap first two columns, and output new file."""
    with open(in_file, mode='r', newline='') as old_file:
        with open(out_file, mode='w', newline='') as new_file:
            for row in csv.reader(old_file):
                row[1], row[0] = row[0], row[1]
                csv.writer(new_file).writerow(row)


if __name__ == "__main__":
    re_order(*sys.argv[1:])
