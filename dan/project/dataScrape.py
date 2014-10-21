# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 17:36:03 2014

@author: danielmatthews
"""

import trulia.stats
import trulia.location
from pprint import pprint

TRULIA_KEY = "TRULIA_API_KEY"

#Get all neighborhoods in DC
neighborhoods = trulia.location.LocationInfo(TRULIA_KEY).get_neighborhoods_in_city("Washington", "DC")

pprint(neighborhoods)

#Get neighborhood_id
neighborhood_header = neighborhoods[0].keys()
neighborhood_data = [neighborhood.values() for neighborhood in neighborhoods]
neighborhood_id = [int(row[0]) for row in neighborhood_data]

#Get neighborhood stats (1790 is Adams Morgan)
neighborhood_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_neighborhood_stats(neighborhood_id=1790, start_date="2014-01-01", end_date="2014-01-31")

#Get avg price per neighborhood
avg_price = neighborhood_stats['listingStats']['listingStat'][0]['listingPrice']['subcategory'][0]['averageListingPrice']