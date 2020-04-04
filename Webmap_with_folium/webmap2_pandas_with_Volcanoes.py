import folium
import pandas

# Reading and storing the values from Volcanoes.txt 
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])     # Taking only the latitudes from the data
lon = list(data["LON"])     # Taking and Storing the longitudes from the data
name = list(data["NAME"])   # Taking and Storidng the names from the data

#Initializing map
map = folium.Map(location=[39.828492, -100.542930], zoom_start=6, titles = "Mapbox Bright")

#Creating a FeatureGroup
fg = folium.FeatureGroup(name="My Map")

# Using loop for more markers, using zip() to zip the values and than iterate
for lt, ln, nm in zip(lat, lon,name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color="blue", icon="cloud")))
map.add_child(fg)       # or fg.add_to(Map)

map.add_child(folium.ClickForMarker(
    popup="Waypoint"))

map.save("Map1.html")
