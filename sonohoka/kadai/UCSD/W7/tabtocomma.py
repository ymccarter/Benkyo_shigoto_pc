import csv
import sys
import os

inputPath = sys.argv[1]
#outputPath = os.path.dirname(inputPath) + "output.csv"
outputPath = sys.argv[2]
print("Converting CSV to tab-delimited file...")
with open(inputPath) as inputFile:
	with open(outputPath, 'w') as outputFile:
		reader = csv.DictReader(inputFile, delimiter='\t')
		writer = csv.DictWriter(outputFile, reader.fieldnames, delimiter=',')
		writer.writeheader()
		writer.writerows(reader)
print("Conversion complete.")