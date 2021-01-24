# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:20:09 2021

@author: Alice
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import random
import threading
import time
import concurrent.futures

from flask import Flask, request, render_template, session, redirect
from wtforms import Form, FloatField, validators
app = Flask(__name__)

start_time = time.time()

# Model
class InputForm(Form):
    lat = FloatField(
        label='latitude', default=51.466767,
        validators=[validators.InputRequired()])
    lon = FloatField(
        label='longitude', default=-0.070416,
        validators=[validators.InputRequired()])
    radius = FloatField(
        label='radius', default=2.0,
        validators=[validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        lat = form.lat.data
        lon = form.lon.data
        radius = form.radius.data
        
        num_select = 3
        month = f"{datetime.datetime.now().month:02d}"
        results = get_plant_list(lat, lon, radius, month, num_select)
        plant_df = get_plant_df(results)
        return render_template('view_output.html',  tables=[plant_df.to_html(classes='data')], titles=plant_df.columns.values)
        #return render_template("view_found_plants.html",
        #                       total_plant_count=len(all_results), plant_count=len(results))
    else:
        return render_template("view_input.html", form=form)

        print("--- %s seconds ---" % (time.time() - start_time))
        

def get_plant_list(lat, lon, radius, month, num_select):
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
    return(results)

def get_plant_df(results):
    url_base = r"https://records.nbnatlas.org"
    plantNum = 1
    plant_df = pd.DataFrame(columns=['species', 'commonName', 'lat', 'long', 'loc_remarks'])
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
    return plant_df

def print_time():
    i=0
    while i < 10: 
       print(time.time() - start_time)
       time.sleep(1)
       i+=1


if __name__ == '__main__':
    lat = 51.466767
    lon = -0.070416
    radius = 2.0
    num_select = 10
    month = f"{datetime.datetime.now().month:02d}"
    results = get_plant_list(lat, lon, radius, num_select)
    print("--- %s seconds ---" % (time.time() - start_time))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        data_thread = executor.submit(get_plant_df, results)
        print_thread = executor.submit(print_time)
        plant_df = data_thread.result()
        print(plant_df)
        
if __name__ == '__main__':
    app.run(debug=True)

#print("--- %s seconds ---" % (time.time() - start_time))