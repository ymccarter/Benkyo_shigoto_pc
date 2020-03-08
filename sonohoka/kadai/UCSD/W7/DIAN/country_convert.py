"""HW7 answers for CSE-41273 country_convert.py
    Read file 'countryInfo.csv' and create new file 'country_simple_info.csv'
    containing only country, capital and population; sorted by population.
"""
import csv


def by_population(row):
    """Helper Function to get the key to use for sorting data"""
    return int(row['population'])


def main():
    """Main program for country_convert.py"""
    # Step 1: Get the data from the file
    with open(
        'countryInfo.csv',
        mode='r',
        newline='',
        encoding='utf-8'
    ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter="\t")
        # Doing list(reader) iterates over the whole file until done.
        # Each element of the list is a dictionary of row data.
        old_rows = list(reader)

    # Step 2: Sort CSV data by population and rename country column.
    # Create a new list of dictionaries that only contain what we want.
    new_rows = [{
        'country': row['name'],
        'capital': row['capital'],
        'population': row['population'],
    } for row in old_rows]
    # Yes, steps 1 & 2 can and in real life probably should be combined.
    # I show them separately for clarity.

    # Step 3: Sort! The function sorted() returns a new list in sorted order.
    csv_rows = sorted(new_rows, reverse=True, key=by_population)

    # Step 4: Write country rows to new CSV file.
    headers = ["country", "capital", "population"]
    with open(
        'country_simple_info.csv',
        mode='w',
        newline='',
        encoding='utf-8'
    ) as out_file:
        writer = csv.DictWriter(
            out_file,
            delimiter=",",
            fieldnames=headers
        )
        writer.writeheader()
        writer.writerows(csv_rows)


if __name__ == "__main__":
    main()
