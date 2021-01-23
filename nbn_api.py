# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:20:09 2021

@author: Alice
"""

import json
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import datetime

start_time = time.time()

url = r"https://records.nbnatlas.org/occurrences/search?q=*:*&fq=(geospatial_kosher:true%20AND%20-occurrence_status:absent)&pageSize=100&lat=52.210083&lon=0.1238049&radius=1"
url_base = r"https://records.nbnatlas.org"
lat = 52.210083
lon = 0.1238049
radius = 1.0
pageSize = 10
kingdom = "Plantae"
month = f"{datetime.datetime.now().month:02d}"

url = f"https://records.nbnatlas.org/occurrences/search?q=*%3A*&fq=(geospatial_kosher%3Atrue%20AND%20-occurrence_status%3Aabsent)&fq=kingdom%3A\"{kingdom}\"&lat={lat}&lon={lon}&radius={radius}&fq=month%3A\"{month}\""
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# scrape out the tooltips with plant names and grab the individual tooltip link
raw_results = soup.findAll(lambda tag: tag.name == 'a' and 
                                  tag.get('class') == ['occurrenceLink'],
                           href=True)
results = [a['href'] for a in raw_results]

print(f"{len(results)} plants found!")
print("--- %s seconds ---" % (time.time() - start_time))

plant_df = pd.DataFrame(columns=['species', 'commonName', 'lat', 'long', 'loc_remarks'])

plantNum = 0
for plant in results:
    print(f"processing plant {plantNum} of {pageSize}")
    plant_soup = BeautifulSoup(requests.get(url_base + plant).text,'html.parser')
    # get various attributes on each plant datum
    species = plant_soup.find(id='species').find(class_='value').text.strip()
    try:
        commonName = plant_soup.find(id='commonname').find(class_='value').text.strip()
    except:
        commonName = ''
    lat = float(plant_soup.find(id='latitude').find(class_='value').text.strip())
    long = float(plant_soup.find(id='longitude').find(class_='value').text.strip())
    try:
        loc_remarks = plant_soup.find(id='locationRemarks').find(class_='value').text.strip()
    except:
        loc_remarks = ''
    plant_df = plant_df.append({'species': species, 'commonName': commonName,
                                'lat': lat, 'long': long, 'loc_remarks': loc_remarks},
                               ignore_index=True)
    plantNum += 1
    

print("--- %s seconds ---" % (time.time() - start_time))