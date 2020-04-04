import folium
import pandas
import random

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1500:
        return "green"
    elif 1500<=elevation<2500:
        return "grey"
    else:
        return "cadetblue"

map = folium.Map(location=[39.828492, -100.542930], zoom_start=1, titles = "Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

# Using loop for more markers
for lt, ln, el in zip(lat, lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m",
    fill_color=color_producer(el), color="grey", fill_opacity=0.7))

# using GeoJason() in folium to take .json file
fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {"fillColor":"yellow"} ))

map.add_child(fg)       # or fg.add_to(Map)

map.save("Map1.html")
