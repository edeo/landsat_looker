import csv
input_file = csv.DictReader(open("drinks_2.csv"))
NA_beers = [int(row['beer_servings']) for row in input_file if row['continent']=='NA']
import csv
input_file = csv.DictReader(open("drinks_2.csv"))
EU_beers = [int(row['beer_servings']) for row in input_file if row['continent']=='EU']
NA_avg = round(sum(NA_beers) / float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers) / float(len(EU_beers)), 2)
print NA_avg
print EU_avg
