import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# we can also use random module to pick up random values 
# col = ['pink', 'lightgreen', 'blue', 'darkpurple', 'white', 'gray', 'orange', 'green', 'darkgreen', 'darkred', 'darkblue',
#       'lightgray', 'purple', 'black', 'cadetblue', 'red', 'lightblue', 'lightred', 'beige']
# by using random.choice(col) at folium.Icon(color=random.choice(col))

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
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=color_producer(el), icon="cloud")))

map.add_child(fg)       # or fg.add_to(Map)

map.save("Map.html")
