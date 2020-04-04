import folium

map = folium.Map(location=[28.339080, 77.319134], zoom_start=6, titles = "Mapbox Control Room")

map.add_child(folium.Marker(location=[28.339080, 77.319134], popup="Cave", icon=folium.Icon(color='blue')))

map.add_child(folium.Marker(location =[29.339080, 77.319134], popup="Hacienda Del Patron", icon=folium.Icon(color='red') ))

# One more way of marking
tooltip = "Click Me !"
folium.Marker([28.539080, 77.319134], popup="<i>Camp Alpha</i>", tooltip=tooltip).add_to(map)
folium.Marker([28.539080, 77.519134], popup="Pochinki").add_to(map)

# Another Way of marking
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location =[29.439080, 77.319134], popup="Bootcamp", icon=folium.Icon(color='green') ))
map.add_child(fg)

#Using some other functionality - marking with the click of the mouse
map.add_child(folium.ClickForMarker(popup='Waypoint'))                      # This ClickForMarker is used to have mouse button click functionality



map.save("Map1.html")
