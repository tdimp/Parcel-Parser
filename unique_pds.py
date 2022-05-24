import csv

# This module takes the list of parcels zoned PD and gets the unique subdivision names in the list. 
# Generally, PDs are named the same as their subdivision, so ideally this will leave us with a list of all
# PDs in the city to aid with the zoning-future land use comparison.

def get_unique_pds(input, output):
    with open(input, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        uniquepds = open(output, 'w', newline='')

        subs = []

        for row in reader:
            subs.append(row['SUBDIVISION_PLAT_NAME'])

        unique_subs = set(subs)


        for sub in unique_subs:
            outputDictWriter = csv.writer(uniquepds, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            outputDictWriter.writerow(sub)

        uniquepds.close()