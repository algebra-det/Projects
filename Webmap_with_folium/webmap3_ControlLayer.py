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

map = folium.Map(location=[39.828492, -100.542930], zoom_start=3, titles = "Mapbox Bright")


fg = folium.FeatureGroup(name="Volcanoes")

# Using loop for more markers
for lt, ln, el in zip(lat, lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m",
    fill_color=color_producer(el), color="grey", fill_opacity=0.7))


fgv = folium.FeatureGroup(name="Population")
# using GeoJason() in folium to take .json file
fgv.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"] < 1000000
    else "orange" if 1000000<=x["properties"]["POP2005"]<2000000 else "red"} ))

# Controling Layers as there are currently 3 layers i.e.
# Base Layer
# Polygon Layers
# Marker Layer
map.add_child(fg)       # or fg.add_to(Map)
map.add_child(fgv)
map.add_child(folium.LayerControl())           # this marks the end of layering - check the topright corner of the page
# if the above sentence is placed than the after add_child won't work
# so we have to place the map.add_child(fg) above LayerControl


map.save("Map1.html")
