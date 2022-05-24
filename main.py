

import csv
import pdb
from os.path import exists
from separate_pds import separate_pds
from separate_city_parcels import separate_city_parcels
from unique_pds import get_unique_pds

full_parcel_list = 'parcels.csv'
parcels_zoned_pd = 'pudlist.csv'
parcels_minus_pds = 'parcelsnopds.csv'
unique_pd_list = 'uniquepds.csv'

input_file = 'cityparcels.csv'
output_file = 'reducedlist.csv'
fieldnames = ['PARCEL_PIN', 'SOURCE', 'Future Land Use Code', 'ZONING_DISTRICT', 'SUBDIVISION_PLAT_NAME']


ESTATE_NEIGHBORHOOD = {'RE'}
SINGLE_FAMILY_NEIGHBORHOODS = {'SFA', 'SFD'}
MIXED_RESIDENTIAL_NEIGHBORHOODS = {'SFA', 'SFD', 'MF'}
MIXED_USE_NEIGHBORHOODS = {'SFA', 'SFD', 'MF', 'CR', 'NS'}
COMMERCIAL = {'CR', 'RC', 'CC', 'NS'}
COMMUNITY_MIXED_USE = {'CR', 'SFA', 'MF', 'NS'}
REGIONAL_MIXED_USE = {'CC', 'BP', 'NS', 'SFA', 'MF'}
TRANSIT_ORIENTED_DEVELOPMENT = {'TOD', 'MU', 'NS'}
EMPOLOYMENT_CENTER = {'EC', 'BP'}
EMPLOYMENT_CENTER_WAREHOUSE = {'EC', 'BP', 'I'}
INSTITUTIONAL = {'OI'}
PARKS_TRAILS_OPENSPACE = {'POS'}
URBAN_RESERVE = {'A'}

FUTURE_LAND_USE_CODE_TO_ZONING_DISTRICT = {
    'Estate Neighborhood': ESTATE_NEIGHBORHOOD,
    'Single-Family Neighborhoods': SINGLE_FAMILY_NEIGHBORHOODS,
    'Mixed Residential Neighborhoods': MIXED_RESIDENTIAL_NEIGHBORHOODS,
    'Mixed-Use Neighborhoods': MIXED_USE_NEIGHBORHOODS,
    'Commercial': COMMERCIAL,
    'Community Mixed-Use': COMMUNITY_MIXED_USE,
    'Regional Mixed-Use': REGIONAL_MIXED_USE,
    'Transit-Oriented Development': TRANSIT_ORIENTED_DEVELOPMENT,
    'Employment Center': EMPOLOYMENT_CENTER,
    'Employment Center - Warehousing Overlay': EMPLOYMENT_CENTER_WAREHOUSE,
    'Institutional': INSTITUTIONAL,
    'Parks, Trails, and Open Space': PARKS_TRAILS_OPENSPACE,
    'Urban Reserve': URBAN_RESERVE
}

def find_mismatched_parcels():
    with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        reducedlist = open(output_file, 'w', newline='')
        writer = csv.DictWriter(reducedlist, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            future_land_use = row['Future Land Use Code']
            zoning = row['ZONING_DISTRICT']
            zones_not_in_future_land = FUTURE_LAND_USE_CODE_TO_ZONING_DISTRICT.get(future_land_use)
            if zones_not_in_future_land is not None and zoning not in zones_not_in_future_land:
                writer.writerow(row)            
        reducedlist.close()

if __name__ == "__main__":
    if not exists(parcels_zoned_pd):
        separate_pds(full_parcel_list, parcels_zoned_pd, parcels_minus_pds) # Loops through entire parcel list to remove PDs into their own list
    if not exists(unique_pd_list):
        get_unique_pds(parcels_zoned_pd, unique_pd_list)
    if not exists(input_file):
        separate_city_parcels(parcels_minus_pds, input_file) # Loops through the parcel list sans PDs to remove parcels not in city limits
    if not exists(output_file):
        find_mismatched_parcels()




"""
unique zone districts: 
'PD', 'SFA', 'POS', 'BP', 
'NS', 'CR', None, 'EO', 'EB', 
'ES', 'RE', 'SFD', 'MC', 'MF', 
'ETD', 'I', 'RC', 'CC', 'ER', 
'MH', 'A', 'DR'
"""

"""
unique FLUM categories: 
'Institutional', 'Mixed Residential Neighborhoods', 
'Regional Mixed-Use', None, 'Mixed-Use Neighborhoods', 
'Employment Center', 'Employment Center - Warehousing Overlay', 
'Estate Neighborhood', 'None', 'Parks, Trails, and Open Space', 
'Transit-Oriented Development', 'Single-Family Neighborhoods', 
'Community Mixed-Use', 'Commercial'
"""