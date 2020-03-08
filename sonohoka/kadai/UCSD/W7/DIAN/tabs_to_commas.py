"""HW7 answers for CSE-41273 tabs_to_commas.py
    Module tabs_to_commas that includes function tab_to_comma
    $ python tabs_to_commas in_file.tsv
    Creates new file in_file_commas.csv with tabs of .tsv file changed
    to commas. In_file can be csv named.
"""
import csv
import sys


def tab_to_comma(in_file, out_file):
    """Read tab-delimited file and write CSV file back out."""
    with open(in_file, mode='r', newline='') as old_file:
        csv_reader = csv.reader(old_file, delimiter="\t")
        rows = [row for row in csv_reader]
        # Or you could do rows = list(csv_reader)

    with open(out_file, mode='w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=",")
        csv_writer.writerows(rows)


if __name__ == "__main__":
    tab_file = sys.argv[1]
    file_parts = tab_file.rsplit('.', maxsplit=1)
    # File with commas should always be a .csv file
    comma_file = file_parts[0] + '_commas.csv'
    tab_to_comma(in_file=tab_file, out_file=comma_file)
