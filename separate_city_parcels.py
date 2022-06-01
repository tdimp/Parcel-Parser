import csv

# This module checks rows in a list of parcels and checks whether its SOURCE value is 'Within City Boundary'.
# If the parcel is within the city, the row is copied to another file.

def separate_city_parcels(input, output):
    with open(input, newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['PARCEL_PIN', 'SOURCE', 'ZONING_DISTRICT', 'FUTURE_LAND_USE', 'SUBDIVISION_NAME']
        reader = csv.DictReader(csvfile)

        city_parcels = open(output, 'w', newline='')
        writer = csv.DictWriter(city_parcels, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row['SOURCE'] == 'COT':
                writer.writerow(row)
        city_parcels.close()