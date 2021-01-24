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
import random

start_time = time.time()

lat = 51.466767
lon = -0.070416
radius = 2.0
num_select = 10
month = f"{datetime.datetime.now().month:02d}"

url_base = r"https://records.nbnatlas.org"
url = f"https://records.nbnatlas.org/occurrences/search?q=*%3A*&fq=(geospatial_kosher%3Atrue%20AND%20-occurrence_status%3Aabsent)&fq=(species_group%3A\"FloweringPlants\"%20OR%20species_group%3A\"Plants\")&lat={lat}&lon={lon}&radius={radius}&fq=month%3A\"{month}\"&max=100"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# scrape out the tooltips with plant names and grab the individual tooltip link
raw_results = soup.findAll(lambda tag: tag.name == 'a' and 
                                  tag.get('class') == ['occurrenceLink'],
                           href=True)
all_results = [a['href'] for a in raw_results]
results = random.sample(all_results, min(num_select, len(all_results)))

print(f"{len(all_results)} plants found, {len(results)} selected!")
print("--- %s seconds ---" % (time.time() - start_time))

plant_df = pd.DataFrame(columns=['species', 'commonName', 'lat', 'long', 'loc_remarks'])

plantNum = 0
for plant in results:
    print(f"processing plant {plantNum} of {len(results)}")
    plant_soup = BeautifulSoup(requests.get(url_base + plant).text,'html.parser')
    # get various attributes on each plant datum
    try:
        species = plant_soup.find(id='species').find(class_='value').text.strip()
    except:  # if the plant doesn't have a species, what even is the point?
        print("skipped a species-less plant")
        continue
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