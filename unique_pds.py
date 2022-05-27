import csv

# This module takes the list of parcels zoned PD and gets the unique subdivision names in the list. 
# Generally, PDs are named the same as their subdivision, so ideally this will leave us with a list of all
# PDs in the city to aid with the zoning-future land use comparison.

def get_unique_pds(input, output):
    with open(input, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        
        subs = []
        for row in reader:
            subs.append(row['SUBDIVISION_PLAT_NAME'])

        unique_subs = set(subs)

        uniquepds = open(output, 'w', newline='')
    
        for sub in unique_subs:
            writer = csv.writer(uniquepds, delimiter=' ')
            writer.writerow([sub])

        uniquepds.close()