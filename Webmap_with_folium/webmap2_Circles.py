import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Creating a function that will return color according to the elevation value passed
def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<2000:
        return 'orange'
    else:
        return 'cadetblue'

map = folium.Map(location=[39.828492, -100.542930], zoom_start=6, titles = "Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

# Using loop for more markers
for lt, ln, el in zip(lat, lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m",
    fill_color=color_producer(el), color="grey", fill_opacity=0.7))

map.add_child(fg)       # or fg.add_to(Map)

map.add_child(folium.ClickForMarker(
    popup="Waypoint"))

map.save("Map1.html")
