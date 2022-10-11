"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
import pandas as pd
import folium
import webbrowser
import pathlib

path = f"{pathlib.Path().resolve()}/Yellowpages Results (10_08_22 232624).csv"

geolocator = Nominatim(user_agent="example app")
data = pd.read_csv(path)
data['full_address'] = data['Street_Address']+ ', ' +data['Locality']
data['full_address'] = [x[:-6] for x in data['full_address']]
data["loc"] = data["full_address"].apply(geolocator.geocode)
data["point"] = data["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
data = data[data['point'] != None]
data[['lat', 'lon', 'altitude']] = pd.DataFrame(data['point'].to_list(), index=data.index)
data['lat'].isnull().count()
data.dropna(axis=0, inplace=True)


# Create a map object and center it to the avarage coordinates to m
m = folium.Map(location=data[["lat", "lon"]].mean().to_list(), zoom_start=2)
# if the points are too close to each other, cluster them, create a cluster overlay with MarkerCluster, add to m
marker_cluster = MarkerCluster().add_to(m)
# draw the markers and assign popup and hover texts
# add the markers the the cluster layers so that they are automatically clustered
for i, r in data.iterrows():
    location = (r["lat"], r["lon"])
    folium.Marker(location=location,
                      popup = r['Name'],
                      tooltip = r['Name'])\
        .add_to(marker_cluster)
# display the map
m.save("mymap.html")
webbrowser.open('mymap.html')