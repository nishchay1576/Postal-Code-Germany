# -*- coding: utf-8 -*-
#Postal Codes Germany
"""
Code Challenge

    We have to bring together the information of two files. 
    In the first file, we have a list of nearly 15000 lines of post codes with the 
    corresponding city names plus additional information. 

    The other file contains a list of the 19 largest German cities. 
    Each line consists of the rank, the name of the city, the population, 
    and the state (Bundesland): 
    
    Our task is to create a list with the top 19 cities,
    with the city names accompanied by the first three postal code. 

  Output:
    The output of this code looks like this. 
    Output is in form of dictionary.
         
{
    'Berlin': ['10115', '10117', '10119'],
     'Hamburg': ['20095', '20097', '20099'],
     'München': ['85748', '85551', '80331'],
     'Köln': ['50667', '50668', '50670'],
     'Frankfurt am Main': ['60306', '60308', '60310'],
     'Essen': ['49152', '45127', '45128'],
     'Dortmund': ['44135', '44137', '44139'],
     'Stuttgart': ['70173', '70174', '70176'],
     'Düsseldorf': ['40210', '40211', '40212'],
     'Bremen': ['27568', '28195', '28197'],
     'Hannover': ['30159', '30161', '30163'],
     'Duisburg': ['47051', '47053', '47055'],
     'Leipzig': ['4103', '4105', '4107'],
     'Nürnberg': ['90518', '90402', '90403'],
     'Dresden': ['1067', '1069', '1097'],
     'Bochum': ['44787', '44789', '44791'],
     'Wuppertal': ['42103', '42105', '42107'],
     'Bielefeld': ['33602', '33604', '33605'],
     'Mannheim': ['68159', '68161', '68163']
 }

"""

import re
largest_city_file = open('/Users/nishchay/Documents/datafiles/largest_cities_germany.txt','r')

largest_city_name = largest_city_file.readlines()

regex_cities = re.compile(r'\s[\w\s]+\s+')

city_name_list = []
for cities in largest_city_name:
    city_name = regex_cities.findall(cities)[0]
    city_name_list.append(city_name.strip())
    
postal_code_file = open('/Users/nishchay/Documents/datafiles/postal_codes_germany.txt','r')

postal_code = postal_code_file.read()

city_postal_dict = {}

for city in city_name_list:
    regex_postal = '\s'+city+'\s[\d]+\s'
    city_match = (re.findall(regex_postal,postal_code)[0:3])
    city_match_str = "".join(city_match)
    city_postal_dict[city] = re.findall(r'[0-9]+',city_match_str)

print(city_postal_dict)