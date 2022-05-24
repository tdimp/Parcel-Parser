import csv

# This module has two functions: it iterates over a list of parcels from the city, checking each parcel's ZONING_DISTRICT.
# If the parcel's ZONING_DISTRICT == 'PD', the row is copied to the list of parcels zoned PD.
# If the parcel's ZONING_District != 'PD', the row is copied to the list of parcels not zoned PD.
# PDs are customized zone districts, so when comparing zoning to future land use, each PD will have to be evaluated
# on a case by case basis. Therefore, it is helpful to remove them from the main parcel list and put them in their own list.

def separate_pds(input, output1, output2):
    with open(input, newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['PARCEL_PIN', 'SOURCE', 'Future Land Use Code', 'ZONING_DISTRICT', 'SUBDIVISION_PLAT_NAME']
        reader = csv.DictReader(csvfile)

        # Loop through parcel list, checking for PD zoning.
        # If ZONING_DISTRICT == PD, copy that row to pudlist.csv
        # else, copy row to parcelsnopds.csv
        pdfile = open(output1, 'w', newline='')
        writer1 = csv.DictWriter(pdfile, fieldnames=fieldnames)
        writer1.writeheader()

        parcelsnopds = open(output2, 'w', newline='')
        writer2 = csv.DictWriter(parcelsnopds, fieldnames=fieldnames)
        writer2.writeheader()

        for row in reader:
            if row['ZONING_DISTRICT'] == 'PD':
                writer1.writerow(row)
            else:
                writer2.writerow(row)
        pdfile.close()
        parcelsnopds.close()