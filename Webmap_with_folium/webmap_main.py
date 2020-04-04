from folium import *
import pandas

# For Volcanoes
data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name_v = list(data["NAME"])


# For airport
data_airports = pandas.read_csv("airport.txt")

cor = list(data_airports["coordinates"])        # as in airports.txt file contains cordinates but they are not in list unlike Volcanoes_USA.txt and are seperated by commas
name = list(data_airports["name"])
lati_for_airport = []
long_for_airport = []

for i in cor:               # breaking the coordinates and storing them seperately in a list
    j,k = i.split(",")
    lati_for_airport.append(j)
    long_for_airport.append(k)



def color_producer(elevation):
    if elevation<1500:
        return "green"
    elif 1500<=elevation<2500:
        return "grey"
    else:
        return "cadetblue"



# Initializing Map
map = Map(location=[28.339080, 77.319134], zoom_start=7, title="Mapbox Bright")


# INDIA - Defining a Marker
map.add_child(Marker(location=[28.539080, 77.319134], popup="<i>Pochinki</i>", tooltip="click to know more", icon=Icon(color='blue')))



#creating a FeatureGroup() for airport
# AIRPORT Marker
fg_airport = FeatureGroup(name="Airports")
for laa,loa,na in zip(lati_for_airport,long_for_airport,name):
    fg_airport.add_child(Marker(location=[laa,loa], popup =na, icon=Icon(color="orange")))
fg_airport.add_to(map)

# Taking a variable for Tooltip
tooltip = "Click Me!"



#creating a FeatureGroup() for volcanoes
# for VOLCANOES circles
fg_volcanoes = FeatureGroup(name="Volcanoes")
# Using loop for more markers
for lt, ln, el, nm in zip(lat, lon, elev, name_v):
    fg_volcanoes.add_child(CircleMarker(location=[lt, ln], radius=7, popup=nm,
    fill_color=color_producer(el), color="grey", fill_opacity=0.7))

map.add_child(fg_volcanoes)       # or fg.add_to(Map)


# using GeoJason() in folium to take .json file - Polygon
fg_polygon = FeatureGroup(name="Polygon Layer")
fg_polygon.add_child(GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
    control=False, style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"] < 1000000
    else "orange" if 1000000<=x["properties"]["POP2005"]<2000000 else "red"} ))

fg_polygon.add_to(map)


#INDIA -  Anothere way of marking - in here we can enable the whole set with map.add_child(fg)
#If map.add_child(fg) is not written this whole fg won't work
fg2 = FeatureGroup(name="Pubg In INDIA")
fg2.add_child(Marker(location=[28.739080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green", icon="info-sign", angle='30'),tooltip=tooltip))
fg2.add_child(Marker(location=[28.939080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green",icon="info-sign",angle=30),tooltip=tooltip))
fg2.add_child(Marker(location=[28.139080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green",icon="info-sign",angle=30),tooltip=tooltip))
map.add_child(fg2)

# INDIA - Iterating via for Loop
fg1 = FeatureGroup(name="Pubg2 In INDIA")
for coordinate in [[28.139080, 77.919134],[28.239080, 77.319134]]:
    fg1.add_child(Marker(location=coordinate, popup="Something New", icon=Icon(color="lightgray", icon="cloud")))
fg1.add_to(map)

# INDIA - One more way of marking
Marker([28.739080, 77.519134], popup="Camp Alpha", icon=Icon(color="red", icon="cloud"), tooltip="CLICK").add_to(map)
Marker([27.739080, 77.519134], popup="School", icon=Icon(color="cadetblue",icon_color="white"), tooltip="NewOne").add_to(map)

# INDIA - defining click to mark function

map.add_child(ClickForMarker(popup="Waypoint Bro"))

# defining latitude/longitude popovers
#map.add_child(LatLngPopup())

# Creating custom icon - just simply download any image in png from anywhere in the current direcotry
url = 'http://leafletjs.com/examples/custom-icons/{}'.format

icon = CustomIcon(
    icon_image="leaf-green.png",
    icon_size=(28,55),
    icon_anchor=(22,94),
    shadow_image="leaf-shadow.png",
    shadow_size=(50,64),
    shadow_anchor=(4,62),
    popup_anchor=(-3,-76)
    )

mark = Marker(location=[27.739080, 76.519134], Popup="Ballabgarh",icon=icon)
map.add_child(mark)

map.add_child(LayerControl())


map.save("map.html")
